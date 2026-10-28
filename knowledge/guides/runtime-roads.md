---
type: Guide
title: Straßen im Spiel bauen, speichern und neu laden
description: Den eigenen RoadLab-Prototyp mit gemeinsamer ShaderWorld-Terraintrasse,
  sichtbarem RCP-Asphalt und geprüftem Neustart bedienen.
status: stable
tags: [shaderworld, citylab, roads, runtime, savegame, spline]
engine_version: "5.8.4"
plugin_version: "4.1"
generated: { by: codex/gpt-6, at: "2026-10-28T01:55:41Z" }
evidence_scope:
  implementation: Eigener nativer RoadLab-Prototyp gebaut; gemeinsamer ShaderWorld-Spline
    und eigene SplineMesh-Straßenoberfläche
  runtime: Zwei getrennte gerenderte uncooked Spielprozesse bestanden; je 72 Kollisionsproben,
    identische gespeicherte Trassen, zwei Straßen und 16 Meshsegmente
  vegetation: Gemessene Instanzursprünge im Kern 999 zu 0 zu 999 zu 0; Referenzbereich
    8615; je Phase drei gleiche vollständige Matrix-Fingerprints, keine GPU-Maskenmessung
  ui: Tatsächliche native Slate-Tasten R/Enter, Backspace, X, Q/E und K/L geprüft;
    normaler PIE-Neustart mit identischem Auto-Load bestanden, Kamera per ActorTools versetzt
  regression: Frühere Bauplatz-/Terraintrassenprüfung in zwei frischen Prozessen mit Format 2 bestanden
  visual: Drei native Frames inspiziert, darunter normale PIE-Ansicht nach Auto-Load
  not_tested: WASD, rechte Maustaste, Mausrad und F5/F9-Aliasse; Cook und Shipping
sources:
  - id: road-proof
    resource: ../evidence/runtime-roads-report.json
    title: Bereinigte Create-/Load-Nachweise mit Kollisions- und Pflanzenmessung
  - id: roadlab-code
    resource: "Eigene Source/UnrealMcpTest/CityLabRoadGameMode.h/.cpp, CityLabRoadSurfaceComponent.h/.cpp und CityLabPersistence.h/.cpp im ursprünglichen UnrealMcpTest; gelesen, gebaut und mit nativem Verifier geprüft; Projektcode nicht im öffentlichen Bundle enthalten"
    title: RoadLab-Bedienung, gemeinsame Spline und logische Spielstände
  - id: roadlab-setup
    resource: "Projektlokales Tools/setup_runtime_roads.py im ursprünglichen UnrealMcpTest: Kartenkopie, Demo-Bereinigung und CPU-lesbare Kopie des lizenzierten Road-Creator-Pro-Meshes; Skript und Unreal-Assets nicht im Bundle enthalten"
    title: Aufbau des gesonderten Straßenlabors
  - id: test-gates
    resource: "UE 5.8.4 HierarchicalInstancedStaticMeshComponent.h:331–332; ShaderWorld 4.1 SWHISMComponent.cpp, SWBuiltTreeReception/NewRender; eigene CityLabRoadVerification.cpp und CityLabPersistence.cpp; zwei frühere Create-Diagnosen vom 28. Oktober 2026. Quellcode und private Rohberichte nicht mitgeliefert"
    title: Korrigiertes Pflanzen-Testgate und eigene Pad-Shader-Abhängigkeit
  - id: first-frame
    resource: ../assets/images/runtime-road-first-pie.png
    title: Erster inspizierter PIE-Frame mit einer Beispielstraße
  - id: create-frame
    resource: ../assets/images/runtime-road-create-verified.png
    title: Inspizierter Frame des bestandenen Erzeugen-/Speichern-Laufs
  - id: autoload-frame
    resource: ../assets/images/runtime-road-normal-autoload-pie.png
    title: Normale PIE-Ansicht nach Straßenbau per Tasten, Speichern und Auto-Load
  - id: image-manifest
    resource: ../evidence/image-manifest.json
    title: Bildherkunft, Dateigrößen und SHA-256
  - id: terrain-road-basics
    resource: building-pads-and-roads.md
    title: Geländeform, Bodenmaterial und Straßenmesh unterscheiden
---
# Straßen im Spiel bauen, speichern und neu laden

Das eigene **RoadLab** verwendet **dieselbe Spline** für ShaderWorld-Gelände und Asphalt. Gespeichert wird die logische Trasse; Terrainwirkung und Meshes werden daraus neu aufgebaut. **Erzeugen/Speichern und Laden in einem neuen Spielprozess sind bestanden**, einschließlich Kollision und gemessener Pflanzenursprünge. Auch R/Enter, Entwurfskorrektur, Q/E und K/L wurden per nativen Slate-Tasten geprüft; ein normaler PIE-Neustart stellte den Stand automatisch wieder her. Kameraeingaben und F5/F9-Aliasse bleiben offen.[^road-proof]

![Normale PIE-Ansicht mit zwei nach Neustart automatisch geladenen Straßen](../assets/images/runtime-road-normal-autoload-pie.png)

*Normale PIE-Ansicht nach der Bedienprobe und erneutem Play am 28. Oktober 2026: zwei wiederhergestellte Straßen, HUD-Meldung „Gespeicherte Strassen wiederhergestellt“. Die zweite Trasse wurde bei der Bedienprobe gesetzt und unterscheidet sich vom nativen Testfixture. Ein inspizierter Frame ist keine Dauerprüfung.*[^autoload-frame][^image-manifest]

## Die richtige Karte starten

1. Verwende das ursprüngliche **UnrealMcpTest** mit gebauter C++-Erweiterung, ShaderWorld 4.1 und vorbereitetem RCP-Mesh. Dieses Doku-Repository enthält Klassen und Unreal-Assets nicht.
2. Öffne **Content → Maps → ShaderWorldRoadLab** (`/Game/Maps/ShaderWorldRoadLab`).
3. Prüfe in **World Settings** den eigenen **CityLabRoadGameMode**. Starte **Play**, klicke in den Spielbereich und warte auf Terrain und Kollision. Das HUD zeigt die Straßensteuerung.

RoadLab ist eine **CityBasics-Kopie**. Nur hier entfernt das Einrichtungsskript die `Basics_`-Demobauten außer **Basics_CollisionAnchor**: alter Berg, Tunnel und vorgebaute Straßen. Insel, Wald und Ozean bleiben erhalten.[^roadlab-setup]

Der normale Start soll nach der Terrainvorbereitung den separaten Slot **CityLabRoads** laden. Fehlt er, entsteht die Beispielstraße zur Laufzeit. **Sie ist erst mit K/F5 gespeichert.** **B** fordert das Beispiel erneut an, wenn keine Straße existiert. Ein fehlgeschlagener Load meldet einen Fehler, statt eine Ersatzstraße einzuschleusen. Normales PIE-Autoload wurde zusätzlich geprüft; den Nachweis über getrennte Spielprozesse liefert der native Verifikationsmodus.[^roadlab-code][^road-proof]

## Eine Trasse zeichnen

1. **WASD** bewegt die Kamera, die **rechte Maustaste** steuert den Blick und das **Mausrad** zoomt entlang der Blickrichtung.
2. Zeige auf fertiges Gelände und drücke **R**. Die Abfrage überspringt Baum-/Propkomponenten; ohne gültigen Bodentreffer entsteht kein Punkt.
3. Setze weitere Punkte mit **R**: mindestens **2 m** Abstand in der Draufsicht, höchstens **64 Punkte** je UI-Trasse.
4. **Q/E** senkt/erhöht den Versatz für die **nächsten** Punkte um **0,5 m**. Bereits gesetzte Punkte bleiben stehen. Unterschiedliche Höhen ergeben eine Steigung; Brücken entstehen dadurch nicht.
5. **Backspace** entfernt den letzten Entwurfspunkt, **X** verwirft den Entwurf. Gebaute Straßen bleiben erhalten.
6. Drücke mit mindestens zwei Punkten **Enter**. Die glatte Trasse bekommt **8 m Breite** und je **3 m** weichen Terrainübergang.
7. Warte auf Terrain, Kollision und Vegetation; sie aktualisieren sich asynchron. Beachte die Statusmeldung.[^roadlab-code]

Diese Tasten gelten für **RoadLab**. Das frühere **ShaderWorldPersistenceLab** nutzt R/R für Zweipunkttrassen; im **CityBasics**-Buggy setzt R das Fahrzeug zurück.

## Speichern und nach Neustart laden

1. Drücke **K/F5** und prüfe die Speichermeldung für **CityLabRoads**.
2. Baue zum Vergleich eine weitere Straße. **L/F9** ersetzt bei erfolgreichem Laden ungespeicherte Änderungen durch den gespeicherten Stand.
3. Beende das Spiel und starte **dieselbe RoadLab-Karte** neu. Der vorhandene Slot soll Terraintrassen und Asphalt automatisch wiederherstellen.

Die Bedienprobe bestätigte **K/L**, anschließend **Stop PIE → Play** und denselben automatisch geladenen Stand ohne Duplikate. IDs, Splinepunkte, Tangenten und Straßeneinstellungen waren identisch. Ein PIE-Neustart bleibt vom separaten nativen Zwei-Prozess-Test unterschieden; **F5/F9** sind bisher nur die im Code gelesenen Aliasse.[^roadlab-code][^road-proof]

## Gelände und Asphalt teilen dieselbe Trasse

| Teil | Eigene Umsetzung |
| --- | --- |
| Gelände | Native ShaderWorld-**SWSplineRoadComponent** mit Höhenverformung |
| Boden/Bewuchs | **AltitudeBasedLayer**, RedGround-Kern, Sandrand, **Biom ID 3** im blauen Kanal für die bewuchsfreie Reference-Variante |
| Asphalt | Eigene native **USplineMeshComponent**-Segmente an derselben Spline |
| Kurve | Kontrollpunkte und gespeichertes **bSmoothSpline** |

**Road Creator Pro liefert das lizenzierte Meshasset.** Unser Projektcode baut Unreal-SplineMeshes zur Laufzeit; der RCP-Editorbuilder wird dafür nicht im Spiel aufgerufen.[^roadlab-code]

Die Projektkopie **SM_CityLab_RCP_TwoLane** liegt unter `/Game/ShaderWorldRoadLab/Meshes`, benötigt **Allow CPU Access** und stammt von einem ungefähr **12 × 9 × 0,2 m** großen Mesh. Sie wird auf **8 m Breite** angepasst und in höchstens **12 m** lange Abschnitte aufgeteilt. Auf waagerechten Abschnitten liegt die Oberseite nominell **3 cm über der Spline**; geneigte Querschnitte folgen dem Spline-Rahmen.[^roadlab-setup][^roadlab-code]

**Biom ID 3 ist keine allgemeine Baumfällung.** Sie braucht den passenden Layer und die Reference-Spawnkonfiguration. Beliebige selbst platzierte Bäume sind nicht erfasst.[^terrain-road-basics]

## Was tatsächlich geprüft wurde

Der [bereinigte Bericht](../evidence/runtime-roads-report.json) ist **passed_with_limits**: Zwei Prozesse bestanden **18/18 beziehungsweise 19/19 Checks**. IDs, Kontrollpunkte, Stil und Glättung waren identisch; beide stellten **zwei Straßen mit 16 Meshsegmenten** her.

Je Prozess bestanden **72 Kollisionsproben**: 13 Grundterrain, 23 nach Bau/Laden, 13 nach Rücknahme, 23 nach erneutem Laden. Die Straßenphasen enthalten getrennte Treffer auf **ShaderWorldCollisionComponent** und **SplineMeshComponent**. Größter Höhenfehler: **0,204 cm Terrain**, **0,077 cm Asphalt**, bei **3 cm Toleranz**.[^road-proof]

| Pflanzenphase, in beiden Prozessen | Ursprünge im Kern | Referenzbereich |
| --- | ---: | ---: |
| Vor Straßen | 999 | 8615 |
| Nach Bau/Laden | 0 | 8615 |
| Nach Rücknahme/Nachwachsen | 999 | 8615 |
| Nach erneutem Laden | 0 | 8615 |

Pro Phase wurden drei gleiche Fingerprints der vollständigen gültigen Instanzmatrizen abgewartet. Der Kern liegt höchstens **3,5 m** von der Trasse in XY entfernt, die Referenzen **10–30 m**. Gezählt wurden **Instanzursprünge** aus dem CPU-Spiegel der ShaderWorld-Renderdaten: keine Äste, Kronen oder Überhänge und keine GPU-Maskenpixel. Stabile CPU-Daten sind kein Renderthread-Fertigstellungsnachweis.[^road-proof]

Die Bedienprobe nutzte echte **native Slate-Klicks und Tastenereignisse** für **R/Enter**, **Backspace**, **X**, **Q/E** (0 → 50 → 0 cm) und **K/L**. Zwischen den zwei Cursorpunkten wurde die Kamera per **ActorTools** versetzt; **WASD, rechte Maustaste und Mausrad** wurden damit nicht bedient. Ein früher R-Versuch wurde während noch fehlender Bodenkollision korrekt abgewiesen; nach Terrainbereitschaft gelang der erneute Versuch.[^road-proof]

Die unabhängige Regression der älteren **ShaderWorldPersistenceLab**-Karte bestand danach ebenfalls: zwei frische Prozesse mit **Format 2**, zwei Pads/zwei Terraintrassen und je **26 ursprünglichen plus 26 geänderten Terrainproben**. Dieser Zusatz prüft den bestehenden Bauplatzpfad nach dem Pad-Shader-Fix, keine Asphaltmeshes.[^road-proof]

## Spielstand und Fehlerfälle

Das logische **Format 2** speichert Kontrollpunkte, Maße, Reihenfolge, **RCP_TwoLane** und **bSmoothSpline**. Meshsegmente entstehen neu; beliebige Assetpfade sind keine erlaubten Stile. Der Loader prüft Karten-/Generator-/Terrainidentität und Datensätze, bereitet Ersatzobjekte vor und übernimmt sie erst nach erfolgreicher Vorbereitung.[^roadlab-code]

Wiederholtes Laden erzeugte keine Duplikate. Fehlender Slot, falsche Formatversion, ungültiger Stil und erzwungener Oberflächen-Baufehler ließen die bestehende Stadt erhalten. **Format 1** wurde mit einer **synthetischen Testdatei** als lineare Terraintrasse ohne Mesh eingelesen; eine archivierte Datei aus einer alten ausführbaren Spielversion wurde nicht getestet. Separate Generator-/Seed-Konflikte bleiben Codebefunde.[^road-proof]

## Wenn etwas nicht passt

| Beobachtung | Prüfen |
| --- | --- |
| Buggy statt Straßen-HUD | RoadLab-Karte und **CityLabRoadGameMode** |
| R setzt keinen Punkt | Fertige Terrainkollision, Bodentreffer, 2 m Punktabstand |
| Nur Entwurfslinien | Mindestens zwei Punkte, **Enter**, Statusmeldung |
| Terrain ohne Asphalt | Vorbereitete Meshkopie, CPU-Zugriff, Buildfehler |
| Nach Neustart nur Beispiel | Speichermeldung für **CityLabRoads**, dieselbe Karte |
| Bewuchs auf der Trasse | Layer/Biom und Neuerzeugung; keine allgemeine Rodung erwarten |

Zwei frühere Timeouts hatten konkrete Ursachen: **IsTreeFullyBuilt** war im untersuchten ShaderWorld-NewRender-Pfad kein passendes Fertigsignal. Unser Verifier verwendet nun **IsAsyncBuilding plus drei stabile Matrix-Fingerprints** und liest gemeinsame Instanzdaten unter **DataLock**, statt nur **GetInstanceCount**. Danach blockierte unser Manager ohne Pad-Instanz an **PadMaterial->IsComplete()**; diese Abfrage startet keine Kompilierung. Die eigene Integration prüft den Pad-Shader nun nur bei **PadActors.Num() > 0**. Der anschließende Zwei-Prozess-Test bestand; daraus folgt kein allgemeiner ShaderWorld-Fehlerbefund.[^test-gates]

Der Prototyp enthält **keine Kreuzungen, Verkehrssimulation, Brücken-/Tunnelgenerierung, Kurvenüberhöhung oder Fahrspurplanung**. Cook/Shipping und die genannten Kamera-/Aliastasten bleiben offen. Die [erste PIE-Aufnahme mit einer Straße](../assets/images/runtime-road-first-pie.png) und die [Aufnahme des nativen Create-Laufs](../assets/images/runtime-road-create-verified.png) bleiben als frühere Sichtbelege erhalten. Die Vorbereitungsmeldung im Create-Bild gehört zu dessen Testmodus.[^first-frame][^create-frame]

[^road-proof]: [Bereinigter RoadLab-Bericht](../evidence/runtime-roads-report.json): getrennte Create-/Load-Prozesse, Kollisionsproben, logische Daten, Pflanzenursprünge und Nachweisgrenzen.
[^roadlab-code]: Eigene RoadLab-/SplineMesh-/Persistenzklassen im ursprünglichen UnrealMcpTest gelesen und nativ geprüft; Projektcode nicht mitgeliefert.
[^roadlab-setup]: Eigenes `Tools/setup_runtime_roads.py`; Skript und lizenzierte Unreal-Assets nicht mitgeliefert.
[^test-gates]: UE-Header `HierarchicalInstancedStaticMeshComponent.h`, `SWBuiltTreeReception`/NewRender in ShaderWorld und eigene Verifier-/Managerlogik; frühere Diagnoseberichte und erfolgreicher Folgelauf getrennt betrachtet.
[^first-frame]: [Erster PIE-Frame](../assets/images/runtime-road-first-pie.png), keine Bedienungs- oder Dauerprüfung.
[^create-frame]: [Native Aufnahme des Create-Laufs](../assets/images/runtime-road-create-verified.png), ein inspizierter Frame des automatisierten Tests.
[^image-manifest]: [Bildherkunft, Dateigröße und SHA-256](../evidence/image-manifest.json).
[^terrain-road-basics]: [Geländeform, Bodentextur und Straßenmesh](building-pads-and-roads.md).
[^autoload-frame]: [Native CaptureEditorImage-Aufnahme nach normalem PIE-Autoload](../assets/images/runtime-road-normal-autoload-pie.png), ein inspizierter Frame nach der Slate-Bedienprobe; kein separater Prozess- oder Langzeitnachweis.
