---
type: Playbook
title: Wissen dokumentieren und aktuell halten
description: Neue ShaderWorld-Erkenntnisse nachvollziehbar erfassen, prüfen und bei Versionswechseln erneut bewerten.
status: stable
generated:
  by: codex/gpt-6
  at: 2026-10-27T21:51:29Z
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: Dokumentationsprozess; kein Nachweis weiterer Plugin-Laufzeitfunktionen.
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
    title: Open Knowledge Format v0.2
---
# Wissen dokumentieren und aktuell halten

Diese Wissensbasis richtet sich an Menschen, die ShaderWorld im Editor benutzen möchten, und an Agenten, die dabei helfen. Eine Anleitung muss deshalb auch ohne Lesen des Plugin-Quellcodes ausführbar sein. Der [Einstieg](index.md) führt zu den Themen.

## Eine neue Erkenntnis festhalten

1. Eine bestehende Seite ergänzen oder für ein eigenständiges Thema eine kurze Markdown-Seite anlegen. Der Dateipfad ist ihre dauerhafte Identität; aussagekräftige, stabile Namen verwenden.
2. Zuerst erklären, welches sichtbare Ergebnis die Seite erreichen soll und in welcher Beispielkarte es ausprobiert wurde.
3. Benötigte Versionen und Voraussetzungen nennen. Editor-Bezeichnungen genau übernehmen und Einheiten erläutern, etwa m/s für Wind und Zentimeter für Weltpositionen.
4. Die Bedienfolge beschreiben. Danach das erwartete Ergebnis, bekannte Grenzen und einen Weg zum Rücksetzen nennen. Ein Screenshot hilft, wenn man den Unterschied sehen muss.
5. Quellen mit `sources` erfassen und wichtige Aussagen bei Bedarf mit einer Quellenfußnote zuordnen. Beobachtetes Verhalten und Schlussfolgerungen aus Code ausdrücklich unterscheiden.
6. Den Prüfumfang festhalten. Erst dann `status` und gegebenenfalls `verified` aktualisieren. Links im Index ergänzen und die Änderung im `log.md` des Bundles vermerken.
7. Vom Repository-Verzeichnis `python tools/validate_knowledge.py` ausführen. Anschließend die Seite im Viewer lesen und die praktische Anleitung gegenprüfen.

## Metadaten richtig verwenden

Die Basis ist OKF 0.2. `type` ist dort grundsätzlich verpflichtend; dieses Repository verlangt für seine eigenen Konzepte zusätzlich `title`, `description`, `status`, `generated` und mindestens eine Quelle. Das ist ein lokales Qualitätsprofil und keine zusätzliche Forderung des Standards.

- `generated.by` nennt den tatsächlichen Autor oder das Werkzeug, zum Beispiel `codex/gpt-6`; `generated.at` hält die letzte wesentliche Inhaltsänderung fest.
- `verified` nennt eine tatsächlich erfolgte Bestätigung mit Prüfer und Zeitpunkt. Agenten und Prozesse tragen ihre eigene Identität ein. `human:<id>` darf nur nach einer direkten, dokumentierten Bestätigung dieser Person eingetragen werden. Eine generierte Seite wird dadurch nicht automatisch menschlich geprüft.
- `status: stable` bedeutet, dass die Seite für ihre beschriebene Nutzung bereitsteht. Es bedeutet nicht, dass jede erwähnte Funktion in einem ausgelieferten Spiel getestet wurde. Unvollständige Seiten bleiben `draft`; überholte Seiten können als `deprecated` erhalten bleiben.
- `engine_version` und `plugin_version` sind lokale Zusatzfelder. Sie begrenzen, für welche Installation die Aussage geprüft wurde.
- `evidence_scope` oder `test_scope` beschreibt den tatsächlichen Nachweis. Geeignete Angaben sind etwa „Quellcode gelesen“, „Editoransicht geprüft“, „PIE mit Kollisionsmessung“ oder „Laden in einem zweiten Spielprozess geprüft“. Diese Stufen nicht gleichsetzen.
- `stale_after` kann einen Zeitpunkt zur erneuten Prüfung setzen. Das Datum braucht wie alle OKF-Zeitstempel eine ausdrückliche Zeitzone. Ein Plugin-Update kann eine frühere Prüfung erforderlich machen.

Eine Seite darf eine API erklären und trotzdem ausdrücklich festhalten, dass ihr Laufzeitverhalten noch nicht getestet wurde. Für einzelne Aussagen innerhalb einer Seite den jeweiligen Nachweis direkt dazuschreiben; ein pauschales `verified` ersetzt diese Unterscheidung nicht.

## Quellen und Verweise

Quellen gehören als Objekte unter `sources`. Jede Quelle benötigt `resource`; eine stabile `id` und ein verständlicher `title` helfen beim Zuordnen. Eine Fußnote `[^source-id]` verweist auf die gleichnamige Quellen-ID. Quellen-URLs sollen direkt auf die offizielle Anleitung oder den konkreten Quellcode zeigen.

OKF erlaubt auch eine genaue Beschreibung einer externen Quelle, die sich aus dem Bundle nicht direkt öffnen lässt. Das ist beispielsweise für den separat lizenzierten Plugin-Code sinnvoll: Version und relative Quelldateien nennen und die fehlende Mitlieferung offenlegen. Der Validator meldet solche Quellen zur manuellen Kontrolle. Ein fehlender lokaler Dateilink ist dagegen ein Fehler.

Interne Links verwenden normale relative Pfade. Ein mit `/` beginnender Pfad bedeutet die Wurzel des Wissensbundles. Links und lokale Quellen müssen im Bundle bleiben. Prüfergebnisse oder Bilder, die dauerhaft als Beleg benötigt werden, deshalb gezielt in das Bundle übernehmen und im Text erklären.

Plugin-interne Klassennamen, Assetpfade und relative Quelldateien können im Text genannt werden. Persönliche Windows-Verzeichnisse, Zugangsdaten, vollständige Projektbestände und lizenzierte Plugin-Assets gehören nicht in dieses Dokumentations-Repository. Screenshots und selbst erstellte Berichte vor der Aufnahme prüfen. Die Wissensbasis beschreibt das Plugin; sie enthält keine Kopie des Plugins.

`index.md` und `log.md` sind reservierte Dateien. Indizes haben kein Konzept-Frontmatter; allein der Wurzelindex darf `okf_version: "0.2"` angeben. Das Log verwendet Datumsüberschriften im Format `YYYY-MM-DD`. Andere Markdown-Dateien innerhalb des Bundles benötigen Konzept-Frontmatter. Allgemeine Repository-Dateien wie `README.md` und `AGENTS.md` liegen außerhalb von `knowledge/`.

## Nach einem Plugin- oder Engine-Update

1. Die neue Version erfassen und die bisherige Prüfbasis im Änderungsprotokoll erhalten.
2. Betroffene Anleitungen, API-Namen, Beispielkarten und Standardwerte mit der neuen Installation vergleichen. Eine Versionsnummer nicht bloß über alle Seiten ersetzen.
3. Die beschriebenen Schritte erneut ausführen. Editor-Vorschau, PIE, eigener Spielprozess und verpacktes Spiel bleiben getrennte Prüfumfänge.
4. Neue Beobachtungen samt Nachweis eintragen. Alte Bestätigungen nicht als Prüfung der neuen Version darstellen; nicht erneut geprüfte Aussagen sichtbar kennzeichnen.
5. Erst nach der Prüfung Versions- und Verifikationsmetadaten anpassen. Veraltete Rezepte bei Bedarf erhalten und auf ihren Ersatz verlinken.

## Was der Validator prüft

```powershell
python tools/validate_knowledge.py
python tools/validate_knowledge.py --json
```

Der Validator benötigt Python 3.11 oder neuer und PyYAML aus `requirements.txt`. Er verwendet einen sicheren YAML-Parser und lehnt doppelte YAML-Schlüssel ab. Er prüft UTF-8 ohne BOM, einheitliche CRLF-Zeilenenden, die hier beschriebenen Metadaten, interne Quellen- und Linkziele, Bundle-Grenzen sowie einfache Markdown-Überschriftsanker. Direkte Markdown-Links, Bilder und definierte Referenzlinks werden berücksichtigt; Codebeispiele sind davon ausgenommen.

Das Werkzeug ruft keine externen Seiten auf und führt keine Inhalte aus. Es ist ein Validator unseres Repository-Profils, kein vollständiger Markdown-Parser und keine vollständige OKF-Konformitätsprüfung. Es kann weder die Wahrheit einer Quelle noch eine menschliche Zustimmung oder einen praktischen Unreal-Test beweisen. Vermerke über menschliche Prüfung werden deshalb gesondert zur Kontrolle ausgegeben.
