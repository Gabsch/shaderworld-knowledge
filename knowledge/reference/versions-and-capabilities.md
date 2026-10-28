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
  at: '2026-10-28T01:51:24Z'
sources:
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

Der aktuelle Wissensstand gilt für **Unreal Engine 5.8.4 und ShaderWorld 4.1**. In der alten UE-5.5-Installation wurde **ShaderWorld 3.9.96** gefunden; das alte Beispielprojekt verwendet UE 5.5.4 und enthält Logs vom Juli 2025. Dieser installierte Altbestand passt zeitlich zum früheren Versuch. Er belegt nicht lückenlos, welche Plugindateien bei jedem damaligen Start geladen waren.[^local-comparison]

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
