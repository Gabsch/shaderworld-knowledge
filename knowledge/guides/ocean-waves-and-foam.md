---
type: concept
title: Ozean, Wellen und Schaum im Editor einstellen
description: Klickanleitung für die getestete OceanOnly-Kopie mit sichtbarem Schaum
  und 18 m/s Wind; Einordnung der weiteren Wasserfunktionen.
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
generated:
  by: codex/gpt-6
  at: '2026-10-27T21:48:46Z'
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: 'Editorversuch an einer Projektkopie von Map_OceanOnly: Parameter
  gelesen, Schaum aktiviert, WindSpeed auf 18 m/s gesetzt, Rebuild ausgelöst und sichtbarer
  Schaum gerendert. Weitere Funktionen teilweise nur aus installierter API und offizieller
  Produktbeschreibung eingeordnet.'
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
| **Foam Coverage** | Beeinflusst, wie leicht sich Schaum an zusammengedrückten Wellenkämmen bildet. Höher bedeutet mehr Schaum. |

Die Bedeutung der zusätzlichen Regler stammt aus der installierten API.[^ocean-api] Diese Seite belegt keinen separaten praktischen Test jeder Reglerkombination. Schaum kann außerdem an flachen Küsten entstehen. Dafür muss der Ozean passende Geländedaten erhalten; die reine OceanOnly-Karte ist kein Nachweis für fertige Uferinteraktion mit einer Stadt.[^detail-panel][^ocean-proof]

## OceanOnly und Reference unterscheiden

Die große Reference-Welt enthält bereits Terrain, Ozean, Vegetation, Straßenbeispiele und Tunnel. Beide untersuchten Karten referenzieren einen SpectrumProducer, das Ozeanmaterial und die Wasserlinien-/Unterwasseranbindung. **OceanOnly** macht das Wasser isoliert untersuchbar. Ihr zusätzlicher Niagara-Test heißt `NS_WaterTest`; der alte Assetpfad `/ShaderWorld/Demo_Ocean/VFX/NS_WaterTest` wird auf `/ShaderWorld/Demo_Ocean/FX/NS_WaterTest` weitergeleitet.

Die untersuchte Niagara-Schnittstelle kann für CPU-Partikel Wasserhöhe, Oberflächennormale, Geschwindigkeit und Eintauchstatus abfragen.[^ocean-api] Auftrieb, replizierter Seegang und weitere Unterwasserfunktionen werden für 4.1 offiziell beschrieben. Ihr Vorhandensein bedeutet noch keinen abgenommenen Boots-, Multiplayer- oder Überflutungstest in diesem Projekt.[^fab-ocean]

## Wenn das Bild nicht reagiert

- Kontrolliere, ob **BP_SWOcean** ausgewählt ist und du den **Height**-Eintrag dieses Actors bearbeitest.
- Prüfe nach einer Schaumumschaltung, ob **Rebuild** ausgelöst und verarbeitet wurde.
- Warte auf Shaderkompilierung und verwende einen aktiven Echtzeit-Viewport oder **Play**. ShaderWorld braucht gerenderte Frames.
- Vergleiche die normale **Lit**-Ansicht mit den Bildern. Debug-Ansichten können das Wasser anders darstellen.

Praktisch bestätigt sind die Editoransicht, die genannten Parameter und sichtbarer Schaum nach dem Rebuild. Ein verpackter Build, Leistungsmessungen, schwimmende Schiffe und eine Stadt mit veränderten Küsten wurden in diesem Ocean-Versuch nicht geprüft.[^ocean-proof]

[^ocean-proof]: [Beobachtungsbericht zum Ocean-Test](../evidence/ocean-report.json).
[^fab-ocean]: [Offizielle ShaderWorld-Produktseite](https://www.fab.com/listings/ee4bcbaf-36ea-4dd9-aade-068e1a8a4794).
[^detail-panel]: [Offizielle Dokumentation: Detail Panel](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/detail-panel).
[^ocean-api]: Lokale Prüfung von ShaderWorldComputeProducer.h, ShaderWorldActor_Build.cpp und NiagaraDataInterfaceShaderWorldWater.h in der lizenzierten Installation von ShaderWorld 4.1. Die Plugindateien werden nicht mitgeliefert.
