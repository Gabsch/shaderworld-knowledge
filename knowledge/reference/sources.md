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
  at: '2026-10-27T21:55:15Z'
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

## OKF

Der [Google-Artikel](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/?hl=en) erläutert das Was und Warum von OKF anhand von v0.1. Für das Dateiformat dieser Wissensbasis gilt die [kanonische Spezifikation v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md). Die Formatversion ist im Wurzelindex festgehalten.
