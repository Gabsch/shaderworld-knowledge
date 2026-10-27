---
type: Guide
title: Löcher im Gelände und Eingänge für Bergtunnel
description: Die mitgelieferten Holebrushes ansehen und verstehen, was für einen befahrbaren Bergtunnel zusätzlich nötig ist.
tags: [shaderworld, terrain, holes, tunnels, collision, editor]
engine_version: "5.8.4"
plugin_version: "4.1"
status: draft
generated: { by: codex/gpt-6, at: "2026-10-27T21:49:03Z" }
evidence_scope:
  inspected: Holebrush-Beispiele der Heightmap-Karte im Editor und installierter ShaderWorld-4.1-Quellcode
  derived: Bauweise eines Bergtunnels aus Portalöffnungen und eigenen Tunnelmeshes
  not_tested: Vollständiger Bergtunnel, Fahrbetrieb, Navigation und verpackter Build
sources:
  - id: heightmap-view
    resource: ../assets/images/heightmap-holes.png
    title: Holebrush-Beispiele der Heightmap-Demo
  - id: brush-docs
    resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass
    title: Offizielle Einführung in das Brush-System
  - id: shaderworld-product
    resource: https://www.fab.com/listings/ee4bcbaf-36ea-4dd9-aade-068e1a8a4794
    title: Offizielle ShaderWorld-Produktbeschreibung
  - id: installed-hole-source
    resource: "Lizenzierte ShaderWorld-4.1-Installation: SW_HoleMeshBrushComponent.h/.cpp, ShaderWorldActor_Collision.cpp und SWPatchVertexFactory.ush; nicht im Bundle enthalten"
    title: Lokale Prüfung von Holebrush, Darstellung und Kollision
  - id: installed-tunnel-source
    resource: "Lizenzierte ShaderWorld-4.1-Installation: SWSplineRoadComponent.h, ShaderWorldSplineRoads.usf, ShaderWorldAirPocketComponents.h/.cpp und ShaderWorldVoxelActor.cpp; nicht im Bundle enthalten"
    title: Lokale Prüfung der Tunnel-, AirPocket- und Voxel-Grenzen
---
# Löcher im Gelände und Eingänge für Bergtunnel

ShaderWorld kann eine Fläche aus dem Gelände ausschneiden und dort auch die Terrainkollision entfernen. Ein solcher Ausschnitt ist ein Baustein für einen Tunneleingang. Den befahrbaren Tunnel mit Boden, Wänden und Decke musst du zusätzlich als Geometrie anlegen.[^installed-hole-source]

Die Holebrush-Beispiele wurden in der mitgelieferten Heightmap-Karte angesehen. Die nachfolgende Tunnelbauweise ist aus der Implementierung abgeleitet; ein vollständiger Bergtunnel wurde in diesem Versuch noch nicht gebaut oder durchfahren.

![Holebrush-Beispiele in der Heightmap-Demo](../assets/images/heightmap-holes.png)

Die Aufnahme zeigt die untersuchte Heightmap-Demo, keinen abgenommenen Bergtunnel.[^heightmap-view]

## Voraussetzungen

Du brauchst Unreal Engine 5.8.4 mit aktiviertem ShaderWorld 4.1. Die Beispiele sind Plugin-Inhalte. Dieses Dokumentations-Repository enthält weder das Plugin noch seine Karten. Für diesen Rundgang ist kein eigener C++-Code nötig.

## Die vorhandenen Löcher ansehen

1. Öffne im Content Browser die Einstellungen und aktiviere **Show Plugin Content** und bei Bedarf **Show Engine Content**. Öffne `/ShaderWorld/Maps/Map_Heightmap`.
2. Speichere für eigene Änderungen zuerst eine Kopie über **Save Current Level As** in deinem Projekt. In unserem Testprojekt heißt die Kopie `/Game/Maps/ShaderWorldTour_Map_Heightmap`.
3. Lass den Viewport in **Lit** mit **Realtime** laufen. Warte, bis Shaderkompilierung und Terrainaufbau fertig sind. Ein pausierter oder inaktiver Viewport kann die Aktualisierung verzögern.
4. Suche im World Outliner nach **BP_HoleBrush**, wähle ihn aus und drücke **F**, um ihn zu fokussieren. Wähle in seinen Komponenten **SW_HoleMeshBrush**. Prüfe **Enabled**. Schalte die Komponente probeweise aus, warte auf die Aktualisierung und schalte sie wieder ein. Der zugehörige Ausschnitt sollte verschwinden und zurückkehren.
5. Suche danach **SplineHoleBrush** und fokussiere ihn ebenfalls. Seine Spline und die Komponente **ProceduralHoleMeshComponent** beschreiben eine andere Lochform. Verschiebe zum Experimentieren einen Splinepunkt ein kleines Stück in der horizontalen Ebene und beobachte den veränderten Grundriss. Setze die Änderung anschließend zurück.

Das allgemeine Prinzip aus Gelände, Brush Manager und XY-Fußabdruck beschreibt auch die Herstellerdokumentation. Die konkreten Hole-Komponenten werden dort auf der verlinkten Einführungsseite nicht Schritt für Schritt erklärt.[^brush-docs]

## Die Form steuern

**BP_HoleBrush** verwendet ein Static Mesh als Schablone. In der Demo heißt die Komponente **MeshForBrush**. Ihre Geometrie wird von oben auf die XY-Ebene projiziert. Die Größe änderst du über das verwendete Mesh und dessen Skalierung; die angezeigte **Width** der Hole-Komponente wird daraus berechnet. Sie ist kein frei einstellbarer Radius.[^installed-hole-source]

Öffne bei einem eigenen Schablonenmesh dessen Static-Mesh-Editor und suche in den Asset-Details nach **Allow CPU Access**. Aktiviere die Einstellung und speichere das Mesh vor dem Verpacken. Der Brush benötigt seine Vertexdaten auch zur Laufzeit. Verwende dafür eine projektlokale Kopie des Assets. Das Schablonenmesh sollte selbst keine blockierende Kollision im späteren Durchgang haben.[^installed-hole-source]

**SplineHoleBrush** erzeugt seine Schablone prozedural aus der Spline. Hier entfällt der CPU-Zugriff auf ein Static-Mesh-Asset. Auch diese Variante erzeugt einen horizontalen Ausschnitt und kein dreidimensionales Abzugsvolumen.[^installed-hole-source]

## Darstellung und Kollision prüfen

Für die sichtbare Öffnung muss das Terrain-Oberflächenmaterial die Lochmaske aus **Vertex Color → R** als **Opacity Mask** verwenden und auf **Masked** stehen. Das Material der untersuchten Heightmap-Demo ist bereits entsprechend vorbereitet. Wenn du ein eigenes Material übernimmst, übernimm auch diese Maskierung; ändere dazu eine Projektkopie.[^installed-hole-source]

Für die Physik prüfst du am Terrain-Actor, in dieser Karte **BP_SWHeightmap**, dass **Generate Collision** eingeschaltet ist. Die Kollision wird um Spieler beziehungsweise Kollisionsanforderer herum erzeugt. Eine weit entfernte Editoransicht garantiert deshalb noch keine fertige Kollision am Loch.[^installed-hole-source]

Falls dein Spieler eine **SW_Collision**-Komponente trägt, prüfe dort **Prevent Falling Under Terrain**. Für unterirdische Wege muss diese Einstellung aus sein: Sie kann einen Spieler unter der Oberfläche sonst wieder nach oben teleportieren. Der aktuelle native Standard ist aus; ältere Demo-Hinweistexte beschreiben noch ein anderes Standardverhalten.

Erfolgreich ist der Versuch erst, wenn die Öffnung sichtbar ist und dort keine unsichtbare Terrainfläche blockiert. Für eine genaue Abnahme müssen Bodenabfragen außerhalb der Öffnung das Terrain treffen und innerhalb der Öffnung dessen Kollision verfehlen. Ein darunterliegendes Tunnel- oder Bodenmesh darf dabei natürlich einen eigenen Treffer liefern. Solche Kollisionsproben und ein Fahrtest sind für den geplanten Bergtunnel noch offen.

## Einen Eingang in einen Berg planen

ShaderWorld-Terrain beschreibt eine Höhe je XY-Position. Der Holebrush schneidet den gesamten horizontalen Fußabdruck aus; seine Z-Position begrenzt keinen unterirdischen Hohlraum. Eine senkrecht gestellte Portalscheibe ist daher keine geeignete Bohrschablone. Eine Schablone entlang der ganzen Tunnelstrecke würde auch die Bergoberfläche darüber öffnen.[^installed-hole-source]

Ein daraus abgeleiteter Aufbau für einen City Builder ist:

1. Lege die Trasse und die gewünschte Einfahrtshöhe fest. Führe die Zufahrt bis zum Hang und ebne dort nur den benötigten Vorplatz.
2. Öffne mit einem kleinen Holebrush den Grundriss am Hangdurchtritt. Prüfe die Öffnung aus der späteren Fahrperspektive, nicht nur von oben.
3. Setze einen Portalrahmen und das erste Tunnelstück so ein, dass sie die ausgeschnittenen Terrainränder überdecken. Passe Form und Überdeckung gemeinsam an.
4. Verlängere den Tunnel mit eigenen Meshes für Wände, Decke und Fahrbahn. Diese brauchen passende Kollision. Unterirdische Straßensegmente sollen die Geländeoberfläche darüber nicht nach unten ziehen; deaktiviere dort bei einer nativen ShaderWorld-Straßenkomponente **Deform Terrain**.
5. Wiederhole die Portalöffnung am Ausgang. Prüfe Fahrzeugdurchfahrt, Kollision und Navigation auf beiden Übergängen sowie im Tunnel.

Diese Schritte sind ein Bauvorschlag, keine bereits getestete Komplettlösung.

| Ähnlich benannte Funktion | Was sie für den Tunnel leistet |
| --- | --- |
| Road **Tunnel mode** | Regelt Höhenkonflikte kreuzender Straßen. Erzeugt keinen Tunnelkörper und keine automatische Bohrung durch einen Berg. |
| **AirPocket** | Hält Wasserabfragen und entsprechend maskiertes Wasser aus einem Innenraum heraus. Erzeugt keine Terrainöffnung und keine feste Tunnelwand. |
| Glastunnel aus **Map_Reference** | Zeigt Spline-Meshes und Unterwasserfunktionen. Das ist kein automatisch erzeugter Bergtunnel. |
| **Map_VoxelMap** | Enthält ein Voxel-/Octree-Beispiel. Ein fertiges Voxel-Höhlensystem wurde im untersuchten Bestand nicht belegt. |

Diese Abgrenzungen ergeben sich aus dem installierten Code und den Beispielassets.[^installed-tunnel-source] Der Hersteller führt Terrainlöcher und die Unterwasser-Glastunneldemo ebenfalls als getrennte Funktionen auf.[^shaderworld-product]

## Häufige Ursachen für ein falsches Ergebnis

| Beobachtung | Als Nächstes prüfen |
| --- | --- |
| Keine sichtbare Änderung | Realtime-Viewport, fertige Shader, Enabled und Zuordnung zum Brush Manager. |
| Gelände bleibt sichtbar, Kollision fehlt | Masked-Oberflächenmaterial und Vertex Color R als Lochmaske. |
| Sichtbares Loch, aber der Spieler kommt nicht hindurch | Fertige lokale Terrainkollision und zusätzliche Meshkollision im Ausschnitt. |
| Spieler springt auf den Berg zurück | Prevent Falling Under Terrain am Spieler prüfen. |
| Loch funktioniert im Editor, später nicht | Allow CPU Access des Schablonenmeshes vor dem Cook prüfen. |
| Bergdecke verschwindet über der ganzen Trasse | Holebrush auf die Portale begrenzen und den Tunnelkörper separat bauen. |

Speicherbare Tunnel brauchen später eigene Daten für Trasse, Profil, Portalformen und Mesh-Auswahl. Das bestehende [Spielstandlabor](save-and-load.md) speichert bisher nur Bauplätze und Straßentrassen.

[^heightmap-view]: [Aufnahme der untersuchten Heightmap-Beispiele](../assets/images/heightmap-holes.png).
[^brush-docs]: [ShaderWorld: Blueprint Brush System – Landmass](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass).
[^shaderworld-product]: [Offizielle ShaderWorld-Produktbeschreibung](https://www.fab.com/listings/ee4bcbaf-36ea-4dd9-aade-068e1a8a4794).
[^installed-hole-source]: Lokale Quellcodeprüfung von ShaderWorld 4.1: `SW_HoleMeshBrushComponent.h/.cpp`, `ShaderWorldActor_Collision.cpp`, `SWPatchVertexFactory.ush` und das Heightmap-Oberflächenmaterial. Die lizenzierten Plugin-Dateien werden nicht mit diesem Bundle verteilt.
[^installed-tunnel-source]: Lokale Quellcode- und Assetprüfung von ShaderWorld 4.1: `SWSplineRoadComponent.h`, `ShaderWorldSplineRoads.usf`, `ShaderWorldAirPocketComponents.h/.cpp`, `ShaderWorldVoxelActor.cpp` und die Tunnelbeispiele. Die lizenzierten Plugin-Dateien werden nicht mit diesem Bundle verteilt.
