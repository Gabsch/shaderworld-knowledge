---
type: Playbook
title: Quellen und Bildherkunft
description: Offizielle Dokumentation, eigene Nachweise und die Herkunft der Bilder
  finden.
tags:
- shaderworld
- unreal-engine
- city-builder
status: stable
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: Quellenverzeichnis und exportierte eigene Testnachweise
generated:
  by: codex/gpt-6
  at: "2026-10-28T01:55:41Z"
sources:
- id: official
  resource: https://universgen.gitbook.io/shader-world
  title: ShaderWorld Dokumentation
- id: okf
  resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
  title: OKF 0.2
- id: images
  resource: ../evidence/image-manifest.json
  title: Bildmanifest
---


# Quellen und Bildherkunft

## Offizielle Einstiege

| Quelle | Wofür sie hier verwendet wird |
| --- | --- |
| [ShaderWorld GitBook](https://universgen.gitbook.io/shader-world) | Grundlagen und vom Hersteller beschriebene Arbeitsweisen |
| [Kick-start](https://universgen.gitbook.io/shader-world/fundamentals/kick-start) | Plugin-Inhalte, Demo-Maps und Materialgeneratoren |
| [Detail panel](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/detail-panel) | Height-Producer, Kollisionsgitter, Biome und Spawnables |
| [Brush-System](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass) | Brush-Fußabdrücke und Aktualisierung von Terrain/Kollision |
| [Aktuelle Fab-Seite](https://www.fab.com/listings/ee4bcbaf-36ea-4dd9-aade-068e1a8a4794) | Angekündigter Funktionsumfang des 4.1-Ozeans |
| [Herstellerforum](https://forums.unrealengine.com/t/maximedupart-shader-world-plugin-procedural-terrain-oceans-foliage-gpu-accelerated/2721667) | Versionshistorie und ältere Beschreibungen |
| [Epic Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor) | Allgemeiner Editorzugriff und eigene Toolsets |

Die öffentlichen Anleitungen erklären einige aktuelle Arbeitsabläufe noch nicht vollständig. Besonders Ocean-Schaum und ComputeProducer wurden deshalb zusätzlich im installierten Plugin und am sichtbaren Ergebnis untersucht. Ein eigener Nachweis bleibt auf seinen angegebenen Prüfumfang begrenzt.

## Eigene Nachweise

- [Flaches Terrain](../evidence/terrain-report.json): Editor, PIE, Kollision und erneutes Laden.
- [CityLab](../evidence/citylab-report.json): Bauflächen und Straßen in sechs Prüfphasen.
- [Persistenz](../evidence/persistence-report.json): Erzeugen und Laden in getrennten Spielprozessen plus beobachteter UI-Test.
- [Ozean](../evidence/ocean-report.json): Parameter vorher/nachher und visuell bestätigter Schaum nach Rebuild.
- [Heightmap-Löcher](../evidence/hole-report.json): Komponenten, Ansicht und getrennt benannte Codebefunde; kein fertiger Bergtunnel.

Die JSON-Dateien sind ausgewählte Exporte der lokalen Prüfberichte. Private Dateipfade und unnötige Prozess-/Laufkennungen wurden entfernt; der fachliche Prüfumfang ist erhalten. Das JSON ist ein lesbarer Beleg, kein im Doku-Repository ausführbarer Unreal-Test.

## Bilder

Alle sieben Startbilder sind unveränderte native Viewport-Aufnahmen aus dem eigenen Lernprojekt vom **27. Oktober 2026**. Sie zeigen ShaderWorld-Demoinhalte beziehungsweise unsere Laboranordnung. Es sind keine generierten Illustrationen. Die dargestellten Plugin-/Demo-Inhalte stammen von ihren jeweiligen Rechteinhabern; das Repository verteilt keine Quelldateien dieser Inhalte.

| Bild | Aussage |
| --- | --- |
| [Reference-Übersicht](../assets/images/reference-overview.png) | Wald, Küste, Wasser und Straßentrasse im selben Beispiel |
| [Reference-Dreckweg](../assets/images/reference-road.png) | Geländeform und Materialwirkung entlang eines Splines |
| [Heightmap-Loch und Hinweistafel](../assets/images/heightmap-holes.png) | Lochbeispiel; die alte Texttafel enthält einen heute abweichenden Standardwert |
| [Ozean vor der Änderung](../assets/images/ocean-before.png) | Sichtbares Wasser bei ursprünglicher Konfiguration |
| [Ozean mit Schaum](../assets/images/ocean-foam-wind18.png) | Aktivierter Schaum nach Rebuild und Wind auf 18 m/s |
| [CityLab-Formen](../assets/images/citylab-terrain.png) | Technische Illustration von Bauplatz und Straßentrasse |
| [Flache Referenz](../assets/images/flat-terrain.png) | Flaches Terrain mit getrenntem Road-Creator-Pro-Testobjekt |

Aufnahmen vor/nach dem Ozeanversuch haben unterschiedliche Kamerawinkel; sie dienen als Ergebnisansichten, nicht als maßstäblicher Vergleich. Rote Lumen-Meldungen und sichtbare Hilfskästen wurden nicht retuschiert. Die Bilder enthalten keine Bestätigung einer fertigen Renderer-Konfiguration.

Dateigrößen und SHA-256-Hashes stehen im [Bildmanifest](../evidence/image-manifest.json).

## Neue CityBasics-Belege

Der [CityBasics-Bericht](../evidence/citybasics-report.json) enthält bereinigte native Kollisionsproben und tatsächliche CharacterMovement-Durchfahrten. Die [Waldstraße](../assets/images/citybasics-road.png) und [Portalzufahrt](../assets/images/citybasics-portal-approach.png) sind unveränderte native **CaptureEditorImage**-Aufnahmen vom 28. Oktober 2026 mit sichtbarer Editoroberfläche. Sie zeigen den spielbaren Prototyp; Fahrbahn, Portal und Testbuggy sind noch einfache Laborgeometrie. Größen und Hashes stehen im [Manifest](../evidence/image-manifest.json).

## Küsten-, Biom- und Straßenprüfung

Die [lesende Prüfung vom 28. Oktober 2026](../evidence/coast-biome-road-inspection.json) hält aktuelle PIE-Parameter, die Wassermaterial-Verkabelung, Pflanzen-Höhenintervalle und die tatsächliche Straßenherkunft fest. Sie enthält außerdem getrennte Asset-/Codebefunde und noch nicht ausgeführte Testvorschläge. Der vom Nutzer gemeldete Wellendurchbruch wurde dabei nicht reproduziert oder behoben.

Der [Korrekturbericht](../evidence/coast-correction-report.json) ergänzt die anschließend gespeicherten Projektfilter, Dämpfung 1,0 und den nativen Tunnel-Wasserausschluss. Er enthält Original-/Projektwerte sowie die Boxeigenschaften nach PIE-Neustart. Nutzerangabe zum Tunnel, Codebefund zum Hole-Sentinel und die erste Rückmeldung „Bisher trocken“ nach dem Fix sind getrennt erfasst; Langzeit- und gültige GPU-Prüfung fehlen weiterhin.

## Wiederverwendbare Tunnelkomponente

Der [Komponentenbericht](../evidence/tunnel-component-report.json) enthält den erfolgreichen nativen Build, zwei bestandene Automationtests und Eigenschaften der neuen **CityLab Tunnel (Dry)**-Komponente im Editor, nach tatsächlichem Kartenladen und im neu gestarteten PIE. Die API-Tests verwenden **NullRHI** und einen kontrollierten Wasserprovider im echten WaterSubsystem. Ihr Archive-/PostLoad-Test ist von der zusätzlichen echten Kartenladung getrennt. Ein frischer Spielprozess bestand danach 65/65 Kollisionsproben und rund 259,44 m bodengebundene Durchfahrt; der Gesamtbericht ist **passed_with_limits**. Die [neue native PIE-Aufnahme](../assets/images/citybasics-dry-tunnel-component.png) zeigt den sichtbaren Innenraum trocken; ein inspizierter Frame ist keine Langzeitabnahme. Herkunft und Hash stehen im [Bildmanifest](../evidence/image-manifest.json). Die frühere Nutzerantwort „Bisher trocken“ betrifft weiterhin die vorherige separate Box.

## Laufzeitstraßen im RoadLab

Der [RoadLab-Bericht](../evidence/runtime-roads-report.json) exportiert zwei erfolgreiche gerenderte uncooked Spielprozesse: je 72 Kollisionsproben, zwei Straßen mit 16 Meshsegmenten, identische logische Datensätze und Pflanzenursprünge im Trassenkern vor Bau, nach Bau/Laden, nach Rücknahme und nach erneutem Laden. Je Phase bleiben drei gleiche vollständige Matrix-Fingerprints erhalten. Die Herkunft der Rohdaten und Grenzen sind im JSON genannt; PIDs, Slot-/Laufkennungen und lokale Pfade wurden weggelassen. Format-1-Kompatibilität betrifft ein synthetisches Fixture, keinen archivierten historischen Spielstand.

Die [erste PIE-Aufnahme](../assets/images/runtime-road-first-pie.png) zeigt eine Beispielstraße; die [Aufnahme des bestandenen Create-Laufs](../assets/images/runtime-road-create-verified.png) zeigt zwei Straßen mit Markierungen. Die zusätzliche [normale PIE-Aufnahme nach Auto-Load](../assets/images/runtime-road-normal-autoload-pie.png) zeigt den durch R/Enter ergänzten und per K gespeicherten Stand nach erneutem Play; der zweite Straßenverlauf weicht deshalb vom nativen Fixture ab. Alle drei Bilder sind unveränderte, inspizierte native Frames vom 28. Oktober 2026. Die Vorbereitungsmeldung im Create-Bild gehört zum Testmodus. Bilder ersetzen keine Dauer-, GPU-Masken- oder Überhangmessung; Herkunft, Bytes und Hashes stehen im [Manifest](../evidence/image-manifest.json).

Der Bericht enthält außerdem die zusätzliche native Slate-Bedienprobe für R/Enter, Entwurfskorrektur, Q/E, K/L und normales PIE-Autoload sowie die frische Format-2-Regression der alten Bauplatzkarte. Kamerabewegung per ActorTools ist von ungeprüften WASD-/Maus-Eingaben getrennt; die PIE-Bedienprobe ist kein eigener Kaltstartprozess.

## OKF

Der [Google-Artikel](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/?hl=en) erläutert das Was und Warum von OKF anhand von v0.1. Für das Dateiformat dieser Wissensbasis gilt die [kanonische Spezifikation v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md). Die Formatversion ist im Wurzelindex festgehalten.
