---
type: Playbook
title: Prüfstand und offene Tests
description: Den tatsächlichen Nachweis je Thema und die verbleibenden City-Builder-Tests
  erkennen.
tags:
- shaderworld
- unreal-engine
- city-builder
status: stable
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: Zusammenfassung der vorhandenen Nachweise mit getrennten offenen Tests
generated:
  by: codex/gpt-6
  at: "2026-10-28T00:08:51Z"
sources:
- id: tunnel-component
  resource: evidence/tunnel-component-report.json
  title: CityLab-Tunnelkomponente; native Tests und offene Kartenabnahme
- id: terrain
  resource: evidence/terrain-report.json
  title: Terrainprüfung
- id: citylab
  resource: evidence/citylab-report.json
  title: CityLabprüfung
- id: persistence
  resource: evidence/persistence-report.json
  title: Neustartprüfung
- id: ocean
  resource: evidence/ocean-report.json
  title: Ozeanprüfung
- id: basics
  resource: evidence/citybasics-report.json
  title: CityBasics mit zwei echten Durchfahrten
- id: holes
  resource: evidence/hole-report.json
  title: Lochprüfung
---


# Prüfstand und offene Tests

Stand: **28. Oktober 2026**, Unreal **5.8.4**, ShaderWorld **4.1**. Die Statusangaben beschreiben den jeweiligen Versuch. Eine schöne Ansicht bestätigt weder dauerhafte Speicherung noch Physikkollision oder Leistung einer großen Welt.

## So liest du den Prüfstatus

| Begriff | Bedeutung |
| --- | --- |
| Herstellerangabe | In einer offiziellen Quelle beschrieben; hier noch nicht selbst bestätigt |
| Code-/Assetbefund | API, Einstellung oder Beispiel im installierten Bestand gelesen |
| Editor visuell | Tatsächliches Bild in der Editoransicht gesehen |
| Editor/PIE geprüft | Konkrete Bedingungen oder Kollisionen in der Vorschau gemessen |
| Neustart geprüft | Getrennter Spielprozess hat gespeicherte Änderungen wiederhergestellt |
| Offen | Der konkrete Anwendungsfall braucht noch einen eigenen Versuch |

`status: stable` im OKF-Frontmatter bedeutet, dass die Seite als Anleitung bereitsteht. Es bedeutet nicht, dass alle erwähnten Funktionen abgenommen sind. `generated` dokumentiert die Erstellung, `verified` eine Bestätigung der Seite gegen Quellen. Den fachlichen Testumfang halten unsere zusätzlichen Felder `evidence_scope` und der sichtbare Text fest. Eine technische Linkprüfung darf daraus keinen erfolgreichen Unreal-Test machen.

## Bisheriger Stand

| Thema | Nachweis | Grenze |
| --- | --- | --- |
| Flaches 1-km-Terrain und Kollision | [Terrain-Bericht](evidence/terrain-report.json), Editor-Einstellungen/erneutes Laden und vier PIE-Terrainproben | Kein verpackter Build |
| Bauplatz und native Straße | [CityLab-Bericht](evidence/citylab-report.json), sechs Phasen mit je 14 Proben | Kleiner Laborbereich, keine Verkehrssimulation |
| Dauerhafte Pads und Straßen | [Neustart-Bericht](evidence/persistence-report.json), zwei getrennte Prozesse; je 26 ursprüngliche und 26 geänderte Terrainproben | Eigene CityLab-SaveGame-Implementierung; uncooked Standalone |
| P/R, K/L und automatisches Laden | Beobachteter UI-Test im Persistenzbericht | Kein allgemeines Plugin-Bedienkonzept |
| Reference-Biom und Dreckstraße | Live-Ansicht und Actor-/Komponentenprüfung | Eigene Biome, dauerhafte Rodung und Road-Creator-Integration offen |
| Ozean mit Wind und Schaum | [Ozeanbericht](evidence/ocean-report.json), Wind 18 m/s, Schaum aktiv, Rebuild beendet, sichtbare Schaumflächen | Keine Auftriebs-, Dedicated-Server- oder Mehrspielerabnahme |
| CityBasics-Tunnel und Testbuggy | [CityBasics-Bericht](evidence/citybasics-report.json): zwei eigenständige Spielstarts, je 65/65 Kollisionsproben und rund 259,48 m bodengebundene Durchfahrt | Eigene Fahrbahn-/Tunnelmeshes; CharacterMovement, keine Chaos-Fahrzeugphysik; F-/Mausbedienung manuell offen |
| Eigene Tunnelkomponente | [Komponentenbericht](evidence/tunnel-component-report.json): Build und zwei native Automationtests zu Profil/Lebenszyklus und echten WaterSubsystem-Abfragen bestanden | NullRHI mit kontrolliertem Wasserprovider; gespeicherte Karte und neues PIE zusätzlich per Eigenschaften geprüft, zusätzlich frischer Spielprozess mit 65/65 Kollisionsproben und rund 259,44 m Fahrt; neuer Sichtnachweis nur ein inspizierter PIE-Frame |
| Terrainlöcher | [Lochbericht](evidence/hole-report.json), Demoansicht, Komponenten und Implementierung gelesen | Eigene Bergportale und Tunnelkörper im CityBasics-Bericht geprüft; Verpackung offen |
| DX12/SM6 | Nanite-Warnung im Basistest behoben | Lumen-Konfiguration in Demoansichten weiterhin offen |

Beim Persistenztest lag der größte ursprüngliche Gelände-Höhenfehler bei rund **0,949 cm**, nach Änderungen bei rund **0,630 cm**; die Toleranz betrug **3 cm**. IDs, Kontrollpunkte und Änderungsreihenfolge wurden zwischen Erzeugen und Laden verglichen. Wiederholtes Laden erzeugte keine Duplikate, ein fehlender Slot und eine falsche Speicherformatversion ließen die vorhandene Stadt erhalten. Generator-/Seed-Konflikte werden im Code geprüft, wurden aber nicht als eigene Negativversuche abgenommen. Im JSON bedeuten `false`-Checks in nicht zuständigen Phasen **nicht anwendbar**; die Gesamt- und Phasenurteile sind separat angegeben.

Nach der Korrektur der Zufahrts-Längentabellen bestand die gespeicherte Endfassung am **28. Oktober 2026** eine zusätzliche Prüfung: nochmals **65/65 Proben**, **133/133 Fahrproben am Boden** und **259,35 m** tatsächliche Durchfahrt. Die zwei ursprünglichen Läufe und die abschließende Kontrolle sind im [CityBasics-Bericht](evidence/citybasics-report.json) getrennt erhalten.

Die [Küsten-/Biomprüfung vom 28. Oktober](evidence/coast-biome-road-inspection.json) ist eine lesende Parameter-, Material-, Asset- und Codeprüfung. Sie bestätigt die vorhandene Ground/Ocean-Verbindung und den angeschlossenen Water-Exclusion-Materialknoten. Die alten Pflanzen-Minimalhöhen erlauben den neuen Meeresboden als Waldstandort. Die [Korrektur](evidence/coast-correction-report.json) ist inzwischen gespeichert: eigenes Landbiom mit drei Pflanzenfiltern ab 150 cm, Dämpfung 1,0 und native Tunnel-Air-Pocket-Box. Assetwerte, unveränderte Plugin-Originale und die Box nach PIE-Neustart wurden zurückgelesen. Der Nutzer berichtete weiterhin Wellen bei Dämpfung 1,0 am Tunnel; der gelesene Hole-Cache-Pfad erklärt dort fehlende Küstendämpfung. Nach dem Einbau bestätigte der Nutzer an der betroffenen Tunnelstelle **„Bisher trocken“**. Eine längere Sichtprüfung, die Unterwasservegetation und gültige GPU-Höhenmessungen bleiben gesondert offen.

Die neue **CityLab Tunnel (Dry)**-Komponente integriert die native Air Pocket in den Tunnelbaustein. Die bestandenen Tests prüfen auch Größenänderung, Registrierung, Entfernen und transformierte beziehungsweise gespiegelte Ausschlüsse. Der Archive-/PostLoad-Test ist kein Package-Ladetest. Die Laborkarte ist auf die neue Instanz **Tunnel** mit relativer **Z = 600 cm** umgestellt und gespeichert. Nach tatsächlichem Neuladen der Karte und neuem PIE sind die sechs Profilwerte, Extents, Transformation und NoCollision bestätigt; die alte DryTunnel-Box ist entfernt. Ein frischer Spielprozess bestand anschließend nochmals **65/65 Kollisionsproben**, **134/134 Bewegungs-Samples am Boden** und rund **259,44 m** bodengebundene Fahrt. Der Bericht ist für diesen abgegrenzten Umfang **passed_with_limits**. Die frühere Nutzerantwort „Bisher trocken“ bezieht sich auf die vorherige separate Box bei Z = 0. Nach der Migration wurde eine neue native PIE-Aufnahme inspiziert: Der sichtbare Innenraum mit Boden, Wänden und Buggy ist trocken. Dieser eine Frame ersetzt keine Langzeit- oder GPU-Wasserhöhenprüfung.

## Nächste Abnahmen für den City Builder

1. Dauerhafte Rodungsmaske nach Speichern und Laden; der farbige CityBasics-Aufbau verwendet zunächst Reference-Materialien.
2. Manuelle F-/Mausbedienung des Laufmodus, weitere Fahrzeugprofile und speicherbare Tunnel.
3. Auftrieb mit einem definierten Physikobjekt und kontrollierten Wellenbedingungen.
4. NavMesh nach Bauflächen-, Straßen- und Gebäudeänderungen.
5. Verpackter Build und danach Leistung bei größerer Karte und vielen Änderungen.

Neue Versuche ergänzen die jeweilige Anleitung und ihren Beleg. Die Anleitung [Wissen pflegen](maintenance.md) beschreibt diesen Ablauf.
