---
type: Reference
title: ShaderWorld-Datenlayer und dauerhafter Spielstand
description: Räumliche Terrain-Daten, gespeicherte Projektkarten, transiente GPU-Caches und unsere eigene Persistenz auseinanderhalten.
status: draft
tags: [shaderworld, data-layers, persistence, savegame, city-builder]
engine_version: "5.8.4"
plugin_version: "4.1"
generated:
  by: codex/gpt-6
  at: "2026-10-29T00:01:27Z"
evidence_scope: Herstellerdokumentation und lesende Quellprüfung der installierten Version 4.1; kein neuer Layer-, Export-, Persistenz- oder cooked Laufzeittest.
sources:
  - id: manufacturer
    resource: https://www.shader.world/
    title: Herstellerbeschreibung der Landscape Data Layers
  - id: brush-layer
    resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/heightmap-import-16-bits-raw-png
    title: Heightmap Brush schreibt Datenlayer im Reference-Beispiel
  - id: detail-panel
    resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/detail-panel
    title: Cache, Producer, Spawnables und fehlende dauerhafte Ressourcenbuchhaltung
  - id: audit
    resource: ../evidence/shaderworld-storage-source-audit.json
    title: Bereinigter Quellbefund mit untersuchten Symbolen und Grenzen
  - id: current-saves
    resource: ../guides/save-and-load.md
    title: Vorhandene eigene CityLab-Persistenz mit getrennten Laufzeitnachweisen
  - id: next-plan
    resource: scaping-machine-work-plan.md
    title: Beschlossener nächster Maschinen-/Scaping-Slice
---
# ShaderWorld-Datenlayer und dauerhafter Spielstand

**Daten neben dem Terrain speichern** und **das Spiel nach einem Neustart fortsetzen** sind unterschiedliche Aufgaben. ShaderWorld bietet räumliche Datenlayer für seine Terrainverarbeitung. Der Hersteller nennt unter anderem Biom, Bodenmaterial, Feuchtigkeit und Temperatur. Brushes können in Layer schreiben; Terrainmaterial und Bewuchs können diese Informationen auswerten.[^manufacturer][^brush-layer]

Der Quellbefund zur installierten Version **4.1** bestätigt benannte Producer mit Generatormaterial, Texturformat und Filter. Die Daten werden räumlich auf dem Terrain bereitgestellt. Daraus folgt noch keine Speicherung ihrer GPU-Inhalte auf Datenträger oder in einer Laufzeit-Mapdatei.[^audit]

## Was wir wo ablegen wollen

| Inhalt | Vorgeschlagener Ort |
| --- | --- |
| Feste Startwelt, Generatoren, redaktionell platzierte Brushes | Projektkarte und passende Projektassets, die mit dem Spiel ausgeliefert werden. |
| Bodenart, Feuchtigkeit, Freistellung, später Verdichtung und Bauvisualisierung | ShaderWorld-Layer als räumliche Projektion des generierten oder gespeicherten fachlichen Zustands. |
| Baumkennungen, Grundstücke, Straßen-Splines, Planrevisionen, Maschinenfortschritt | Unsere dauerhafte Spielstandverwaltung mit stabilen Identitäten. |
| Exakte Grammkonten, Lager, Reservierungen, Lkw-Ladungen und Transportschritte | Dieselbe autoritative Spielstandverwaltung; keine alleinige Ablage in GPU-Farbkanälen. |
| Später sehr viele Geländeänderungen | Bei nachgewiesenem Bedarf regionale Checkpoints plus jüngere Änderungen, gemeinsam versioniert mit dem Spielstand. Noch kein implementiertes Format. |

Der Spieler soll einen zusammengehörigen Spielstand speichern und laden. Eine spätere interne Aufteilung in regionale Dateien darf nicht zu teilweise neuen Materialkonten und teilweise altem Gelände führen. Dafür wären gemeinsame Checkpointkennung, Welt-/Generatorbindung und ein geprüftes Commit-/Wiederherstellungsverfahren nötig.[^next-plan]

## Welche nativen Namen noch keinen Speichervertrag belegen

| Geprüfter Bereich | Quellbefund in der installierten Version 4.1 |
| --- | --- |
| `USWStorageBase` | Zielpfad, transienter Trigger und leere TerrainStorage-Klasse gefunden; kein fertiger Save-/Load-Vertrag. |
| `ApplyBrushToCache` | Im untersuchten Pfad nicht implementierter Schreibbereich; kann trotzdem true zurückgeben. Nicht als funktionierendes dauerhaftes SetData verwenden. |
| `ExportCacheInBounds` | Kopiert Daten in RenderTargets, schreibt keinen Spielstand auf Datenträger. Ein positives Ergebnis allein belegt nicht jeden inneren Exportpfad. |
| `ProduceTerrainRegion` | Exportiert Höhe, Normalen und optionale Layer in transiente GPU-Targets. Bereitschaft, Bereich und Auflösung sind zu beachten; kein Diskwrite. |
| `UShaderWorld_TiledData`-Hilfen | Untersuchte AddData-/Bounds-/Hierarchie-/Mip-Hilfen sind leer. Daraus keine fertige Tile-Datenbank ableiten. |
| Heightmap-Import und `SavePackage` | Gefundene Dateispeicherung gehört zum Editor-Assetimport. Diese Pfade belegen kein Laufzeit-Saveformat für ein verpacktes Spiel. |

Diese Aussagen gelten für die untersuchten Dateien der installierten Version. Sie behaupten weder, dass jede denkbare Pluginerweiterung unmöglich ist, noch dass spätere Versionen denselben Stand haben. Details und genaue Quellstellen stehen im [Quellbefund](../evidence/shaderworld-storage-source-audit.json); lizenzierter Code wird nicht mitgeliefert.[^audit]

## Wie wir die Layer sinnvoll nutzen

Nach dem Laden stellen wir den fachlichen Stadtzustand wieder her und erzeugen daraus Terrain, Oberflächenzustände und Masken. ShaderWorld wertet diese räumlichen Daten für sichtbaren Boden und Spawnregeln aus. Die bereits eigene Baumverwaltung bleibt nötig: Die Herstellerdokumentation beschreibt ausdrücklich keine dauerhafte Buchhaltung eingesammelter Spawnables.[^detail-panel]

Zunächst keine komplette Stadt-ID oder exakten Lagerbestand in Farbkanäle packen. Formate, Filterung, Auflösung und LOD können ihre Bedeutung ändern. Diskrete Kennungen und weiche Gewichte benötigen unterschiedliche Behandlung. Die Wahl eines geeigneten Layers ersetzt zudem keine CPU-Abfrage, verlässliche Kollisionsbereitschaft oder geprüfte Speicherung.

## Kleine nächste Untersuchung

1. Einen zusätzlichen eigenen Layer mit klarer Bedeutung anlegen, etwa Bodenklasse oder Baufreigabe. Vorhandene Material-/Biomkanäle erhalten.
2. Einen kleinen Bereich über einen nachvollziehbaren Brush-/Producerpfad verändern; Sichtanzeige, Bewuchsauswertung und geeigneten Readback separat prüfen.
3. Bereich verlassen, tatsächliche Regeneration auslösen und zurückkehren. Die Bedeutung muss erhalten beziehungsweise aus dem gespeicherten Zustand korrekt rekonstruiert werden.
4. In einem neuen Spielprozess laden; Ausgangsdaten, Layerergebnis und unveränderte Kontrollen vergleichen. Anschließend im verpackten Spiel wiederholen.
5. Erst aus diesen Ergebnissen entscheiden, ob ein zusätzlicher regionaler Snapshot Nutzen bringt. Messgrößen: Ladezeit, Dateigröße, Speicherbedarf, Bearbeitungskosten und Wiederherstellung.

**Prüfstatus:** reine Dokumentations-/Quellprüfung. Der beschriebene zusätzliche Layer-Neustartversuch ist geplant, noch nicht durchgeführt. Die vorhandenen [CityLab-Speichernachweise](../guides/save-and-load.md) gelten weiterhin nur für ihren jeweiligen dokumentierten Umfang. Eine im Editor gespeicherte `.umap` ist kein Nachweis, dass während des Spiels erzeugte Änderungen automatisch in diese Karte zurückgeschrieben werden.

[^manufacturer]: [Shader World](https://www.shader.world/), Herstellerbeschreibung Landscape Data Layer System.
[^brush-layer]: [Heightmap-Brush und Datenlayer](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/heightmap-import-16-bits-raw-png).
[^detail-panel]: [Detail panel](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/detail-panel), Producer/Cache/Spawnables; fehlendes Ressourcen-Bookkeeping ausdrücklich beschrieben.
[^audit]: [Quellprüfung ShaderWorld 4.1](../evidence/shaderworld-storage-source-audit.json); keine neue Laufzeitabnahme.
[^next-plan]: [Beschlossener Scaping-/Maschinenplan](scaping-machine-work-plan.md).
