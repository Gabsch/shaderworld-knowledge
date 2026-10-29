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
  at: "2026-10-29T00:02:31Z"
sources:
- id: storage-source-audit
  resource: ../evidence/shaderworld-storage-source-audit.json
  title: Speicher-/Datenlayer-Quellbefund mit Herstellerlinks, ohne Laufzeitbehauptung
- id: foundations
  resource: ../evidence/foundations-report.json
  title: Bereinigte Foundations-Abnahme und getrennte Setup-, Automation- und Sichtbelege
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

## Aktuelle eigene Planer-, Rodungs- und Untergrundnachweise

- [Speicher-/Datenlayerprüfung](../evidence/shaderworld-storage-source-audit.json): lesender Befund der installierten 4.1-Symbole. Vom [beschlossenen Umsetzungsplan](scaping-machine-work-plan.md) und bestehenden Laufzeitnachweisen getrennt; keine neue Persistenzabnahme.
- [Baustellenplaner](../evidence/construction-planner-test.json): 36 native Tests, je vier neue uncooked/cooked Neustarts, normale Controller-Speicherprobe; Eingabe- und Karten-Cookgrenzen getrennt.
- [Rodungscache](../evidence/clearing-cache-test.json): Quellen-/Snapshotvertrag, nativer Rotationsverlust versus eigener Ledgerrestore und acht isolierte cooked CPU-Messfenster mit historischem Vergleich.
- [Untergrund-Hybrid](../evidence/underground-hybrid-test.json): eigene Huelle, unveraenderte Oberflaeche, Kollision, Profil-Neustart und getrennte Sichtbelege. Keine Behauptung frei grabbarer 3D-ShaderWorld-Geologie.
- Die neuen Bilder zeigen eigene Laboraufnahmen. Herkunft, Sichtpruefung und unveraenderte Dateihashes stehen im [Bildverzeichnis](../evidence/image-manifest.json). Projekt-/Pluginquellen, lizenzierte Kartenassets und Rohspielstaende sind nicht im Bundle enthalten.


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

## Neue CityBasics-Belege

Der [CityBasics-Bericht](../evidence/citybasics-report.json) enthält bereinigte native Kollisionsproben und tatsächliche CharacterMovement-Durchfahrten. Die [Waldstraße](../assets/images/citybasics-road.png) und [Portalzufahrt](../assets/images/citybasics-portal-approach.png) sind unveränderte native **CaptureEditorImage**-Aufnahmen vom 28. Oktober 2026 mit sichtbarer Editoroberfläche. Sie zeigen den spielbaren Prototyp; Fahrbahn, Portal und Testbuggy sind noch einfache Laborgeometrie. Größen und Hashes stehen im [Manifest](../evidence/image-manifest.json).

## Küsten-, Biom- und Straßenprüfung

Die [lesende Prüfung vom 28. Oktober 2026](../evidence/coast-biome-road-inspection.json) hält aktuelle PIE-Parameter, die Wassermaterial-Verkabelung, Pflanzen-Höhenintervalle und die tatsächliche Straßenherkunft fest. Sie enthält außerdem getrennte Asset-/Codebefunde und noch nicht ausgeführte Testvorschläge. Der vom Nutzer gemeldete Wellendurchbruch wurde dabei nicht reproduziert oder behoben.

Der [Korrekturbericht](../evidence/coast-correction-report.json) ergänzt die anschließend gespeicherten Projektfilter, Dämpfung 1,0 und den nativen Tunnel-Wasserausschluss. Er enthält Original-/Projektwerte sowie die Boxeigenschaften nach PIE-Neustart. Nutzerangabe zum Tunnel, Codebefund zum Hole-Sentinel und die erste Rückmeldung „Bisher trocken“ nach dem Fix sind getrennt erfasst; Langzeit- und gültige GPU-Prüfung fehlen weiterhin.

## Wiederverwendbare Tunnelkomponente

Der [Komponentenbericht](../evidence/tunnel-component-report.json) enthält den erfolgreichen nativen Build, zwei bestandene Automationtests und Eigenschaften der neuen **CityLab Tunnel (Dry)**-Komponente im Editor, nach tatsächlichem Kartenladen und im neu gestarteten PIE. Die API-Tests verwenden **NullRHI** und einen kontrollierten Wasserprovider im echten WaterSubsystem. Ihr Archive-/PostLoad-Test ist von der zusätzlichen echten Kartenladung getrennt. Ein frischer Spielprozess bestand danach 65/65 Kollisionsproben und rund 259,44 m bodengebundene Durchfahrt; der Gesamtbericht ist **passed_with_limits**. Die [neue native PIE-Aufnahme](../assets/images/citybasics-dry-tunnel-component.png) zeigt den sichtbaren Innenraum trocken; ein inspizierter Frame ist keine Langzeitabnahme. Herkunft und Hash stehen im [Bildmanifest](../evidence/image-manifest.json). Die frühere Nutzerantwort „Bisher trocken“ betrifft weiterhin die vorherige separate Box.

## Laufzeitstraßen im RoadLab

Der [RoadLab-Bericht](../evidence/runtime-roads-report.json) exportiert zwei erfolgreiche gerenderte uncooked Spielprozesse: je 72 Kollisionsproben, zwei Straßen mit 16 Meshsegmenten, identische logische Datensätze und Pflanzenursprünge im Trassenkern vor Bau, nach Bau/Laden, nach Rücknahme und nach erneutem Laden. Je Phase bleiben drei gleiche vollständige Matrix-Fingerprints erhalten. Die Herkunft der Rohdaten und Grenzen sind im JSON genannt; PIDs, Slot-/Laufkennungen und lokale Pfade wurden weggelassen. Format-1-Kompatibilität betrifft ein synthetisches Fixture, keinen archivierten historischen Spielstand.

Die [erste PIE-Aufnahme](../assets/images/runtime-road-first-pie.png) zeigt eine Beispielstraße; die [Aufnahme des bestandenen Create-Laufs](../assets/images/runtime-road-create-verified.png) zeigt zwei Straßen mit Markierungen. Die zusätzliche [normale PIE-Aufnahme nach Auto-Load](../assets/images/runtime-road-normal-autoload-pie.png) zeigt den durch R/Enter ergänzten und per K gespeicherten Stand nach erneutem Play; der zweite Straßenverlauf weicht deshalb vom nativen Fixture ab. Alle drei Bilder sind unveränderte, inspizierte native Frames vom 28. Oktober 2026. Die Vorbereitungsmeldung im Create-Bild gehört zum Testmodus. Bilder ersetzen keine Dauer-, GPU-Masken- oder Überhangmessung; Herkunft, Bytes und Hashes stehen im [Manifest](../evidence/image-manifest.json).

Der Bericht enthält außerdem die zusätzliche native Slate-Bedienprobe für R/Enter, Entwurfskorrektur, Q/E, K/L und normales PIE-Autoload sowie die frische Format-2-Regression der alten Bauplatzkarte. Kamerabewegung per ActorTools ist von ungeprüften WASD-/Maus-Eingaben getrennt; die PIE-Bedienprobe ist kein eigener Kaltstartprozess.

## Zusammenhängende CityLoop-Spielschleife

Der [CityLoop-Bericht](../evidence/cityloop-report.json) ist ein bereinigter Export dreier getrennter gerenderter Spielprozesse mit Format 3. Er trennt den gespeicherten Wegfortschritt, das Weiterlaufen nach Neustart und die erhaltene Ankunft nach einem weiteren Neustart. Terrainhöhe, sichtbare HISM-Instanzursprünge und Bodenkontakt der Figur sind gemessen; allgemeine NavMesh-Navigation und Cook sind offen. Persönliche Dateipfade, Slot-/Laufkennungen, Objekt-GUIDs und Prozessnummern fehlen im öffentlichen Export.

Die [Aufnahme unterwegs](../assets/images/cityloop-midroute.png) und [Ankunft nach erneutem Neustart](../assets/images/cityloop-restarted-arrival.png) sind unveränderte native **FScreenshotRequest**-Frames vom 28. Oktober 2026. Beide wurden visuell inspiziert. Der erste Frame zeigt die für den Speichervorgang pausierte Figur; die Vorbereitungsmeldung im HUD gehört zum Testmodus. Haus, freier Bauplatz, Zugang und Straße sind sichtbar. Herkunft, Bytes und Hashes stehen im [Bildmanifest](../evidence/image-manifest.json).

Der [gesonderte Regressionsbericht](../evidence/cityloop-regression-report.json) hält die erneuten RoadLab- und älteren Bauplatztests mit Speicherformat 3 fest. Insgesamt vier frische gerenderte Spielprozesse bestanden. Die vorherigen Format-2-Belege bleiben als frühere Abnahmen erhalten.

Die zusätzliche [normale CityLoop-PIE-Aufnahme](../assets/images/cityloop-normal-autoload-house.png) zeigt das zweite Testhaus mit blauem Bürger nach nativem R/Enter/P/L, automatischem Speichern ohne K und normalem Stop/Play-Autoload. Zwei Grundstücks-IDs und zwei angekommene Bürger wurden dabei zurückgelesen. Dieses inspizierte CaptureEditorImage ist unverändert; sichtbare Editor-Diagnosehinweise wurden nicht retuschiert und gelten nicht als gelöst.

## Foundations: neue Geländeplanung und dauerhafte Einzelrodung

Der [Foundations-Bericht](../evidence/foundations-report.json) ergänzt am **28. Oktober 2026** zwei erfolgreiche gerenderte **uncooked** Spielprozesse mit **Speicherformat 4**: Nach der nativen Paintkorrektur mit schwarzer Datamap bestanden **29/29 Checks in 127,1 s** beim Erzeugen und **12/12 in 70,1 s** beim Wiederherstellen, mit **306 + 288** erfolgreichen echten Terrain-Physikproben und **35 + 32** protokollierten Abfragesamples. Er trennt inerte Planung von expliziter Lab-Debug-Ausführung, hält gespeicherte noch nicht ausgeführte/stornierte Pläne getrennt von Backends und bestätigt Einzelrodungszustände anhand von CPU-Transformpuffern und aktiven Kollisionsinstanzen, tatsächlicher Instanzregeneration und 30 s Beobachtungszeit; die damaligen Baumzähler waren kein GPU-Pixelbeleg. Wiederholte Loads und atomare Ablehnung einer falschen Identität sind ebenfalls enthalten. Personenpfade, Slot-/Laufkennungen, Objekt-GUIDs und PIDs gehören nicht in den öffentlichen Export.

Derselbe Bericht erfasst getrennt **fünf Biomprofile und 19 eigene Assets nach gespeichertem Kartenreload**, **acht erfolgreiche native Automationtests unter NullRHI** und die zusätzliche CityLoop-Regression mit Format 4. Der kontrollierte Hochkamera-/Umwegtest ist kein globaler NavMesh-Nachweis; die normale reale Hochkamera-Planbedienung wurde später separat geprüft. Sechs Tests liefen ohne Warnung; die zwei Warnungen aus dem Aufräumen einer Testwelt ohne World Context und der absichtlichen Ablehnung alten ausgeführten Paints sind erhalten. Der neue Migrationstest prüft logische Records und Livezustand, keine archivierte binäre SaveGame-Datei. Die früheren Format-2-/Format-3-Berichte werden durch diese neue Abnahme nicht umgedeutet.

Die [Dach-Nahaufnahme](../assets/images/foundations-roof.png) ist ein unveränderter, inspizierter nativer GameViewport-Frame aus normalem PIE, aufgenommen über den Konsolenbefehl **Shot / FScreenshotRequest** ohne Editoroberfläche: geschlossenes oranges Satteldach, Testhaus und Bürger sind sichtbar. Das Bild entstand nach Korrektur der Dreiecksorientierung und ist von den späteren Foundations-Physikläufen getrennt. Herkunft, Größe und SHA-256 stehen im [Bildmanifest](../evidence/image-manifest.json). Der [Foundations-Guide](../guides/foundations-lab.md) erklärt Bedienung und Grenzen ohne vorausgesetzte Quellcodelektüre.

Die korrigierte verpackte V2-Fassung bestand anschließend **zwei frische gekochte Spielprozesse** mit **RequiresCookedData = true**: **29/29 Checks in 118,6 s** beim Erzeugen und **12/12 in 66,1 s** beim Wiederherstellen, **306 + 279** erfolgreiche Terrainproben und **35 + 31** protokollierte Abfragesamples. Der vollständige UAT-Lauf mit Cook, Stage und Archive endete nach **96,15 s mit Exit 0**. Das Development-Paket enthält zwei gekochte Karten; die Laufzeitabnahme gilt für Foundations. Eine Shipping-Abnahme und andere Karten werden daraus nicht abgeleitet; die älteren kartenbezogenen Cook-Grenzen bleiben erhalten.

Eine separate normale PIE-Bedienprobe verwendete echte native Slate-Tasten aus **500300 cm Kamerahöhe**, neun reale Terrainproben bei **Z = 299,995 cm** und vier stabile Durchläufe. Inerte Planerstellung, PageUp/Undo, Tab-Auswahl, K und Stop/Start-Autoload mit derselben Plan-ID und absoluter Ebnen-Höhe wurden geprüft; Verschieben auf anderen Boden behielt das Ziel 4 m bei. Dieser PIE-Neustart ist kein eigener Betriebssystemprozess.

Bei der anschließenden Material-Sichtprüfung brachte Snow-Paint Bewuchs auf einem geräumten Bauplatz zurück. Die früheren Einstellungen und die unveränderte Physikhöhe hatten diese Wechselwirkung mit der NoGrowth-Maske nicht erfasst; der frühere „noBiome“-Checkname war deshalb zu weit gefasst. Die Korrektur durch einen nativen LayerMask-Brush bestand anschließend die neue uncooked Core-/Side-Vegetationsregression: in der letzten erfolgreichen Ausgangsprobe des uncooked Create-Laufs **436 Kernursprünge mit drei Bäumen und 29 Randursprünge**, nach Maske, Paint, Regeneration und drei Loads pro Prozess **0/0**. Der separate Waldbaum behielt seine nichtnull CPU-Transformdaten, aktiven Kollisionsinstanzen und Transformation; seine sichtbare Krone wurde in diesem Lauf nicht separat ausgewertet. Die nicht gespeicherten Maskenfixtures werden in jedem Prozess neu erzeugt; die Loads verwenden den tatsächlichen Managerpfad. Der erneute verpackte V2-Lauf bestätigte dieselben Masken-/Kontrollbedingungen nach tatsächlicher Regeneration und drei Loads pro Prozess. Ein weiterer tatsächlicher Sichtvergleich fand die weiße Datamap als falschen Selektor des ungesetzten Flow-Materials; die aktuelle Fassung verwendet deshalb schwarz (Flow-Anteil 0), und die Verifier prüfen Datamap und deaktivierte Neben-IDs ausdrücklich. Der abschließende Materialbildvergleich der kompilierten Black-Fassung bestand anschließend in normalem PIE: native T/F6/K/L-Eingaben, keine Brush-Parameterüberschreibung, sichtbares Snow nach Ausführung und erneut nach Laden. Der übermalte Bauplatz behielt seinen strukturellen Sandboden, blieb im geprüften Frame frei von Bewuchs und hielt 500 cm Terrainhöhe.

Die [Ausgangsaufnahme](../assets/images/foundations-paint-before.png), [Snow nach K/L](../assets/images/foundations-paint-reloaded.png) und [geschützter Bauplatz nach überlappendem Snow-Paint](../assets/images/foundations-protected-pad.png) sind unveränderte, visuell inspizierte native **Shot-/FScreenshotRequest**-GameViewport-Frames vom 28. Oktober 2026. Das HUD wurde vor der Aufnahme ausgeblendet; die Bilder wurden nicht nachbearbeitet. Herkunft, Größe und SHA-256 stehen im [Bildmanifest](../evidence/image-manifest.json). Diese ausgewählten normalen PIE-Bilder ergänzen die Prozessberichte; sie sind kein Pixelgleichheitstest, keine eigene Materialbild-Abnahme im Paket und keine vollständige Biom- oder Leistungsprüfung.

## Sichtbare Einzelrodung korrigiert

Der eigene [Rodungsbericht](../evidence/tree-clearing-test.json) trennt den neuen Mausstrahl-/Renderbaum-Codebefund, zwölf bestandene native Tests, zwei neue cooked Spielprozesse (29/29 und 12/12) und einen tatsächlichen normalen PIE-Bildvergleich per Backend-API. Der Zielbaum verschwindet im gerenderten Bild und bleibt nach Laden entfernt; ein markierter Kontrollbaum bleibt erhalten. Die drei unveränderten eigenen Bilder stehen im [Bildmanifest](../evidence/image-manifest.json). Die Konsole/API-Abnahme ist keine beobachtete C-Tasten-/Gelbpreview-Bedienung.

## Geschlossener Materialkreislauf

Die [Kreislaufanleitung](../guides/closed-material-cycle.md) und ihr [bereinigter Bericht](../evidence/fill-cycle-test.json) stammen aus der eigenen ConstructionLab-Erweiterung. Native 29er-Suite, zwei uncooked und zwei cooked Prozesse, exakte Modellhashes und unabhängige Kollisionsproben sind getrennt geführt. Die [pausierte Übersicht](../assets/images/fill-cycle-planned.png) ist eine unveränderte native Slate-Aufnahme aus normalem PIE, visuell vom Agenten geprüft: vorhandenes Lager, fertige Grube und noch ungerodeter Zielbereich. Sie zeigt keinen fertig aufgeschütteten Boden und ersetzt keinen Pixelvergleich. Herkunft und Hash stehen im [Bildmanifest](../evidence/image-manifest.json).

## OKF

Der [Google-Artikel](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/?hl=en) erläutert das Was und Warum von OKF anhand von v0.1. Für das Dateiformat dieser Wissensbasis gilt die [kanonische Spezifikation v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md). Die Formatversion ist im Wurzelindex festgehalten.
