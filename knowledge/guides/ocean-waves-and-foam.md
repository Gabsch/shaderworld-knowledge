---
type: concept
title: Ozean, Wellen und Schaum im Editor einstellen
description: Schaum und Wind einstellen; Küstendämpfung, Wasser unter Inseln und
  trockene Tunnel anhand von Beobachtungen und Codebefunden unterscheiden.
tags:
- shaderworld
- unreal-engine
- ocean
- foam
- editor
status: stable
sources:
- id: ocean-proof
  resource: ../evidence/ocean-report.json
  title: Beobachtungsbericht zum Ocean-Test
- id: fab-ocean
  resource: https://www.fab.com/listings/ee4bcbaf-36ea-4dd9-aade-068e1a8a4794
  title: Offizielle Produktseite mit Ocean-Funktionen von ShaderWorld 4.1
- id: detail-panel
  resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/detail-panel
  title: 'Offizielle Dokumentation: Producers und World Settings'
- id: ocean-api
  resource: 'Lizenzierte ShaderWorld-4.1-Installation: ShaderWorldComputeProducer.h,
    ShaderWorldActor_Build.cpp und NiagaraDataInterfaceShaderWorldWater.h; nicht im
    Bundle enthalten'
  title: Geprüfte native Wellen-, Schaum- und Niagara-Schnittstellen
- id: coast-inspection
  resource: ../evidence/coast-biome-road-inspection.json
  title: Insel-/Ozeaneinstellungen und Materialanschluss; Fehlerursache noch offen
- id: coast-water-code
  resource: 'Lizenzierte ShaderWorld-4.1-Installation: Source/ShaderWorld/Public/Producers/ShaderWorldComputeProducer.h,
    Shaders/Private/ShaderWorldComputeProducers.usf, Source/ShaderWorld/Public/Water/ShaderWorldAirPocketComponents.h,
    Source/ShaderWorld/Public/MaterialInterface/ShaderWorldWaterExclusion.h,
    Source/ShaderWorld/Private/Water/ShaderWorldWaterSubsystem.cpp und ShaderWorldOceanWaterProvider.h;
    nicht im Bundle enthalten'
  title: Gelesene Küstendämpfung, Wasserausschlüsse und Grenzen der CPU-Wasserabfragen
generated:
  by: codex/gpt-6
  at: '2026-10-27T23:19:32Z'
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: 'Editorversuch an einer Projektkopie von Map_OceanOnly: Parameter
  gelesen, Schaum aktiviert, WindSpeed auf 18 m/s gesetzt, Rebuild ausgelöst und sichtbarer
  Schaum gerendert. Weitere Funktionen teilweise nur aus installierter API und offizieller
  Produktbeschreibung eingeordnet. Ergänzung vom 28. Oktober: CityBasics-Parameter
  in PIE gelesen, Wasser-Exclusion im Materialgraph geprüft und Küstendämpfung,
  Air Pockets sowie CPU-Abfragen im Code geprüft;
  kein bestätigter Fix für Wasser über dem Inselboden und kein praktischer Air-Pocket-Test.'
---
# Ozean, Wellen und Schaum im Editor einstellen

In ShaderWorld 4.1 lässt sich das Meer direkt an einem Ozean-Actor einstellen. Für den hier beschriebenen Versuch wurde `/ShaderWorld/Maps/Map_OceanOnly` als `/Game/Maps/ShaderWorldTour_Map_OceanOnly` in das Testprojekt kopiert. Die Projektkopie zeigte nach Aktivieren von Schaum, Einstellen von 18 m/s Wind und einem Rebuild sichtbare weiße Schaumkämme. 18 m/s entsprechen rund 65 km/h.[^ocean-proof]

## Die richtige Karte und den Ozean finden

1. Öffne im **Content Browser** den Projektordner **Content → Maps** und doppelklicke auf **ShaderWorldTour_Map_OceanOnly**. Falls diese Projektkopie bei dir fehlt, folge zuerst der Anleitung zu den [Beispielkarten](../reference/example-maps.md).
2. Suche im **Outliner** nach **BP_SWOcean** und wähle diesen Actor aus. Im untersuchten Level ist sein Typ **ShaderWorldActor**. Die Welt enthält außerdem Licht, Kamera und einen separaten Niagara-Actor.
3. Öffne rechts **Details**. Falls dort ein Suchtext steht, lösche ihn zunächst, damit alle Einstellungen erscheinen.
4. Klappe **World Settings → Producers** auf. Öffne den Eintrag, dessen **Layer Name** den Wert **Height** trägt.
5. Klappe in diesem Eintrag **Compute Producer** auf. Hier liegen die Einstellungen des Ozeans. Der verwendete Typ heißt **Ocean Spectrum (compute)** beziehungsweise `ShaderWorldSpectrumProducer`.

Der Eintrag `Height` gehört zur aktuellen Producer-Struktur. Ältere Anleitungen führen stärker über ein Generatormaterial. Bei einem aktiven Ocean-ComputeProducer wird das Höhenmaterial dieses Eintrags durch den ComputeProducer ersetzt; ein alter Materialname allein erklärt deshalb nicht den sichtbaren Seegang.[^ocean-api][^ocean-proof]

![OceanOnly vor dem Schaumversuch](../assets/images/ocean-before.png)

*Ausgangsansicht der OceanOnly-Kopie. Wasserbewegung und Blickwinkel beeinflussen das einzelne Bild.*

## Schaum einschalten und den Wind verstärken

1. Bleibe im aufgeklappten **Compute Producer**. Aktiviere unter **Foam** das Kontrollkästchen **Foam**. Im Code heißt diese Eigenschaft `bFoam`.
2. Stelle unter **Spectrum** den Wert **Wind Speed** auf **18**. Die Einheit ist **Meter pro Sekunde**, nicht km/h.
3. Lösche bei Bedarf den Details-Suchtext und suche nach **Rebuild**. Aktiviere das Kontrollkästchen **Rebuild** unter **World Settings** am Ozean-Actor einmal.
4. Lass den Viewport aktiv und warte, bis Shaderkompilierung und Neuaufbau abgeschlossen sind. **Rebuild** ist ein Auslöser und springt nach der Verarbeitung wieder auf **aus**. Im geprüften Versuch wurde dieser Rücksprung bestätigt.
5. Betrachte das Meer in der normalen **Lit**-Ansicht. Starte bei Bedarf **Play**, damit fortlaufend Frames gerendert werden. Im geprüften Zustand waren weiße Schaumkämme sichtbar.[^ocean-proof]

Das Einschalten von Schaum benötigt einen Neuaufbau der Wasserressourcen. Nur den Haken zu setzen und anschließend ein unverändertes Bild zu betrachten, reicht als Funktionsprüfung nicht aus. Falls **Rebuild** noch aktiv bleibt, zuerst die Verarbeitung und gerenderte Frames abwarten.

![OceanOnly mit Schaum und 18 m/s Wind](../assets/images/ocean-foam-wind18.png)

*Geprüfter Zustand: Schaum aktiv, Wind Speed 18 m/s, Rebuild verarbeitet.*

## Was die Regler bewirken

| Einstellung im ComputeProducer | Bedeutung |
| --- | --- |
| **Wind Speed** | Bestimmt die Windstärke und beeinflusst Wellenlängen sowie Seegang. Im Versuch: 18 m/s. |
| **Wind Direction** | Bestimmt die Ausbreitungsrichtung der Wellen. |
| **Amplitude** | Skaliert die Wellenhöhe. |
| **Choppiness** | Schiebt Wasser horizontal zu den Wellenkämmen und schärft sie. Der Wechsel zwischen null und einem positiven Wert benötigt laut installierter API einen Rebuild. |
| **Shallow Attenuation** | Dämpft die Wellen anhand der Tiefe über dem gelieferten Terrain. `1` bedeutet an der Wasserlinie vollständig gedämpft, `0.95` lässt dort 5 % des vertikalen Ausschlags übrig, `0` schaltet diese Dämpfung ab. |
| **Max Attenuation Depth** | Tiefe in Zentimetern, ab der wieder volle Wellen gelten. `0` deaktiviert diese zusätzliche Tiefengrenze; die durch **Shallow Attenuation** gesteuerte Küstendämpfung bleibt wirksam. |
| **Foam Coverage** | Beeinflusst, wie leicht sich Schaum an zusammengedrückten Wellenkämmen bildet. Höher bedeutet mehr Schaum. |

Die Bedeutung der zusätzlichen Regler stammt aus der installierten API.[^ocean-api] Diese Seite belegt keinen separaten praktischen Test jeder Reglerkombination. Schaum kann außerdem an flachen Küsten entstehen. Dafür muss der Ozean passende Geländedaten erhalten; die reine OceanOnly-Karte ist kein Nachweis für fertige Uferinteraktion mit einer Stadt.[^detail-panel][^ocean-proof]

## Warum kann Wasser unter einer Insel liegen?

Der Ozean bildet eine eigene Oberfläche. Terrain darüber schneidet diese Oberfläche nicht automatisch zu einer Küstenkontur aus. Dass sich das Wasser unter dem Land fortsetzt, ist deshalb etwas anderes als sichtbares Wasser **über** dem Inselboden. Für einen Tunnel unter dem Meer ist außerdem ein gezielter trockener Innenraum nötig.

Im aktuellen [CityBasics-Labor](city-basics-lab.md) liegt der mittlere Meeresspiegel bei **Z = 0 cm**, das Inselplateau bei **Z = 300 cm**. In PIE waren am Ozean **Wind Speed = 14 m/s**, **Amplitude = 1**, **Shallow Attenuation = 0.95** und **Max Attenuation Depth = 0** eingestellt. Die Abhängigkeiten waren bereits richtig verbunden: Das Terrain hat den Ozean als **Data Receiver**, der Ozean das Terrain als **Data Source**.[^coast-inspection] Die offizielle Anleitung beschreibt diese Richtung unter **Advanced → Dependencies**.[^detail-panel]

Der Nutzer hat Wellen gemeldet, die durch die Insel sichtbar werden. Ort, Zeitpunkt und Cache-Zustand wurden dafür noch nicht reproduziert oder vermessen.[^coast-inspection]

Der gelesene Shader behandelt eine Position über Land als negative Wassertiefe. Bei `0.95` bleiben dort rechnerisch 5 % Restbewegung. **Das allein erklärt keinen Durchbruch durch ein 3 m hohes Plateau:** Dafür wäre bei wirksamer 5-%-Dämpfung ein ungedämpfter vertikaler Ausschlag von mehr als 60 m nötig. Außerhalb des verfügbaren Terrain-Caches behandelt derselbe Code die Position dagegen als tiefes Wasser und lässt volle Wellen zu. Das ist ein Ansatz für die Diagnose, kein Nachweis, dass gerade diese Cache-Grenze den gemeldeten Fehler verursacht.[^coast-water-code]

### Nächster Versuch zur Eingrenzung — noch nicht durchgeführt

1. Öffne eine Projektkopie der betroffenen Inselkarte. Wähle Terrain und Ozean nacheinander aus und kontrolliere unter **Advanced → Dependencies** die oben beschriebene Verbindung.
2. Wähle am Ozean **World Settings → Producers → Height → Compute Producer**. Notiere die Ausgangswerte und ändere zunächst nur **Shallow Attenuation** von `0.95` auf `1.0`.
3. Löse am Ozean **Rebuild** aus und warte bei aktivem Echtzeit-Viewport oder in **Play** auf den Neuaufbau. Vergleiche dieselbe Stelle, auch nach einer Kamerafahrt vom Strand ins Inselinnere.
4. Bleibt Wasser über dem Boden sichtbar, prüfe als Nächstes die Abdeckung und Aktualisierung der Terrain-Daten für den Ozean. Eine korrekt gesetzte **Data Source** allein beweist noch keine korrekten Cache-Daten an jeder Position.
5. Stelle für einen Vergleich wieder `0.95` her und baue erneut auf. Halte fest, ob sich das Problem durch den einzelnen Parameter verändert hat.

**`1.0` ist hier ein vorgeschlagener Diagnosetest und kein bewiesener Fix.** Die konkrete Ursache des Wasserdurchbruchs ist noch nicht isoliert. Ein hoher Windwert allein reicht ebenfalls nicht als Erklärung.[^coast-inspection][^coast-water-code]

## Trockene Tunnel und Räume unter Wasser planen

ShaderWorld 4.1 enthält dafür Komponenten namens **ShaderWorld Air Pocket Box**, **ShaderWorld Air Pocket Capsule** und **ShaderWorld Air Pocket Spline Tube**. Eine Box eignet sich als Ausgangspunkt für einen geraden Raum, die Spline Tube für einen gekrümmten Tunnel. Die Komponenten beschreiben einen Bereich, in dem Wasser ausgeschlossen werden soll; sie erzeugen keine Tunnelwände und ersetzen keine Kollision.[^coast-water-code]

Zwei Wirkungen müssen getrennt geprüft werden:

- **Spielabfragen:** Das WaterSubsystem liefert für Punkte in einer registrierten Air Pocket keinen Wasseranbieter, solange die Abfrage Air Pockets nicht ausdrücklich ignoriert.
- **Sichtbare Oberfläche:** Das Wassermaterial muss als **Masked** arbeiten und den Materialknoten **ShaderWorld Water Exclusion** an **Opacity Mask** anschließen. Nur die Komponente zu platzieren garantiert diese visuelle Wirkung nicht.[^coast-water-code]

Ein noch ungeprüftes Vorgehen wäre: Im Tunnel-Blueprint über **Add Component** eine Air-Pocket-Komponente hinzufügen, auf den trockenen Innenraum innerhalb der Wände begrenzen und anschließend die tatsächlich verwendete Wasser-Materialkette prüfen. Am aktuell verwendeten **M_Ocean_Material** wurde dieser Anschluss inzwischen geprüft: Das Material ist **Masked** und verwendet **Material Attributes**. Der Knoten **ShaderWorldWaterExclusion_0** ist über **Multiply_0** mit **Opacity Mask** in **MakeMaterialAttributes_0** verbunden; dessen Attribute gehen an den Materialausgang. Die erforderliche Materialanbindung ist damit bereits vorhanden. **Eine Air Pocket wurde in CityBasics noch nicht angelegt oder praktisch geprüft.** Ein trockener Tunnel unter Wasser ist deshalb weiterhin kein bestätigtes Ergebnis.[^coast-inspection]

Auch Wasserabfragen für Auftrieb brauchen einen eigenen Test: Der gelesene CPU-Ozeanprovider berechnet Tiefwasserwellen **ohne Küstendämpfung**. Die gerenderte Oberfläche und eine abgefragte Wasserhöhe können an Land oder am Ufer deshalb unterschiedliche Ergebnisse liefern. Sichtprüfung und Gameplay-Abfrage sollten am selben Ort getrennt gemessen werden; ein ruhiges Bild beweist dort noch keine passende Auftriebsantwort.[^coast-water-code]

## OceanOnly und Reference unterscheiden

Die große Reference-Welt enthält bereits Terrain, Ozean, Vegetation, Straßenbeispiele und Tunnel. Beide untersuchten Karten referenzieren einen SpectrumProducer, das Ozeanmaterial und die Wasserlinien-/Unterwasseranbindung. **OceanOnly** macht das Wasser isoliert untersuchbar. Ihr zusätzlicher Niagara-Test heißt `NS_WaterTest`; der alte Assetpfad `/ShaderWorld/Demo_Ocean/VFX/NS_WaterTest` wird auf `/ShaderWorld/Demo_Ocean/FX/NS_WaterTest` weitergeleitet.

Die untersuchte Niagara-Schnittstelle kann für CPU-Partikel Wasserhöhe, Oberflächennormale, Geschwindigkeit und Eintauchstatus abfragen.[^ocean-api] Auftrieb, replizierter Seegang und weitere Unterwasserfunktionen werden für 4.1 offiziell beschrieben. Ihr Vorhandensein bedeutet noch keinen abgenommenen Boots-, Multiplayer- oder Überflutungstest in diesem Projekt.[^fab-ocean]

## Wenn das Bild nicht reagiert

- Kontrolliere, ob **BP_SWOcean** ausgewählt ist und du den **Height**-Eintrag dieses Actors bearbeitest.
- Prüfe nach einer Schaumumschaltung, ob **Rebuild** ausgelöst und verarbeitet wurde.
- Warte auf Shaderkompilierung und verwende einen aktiven Echtzeit-Viewport oder **Play**. ShaderWorld braucht gerenderte Frames.
- Vergleiche die normale **Lit**-Ansicht mit den Bildern. Debug-Ansichten können das Wasser anders darstellen.

Der OceanOnly-Versuch bestätigt die Editoransicht, die dort genannten Parameter und sichtbaren Schaum nach dem Rebuild. Die neue Insel-Diagnose ergänzt ausgelesene PIE-Einstellungen und Codebefunde. Ein bestätigter Fix für den Wasserdurchbruch, ein trockener Unterwassertunnel, ein verpackter Build, Leistungsmessungen und schwimmende Schiffe fehlen weiterhin.[^ocean-proof][^coast-inspection]

[^ocean-proof]: [Beobachtungsbericht zum Ocean-Test](../evidence/ocean-report.json).
[^fab-ocean]: [Offizielle ShaderWorld-Produktseite](https://www.fab.com/listings/ee4bcbaf-36ea-4dd9-aade-068e1a8a4794).
[^detail-panel]: [Offizielle Dokumentation: Detail Panel](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/detail-panel).
[^ocean-api]: Lokale Prüfung von ShaderWorldComputeProducer.h, ShaderWorldActor_Build.cpp und NiagaraDataInterfaceShaderWorldWater.h in der lizenzierten Installation von ShaderWorld 4.1. Die Plugindateien werden nicht mitgeliefert.
[^coast-inspection]: [Bereinigte Küsten-/Straßeninspektion vom 28. Oktober 2026](../evidence/coast-biome-road-inspection.json): PIE-Einstellungen und Abhängigkeiten gelesen sowie Materialgraph geprüft. Die Ursache des sichtbaren Wasserdurchbruchs und ein Fix wurden nicht bestätigt; Air Pockets wurden noch nicht praktisch ausprobiert.
[^coast-water-code]: Gelesene ShaderWorld-4.1-Quellen: `ShaderWorldComputeProducer.h`, Zeilen 213–222; `ShaderWorldComputeProducers.usf`, Zeilen 109–130; `ShaderWorldAirPocketComponents.h`; `ShaderWorldWaterExclusion.h`; `ShaderWorldWaterSubsystem.cpp`, Zeilen 62–72; `ShaderWorldOceanWaterProvider.h`, Zeile 42. Relative Verzeichnisse stehen in den Quellenmetadaten. Lizenzierte Dateien werden nicht mitgeliefert; diese Befunde ersetzen keinen Laufzeittest.
