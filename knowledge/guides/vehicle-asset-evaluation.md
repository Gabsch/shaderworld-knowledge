---
type: Playbook
title: Kostenlose Fahrzeugassets im CityLab prüfen
description: Liebherr, Radlader und Lkw als getrennte Skeletal-Mesh-Versuche importieren und ihre Animationsgrenzen beurteilen.
status: stable
generated:
  by: codex/gpt-6
  at: "2026-10-29T01:16:18Z"
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: Gespeicherte Assets/Karte neu geladen, Mesh- und Clip-Einheiten getrennt geprüft, eingefrorene Editorposen und Übersichtbild geprüft sowie tatsächliches SimulateInEditor-Ticken gemessen; keine Gameplay-/Cook-/Leistungsabnahme.
sources:
  - id: vehicle-proof
    resource: ../evidence/vehicle-asset-evaluation.json
    title: Bereinigter Fahrzeugprüfstand mit getrennten Export-, Import- und Laufzeitbefunden
  - id: liebherr-source
    resource: https://www.blendkit.com/asset-gallery-detail/422308a0-8f5a-45cb-8132-fdcffac4a52c/
    title: BlenderKit Liebherr 956
  - id: loader-source
    resource: https://www.blendkit.com/asset-gallery-detail/2dd30522-086c-4566-9b2a-b9234f89458f/
    title: BlenderKit Wheel Loader
  - id: truck-source
    resource: https://sketchfab.com/3d-models/dump-truck-781c616da8f44982a59cb3fc3fa67f98
    title: Dump Truck von ElectroNick
  - id: project-tools
    resource: "Projektlokale eigene Werkzeuge Tools/import_vehicle_evaluation.py, repair_vehicle_import_units.py, repair_vehicle_decal_colors.py, repair_vehicle_animation_units.py und verify_vehicle_evaluation.py; Quellcode und Unreal-Assets werden nicht im öffentlichen Wissensbundle mitgeliefert."
    title: Eigene Import-, Korrektur- und Abnahmewerkzeuge
---

# Kostenlose Fahrzeugassets im CityLab prüfen

Die getrennte Karte `/Game/Maps/VehicleEvaluationLab` stellt einen Liebherr 956, einen Radlader und einen Kipper gegenüber. Ihre Assets liegen unter `/Game/VehicleEvaluation`. Die Karte dient der Material-, Maßstabs- und Bewegungsprüfung. Der [Maschinenarbeitsplan](../reference/scaping-machine-work-plan.md) bleibt die gesonderte Gameplay-Integration.

Voraussetzung ist das projektlokale UnrealMcpTest mit Unreal 5.8.4. ShaderWorld 4.1 ist im Projekt vorhanden; die neutrale Testkarte prüft keine neue Terrainfunktion. Dieses öffentliche Bundle liefert weder Fahrzeugmodelle noch Projekt- oder Pluginassets mit.

## Quellen und geeigneter Einsatz

| Modell | Exportierte Dreiecke | Bones nach Unreal-Import | Materialslots nach Unreal-Import | Einschätzung |
| --- | ---: | ---: | ---: | --- |
| Liebherr 956 | 1.854.664 | 162 | 43 | Detailversion für Nahsicht; für viele Maschinen deutlich vereinfachen |
| Wheel Loader | 327.508 | 74 | 20 | Beweglicher Radlader als Ausgangspunkt; LODs und einfacheres Rig erforderlich |
| ElectroNick Dump Truck | 34.307 | 11 | 6 | Technisch leicht; fehlende Texturen und ungeklärte Herkunft begrenzen die Nutzung |

Die lokalen BlenderKit-Quellmetadaten nennen beide Modelle als gratis mit Lizenz `royalty_free` ([BlenderKit-Lizenzbedingungen](https://www.blendkit.com/docs/licenses/)); sie sind damit nicht als CC0 ausgewiesen.

Die BlenderKit-Dateien enthalten eigene Steuerungen, aber keine fertigen Animationsclips. Der Lkw besteht ursprünglich aus einem Mesh ohne Skelett und ohne Clips. Die hier getesteten Skelette und Demonstrationsanimationen sind neue Aufbereitungen. Die zusätzlichen Unreal-Root-Bones gehören zur FBX-Importhierarchie.

Für den Lkw fehlen unter anderem die Kabinen-Farb- und Normaltextur. Tatsächlich geliefert wurden 512-/1024-Pixel-Texturen; Roughness und Metallic verwenden dokumentierte Konstantwerte. Die Kabine erhält einen ausdrücklich gekennzeichneten Ersatz. Im ursprünglichen FBX-Dateipfad findet sich außerdem ein ungeklärter Bezug auf ein fremdes Spielarchiv. Der CC-BY-4.0-Hinweis der Plattform klärt diese Herkunftsfrage nicht. Der Lkw bleibt deshalb ein lokaler Technikversuch; Produktionsfreigabe und öffentliche Weitergabe sind offen.

## Import und Materialaufbau

1. Originaldateien unverändert aufbewahren. Blender-Dateien ohne automatische Skriptausführung öffnen und sichtbare Fahrzeugteile von Bedienhilfen trennen.
2. Ausgewertete Meshes in ein neues Skelettrig übernehmen. Die Blender-Steuerungen werden als Bewegungen gebacken; ihre Solver, Driver und Constraints laufen später nicht in Unreal.
3. FBX-Metadaten beachten: Die drei geprüften Dateien deklarieren eine Einheit als 100 Zentimeter. Für SkeletalMesh- und Animationsimport `convert_scene_unit=True` setzen. Der erste Import ohne diese Umrechnung erzeugte um Faktor 100 zu kleine Assets. Ein ungespeicherter korrigierter Lkw-Probeimport bestätigte die richtige Umrechnung.
4. Materialien anhand der benannten Slots aufbauen. Direkte Farbtexturen mit weißem Tint verbinden. Blender-Prozeduralshader werden nur angenähert; Glas und die Masken der Liebherr-Aufkleber brauchen eigene Behandlung; deren Deckkraft wird aus dem Rotkanal gelesen. Sechs farbige Aufkleber liegen in verschachtelten Blender-Materialgruppen und werden zusätzlich zugeordnet.
5. Texturen für den begrenzten Test auf maximal 2048 Pixel bauen. Nicht virtuelle Sampler benötigen passende nicht virtuelle Texturen. Die Originalbilder bleiben erhalten; ein besonders großes Liebherr-Maskenbild ist über 46.000 Pixel breit.
6. Ausschließlich die eigenen Assets und die eigene Testkarte speichern. Normale CityLab-Karten und ihre Spielstände gehören nicht zu diesem Import.

Beim erneuten Import vorhandener FBX-Assets wechselte UE 5.8.4 automatisch auf Interchange. Die Importdatenklasse änderte sich dabei; der Korrekturlauf brach vor dem Speichern ab. Das eigene Reparaturwerkzeug wählt deshalb für seinen Prozess den geprüften Legacy-FBX-Pfad. Es schreibt dafür keine Projekteinstellung.

Beim vorhandenen SkeletalMesh unterdrückt der Legacy-Reimport ausdrücklich den Animationsimport. Gespeicherte Importflags belegen deshalb noch keine neu eingelesenen Animationsdaten; die drei vorhandenen Clips benötigen einen eigenen AnimSequence-Reimport.

Die Maßstabsprobe muss sowohl Mesh als auch Animation betreffen. Ein passend vergrößerter Actor allein belegt keine korrekt importierten Zentimeterwerte der Mesh- und Bone-Daten.

## Im Editor ausprobieren

1. Die gespeicherte Karte `VehicleEvaluationLab` im Content Browser öffnen.
2. In der Outliner-Liste die drei Actors `VehicleEvaluation_Liebherr956`, `VehicleEvaluation_WheelLoader` und `VehicleEvaluation_ElectroNick` finden. Die Kamera `VehicleEvaluation_Camera` bietet den Überblick.
3. Einen Actor wählen und in seiner SkeletalMeshComponent die Single-Node-Animation ansehen. Der neue Demonstrationsclip ist als wiederholte Wiedergabe gespeichert. Bei deaktivierter Editorvorschau simulieren.
4. Mit **Simulate** Arm und Schaufel beziehungsweise die Lkw-Mulde beobachten. Für reproduzierbare Posen dienen die gespeicherten AnimSequence-Assets.
5. Zum Rücksetzen die Simulation stoppen und die Testkarte erneut laden. Die Fahrzeugprüfung verwendet keine normalen CityLab-Spielstände.

Die neuen Radlader- und Liebherr-Clips dauern fünf Sekunden, der Lkw-Clip vier Sekunden. Am Radlader werden Knicklenkung, Hub und Schaufel demonstriert. Beim Liebherr bewegen sich Arm, Schaufel und zugehörige starre Teile über gebackene Quellsteuerungen. Der Lkw demonstriert Radrotation, Vorderachslenkung und Kippen der Mulde.

## Grenzen vor der Gameplay-Integration

Alle drei Meshes besitzen im geprüften Import nur LOD0. Der Liebherr belegt dort 2.270.319 Rendervertices und 43 Sections, der Radlader 241.704/20 und der Lkw 31.257/6. Die Export-Vertexzahlen sind wegen der Auftrennung an UV-/Normal-/Materialgrenzen nicht mit den Unreal-Rendervertices gleichzusetzen.

Radlader und Liebherr verwenden für diese Prüfung ein starres Bone pro sichtbarem Teil. Ein überschaubares hierarchisches Maschinenskelett, Laufzeitsteuerung und passende Arbeitsposen sind noch eigene Arbeit. Schläuche bleiben in ihrer ausgewerteten Ausgangsform; die Liebherr-Ketten haben keine durchlaufende Fahranimation. Sein Quellsolver hinterlässt am Demo-Loop bis zu 3,35 Millimeter Abweichung. Der Radlader steht ursprünglich mit stark angehobener Schaufel, daher die rund 6,11 Meter hohe Ausgangsbox.

Die Lkw-Mulde hat einen eigenen Drehpunkt; Hydraulikzylinder und Heckklappenöffnung werden nicht simuliert. Der Import erzeugt keine PhysicsAssets; Fahrzeug- und Schaufelkollisionen wurden nicht geprüft. Die neuen Rigs sind keine Chaos-Vehicle-Physik, keine Navigation und kein nachgewiesener Aushub-/Transportanschluss. Viele gleichzeitig sichtbare Fahrzeuge, LOD-Wechsel, Cook/Packaging und Leistungsziele benötigen eigene Abnahmen.

## Nachweis und Fehlerhilfe

Der [bereinigte Prüfbericht](../evidence/vehicle-asset-evaluation.json) trennt Export, Unreal-Import, die getrennte Zentimeterkorrektur der Meshes und Clips, eingefrorene Editorposen und tatsächliches Ticken in SimulateInEditor (SIE). Die Abnahme ist für diesen lokalen Technikversuch abgeschlossen.

Die direkte Source-Poseprüfung verglich 486/222/33 Bone-Translationen des Liebherr/Radladers/Lkw über drei Zeiten. Nach dem separaten Clip-Reimport waren sie exakt um Faktor 100 umgerechnet, mit 0 cm gemessenem Umrechnungsfehler. Eine neue Editorinstanz lud danach die gespeicherte Karte und alle eigenen Assets; die synchrone Poseprüfung bei 0/0,5/1/2/3 Sekunden zeigte 80/42/9 bewegte Bones. Liebherr und Radlader erreichten dabei maximal rund 144,16 beziehungsweise 89,97 cm Positionsänderung.

Die unveränderte native Unreal-Übersichtsaufnahme wurde vom Agenten visuell geprüft: alle drei Fahrzeuggeometrien sind sichtbar, einschließlich angehobener Radladerschaufel und gekippter Lkw-Mulde. Das bestätigt die Ansicht des Technikversuchs; die angenäherten Oberflächen sind keine vollständige Detail- oder Materialtreueabnahme. Wegen der offenen Lkw-Herkunft wird die lokale Aufnahme nicht im öffentlichen Bundle verteilt.

Im anschließenden SIE-Lauf stieg die Weltzeit von rund 0,109 auf 0,930 Sekunden; die Clips liefen bei allen drei Fahrzeugen weiter. Im gemessenen Startfenster bewegten sich 80/42/8 Bones. Die Lkw-Mulde beginnt später im Clip und ist daher durch die längere eingefrorene Poseprobe und die gerenderte gekippte Stellung belegt, nicht durch dieses kurze SIE-Fenster. SIE wurde sauber gestoppt und der eigene Editor mit Exit 0 beendet. Alle 18 vorhandenen Spielstände blieben byteidentisch; es entstand kein zusätzlicher Slot. Das ist keine Abnahme fahrbarer Maschinen oder ihrer Arbeit am Terrain.

Bei winzigen Fahrzeugen zuerst die FBX-Einheitenumrechnung beider Importdatensätze und den gesonderten Reimport der Clips prüfen. `set_position` ändert nur die Animationszeit im Proxy. Für eingefrorene Editorposen erzwingt das eigene Prüfwerkzeug anschließend mit `override_animation_data` eine synchrone Bone-Auswertung; bloße Slate-Ticks sind dafür kein Nachweis. Schwarze rechteckige Aufkleber deuten auf fehlende Masken oder Farbmaps. Flache graue Lackierung kann entstehen, wenn ein nicht verbundener Principled-Standardwert statt der tatsächlichen Blender-Farbquelle übernommen wurde. Fehlende Normalmaps oder abweichende prozedurale Oberflächen werden als Materialgrenze dokumentiert.
