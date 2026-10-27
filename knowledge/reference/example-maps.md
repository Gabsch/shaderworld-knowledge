---
type: concept
title: 'Die installierten Beispielkarten erkunden'
description: 'Reference, Heightmap und OceanOnly als Projektkopien öffnen und ihre City-Builder-Beispiele gezielt finden.'
tags:
  - shaderworld
  - unreal-engine
  - examples
  - terrain
  - city-builder
status: stable
sources:
  - id: official-kickstart
    resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start
    title: 'Offizieller Einstieg über die mitgelieferten Beispielkarten'
  - id: official-brushes
    resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass
    title: 'Offizielle Brush-Dokumentation mit Verweis auf Map_Reference'
  - id: reference-view
    resource: ../assets/images/reference-overview.png
    title: 'Ansicht der Reference-Projektkopie'
  - id: reference-road
    resource: ../assets/images/reference-road.png
    title: 'Straßenbeispiel der Reference-Projektkopie'
  - id: heightmap-view
    resource: ../assets/images/heightmap-holes.png
    title: 'Heightmap-Projektkopie mit Lochbeispielen'
  - id: ocean-proof
    resource: ../evidence/ocean-report.json
    title: 'Beobachtungsbericht zum isolierten Ocean-Test'
generated:
  by: codex/gpt-6
  at: '2026-10-27T21:48:46Z'
engine_version: '5.8.4'
plugin_version: '4.1'
evidence_scope: 'Installierte Karten und Assetverweise statisch verglichen; Reference-, Heightmap- und OceanOnly-Kopien im Testprojekt visuell geöffnet. Screenshots und Ocean-Bericht belegen die beschriebenen Ansichten, keinen vollständigen Laufzeittest sämtlicher Beispiele.'
---

# Die installierten Beispielkarten erkunden

Die große Landschaft mit verschiedenen Bodenarten, Vegetation, Ozean und Testbereichen ist **Map_Reference**. Sie liegt bereits im ShaderWorld-Plugin. Ein zusätzliches Beispielprojekt ist für diese Welt nicht nötig. Auch die offizielle Brush-Dokumentation verweist auf sie als Referenz.[^official-kickstart][^official-brushes]

## Drei vorbereitete Projektkopien

Im untersuchten Testprojekt wurden diese Karten angelegt. Die Namen unter `/Game` gehören zu diesem Projekt und entstehen nicht automatisch bei jeder Plugininstallation.

| Projektkopie | Original im Plugin | Wofür sie sich eignet |
| --- | --- | --- |
| `/Game/Maps/ShaderWorldReferenceTest` | `/ShaderWorld/Maps/Map_Reference` | Die umfangreiche Gesamtwelt: Landschaft, verschiedene Bodenmaterialien, Wald und Gras, Ozean, Straßen- und Tunnelbeispiele. |
| `/Game/Maps/ShaderWorldTour_Map_Heightmap` | `/ShaderWorld/Maps/Map_Heightmap` | Höhenkarten-Terrain, Spline-, Loch- und PCG-Beispiele untersuchen. |
| `/Game/Maps/ShaderWorldTour_Map_OceanOnly` | `/ShaderWorld/Maps/Map_OceanOnly` | Wasser, Wasserlinie, Niagara-Abfragen und Schaum ohne die übrige Landschaft untersuchen. |

Die Reference-Kopie hat 657.010 Byte. Das Original im Plugin blieb unverändert. Kleine Map-Dateien können große prozedurale Welten beschreiben; ihre Dateigröße ist kein Maß für die räumliche Weltgröße.

## Eine Karte öffnen oder selbst kopieren

1. Öffne den **Content Browser**. Sind die vorbereiteten Kopien vorhanden, gehe zu **Content → Maps** und öffne die gewünschte Karte per Doppelklick.
2. Für Pluginoriginale öffne im Content Browser **Settings** und aktiviere **Show Engine Content** sowie **Show Plugin Content**.
3. Navigiere links zu **Engine → Plugins → ShaderWorld Content → Maps**. Dort liegen die Originale **Map_Reference**, **Map_Heightmap** und **Map_OceanOnly**.
4. Öffne eine Originalkarte. Wähle **File → Save Current Level As** und speichere sie unter **Content → Maps** mit einem eigenen Namen. Verwende für diese Anleitung die Namen aus der Tabelle.
5. Warte nach dem Laden auf Shaderkompilierung und lass den Viewport aktiv rendern. Falls Gelände zunächst fehlt, aktiviere Echtzeit im Viewport oder starte **Play**.

Damit bleiben Versuche im Projekt nachvollziehbar. Die Originalkarten stehen weiter zum Vergleichen bereit.[^official-kickstart]

## Reference: die Gesamtwelt für den City Builder

![Gesamtansicht der Reference-Welt](../assets/images/reference-overview.png)

*Die Reference-Kopie zeigt den Zusammenhang von Landschaft, Oberflächen und Vegetation.*[^reference-view]

Für einen ersten Rundgang sind folgende Objekte hilfreich. Suche ihre Namen im **Outliner**, wähle sie aus und drücke im Viewport **F**, um die Auswahl zu fokussieren. Einige Brush- oder Hilfsobjekte sind selbst unsichtbar; entscheidend ist ihre Wirkung auf das Gelände.

| Name oder Asset | Was daran interessant ist |
| --- | --- |
| `BP_SWGround` | Das Gelände der Referenzwelt; hier lohnt sich der Blick auf Producers und Oberflächenmaterial. |
| `BP_SWOcean` | Das Meer derselben Welt. Reference besitzt bereits einen SpectrumProducer und die Wasserlinienanbindung. |
| `SplineRoadDemo`, `SplineRoadDemo2` | Straßenbeispiele mit der nativen `SWSplineRoadComponent`. |
| `SplineMaskDemo` | Ein Beispiel für einen entlang einer Spline beeinflussten Bereich. |
| `BP_Home` | Eine Kombination vorhandener Heightmap-/Mesh-Brush-Komponenten. |
| `/ShaderWorld/Spawnables/SW_GreenBiom` | Vegetationskonfiguration mit Bäumen, Gras und Felsen. |

Die statisch untersuchte Vegetationskonfiguration verweist auf BlackAlder-Bäume, Boulder-Felsen, nahes und fernes FreeGrass sowie ein Dichtematerial namens `M_Density_NotRoad1`. Das liefert eine Referenz dafür, Vegetation an Straßen auszuschließen. Das Aussehen hängt vom Generationsstand und Kamerastandort ab; eine persistente Rodungssimulation ist damit nicht geprüft.

![Straßenbeispiel in der Reference-Kopie](../assets/images/reference-road.png)

*Ein vorhandenes Straßenbeispiel als Ausgangspunkt für eigene Trassen.*[^reference-road]

Die Bodenoberfläche verweist auf Texturarrays für Farbe, Normalen und weitere Materialdaten sowie Triplanar- und POM-Funktionen. Die Reference zeigt damit deutlich mehr als das einfache Material einer kleinen flachen Testkarte. Das Vorhandensein dieser Funktionen belegt jedoch keine abgeschlossene Leistungsoptimierung für eine große Stadt.

## Heightmap: Löcher und vorbereitete Geländedaten

![Heightmap-Kopie mit Lochbeispielen](../assets/images/heightmap-holes.png)

*Die Heightmap-Welt wurde als zusätzliche Karte geöffnet; hier lassen sich Aussparungen im Terrain betrachten.*[^heightmap-view]

Öffne **ShaderWorldTour_Map_Heightmap** und suche im Outliner nach **Hole**, **Spline** oder **PCG**. Die installierte Map enthält unter anderem `BP_HoleBrush`, `SplineHoleBrush`, einen `BP_Spline` und ein PCG-Volume. Der PCG-Graph heißt `/ShaderWorld/BP/PCG/Graph_SWMeshToPointsWithLayer` und referenziert Beispielbäume aus dem PCG-Plugin.

Für einen City Builder sind daran die Kombination von vorgegebenen Höhenkarten, Einschnitten und ausgeschlossenen Bereichen interessant. Ob ein konkretes Loch die gewünschte Kollision, Navigation und Spielfunktion liefert, muss im eigenen Anwendungsfall geprüft werden. Diese Seite belegt die vorhandenen Beispiele und ihre Ansicht.

## OceanOnly: Wasser gezielt untersuchen

Die OceanOnly-Kopie isoliert den Ozean und enthält zusätzlich einen Niagara-Actor mit `NS_WaterTest`. Der frühere Pfad `/ShaderWorld/Demo_Ocean/VFX/NS_WaterTest` ist ein Redirector auf `/ShaderWorld/Demo_Ocean/FX/NS_WaterTest`.

Reference enthält bereits denselben Typ von SpectrumProducer, Ozeanmaterial und Wasserlinienanbindung. OceanOnly ergänzt deshalb vor allem eine übersichtliche Versuchsumgebung und den Niagara-Wasserabfragetest. Den bestätigten Schaumversuch mit **Wind Speed 18 m/s** und verarbeitetem **Rebuild** beschreibt die [Ozean-Klickanleitung](../guides/ocean-waves-and-foam.md).[^ocean-proof]

## Weitere installierte Karten

| Originalpfad | Schwerpunkt aus der statischen Prüfung |
| --- | --- |
| `/ShaderWorld/Maps/Map_Blank` | Einfache Ausgangswelt für eigene Generatoren. |
| `/ShaderWorld/Maps/Map_CPU` | Technischer CPU-Generator und Schreiben in ein Render Target. |
| `/ShaderWorld/Maps/Map_TextureArrayMaterials` | Material-/Texturarray-Beispiel mit `Mat_Numbers`. |
| `/ShaderWorld/Maps/Map_Triplanar` | Demonstration des Materials `M_Triplanar_demo`. |
| `/ShaderWorld/Maps/Map_VoxelMap` | `ShaderWorldVoxelActor`, Voxelgenerator sowie Heightmap-, Spline- und Loch-Brushes. |
| `/ShaderWorld/TestAssets/SWEntityFarmTest` | Separates Testlevel außerhalb des Maps-Ordners. |

Diese zusätzlichen Karten wurden für diese Übersicht statisch inventarisiert. Eine vollständige visuelle oder spielmechanische Abnahme aller Karten ist damit nicht behauptet.

## Alte und aktuelle Beispiele auseinanderhalten

Die untersuchte UE-5.5-Installation verwendet ShaderWorld **3.9.96**, die UE-5.8-Installation **4.1**. Beide enthalten `/ShaderWorld/Maps/Map_Reference`. In 3.9.96 referenziert sie unter anderem `BP_BrushManagero`, `BP_Spline` und `SplineMaskBrush`; die aktuelle Referenz enthält einen nativen `ShaderWorldBrushManager`, native Straßenkomponenten, GPU-PCG- und Tunnelbeispiele. Die frühere zusätzliche `Map_NewReferenceWIP1` ist in der untersuchten 4.1-Installation nicht enthalten.

Alte Projekte sind nützliche Vergleichsquellen. Für neue Arbeit zuerst die Beispiele der passenden aktuellen Pluginversion verwenden und benötigte Assets gezielt mitsamt ihren Abhängigkeiten in das eigene Spielprojekt übernehmen.

[^official-kickstart]: [Offizielle Dokumentation: Kick-start](https://universgen.gitbook.io/shader-world/fundamentals/kick-start).
[^official-brushes]: [Offizielle Dokumentation: Blueprint Brush System](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass).
[^reference-view]: [Reference-Gesamtansicht](../assets/images/reference-overview.png).
[^reference-road]: [Reference-Straßenbeispiel](../assets/images/reference-road.png).
[^heightmap-view]: [Heightmap-Ansicht](../assets/images/heightmap-holes.png).
[^ocean-proof]: [Beobachtungsbericht zum Ocean-Test](../evidence/ocean-report.json).
