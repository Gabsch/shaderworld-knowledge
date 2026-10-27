"""Check this repository's OKF 0.2 documentation profile, not the entire spec.

Uses PyYAML's safe loader, never executes document content, and never contacts
external sources. External claims and human approvals still need review.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML fehlt. Im Repository: python -m pip install -r requirements.txt")


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML with duplicate keys rejected instead of silently overwritten."""


def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ValueError("YAML-Schluessel muessen Zeichenketten sein")
        if key in result:
            raise ValueError(f"Doppelter YAML-Schluessel: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
LINK = re.compile(r'!?\[(?:\\.|[^\]\\])*\]\(\s*(<[^>\n]+>|(?:\\.|[^\s)])*)(?:\s+(?:"[^"\n]*"|\x27[^\x27\n]*\x27))?\s*\)')
REFERENCE = re.compile(r'^\s{0,3}\[([^\]^][^\]]*)\]:\s*(<[^>\n]+>|\S+)', re.MULTILINE)
REFERENCE_USE = re.compile(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]')
PRIVATE_PATH = re.compile(r'(?i)(?:\b[A-Z]:[\\/]|file://)')
ACTOR = re.compile(r'^(?:human:[^\s]+|process:[^\s]+|[^\s/]+/[^\s/]+)$')


def prose(text):
    """Exclude code examples from link checking; this is not a full MD parser."""
    output, fence = [], None
    for line in text.splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            output.append("")
            continue
        output.append("" if fence else re.sub(r'(`+).*?\1', '', line))
    return '\n'.join(output)


def timestamp(value):
    if isinstance(value, dt.datetime):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
        except ValueError:
            return False
    else:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() is not None


def heading_ids(text):
    result, seen = set(), {}
    for line in prose(text).splitlines():
        match = re.match(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*$', line)
        if not match:
            continue
        heading = re.sub(r'<[^>]+>', '', match.group(1)).lower().strip()
        slug = re.sub(r'[^\w\- ]', '', heading).replace(' ', '-')
        number = seen.get(slug, 0)
        seen[slug] = number + 1
        result.add(slug if not number else f'{slug}-{number}')
    return result


def validate_bundle(bundle):
    bundle = bundle.resolve()
    errors, warnings, human_claims, documents = [], [], [], {}

    def fail(path, message):
        errors.append(f'{path}: {message}')

    if not bundle.is_dir():
        return {'errors': [f'Bundle nicht gefunden: {bundle.name}'], 'warnings': [],
                'human_verification_claims': [], 'concepts': 0, 'markdown_files': 0}

    for path in sorted(bundle.rglob('*.md')):
        name = path.relative_to(bundle).as_posix()
        if not path.resolve().is_relative_to(bundle):
            fail(name, 'Datei verweist ausserhalb des Bundles')
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError:
            fail(name, 'Kein gueltiges UTF-8')
            continue
        if raw.startswith(b'\xef\xbb\xbf'):
            fail(name, 'UTF-8 ohne BOM verwenden')
        if b'\n' in raw.replace(b'\r\n', b'') or b'\r' in raw.replace(b'\r\n', b''):
            fail(name, 'Projektprofil verlangt einheitliche CRLF-Zeilenenden')
        if PRIVATE_PATH.search(text):
            fail(name, 'Keine absoluten Windows-/file://-Pfade im portablen Bundle')
        lines, meta, body = text.splitlines(), None, text
        if lines and lines[0] == '---':
            try:
                end = lines.index('---', 1)
                meta = yaml.load('\n'.join(lines[1:end]), Loader=UniqueSafeLoader)
                body = '\n'.join(lines[end + 1:])
                if not isinstance(meta, dict):
                    raise ValueError('Frontmatter muss ein Mapping sein')
            except (ValueError, yaml.YAMLError) as error:
                fail(name, f'Ungueltiges Frontmatter: {error}')
        documents[path.resolve()] = (name, meta, body)

    root_index = bundle / 'index.md'
    if root_index not in documents:
        fail('index.md', 'Wurzelindex fehlt')
    concepts = 0
    for path, (name, meta, body) in documents.items():
        if path.name == 'index.md':
            if path == root_index:
                if not meta or meta.get('okf_version') != '0.2':
                    fail(name, 'Wurzelindex braucht okf_version: "0.2"')
                if meta and set(meta) != {'okf_version'}:
                    fail(name, 'Index-Frontmatter darf nur okf_version enthalten')
            elif meta is not None:
                fail(name, 'Unterverzeichnis-Index darf kein Frontmatter haben')
            continue
        if path.name == 'log.md':
            if meta is not None:
                fail(name, 'log.md darf kein Frontmatter haben')
            for date in re.findall(r'^##\s+(.+)$', body, re.MULTILINE):
                try:
                    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date.strip()):
                        raise ValueError()
                    dt.date.fromisoformat(date.strip())
                except ValueError:
                    fail(name, 'Log-Datumsueberschrift muss YYYY-MM-DD sein')
            continue
        concepts += 1
        if not isinstance(meta, dict):
            fail(name, 'Konzept braucht YAML-Frontmatter')
            continue
        for key in ('type', 'title', 'description'):
            if not isinstance(meta.get(key), str) or not meta[key].strip():
                fail(name, f'Projektprofil verlangt nicht leeres {key}')
        if meta.get('status') not in ('draft', 'stable', 'deprecated'):
            fail(name, 'status muss draft, stable oder deprecated sein')
        if 'stale_after' in meta and not timestamp(meta['stale_after']):
            fail(name, 'stale_after braucht ISO-8601-Datum mit Zeitzone')
        generated = meta.get('generated')
        if not isinstance(generated, dict) or not ACTOR.fullmatch(str(generated.get('by', ''))) or not timestamp(generated.get('at')):
            fail(name, 'generated braucht by (Actor) und at (Datum mit Zeitzone)')
        verified = meta.get('verified', [])
        verified = [verified] if isinstance(verified, dict) else verified
        if not isinstance(verified, list):
            fail(name, 'verified muss Mapping oder Liste sein')
            verified = []
        for event in verified:
            if not isinstance(event, dict) or not ACTOR.fullmatch(str(event.get('by', ''))) or not timestamp(event.get('at')):
                fail(name, 'verified-Eintrag braucht by (Actor) und at (Datum mit Zeitzone)')
            elif event['by'].startswith('human:'):
                human_claims.append(f"{name}: {event['by']} at {event['at']}")
        sources = meta.get('sources')
        if not isinstance(sources, list) or not sources:
            fail(name, 'Projektprofil verlangt mindestens eine sources-Quelle')
            sources = []
        source_ids = set()
        for source in sources:
            if not isinstance(source, dict) or not isinstance(source.get('resource'), str) or not source['resource'].strip():
                fail(name, 'Jede Quelle braucht ein nicht leeres resource')
                continue
            if 'id' in source:
                if not isinstance(source['id'], str) or not source['id'].strip() or source['id'] in source_ids:
                    fail(name, 'Quellen-IDs muessen nicht leer und eindeutig sein')
                source_ids.add(str(source['id']))
            resource = source['resource']
            if is_source_descriptor(resource):
                warnings.append(f'{name}: Quellenbeschreibung ohne automatisch verfolgbares Ziel: {resource}')
            else:
                check_target(bundle, path, resource, documents, fail)
        # OKF per-claim footnotes join their labels to sources[].id.
        for label in set(re.findall(r'\[\^([^\]]+)\]', prose(body))):
            if label not in source_ids:
                fail(name, f'Quellenfussnote {label!r} fehlt in sources[].id')

    # Links are checked in index/log bodies as well as concept bodies.
    for path, (name, meta, body) in documents.items():
        clean = prose(body)
        definitions = {key.strip().lower(): target for key, target in REFERENCE.findall(clean)}
        for match in LINK.finditer(clean):
            check_target(bundle, path, match.group(1), documents, fail)
        for target in definitions.values():
            check_target(bundle, path, target, documents, fail)
        for label, key in REFERENCE_USE.findall(clean):
            key = (key or label).strip().lower()
            if label.startswith('^') or key.startswith('^'):
                continue  # Adjacent source footnotes are not reference-style links.
            if key not in definitions:
                fail(name, f'Linkreferenz {key!r} ist nicht definiert')
    if human_claims:
        warnings.append('Human-Review-Vermerke muessen durch direkte, dokumentierte Bestaetigung gedeckt sein; das kann dieser Validator nicht beweisen.')
    return {'errors': errors, 'warnings': warnings, 'human_verification_claims': human_claims,
            'concepts': concepts, 'markdown_files': len(documents)}


def is_source_descriptor(resource):
    """OKF sources may name a population/scope instead of a followable artifact."""
    return (bool(re.search(r'\s', resource))
            and not resource.startswith(('/', './', '../'))
            and not re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', resource)
            and not PRIVATE_PATH.search(resource)
            and not re.search(r'\.[A-Za-z0-9]{1,6}(?:#.*)?$', resource))


def check_target(bundle, source_path, target, documents, fail):
    """Check local link/source containment and existence, never fetch remote URIs."""
    name = source_path.relative_to(bundle).as_posix()
    target = target.strip().removeprefix('<').removesuffix('>')
    target = re.sub(r'\\([ ()])', r'\1', target)
    if not target:
        fail(name, 'Leeres Linkziel')
        return
    if PRIVATE_PATH.search(target):
        fail(name, f'Nicht portables Linkziel: {target}')
        return
    try:
        parsed = urlsplit(target)
    except ValueError:
        fail(name, f'Ungueltiges Linkziel: {target}')
        return
    if parsed.scheme:
        if parsed.scheme not in ('http', 'https', 'mailto'):
            fail(name, f'Nicht unterstuetztes URI-Schema: {target}')
        elif parsed.scheme in ('http', 'https') and (not parsed.netloc or parsed.username or parsed.password):
            fail(name, f'Ungueltiger oder Zugangsdaten enthaltender URL: {target}')
        return
    if parsed.netloc:
        fail(name, f'Protokollrelative URL nicht verwenden: {target}')
        return
    decoded = unquote(parsed.path)
    if '\\' in decoded or '\x00' in decoded:
        fail(name, f'Linkpfad braucht normale / und darf kein NUL enthalten: {target}')
        return
    root = bundle if decoded.startswith('/') else source_path.parent
    resolved = (root / decoded.lstrip('/')).resolve() if decoded else source_path
    if not resolved.is_relative_to(bundle):
        fail(name, f'Link verlaesst das Bundle: {target}')
    elif not resolved.exists():
        fail(name, f'Linkziel fehlt: {target}')
    elif parsed.fragment and resolved.suffix.lower() == '.md' and resolved in documents:
        if unquote(parsed.fragment) not in heading_ids(documents[resolved][2]):
            fail(name, f'Ueberschriftsanker fehlt: {target}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle', nargs='?', type=Path, default=Path(__file__).resolve().parents[1] / 'knowledge')
    parser.add_argument('--json', action='store_true', help='Pruefbericht als JSON ausgeben')
    args = parser.parse_args()
    report = validate_bundle(args.bundle)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"{report['concepts']} Konzepte, {report['markdown_files']} Markdown-Dateien, {len(report['errors'])} Fehler")
        for key in ('errors', 'warnings', 'human_verification_claims'):
            for message in report[key]:
                print(f'{key}: {message}')
        print('Pruefumfang: Repository-Profil; keine Inhaltswahrheit oder vollstaendige OKF-Konformitaetspruefung.')
    return 1 if report['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
