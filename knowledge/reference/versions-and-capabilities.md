---
type: Playbook
title: Versionen und Fähigkeiten
description: Den alten UE-5.5-Bestand mit ShaderWorld 4.1 vergleichen und nächste
  Tests einordnen.
tags:
- shaderworld
- unreal-engine
- city-builder
status: stable
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: Lokaler Versions-/Sourcevergleich, Herstellerangaben und thematisch
  getrennte Tests
generated:
  by: codex/gpt-6
  at: "2026-10-30T20:47:06.231484+00:00"
sources:
- id: rcp-stage1
  resource: ../evidence/rcp-toolkit-stage1.json
  title: Separater RCP-Bestand mit 907 Paketen, nativer Reflexion, negativem Raw20 und bestandenem begrenztem Eigenadapter20
- id: local-comparison
  resource: Local licensed ShaderWorld 3.9.96 and 4.1 installation comparison
  title: Lokaler Versions- und API-Vergleich
- id: history
  resource: https://forums.unrealengine.com/t/maximedupart-shader-world-plugin-procedural-terrain-oceans-foliage-gpu-accelerated/2721667
  title: Herstellerhistorie
- id: fab
  resource: https://www.fab.com/listings/ee4bcbaf-36ea-4dd9-aade-068e1a8a4794
  title: Aktuelle Produktseite
- id: detail-panel
  resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/detail-panel
  title: Spawnables und Detail panel
- id: pcg
  resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/pcg-procedural-content-generation-framework
  title: Kollisionsbasierte PCG-Anleitung
---


# Versionen und Fähigkeiten

Der folgende historische Pluginvergleich gilt für **Unreal Engine 5.8.4 und ShaderWorld 4.1**. Das inzwischen geprüfte [RoadConstruction11-Straßenlabor](../guides/road-construction-tools.md) verwendet ShaderWorld 4.2; seine Abnahme wird nicht rückwirkend dem älteren Vergleich zugeschrieben. In der alten UE-5.5-Installation wurde **ShaderWorld 3.9.96** gefunden; das alte Beispielprojekt verwendet UE 5.5.4 und enthält Logs vom Juli 2025. Dieser installierte Altbestand passt zeitlich zum früheren Versuch. Er belegt nicht lückenlos, welche Plugindateien bei jedem damaligen Start geladen waren.[^local-comparison]

## RCP-Update: eigener Bestands- und Prüfstand

Road Creator Pro ist ein zusätzliches Content-Assetpack. Nach dem Nutzerupdate wurden **907 Pakete statt zuvor 673** erfasst, einschließlich nun vorhandener Helper-, Parking-, Utility-, LowPoly-/Mirage- und Gebäudegruppen. Die genaue Releasekennung und vollständige Übereinstimmung mit dem aktuellen Herstellerhandbuch bleiben ungeklärt. Der Bestand, sechs gemeldete fehlende Materialverweise, 18 eigene vorbereitete Meshkopien und abgegrenzte Geometriemessungen stehen im [RCP-Integrationsplan](road-creator-pro-runtime-plan.md).[^rcp-stage1]

Die getrennten 128 nativen CityLab-Modell-/API-Tests sind bestanden, mit 126 sauberen Tests und zwei bekannten Warnungen. Ein frischer gekochter Deferred-Spawn ist inzwischen belegt; **alle 20 direkten UCS-Neuaufbauzyklen sind fehlgeschlagen**. Der erste eigene Adapter scheiterte am exakten inneren Kollisionsstoß. Nach begrenzter Geometriekorrektur besteht die zweite getrennt gekochte Eigenadapterprobe alle **20 Zyklen**, Profil-/Material-/Leitplankenwechsel, 300 Szene-/300 Bodytreffer und vollständige Objektbereinigung. Alle sechs Schutzgruppen einschließlich 362 vorhandener Saves bleiben exakt unverändert; Nähte zwischen unabhängigen Outputactoren bleiben gesondert zu prüfen. Daraus folgt weder eine allgemeine Blueprint-Unmöglichkeit noch eine vollständige RCP-, Fahr-, Bedien- oder Neustartfreigabe. Der geprüfte normale Straßenstarter und die alten Spielstände bleiben getrennt.[^rcp-stage1]

## Was schon früher vorhanden war

Producers gab es bereits im untersuchten 3.9.96-Bestand. Auch Terrainlöcher, Spline-Grundlagen, PCG und Biome sind nicht pauschal Neuerungen von 4.1. Die Herstellerhistorie nennt PCG für 3.0, Splines/Biome für 3.2 und Löcher für 3.6.[^history]

## Welche neuen Bausteine wir im aktuellen Bestand fanden

| Baustein | Befund im Vergleich mit 3.9.96 | Unser praktischer Stand |
| --- | --- | --- |
| Native SWSplineRoadComponent | Im alten untersuchten Source nicht gefunden | Geländeformung und Kollision im CityLab geprüft |
| GPU-PCG-Terraintexturen | Neue native Schnittstelle im aktuellen Bestand | Quelle/Referenzasset untersucht, keine eigene Leistungsabnahme |
| Compute Producer | Zusätzlicher Weg neben materialbasierter Erzeugung | Aktiver SpectrumProducer am Ozean ausgelesen |
| WaterSubsystem, Buoyancy, Niagara, AirPockets | Zusätzliche Klassen im aktuellen Bestand | Wasser/Wind/Schaum gezeigt; Auftrieb und Mehrspielerbetrieb offen |
| Native TerrainRegion-/VirtualTexture-Typen | Zusätzliche C++-Typen im aktuellen Bestand; VT-/VHM-Beispiele gab es schon im Altbestand | Keine eigene produktive Einrichtung geprüft |

Die Tabelle beschreibt den untersuchten Dateivergleich, nicht das genaue Einführungsdatum jeder Klasse. Die aktuelle Produktseite nennt FFT, CPU-Wasserabfragen, Auftrieb, Niagara und Unterwasserfunktionen ausdrücklich für den ausgebauten 4.1-Ozean.[^fab]

## Biome und Vegetation für die Stadt

Die Reference-Welt zeigt das Biom `SW_GreenBiom` mit Bäumen, Felsen und Gras. In dessen Abhängigkeiten liegt unter anderem `M_Density_NotRoad1`; Straßen und Vegetation können also auf gemeinsame Geländedaten und Masken reagieren. Die sichtbare Reference-Trasse wurde untersucht. Eine eigene Verwaltung einzelner gefällter Bäume ist noch nicht implementiert. Im getrennten [RoadLab](../guides/runtime-roads.md) ist inzwischen das Wiederherstellen der Straßenmaske aus gespeicherten Trassen in einem neuen Prozess geprüft: Die gemessenen Instanzursprünge im Kern verschwanden, wuchsen nach Rücknahme nach und verschwanden nach Laden erneut. Das ist kein allgemeiner Rodungs-/Ressourcenzustand und keine Überhangprüfung.

Die offizielle Spawnable-Doku beschreibt eine wichtige Grenze: eingesammelte Ressourcen besitzen dort standardmäßig kein dauerhaftes Bookkeeping und können nach Verlassen und Wiederbetreten der Generationsreichweite wieder erscheinen. Für einen City Builder brauchen gerodete Bauflächen deshalb einen bestätigten dauerhaften Zustand.[^detail-panel]

Die klassische PCG-Anleitung arbeitet mit Kollision, dem Actor-Tag `SW` und einer `SW_Collision`-Komponente am PCG-Volume. Die aktuelle GPU-Schnittstelle ist ein zusätzlicher Weg; aus der älteren Anleitung allein ergibt sich ihre Einrichtung nicht.[^pcg]

## Was vor einer großen Spielwelt noch fehlt

- Eigene farbige Biome und dauerhaft gespeicherte Bau-/Rodungsmasken testen.
- Navigation nach Gelände- und Gebäudeänderungen nachführen.
- Höhenabfragen, Kollisionsanforderungen und weite Baukamera gemeinsam abstimmen.
- Viele Änderungen, große Karte, Streaming und Speicher-/Framebudgets messen.
- Verpackten Build, Mehrspielerfälle und SaveGame-Migration prüfen.
- Eigenen Bergtunneleingang mit Fahrbahn, Wänden, Decke und Kollision bauen.

Die vorhandene `Map_VoxelMap` und Voxeltypen sind kein belegter fertiger Höhlen-Workflow. Im untersuchten Code ist die Isosurface-Erzeugung ausdrücklich noch nicht als fertige Extraktion umgesetzt. Für unsere Tunnelplanung gilt daher zunächst der [Höhenfeld- und Portalansatz](../guides/holes-and-mountain-tunnels.md).

[^local-comparison]: Lokaler Lesevergleich der lizenzierten ShaderWorld.uplugin- und Source-Bestände für UE 5.5 und UE 5.8; eigene Zusammenfassung, keine Veröffentlichung der Plugindateien.
[^history]: [Versionshistorie des Entwicklers](https://forums.unrealengine.com/t/maximedupart-shader-world-plugin-procedural-terrain-oceans-foliage-gpu-accelerated/2721667).
[^fab]: [Aktuelle ShaderWorld-Produktseite](https://www.fab.com/listings/ee4bcbaf-36ea-4dd9-aade-068e1a8a4794).
[^detail-panel]: [Detail panel mit Spawnables-Grenzen](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/detail-panel).
[^pcg]: [Offizielle PCG-Anleitung](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/pcg-procedural-content-generation-framework).

[^rcp-stage1]: [Bereinigter Stage1-Bestands- und Prüfbericht](../evidence/rcp-toolkit-stage1.json).
