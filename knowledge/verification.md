---
type: Playbook
title: Prüfstand und offene Tests
description: Den tatsächlichen Nachweis je Thema und die verbleibenden City-Builder-Tests
  erkennen.
tags:
- shaderworld
- unreal-engine
- city-builder
status: stable
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: Zusammenfassung der vorhandenen Nachweise mit getrennten offenen Tests
generated:
  by: codex/gpt-6
  at: "2026-10-28T21:08:00Z"
sources:
- id: fill-cycle
  resource: evidence/fill-cycle-test.json
  title: 29 native Tests und geschlossener Kreislauf in uncooked und cooked Neustarts
- id: camera-tree
  resource: evidence/camera-tree-test.json
  title: Selektiver Kamerabaumfilter mit 25 nativen Tests und separater normaler PIE-Wiederherstellung
- id: construction-lab
  resource: guides/construction-lab.md
  title: Eigenes Baugrubenlabor mit Bedienung und begrenztem cooked Neustartabschluss
- id: construction-proof
  resource: evidence/construction-lab-test.json
  title: Damalige 22 native Construction-Tests, cooked Baugrubenabschluss und begrenzte normale PIE-Bedien-/Speicherproben
- id: navigation-proof
  resource: evidence/terrain-navigation-test.json
  title: Elf bestandene gerenderte Navigationschecks mit zusätzlichen bewussten Harness-Warteticks
- id: height-quantization
  resource: "Separat lizenzierter ShaderWorld-4.1-Code: Shaders/Private/ShaderWorldUtilities.usf, GetShaderWorldHeight-Ausgabe um Zeile 760 mit int-Konvertierung; eigener CityLabConstruction.cpp/CityLabConstructionVerification.cpp-Source jetzt mit explizitem 5-cm-Höhengate und Kollisionsretry. Quellen gelesen; kompilierte cooked Abnahme im Baugrubenbericht bestanden, Code nicht im Bundle enthalten"
  title: Ganzzahlige Höhenkodierung als Scopegrenze der neuen Baugruben-Höhenprüfung
- id: clearing-benchmark
  resource: evidence/clearing-performance-test.json
  title: Acht erfolgreiche isolierte cooked CPU-Messfenster für Rodungsnachlauf und native Rayabfragen
- id: tree-fix
  resource: evidence/tree-clearing-test.json
  title: Neue Builds, zwölf native Tests, cooked Datenregression und separate normale PIE-Backendbilder und nachträgliche Nutzerbestätigung der korrigierten Rodung
- id: build-controls
  resource: evidence/build-controls-test.json
  title: Neue Kamera- und Panelprüfungen mit normalem PIE und getrennten nativen Codeverträgen
- id: region-layer-api
  resource: "ShaderWorld 4.1: Public/Data/ShaderWorldTerrainRegion.h, Private/Actor/ShaderWorldActor_Cache.cpp, Public/SWorldSubsystem.h, Private/Utilities/ReadBackManager.cpp und Shaders/Private/ShaderWorldRegionExport.usf; separat lizenzierter Plugin-Quellcode, nicht mitgeliefert"
  title: Quellenprüfung des nativen Terrainregion-Exports und asynchronen Layer-Readbacks; kein Laufzeittest
- id: foundations
  resource: evidence/foundations-report.json
  title: Foundations mit zwei gerenderten uncooked Spielprozessen, Asset-Readback und getrennten nativen Tests
- id: construction-design
  resource: reference/construction-and-terrain-architecture.md
  title: Weitergehendes Architekturkonzept; kleiner Baugrubenkreislauf mit eigenem cooked Nachweis
- id: cityloop
  resource: evidence/cityloop-report.json
  title: Drei Spielprozesse für Grundstück, Haus und Bürgerzustand
- id: runtime-road-code
  resource: guides/runtime-roads.md
  title: RoadLab-Anleitung und abgegrenzter Zwei-Prozess-Nachweis
- id: tunnel-component
  resource: evidence/tunnel-component-report.json
  title: CityLab-Tunnelkomponente; native Tests und geprüfte Karten-/PIE-Integration
- id: terrain
  resource: evidence/terrain-report.json
  title: Terrainprüfung
- id: citylab
  resource: evidence/citylab-report.json
  title: CityLabprüfung
- id: persistence
  resource: evidence/persistence-report.json
  title: Neustartprüfung
- id: ocean
  resource: evidence/ocean-report.json
  title: Ozeanprüfung
- id: basics
  resource: evidence/citybasics-report.json
  title: CityBasics mit zwei echten Durchfahrten
- id: holes
  resource: evidence/hole-report.json
  title: Lochprüfung
---


# Prüfstand und offene Tests

Stand: **28. Oktober 2026**, Unreal **5.8.4**, ShaderWorld **4.1**. Die Statusangaben beschreiben den jeweiligen Versuch. Eine schöne Ansicht bestätigt weder dauerhafte Speicherung noch Physikkollision oder Leistung einer großen Welt.

## So liest du den Prüfstatus

| Begriff | Bedeutung |
| --- | --- |
| Herstellerangabe | In einer offiziellen Quelle beschrieben; hier noch nicht selbst bestätigt |
| Code-/Assetbefund | API, Einstellung oder Beispiel im installierten Bestand gelesen |
| Editor visuell | Tatsächliches Bild in der Editoransicht gesehen |
| Editor/PIE geprüft | Konkrete Bedingungen oder Kollisionen in der Vorschau gemessen |
| Neustart geprüft | Getrennter Spielprozess hat gespeicherte Änderungen wiederhergestellt |
| Offen | Der konkrete Anwendungsfall braucht noch einen eigenen Versuch |

`status: stable` im OKF-Frontmatter bedeutet, dass die Seite als Anleitung bereitsteht. Es bedeutet nicht, dass alle erwähnten Funktionen abgenommen sind. `generated` dokumentiert die Erstellung, `verified` eine Bestätigung der Seite gegen Quellen. Den fachlichen Testumfang halten unsere zusätzlichen Felder `evidence_scope` und der sichtbare Text fest. Eine technische Linkprüfung darf daraus keinen erfolgreichen Unreal-Test machen.

## Bisheriger Stand

| Thema | Nachweis | Grenze |
| --- | --- | --- |
| Flaches 1-km-Terrain und Kollision | [Terrain-Bericht](evidence/terrain-report.json), Editor-Einstellungen/erneutes Laden und vier PIE-Terrainproben | Kein verpackter Build |
| Bauplatz und native Straße | [CityLab-Bericht](evidence/citylab-report.json), sechs Phasen mit je 14 Proben | Kleiner Laborbereich, keine Verkehrssimulation |
| Dauerhafte Pads und Straßen | [Neustart-Bericht](evidence/persistence-report.json), zwei getrennte Prozesse; je 26 ursprüngliche und 26 geänderte Terrainproben | Eigene CityLab-SaveGame-Implementierung; uncooked Standalone |
| P/R, K/L und automatisches Laden | Beobachteter UI-Test im Persistenzbericht | Kein allgemeines Plugin-Bedienkonzept |
| Reference-Biom und Dreckstraße | Live-Ansicht und Actor-/Komponentenprüfung | Einzelrodung separat im Foundations-Labor geprüft; die begrenzte Straßenmaske hat ihren RoadLab-Nachweis |
| Ozean mit Wind und Schaum | [Ozeanbericht](evidence/ocean-report.json), Wind 18 m/s, Schaum aktiv, Rebuild beendet, sichtbare Schaumflächen | Keine Auftriebs-, Dedicated-Server- oder Mehrspielerabnahme |
| CityBasics-Tunnel und Testbuggy | [CityBasics-Bericht](evidence/citybasics-report.json): zwei eigenständige Spielstarts, je 65/65 Kollisionsproben und rund 259,48 m bodengebundene Durchfahrt | Eigene Fahrbahn-/Tunnelmeshes; CharacterMovement, keine Chaos-Fahrzeugphysik; F-/Mausbedienung manuell offen |
| Eigene Tunnelkomponente | [Komponentenbericht](evidence/tunnel-component-report.json): Build und zwei native Automationtests zu Profil/Lebenszyklus und echten WaterSubsystem-Abfragen bestanden | NullRHI mit kontrolliertem Wasserprovider; gespeicherte Karte und neues PIE zusätzlich per Eigenschaften geprüft, zusätzlich frischer Spielprozess mit 65/65 Kollisionsproben und rund 259,44 m Fahrt; neuer Sichtnachweis nur ein inspizierter PIE-Frame |
| RoadLab-Laufzeitstraßen | [RoadLab-Bericht](evidence/runtime-roads-report.json), zwei Prozesse mit je 72/72 Kollisionsproben; zwei Straßen und 16 Meshes identisch wiederhergestellt, Pflanzenursprünge 999 → 0 → 999 → 0 | 3,5-m-Kern und 10–30-m-Referenzbereich; keine Äste-/Überhang- oder GPU-Maskenmessung; R/Enter, Entwurfstasten, Q/E, K/L und PIE-Autoload geprüft; Kamera-/Aliastasten und Cook/Shipping offen |
| RoadLab-POM-Referenzebene | [Renderbericht](evidence/road-pom-render-report.json) und [Anleitung](guides/runtime-roads.md#nahsicht-boden-erscheint-durch-den-asphalt): reversibler 30-m-Bildvergleich, korrigierte 3-/100-m-Ansichten sowie gespeicherte Actor-Zuweisung nach Kartenneuladen/neuem PIE geprüft | Reguläre eigene Materialinstanz, POM/Relief bleiben an; PIE im selben Editorprozess, keine neue Standalone-Kollisions-/Cook-Abnahme |
| CityLoop: Straße, Grundstück, Haus und Bürger | [Spielschleifen-Bericht](evidence/cityloop-report.json): drei getrennte gerenderte Spielprozesse, Fortschritt unterwegs gespeichert und bis zur Haustür fortgesetzt, Ankunft nach weiterem Neustart erhalten; Grundstückskern 252 → 0 Pflanzenursprünge bei 2374 Referenzen | Sechs Terrain-Messpunkte wiederholt geprüft; straßengeführte Route mit Bodenkontakt, keine allgemeine NavMesh-/Cook-Abnahme; R/Enter/P/L, automatisches Speichern und normales PIE-Autoload zusätzlich geprüft; Kamera-/Aliastasten offen |
| Foundations: Planung, Ausführung und Einzelrodung | [Foundations-Bericht](evidence/foundations-report.json): korrigierte uncooked Fassung mit 29/29 und 12/12 Checks, 306/306 und 288/288 Terrainproben sowie Core-/Side-NoGrowth nach Paint, Regeneration und Loads; Format 4 wiederhergestellt | Aktuelle V2-Fassung auch cooked bestanden, 29/29 und 12/12 Checks mit 306 + 279 Terrainproben; Development, nur Foundations-Laufzeitabnahme; Materialbild separat in normalem PIE geprüft, eigene Paket-Pixelprüfung und Shipping offen |
| Foundations: normale Planbedienung aus großer Höhe | Echte Slate-Tasten aus 500300 cm Kamerahöhe, neun gültige Terrainproben, Plan-Undo, Tab-Auswahl, K und normales PIE-Autoload; absolute Ebnen-Höhe beim Verschieben erhalten | Frühere PIE-Planprobe im selben Editorprozess; die finale Material-Sichtprobe ist separat dokumentiert |
| Foundations-Biomprofile und Testhausdach | Fünf Profile und 19 eigene Assets nach gespeichertem Kartenneuladen zurückgelesen; [Dach-Nahaufnahme](assets/images/foundations-roof.png) in tatsächlichem PIE inspiziert | Assetwerte sind keine vollständige visuelle Abnahme aller Biome; das Dachbild ist ein einzelner Frame |
| Begrenzte Bürgerumwege, Bauabfragen und Backendmigration | Acht erfolgreiche native Automationtests unter NullRHI, darunter Umweg-Wiederherstellung, falsche Endanker und sichere v1-Backendmigration; sechs ohne Warnung, zwei mit protokollierter Warnung | Lokale Hindernisse und analytischer Testboden; keine allgemeine NavMesh-Navigation; reale Hochkamera-Planbedienung separat geprüft |
| Foundations: finale Material-Sichtprobe | Native T/F6/K/L-Eingaben in normalem PIE; Snow nach Ausführung und nach Laden sichtbar; übermalter Bauplatz behält Sand, sichtbare Freistellung und 500 cm Bodenhöhe; [drei Frames](reference/sources.md#foundations-neue-geländeplanung-und-dauerhafte-einzelrodung) | Ausgewählte qualitative Spielbilder im selben Editorprozess; kein Pixelgleichheitstest und keine separate verpackte Materialbild-Abnahme |
| Frühere native Baustellen-/Navigationssuite | [Construction-Bericht](evidence/construction-lab-test.json): nach letztem Fix 22/22 Tests in 0,357 s, 20 ohne und zwei mit bekannten Warnungen, 0 fehlgeschlagen | NullRHI-Logik-/API-Tests; gerenderter Baugrubenabschluss separat geprüft |
| Kamerabaumfilter und damalige native Suite | [Kamerabericht](evidence/camera-tree-test.json): Editor-/Gamebuild, SkipCook-Repackage und 25/25 Tests in 0,460 s; 23 ohne, zwei bekannte Warnungen, drei neue Query-Physikfälle fehlerfrei | Normales ConstructionLab-Wiederladen mit passendem Boden/Kamerapose zusätzlich belegt; keine physische WASD- oder aktuelle cooked Gameplay-Abnahme aus dem Repackage ableiten |
| ConstructionLab: vollständiger cooked Arbeits-/Speicherlauf | [Bericht](evidence/construction-lab-test.json): zwei frische cooked Prozesse, Create 14/14 in 24,7 s und Resume 15/15 in 113,8 s; exakter Hashrestore, drei Loads und Abschluss mit 172,8 t Lager/0 g Modellbilanzfehler | Physischer Maximalfehler 2,000778 cm im lokalen 5-cm-/Drei-Pass-Gate; kein unabhängiges Meshvolumen oder vollständiger korrigierter uncooked Pair; begrenzte normale PIE-Probe separat unten |
| ConstructionLab: normale PIE-Bedienung und Autosave-Schutz | Automatischer pausierter Nullplan samt Save, Arbeit/Transport und eine Pause per nativer Slate-Aktion bestätigt; 18-t-Puffer über 57 weitere Takte stabil; 60-t-Zwischenstand nach Stop/Play gleich; fremdgebundener Stand abgewiesen und bytegleich erhalten | Finale Pause zusätzlich über Controller-API; F5-Injektion ohne bestätigten Callback, keine pauschale Tastatur-/Fokus-/menschliche Bedienabnahme oder automatischer Pixelvergleich[^construction-proof] |
| Geschlossener Materialkreislauf | [Kreislaufbericht](evidence/fill-cycle-test.json): 29/29 native Tests (27 ohne/2 bekannte Warnungen), uncooked 54,8/223,7 s und cooked 30,9/213,3 s mit jeweils 6/6 und 10/10 Checks. Alle 172,8 t wieder eingebaut, 0 g Bilanzfehler; 108 + 270 passende Kollisionsproben je Laufpaar, maximal 2,005 cm bei 5 cm Toleranz. Exakter voller Recordrestore und drei weitere Loads | Zwei Standorte, gemeinsames Lager und feste Routen; beschleunigtes Prüfprofil. Normaler alter Lagerstand, neue pausierte Planung und Save/Load zusätzlich geprüft; kein allgemeines Verkehrs-/Verdichtungs-/Meshvolumen-/Pixel-/Großwelturteil |
| Bürger vor neuer tatsächlicher Grube | [Navigationsbericht](evidence/terrain-navigation-test.json): 11/11 Checks in 40,9 s, 81 bestätigte native Groundhits, Wiederaufnahme und Ankunft nach Reparatur | Harness hält nach Managerbereitschaft zusätzlich zehn Ticks bis zur unabhängigen Höhenprüfung an; keine automatische Produktions-Fence/NavMesh-Abnahme |
| Rodungsbenchmark: 0/1/10/100 Records | [CPU-Bericht](evidence/clearing-performance-test.json): acht isolierte cooked Messfenster, 255 Reapply-/153 Rayaufrufe, CPU-Restore aller 101 gewählten visuellen Ressourcen | Feste Kamera, maximal 100 Records, acht Sekunden je Fenster; 48er Cap ist kein FPS-/GPU-Leistungsnachweis, vollständige UI-Vorschau und finaler Kollisions-Restore separat offen |
| Terrainlöcher | [Lochbericht](evidence/hole-report.json), Demoansicht, Komponenten und Implementierung gelesen | Eigene Bergportale und Tunnelkörper im CityBasics-Bericht geprüft; Verpackung offen |
| DX12/SM6 | Nanite-Warnung im Basistest behoben | Lumen-Konfiguration in Demoansichten weiterhin offen |

Beim Persistenztest lag der größte ursprüngliche Gelände-Höhenfehler bei rund **0,949 cm**, nach Änderungen bei rund **0,630 cm**; die Toleranz betrug **3 cm**. IDs, Kontrollpunkte und Änderungsreihenfolge wurden zwischen Erzeugen und Laden verglichen. Wiederholtes Laden erzeugte keine Duplikate, ein fehlender Slot und eine falsche Speicherformatversion ließen die vorhandene Stadt erhalten. Generator-/Seed-Konflikte werden im Code geprüft, wurden aber nicht als eigene Negativversuche abgenommen. Im JSON bedeuten `false`-Checks in nicht zuständigen Phasen **nicht anwendbar**; die Gesamt- und Phasenurteile sind separat angegeben.

Nach der Korrektur der Zufahrts-Längentabellen bestand die gespeicherte Endfassung am **28. Oktober 2026** eine zusätzliche Prüfung: nochmals **65/65 Proben**, **133/133 Fahrproben am Boden** und **259,35 m** tatsächliche Durchfahrt. Die zwei ursprünglichen Läufe und die abschließende Kontrolle sind im [CityBasics-Bericht](evidence/citybasics-report.json) getrennt erhalten.

Die [Küsten-/Biomprüfung vom 28. Oktober](evidence/coast-biome-road-inspection.json) ist eine lesende Parameter-, Material-, Asset- und Codeprüfung. Sie bestätigt die vorhandene Ground/Ocean-Verbindung und den angeschlossenen Water-Exclusion-Materialknoten. Die alten Pflanzen-Minimalhöhen erlauben den neuen Meeresboden als Waldstandort. Die [Korrektur](evidence/coast-correction-report.json) ist inzwischen gespeichert: eigenes Landbiom mit drei Pflanzenfiltern ab 150 cm, Dämpfung 1,0 und native Tunnel-Air-Pocket-Box. Assetwerte, unveränderte Plugin-Originale und die Box nach PIE-Neustart wurden zurückgelesen. Der Nutzer berichtete weiterhin Wellen bei Dämpfung 1,0 am Tunnel; der gelesene Hole-Cache-Pfad erklärt dort fehlende Küstendämpfung. Nach dem Einbau bestätigte der Nutzer an der betroffenen Tunnelstelle **„Bisher trocken“**. Eine längere Sichtprüfung, die Unterwasservegetation und gültige GPU-Höhenmessungen bleiben gesondert offen.

Die neue **CityLab Tunnel (Dry)**-Komponente integriert die native Air Pocket in den Tunnelbaustein. Die bestandenen Tests prüfen auch Größenänderung, Registrierung, Entfernen und transformierte beziehungsweise gespiegelte Ausschlüsse. Der Archive-/PostLoad-Test ist kein Package-Ladetest. Die Laborkarte ist auf die neue Instanz **Tunnel** mit relativer **Z = 600 cm** umgestellt und gespeichert. Nach tatsächlichem Neuladen der Karte und neuem PIE sind die sechs Profilwerte, Extents, Transformation und NoCollision bestätigt; die alte DryTunnel-Box ist entfernt. Ein frischer Spielprozess bestand anschließend nochmals **65/65 Kollisionsproben**, **134/134 Bewegungs-Samples am Boden** und rund **259,44 m** bodengebundene Fahrt. Der Bericht ist für diesen abgegrenzten Umfang **passed_with_limits**. Die frühere Nutzerantwort „Bisher trocken“ bezieht sich auf die vorherige separate Box bei Z = 0. Nach der Migration wurde eine neue native PIE-Aufnahme inspiziert: Der sichtbare Innenraum mit Boden, Wänden und Buggy ist trocken. Dieser eine Frame ersetzt keine Langzeit- oder GPU-Wasserhöhenprüfung.

Die neue Karte **ShaderWorldRoadLab** verwendet eine gemeinsame Terrain-/Mesh-Spline und den normalen Slot **CityLabRoads**. Der [RoadLab-Bericht](evidence/runtime-roads-report.json) ist **passed_with_limits**: Erzeugen/Speichern und Laden in einem anderen Spielprozess bestanden mit **18/18 und 19/19 Checks**. Pro Prozess bestanden 13 Grundterrain-, 23 Straßen-, 13 Rücksetz- und 23 erneute Ladeproben; die Straßenproben unterscheiden native Terrainkollision und SplineMesh-Physik. Größter Fehler: **0,204 cm Terrain**, **0,077 cm Asphalt**, bei 3 cm Toleranz. IDs, Geometrie, Stil, Glättung sowie zwei Actors/16 Meshsegmente stimmten zwischen Prozessen überein.

In beiden Prozessen wurden bei drei gleichen vollständigen Matrix-Fingerprints je Phase **999 → 0 → 999 → 0 Pflanzenursprünge** im 3,5-m-Trassenkern gezählt; **8615** Referenzursprünge in 10–30 m Abstand blieben erhalten. Rücknahme ließ den Bewuchs nachwachsen, Laden räumte die gemessenen Ursprünge wieder frei. Das sind CPU-Instanzdaten, keine GPU-Maskenpixel oder Äste-/Überhangmessungen. Wiederholtes Laden, mehrere abgewiesene Loads und synthetische Format-1-Migration bestanden. Alte echte Spielstände und Cook/Shipping bleiben offen. Die zusätzliche Slate-Bedienprobe bestätigte R/Enter, Backspace, X, Q/E und K/L sowie identische IDs, Splinepunkte/Tangenten und Einstellungen nach normalem PIE-Neustart mit Auto-Load. Die Kamera wurde zwischen Punkten per ActorTools versetzt; WASD, rechte Maustaste, Mausrad und F5/F9 wurden nicht geprüft. Diese PIE-Prüfung ist kein eigener Betriebssystemprozess. Eine unabhängige Format-2-Regression der früheren Bauplatzkarte bestand in zwei frischen Prozessen mit je 26 ursprünglichen und 26 geänderten Terrainproben; sie bestätigt den bestehenden Padpfad nach dem Shader-Gate-Fix.

Zwei frühere RoadLab-Timeouts sind im [Guide](guides/runtime-roads.md) als Diagnose erhalten: `IsTreeFullyBuilt` war kein geeignetes Pflanzen-Fertigsignal; anschließend wartete unser Manager ohne Pad-Instanz unnötig auf einen Pad-Shader. Nach Korrektur des Testgates und dieser eigenen Projektintegration bestand der Zwei-Prozess-Test. Die frühere Baseline ist kein zusätzlicher Persistenznachweis und keine allgemeine ShaderWorld-Fehlerdiagnose.

Der anschließend gemeldete **Bodenfleck durch Asphalt in Kameranähe** wurde nativ reproduziert und auf den aktiven POM-Pfad eingegrenzt: Bei fast senkrechtem Blick entfällt die Tiefenberechnung wegen kleiner Bildschirmparallaxe, während die voreingestellte Anhebung von 6 cm bleibt. Die eigene **MI_RoadLab_Terrain** setzt **POM: Reference Plane = 1,0** und behält **EnablePOM/EnableReliefDepth = true**. Der reversible 30-m-Vergleich reproduzierte den Fleck bei 0,75 und zeigte bei 1,0 geschlossenen Asphalt; zusätzliche korrigierte 3-/100-m-Ansichten blieben geschlossen. Nach tatsächlichem Kartenneuladen und neuem PIE wurden die Actor-Materialzuweisung und drei geladene Straßen bestätigt. Das ist derselbe Editorprozess, kein neuer Standalone-Prozess. Ein zunächst nur gespeicherter Instanzwert erwies sich als unzureichender Nachweis der gespeicherten Kartenzuweisung und wurde vor der abschließenden Rücklese korrigiert. Der [Renderbericht](evidence/road-pom-render-report.json) trennt diese Sichtprüfung von den früheren Kollisions-/Neustarttests. Die anfängliche Legacy-Displacement-Hypothese wurde korrigiert; 1-cm-Overrides behoben den Fleck nicht und sind entfernt. Ein Live-MID-Parentwechsel und ein Materialgraph-Kopierversuch stürzten ab und gelten nicht als bestandene Vergleiche.

## Zusammenhängende CityLoop-Spielschleife

Die neue Karte **ShaderWorldCityLoop** erweitert die getrennten Laborversuche um ein verbundenes Grundstück mit Haus und Bürger. Der [bereinigte Bericht](evidence/cityloop-report.json) bestätigt **drei unterschiedliche gerenderte uncooked Spielprozesse**: Im ersten wurde nach rund **14,29 m** Bürgerfortschritt gespeichert, im zweiten der Zustand exakt wiederhergestellt und die **61 m** lange Straßen-/Zugangsroute bis zum Haus beendet. Im dritten blieb die Ankunft samt Grundstücksidentität und Route erhalten. Die 29 aufgezeichneten Bürgerpositionen hatten Bodenkontakt; die Figur bewegt sich mit Capsule-Sweeps entlang ihrer vorgegebenen Route. Das ist keine allgemeine NavMesh-Wegsuche.

An sechs wiederholt abgefragten Messpunkten lagen ursprünglicher Boden bei **300 cm** und geebnete Grundstücks-, Zugangs- und Straßenterrainhöhe bei **500 cm**, bei **5 cm** Toleranz. Diese Proben isolieren Terrainkollision; die frühere Asphalt-Meshphysik hat einen separaten RoadLab-Nachweis. Im Grundstückskern von 10 m Radius wechselten die gemessenen sichtbaren HISM-Instanzursprünge in jedem Prozess von **252 auf 0**. **2374** Referenzursprünge blieben erhalten; je Zustand lagen drei identische vollständige Matrix-Fingerprints vor. Das bestätigt Ursprungsfreistellung, keine Blatt-/Überhangfreiheit oder GPU-Maskenpixel.

Wiederholtes Laden erzeugte keine zusätzlichen Häuser oder Bürger. Ein ungültiges Grundstück im Testspielstand wurde ohne Verlust der bestehenden Stadt abgewiesen; ein überlappendes neues Grundstück wurde wegen seiner Lage abgelehnt. Die bei dieser CityLoop-Abnahme verwendete eigene Speicherversion **3** enthält Grundstück, Hauszuordnung, Route, Fortschritt und Ankunft. Build und gespeicherte GameMode-/Materialzuweisung nach tatsächlichem Kartenreload sind bestätigt. Die [Anleitung](guides/city-builder-loop.md) grenzt weitere Bedienungs- und Cook-Nachweise ab. Die übrigen vereinbarten Themen bleiben in der [Roadmap](reference/city-builder-roadmap.md). Die inzwischen eingebrachte Nutzeridee für baugetriebene Geländeveränderung ist im folgenden Konzeptabschnitt eingeordnet.

Die zusätzliche native Slate-Bedienprobe bestätigte **R/Enter**, **P** und **L** in der normalen Vorschau. Ohne manuelles K wurden eine zweite Straße und ein zweites Grundstück gespeichert; nach normalem Stop/Play erschienen beide Grundstücke mit gleichen IDs und zwei angekommenen Bürgern wieder. Kamera per ActorTools versetzt; WASD-/Mauseingaben und F5/F9 bleiben offen. Der [CityLoop-Bericht](evidence/cityloop-report.json) trennt diese Bedienprobe vom Drei-Prozess-Kaltstartnachweis.

Die [zusätzliche Regression mit Speicherversion 3](evidence/cityloop-regression-report.json) bestand anschließend in vier weiteren frischen Spielprozessen: RoadLab mit **18/18 und 19/19 Checks**, insgesamt **144/144** Terrain-/Asphalt-Kollisionsproben sowie Freiräumen und Nachwachsen; danach das ältere Pad-/Terrainstraßenlabor mit zwei Bauplätzen, zwei Trassen und je **26 ursprünglichen plus 26 geänderten** Terrainproben pro Prozess. Diese Wiederholung bestätigt die vorhandenen Wege nach der Speichererweiterung; sie ersetzt keine Prüfung eines verpackten Spiels.

## Foundations: tatsächlicher Umfang am 28. Oktober 2026

Der [Foundations-Bericht](evidence/foundations-report.json) bestätigt **Erzeugen/Speichern und Wiederherstellen in zwei unterschiedlichen gerenderten uncooked Spielprozessen**. Die korrigierte Fassung mit nativem LayerMask-Paint und schwarzer Datamap bestand **29/29 Checks in 127,1 s** beim Erzeugen und **12/12 Checks in 70,1 s** beim Wiederherstellen. Alle **306 + 288** aufgezeichneten Terrain-Physikproben trafen die erwarteten Höhen; der größte gemessene Fehler lag bei rund **0,015 cm**. Das sind Messungen in einem kleinen definierten Laborbereich, keine Genauigkeitszusage für beliebige Welten.

Die Planung blieb inert: Erstellen, Überarbeiten, Plan-Undo und Storno änderten weder tatsächliches Gelände noch Bewuchs. Erst die ausdrücklich getrennte **Lab-Debug-Ausführung** erzeugte Höhenänderungen. Anheben, Absenken und Ebnen auf eine absolute Höhe wurden am echten Terrain geprüft; die Ausführungsreihenfolge blieb unabhängig von der ursprünglichen Planreihenfolge. Der damalige Materialtest bestätigte getrennte Einstellungen und unveränderte Physikhöhe. Die spätere Sichtprüfung deckte dennoch nachwachsendes Grün auf einem geräumten Bauplatz auf: Der bisherige Paint-Road-Brush verdrängte die strukturelle NoGrowth-Maske. Der frühere Checkname mit „noBiome“ war als Nachweis zu weit gefasst. Die Korrektur verwendet jetzt eine native LayerMask-Komponente vor dem abschließenden Straßen-/Bauplatzpass. Die neue uncooked Regression bestand: Die letzte erfolgreiche Ausgangsprobe des uncooked Create-Laufs enthielt **436 Vegetationsursprünge einschließlich drei Bäumen im Kern und 29 am Rand**. Nach struktureller NoGrowth-Maske, aktiviertem Paint, echter Regeneration und drei Loads pro Prozess blieben beide Zonen **0/0**; der separate Waldkontrollbaum behielt Darstellung, Kollision und Transformation. Die Fixture-Masken sind eigens erzeugte, nicht gespeicherte Testobjekte und werden pro Prozess neu angelegt. Der Test belegt Maskenerhalt während der echten Loads. Die finale normale PIE-Sichtprobe des Materials ist zusätzlich und getrennt unten dokumentiert.

Ein weiterer Sichtvergleich fand anschließend einen getrennten Materialfehler: Die weiße Datamap wählte im nativen Brush den ungesetzten Flow-Materialkanal statt des gewünschten Bodenmaterials. Registrierung und fertiges Material allein hatten deshalb noch keine sichtbare Schneefarbe bewiesen. Die aktuelle Fassung verwendet eine **schwarze Datamap mit Flow-Anteil 0**; Flow-, Slope- und Biom-IDs bleiben ungesetzt. Die oben genannten aktuellen Prozessläufe prüfen diese Konfiguration ausdrücklich; der anschließend bestandene Spielbildvergleich verwendete die kompilierte Fassung ohne Brush-Parameteränderungen.

Die frühere Rodungsprüfung setzte die CPU-Visual-/Kollisionsmatches **eines identifizierten Baums auf 0**, während die Kontrollmatches erhalten blieben. Nach tatsächlicher ShaderWorld-Instanzregeneration blieben diese CPU-Werte während einer **30-s-Beobachtung** bei 0. Ein bereits aktualisiertes Einzelbaum-Spielbild wurde damit nicht nachgewiesen; der später gemeldete C-Fehler wird unten gesondert behandelt. Der zweite Prozess zeigte zuerst die unveränderte Ausgangswelt und stellte anschließend Gelände und Rodungszustand aus dem Spielstand wieder her. Drei wiederholte Loads pro Prozess erzeugten keine zusätzlichen Datensätze oder Backends. Ein absichtlich unpassender Identitätsspielstand wurde ohne Austausch der vorhandenen Stadt abgewiesen.

**Speicherformat 4** ergänzt noch nicht ausgeführte beziehungsweise stornierte Pläne, ausgeführte Weltänderungen und logische Ressourcen-/Rodungsdaten. Noch nicht ausgeführte und stornierte Datensätze erzeugten beim Laden keine Brushes. Bürger können zusätzlich einen aktiven lokalen Umweg samt Fortschritt und Wiedereintritt in ihre ursprüngliche Route speichern. Dessen Fortsetzung wurde separat auf kontrolliertem Physikboden getestet; der Foundations-Zwei-Prozess-Lauf ist kein allgemeiner Navigationsnachweis. Die älteren Format-2-/Format-3-Berichte bleiben ihre eigenen historischen Abnahmen. [Speicheranleitung](guides/save-and-load.md) und [Foundations-Bedienung](guides/foundations-lab.md) erklären die getrennten Labore.

Die **fünf Biomprofile und 19 eigenen Assets** sind durch gespeicherten Kartenreload und Readback bestätigt. **Acht native Tests unter NullRHI** bestanden: sechs ohne Warnung, zwei mit Warnung. Die eine Warnung betrifft das Aufräumen einer Testwelt ohne World Context, die andere die absichtlich getestete Ablehnung alten ausgeführten Paints. Die Tests prüfen abgegrenzte Codeverträge, darunter das nach außen gerichtete geschlossene Dach, erwartete Kollisionshöhe, begrenzte Umwege, Tunnel-/Vegetationsbausteine und die sichere Backendmigration. Der Migrationstest bestätigt logische Records und unveränderten Livezustand; er ist kein archivierter binärer Spielstandtest. Die [native PIE-Dachaufnahme](assets/images/foundations-roof.png) bestätigt zusätzlich das sichtbare geschlossene orange Satteldach; sie ist keine Langzeitprüfung.

### Zusätzliche Bedien- und Verpackungsnachweise

Die normale PIE-Bedienprobe verwendete echte native Slate-Tasten aus **500300 cm Kamerahöhe**. Neun lokale Terrainproben trafen **Z = 299,995 cm** in vier stabilen Durchläufen. **1/T** erzeugte Plan A ohne Weltänderung oder WorldEdit-Backend; **PageUp** änderte 1 auf 1,5 m, **U** stellte 1 m wieder her. **3/T** erzeugte Plan B mit absolutem Ziel rund **4 m**. **Tab** wählte beide Pläne, **K** speicherte sie. Nach Stop/Start von PIE lud der normale Start dieselbe Plan-B-ID und Zielhöhe. Ein anschließendes Verschieben auf Boden bei 5 m behielt das absolute Ziel 4 m bei. Diese Bedienprobe läuft im selben Editorprozess; die getrennten Betriebssystemprozesse sind ein eigener Nachweis.

Nach abgeschlossenem vollständigem Cook, Stage und Archive bestand die korrigierte **verpackte V2-Fassung in zwei frischen inneren Spielprozessen**: **29/29 Checks in 118,6 s** beim Erzeugen und **12/12 in 66,1 s** beim Wiederherstellen, jeweils **RequiresCookedData = true**. Alle **306 + 279 Terrainproben** bestanden; die Core-/Side-Zonen blieben nach Paint, Regeneration und drei Loads pro Prozess leer, der Waldkontrollbaum erhalten. Der vollständige UAT-Lauf endete nach **96,15 s mit Exit 0**. Das Paket verwendet **Development** und enthält zwei gekochte Karten; die Laufzeitabnahme gilt für **Foundations**, nicht für Shipping oder automatisch für jede mitgekochte Karte. Die älteren RoadLab-, Tunnel- und CityLoop-Berichte behalten ihre damaligen Cook-Grenzen.

### Finale Material-Sichtprobe in normalem PIE

Native **T/F6/K/L**-Eingaben bestätigten das kompilierte Black-Backend ohne zusätzliche Brush-Parameteränderungen: Ein **Snow-Quadrat mit 4 m halber Kantenlänge** erschien auf freiem Küstengelände und blieb nach Speichern und Laden sichtbar. Neun Bodenproben bestätigten die unveränderte Höhe von rund **94,991 cm**. Ein zweites überlappendes Snow-Paint auf dem Bauplatz ließ dessen strukturellen **Sandboden**, die sichtbare Freistellung und **500 cm** Terrainhöhe bestehen. [Ausgangsbild](assets/images/foundations-paint-before.png), [Snow nach Laden](assets/images/foundations-paint-reloaded.png) und [geschützter Bauplatz](assets/images/foundations-protected-pad.png) sind unveränderte native Shot-/FScreenshotRequest-Aufnahmen mit ausgeblendetem HUD. Das sind qualitativ inspizierte Frames aus normalem PIE im selben Editorprozess; dynamisches Wasser und Vegetations-LOD können zwischen Bildern abweichen. Eine automatische Pixelgleichheit, vollständige Biom-Sichtprüfung oder eigene Materialbild-Abnahme im verpackten Spiel wird daraus nicht abgeleitet.

Nach der Probe wurde der ursprüngliche normale Spielstand mit **zwei ungearbeiteten Plänen**, erhaltener absoluter Ebnen-Höhe und **keinen Test-Paintbackends** wiederhergestellt.

### Noch ausstehende Gesamtprüfungen

Für eine spätere automatische Materialdatenprobe ist in ShaderWorld **4.1** ein nativer Weg vorhanden: `ProduceTerrainRegion` kann mit `bLayers = true` einen kleinen Bereich samt benannten RGBA-Layern erzeugen; `AsyncReadPixelsFromRT` kann diese Daten anschließend asynchron zur CPU zurücklesen. **Nur im Quellcode geprüft, noch nicht implementiert oder praktisch abgenommen.** Eine solche Probe würde die tatsächlich erzeugten Layerdaten statt bloßer Brush-Einstellungen prüfen; sie ersetzt weiterhin keinen Vergleich des endgültigen Terrainmaterials im Spielbild. Die API liefert RGBA16F-Rohdaten und benötigt eine passende Puffergröße, Decodierung und Behandlung noch nicht bereiter Daten.[^region-layer-api]

- **Weitere Materialprüfungen:** eigenes verpacktes Spielbild und vollständiger Biomvergleich. Die normale PIE-Farbprüfung ist bestanden; die separate Core-/Side-NoGrowth-Regression ist uncooked und im Development-Paket bestanden. Automatische GPU-Layerpixel sind weiterhin nicht implementiert.
- **Abfragefrische:** Stabile Treffer allein sind keine globale Revisions-Fertigmeldung nach beliebigen Brushes; bei bekanntem Höhenziel prüfen die Abnahmen zusätzlich die tatsächliche erwartete Höhe.
- **Größere Anwendung:** viele dauerhaft gerodete Ressourcen, durchgehende Biom-Sichtprüfung, globale Wegfindung, Multiplayer sowie Maschinenarbeit und Materialbilanz benötigen eigene Versuche.

### Einzelbaum-Korrektur: Backendbild und nachträgliche Nutzerbestätigung

Eine spätere Nutzermeldung zeigte eine Prüflücke: **C meldete eine Rodung, während der Baum im Spielbild stehen blieb.** Der alte Verifier las `SWPerInstanceSMData` beziehungsweise `PerInstanceSMData` und zählte nicht-null skalierte CPU-Transforms. Seine Felder `visible_visual_matches` und `single_tree_visual_and_collision_cleared_control_unchanged` beweisen daher keinen bereits aktualisierten GPU-Instanzpuffer. Auch löste der Test Rodung direkt an einer bekannten Stammposition aus; er prüfte keine Auswahl des gemeinten Baums durch den Mauszeiger.[^tree-fix]

Die alten **29/12-Läufe bleiben historische CPU-/Physik-/Persistenznachweise**; sie werden nicht als sichtbare C-Einzelbaumabnahme umgedeutet. Die separat inspizierten Snow- und freigehaltenen Grundstücksbilder behalten ihren angegebenen Umfang. Die gebaute Korrektur verwendet den nächsten Mausstrahl-Treffer gegen transformierte Baum-Meshboxen mit vorgeschalteter Visibility-Blockergrenze, ohne 8-m-Bodenfallback. Eine gelbe Vorschau wird ungefähr mit 5 Hz erneuert; C pickt frisch. Das ist eine Boxnäherung, keine pixelgenaue Blattwahl.[^tree-fix]

Damals bestanden Editor- und Gamebuild; **12/12 native Tests** liefen erfolgreich, zehn ohne und zwei mit den bekannten Warnungen. Nach erfolgreichem Repackage mit bereits gekochten Assets bestanden erneut zwei frische cooked Prozesse **29/29 Checks in 120,5 s** und **12/12 in 70,8 s**. Diese Läufe bestätigen CPU-/Physik-/Save-/Regenerationsverhalten, keinen Einzelbaum-Pixelzustand im Paket.

Eine getrennte normale PIE-Bildprobe verwendete **native Konsole und Backend-API**, keine tatsächliche C-Taste oder Mauspreview. Der exakt bestimmte erste Ray-Baum wurde orange am Stamm markiert, ein Kontrollnachbar blau. Im Aufblick war die Zielkrone vorher vorhanden und nach Rodung sowie erneutem Backendladen sichtbar entfernt; die Kontrollkrone blieb erhalten. [Vorher](assets/images/tree-clearing-before.png), [nach Backendrodung](assets/images/tree-clearing-after.png) und [nach Backendladen](assets/images/tree-clearing-loaded.png) sind unveränderte native PNGs. `InspectResource` liefert bei nicht gerodeten IDs nur Defaultwerte; die Kontrolle wurde separat über `FindNearestResource`, identische ID/Transformation und Bild geprüft.

**RenderRefreshRequests = 1** in der ersten A/B-Probe zählt eine native `SWUpdateTree`-Anforderung, keinen fertigen GPU-Commit. Die sichtbare Wirkung folgt aus den Bildern. Der Nutzer hat die korrigierte Rodung anschließend ausprobiert und mit **„Awesome, getestet“** bestätigt. Diese Rückmeldung ist von der vorherigen nativen Backendbildprobe getrennt. Gelbe Vorschau, sämtliche Verdeckungs-/Leerklick-/UI-Fokusrandfälle und ein gezielter Bildtest älterer Zustände mit weniger Rodungen sind nicht einzeln bestätigt; der vorherige Harness hatte den nötigen Viewportfokus nicht etabliert. Der normale Nutzerstand mit 13 Rodungen wurde wiederhergestellt, der gespeicherte Spielstand blieb byteidentisch. Computer Use blieb aus. Die bestehende Produktionsgrenze des getrennten Kollisionsnachlaufs bleibt bestehen; die Kosten der nativen 5-Hz-Rayabfrage sind jetzt im getrennten CPU-Benchmark unten gemessen; vollständige Eingabe/Slate-/Vorschauzeichnung sind nicht Teil davon.[^tree-fix]

## Neue Baukamera und Werkzeugleiste

Die [Bedienanleitung](guides/build-controls.md) erklärt die neue kompilierte Kamera und native Slate-Werkzeugleiste. Die **damaligen elf nativen CityLab-Tests** bestanden: neun ohne und zwei mit den bereits oben erklärten Warnungen; die damalige Zwölf-Test-Abnahme steht im Rodungsabschnitt; die spätere Baustellen-/Navigationssuite mit 22 Tests folgt unten. Die aktuelle Kamerakorrektur erweitert diese auf 25 Tests; ihr Nachweis ist separat dokumentiert.[^camera-tree] Dazu gehören jetzt Kameramathematik mit Boden-/Wertebereichsgrenzen, ein isolierter INI-Roundtrip ohne Änderung echter Benutzervorgaben und die Klickisolierung. Diese NullRHI-Tests sind kein gerenderter Mausnachweis.[^build-controls]

Normales gerendertes PIE mit tatsächlichen nativen Slate-Klicks und Tasten bestätigte beide Regler, die Weltkürzelsperre bei Reglerfokus und zweimaliges Bestätigen desselben **ungearbeiteten Plans** ohne neue angewandte Datensätze. Enter bei einem Entwurf mit zwei kontrolliert vorbereiteten Straßenpunkten baute keine Straße; einer der Punkte war eine gezielt ergänzte Propertyfixture. Escape entfernte den Entwurf, ließ die vorhandenen Straßen und die laufende Vorschau bestehen. Ein per Weltklick gewählter Hausstandort erzeugte nur eine gelbe Vorschau; Abbrechen ließ Stadt und Pläne unverändert. Nach Stop/Start von PIE blieben die Testplan-ID und beide persönlichen Kamerawerte erhalten. Die Prüfung läuft im selben Editorprozess; der native INI-Test und die getrennten Paketprozesse sind eigene Nachweise.[^build-controls]

Das [Panelbild](assets/images/build-controls-panel.png) stammt unverändert aus dem final kompilierten normalen PIE. Die Sichtprüfung fand und korrigierte abgeschnittene Beschriftungen. Anschließend wurden ursprünglicher Stadtspielstand byteidentisch und persönliche Faktoren **1×/1×** wiederhergestellt. Computer Use wurde für diese Prüfung nicht aktiviert.[^build-controls]

Nach dem reinen Layoutfix wurden Editor und Game erneut gebaut und das Development-Paket mit bereits gekochten Assets neu gestagt/archiviert (**15 s**, Exit 0; vorheriger vollständiger Cook/Stage/Archive **58 s**, Exit 0). Die damalige verpackte Layoutfassung bestand in zwei frischen Betriebssystemprozessen: **29/29 Checks in 115,8 s** beim Erzeugen, **12/12 in 69,0 s** beim Wiederherstellen, jeweils mit gekochten Daten. Diese kontrollierte Regression vor der neuen Baumkorrektur prüft Gelände, CPU-Rodungszustand, Regeneration und wiederholtes Laden; sie ersetzt weder den Einzelbaum-Rendernachweis noch physische Mausbedienung oder Pixelabnahme der Leiste im Paket.[^build-controls]

**Praktische Grenze:** Der native synthetische Harness trat wegen nicht bestätigter echter Fokus-/Vordergrundvoraussetzungen nicht in den RMB-Capturepfad ein. Das bestätigt weder erfolgreiche relative Maussteuerung noch einen Kamerafehler. Länger gehaltenes physisches WASD/Shift/RMB, echtes Alt-Tab und das persönliche Mausgefühl benötigen noch eine manuelle Spielprobe. Der Code enthält die entsprechenden Fokus-/Freigabepfade; Quellprüfung und Kameramathematik ersetzen diese Probe nicht.[^build-controls]

## Kamera: Ressourcenbaum-Kollision selektiv ausnehmen

Der neue kameraeigene 50-cm-Visibility-Sweep überspringt ausschließlich getroffene ShaderWorld-HISM-Komponenten mit `CityLab.TreeResource`; Actor-Tag allein, fremde HISM, normale Häuser und andere unmarkierte Hindernisse bleiben blockierend. Niemals wird der ganze Terrainactor ignoriert. Maximal 32 Komponentenversuche und echte Nichtbaum-Startpenetration brechen sicher ab. Die nachträgliche Bodenabstandskorrektur wird im Controller nochmals geprüft; das ist ein Codebefund, kein eigener gerenderter Controller-End-to-End-Fall.[^camera-tree]

Finaler Editor-Testbuild (**45,71 s**), Gamebuild (**111,13 s**) und SkipCook-Repackage (**18,77 s/Exit 0**) bestanden. **25/25 native Tests** liefen in **0,460038 s** erfolgreich: **23 ohne, zwei bekannte Warnungen, 0 fehlgeschlagen/nicht ausgeführt/laufend**. Die drei neuen Kamerafälle verwenden echte Query-Physik mit nativen SW-Pools und einfacher Würfel-/Boxgeometrie: Ressourcenbaum durchqueren, tatsächlicher Overlap nach Kollisionspublikation, Fremd-/Nichtbaumschutz sowie begrenzter Abbruch. Der erste Lauf hatte 24 bestandene Tests und einen fehlerhaften Überlappungsaufbau. Die Vorderseiten-Fixturekorrektur und ein zusätzlicher ungefilterter Sweep ließen die strenge Penetrationsprüfung bestehen; der Produktionscode wurde dafür nicht abgeschwächt.[^camera-tree]

Der zusätzliche **normale ConstructionLab-PIE-Start ohne Verifierflag** bestand die Wiederherstellung: alle Baustellenrecord-Felder per vollständigem `export_text`-Vergleich exakt zum gesicherten Stand, ein pausierter Auftrag, **172800000 g Lager und jeweils 0 g Restboden/Puffer/Lkw**. Neun lokale Bodenpunkte passen zum Bauzustand, der Controller meldet drei stabile Durchläufe und keine ausstehende Kollision. Die Kameraposition wurde innerhalb **0,01 cm** wiederhergestellt. Von **17 vorhandenen Spielständen** blieben **16 unbeteiligte byteidentisch**; der normale Construction-Slot wurde beim Start neu geschrieben. Sein vollständiges Modell stimmt exakt, seine Datei wird nicht als bytegleich behauptet.[^camera-tree]

Der Vergleich las die Sicherung über einen getrennten Diagnoseslot. Computer Use und physische Eingaben wurden nicht verwendet. Diese Query-Physik-/Wiederherstellungsprüfungen sind **keine physische WASD-/RMB-/Fokusabnahme oder gerenderte Baumfahrt**; erfolgreiches Repackage beweist keine aktuelle cooked Kamerafahrt. Frühere Toolbar-, Foundations- und Construction-Spielprüfungen bleiben mit ihrem eigenen damaligen Quellstand gültig.

## ConstructionLab: vollständiger cooked Kreislauf mit lokalen Grenzen

Die eigene Karte **`/Game/Maps/ShaderWorldConstructionLab`** verwendet den getrennten Labor-Slot **CityLabConstruction** und schreibt **SaveGame-Format 5**. Der Code unterstützt ältere Formate 1–4 weiter innerhalb der jeweiligen Feature- und Welt-/Generator-/Terrainprofilprüfungen; das ist keine universelle Migration. [Die Anleitung](guides/construction-lab.md) beschreibt vier **400-cm-Zellen**, schrittweisen Aushub, animierte Bagger-/Laster-Grundformen, **18 t Puffer**, **12 t Laster** und **500 t Lager**. Bei angenommenen 1800 kg/m³ gewachsenem Boden entspricht der normale 1,5-m-Plan analytisch **96 m³/172,8 t**. Materialkonten und Transfers verwenden ganze Gramm; Höhenfeld und Modellbilanz werden getrennt geprüft.[^construction-lab][^construction-proof]

Die damalige nach dem Construction-Initialisierungsfix wiederholte native Suite bestand **22/22 Tests in 0,357113 s**, davon **20 ohne und zwei mit bekannten Warnungen**, **0 fehlgeschlagen**. Diese kontrollierten NullRHI-Tests prüfen Logik-/API-Verträge einschließlich Materialbilanz und Serialisierung. Zusätzlich bestand die tatsächlich verpackte Fassung in **zwei frischen cooked Prozessen**: **Create 14/14 Checks in 24,705998 s**, **Resume 15/15 in 113,845061 s**. Pausierte Planung blieb inert; der volle Puffer stoppte den Aushub, ein beladener Laster transportierte Material, und der echte Zwischenstand wurde gespeichert. Der neue Prozess stellte den vollständigen serialisierten Modellhash vor weiterer Simulation identisch wieder her; **drei wiederholte Loads** bewahrten Zustand und Backendanzahl. Anschließend wurden alle vier Zellen fertig ausgehoben und vollständig abtransportiert. Im Lager lagen exakt **172800000 g = 172,8 t**; **Restboden, Puffer und Laster enthielten jeweils 0 g**, der **Modellbilanzfehler betrug 0 g**. Das ausdrücklich beschleunigte Prüfprofil verwendet 6 t Aushub und 12 t Laden/Entladen je Modellschritt; es ist vom normalen Bedienprofil getrennt und keine realistische Maschinenleistung.[^construction-proof]

Der physische Nachweis verwendet **5 cm Höhentoleranz**, **neun tatsächliche Bodenpunkte und drei stabile Durchläufe**, bei **100 cm Kollisionsauflösung und 129 Vertices je Patch**. Für kalten Restore und drei weitere Loads liegen **108 passende Groundhits** vor; für den Abschluss weitere **27**. Beim Modellziel **150 cm** lagen die tatsächlichen Endhöhen zwischen **147,999222 und 148,998444 cm**, der größte gemessene Fehler betrug **2,000778 cm**. Das 5-cm-Gate ist die akzeptierte lokale Toleranz, kein gemessener Maximalfehler und keine allgemeine Genauigkeitszusage. Im nativen Materialausgang wird Höhe je Pass in ganze Zentimeter konvertiert. Exakte Gramm im analytischen Modell sind deshalb **keine unabhängige Massenmessung des quantisierten Meshvolumens**. Die aktuelle Fassung fordert eine abweichende Kollisionsregion alle zwei Sekunden erneut an; die native Abnahme ist je Phase auf 300 Sekunden begrenzt.[^height-quantization][^construction-proof]

**Historischer Fehlversuch:** Der frühere uncooked Erzeugenlauf bestand 14/14 Checks in 76,4 s und sein Zwischenstandrestore samt drei Loads war erfolgreich. Die Fortsetzung mit dem damaligen **2-cm-Gate** blieb jedoch bei Schritt 76 und 96 t Aushub auf ausstehender Kollision stehen und endete nach 180 s im Timeout. Der spätere cooked PASS mit 5-cm-Gate, weiteren Freiraum-/Retrykorrekturen und Diagnosen ersetzt diesen historischen Befund nicht; der gemeinsame Retest isoliert keine einzelne Ursache des alten Stillstands.[^construction-proof]

**Getrennte normale PIE-Probe:** Ohne Verifierflag entstand nach bereitem Boden automatisch ein **pausierter Plan mit 0 g Aushub**, Transport aus; der automatische Save wurde bestätigt. Native Slate-Aktionen bestätigten **Arbeit starten**, **Transport einschalten** und **eine Pause**; die finale Pause wurde zusätzlich über die kompilierte Controller-API ausgeführt. Bei ausgeschaltetem Transport blieben **18 t Puffer und sämtliche Zellhöhen über 57 weitere Arbeitstakte identisch**. Später standen **60 t Aushub = 12 t Puffer + 12 t Lkw + 36 t Lager** in einem pausierten Zwischenstand. Stop/Play stellte alle serialisierten Baustellenfelder identisch wieder her, die lokale Kollision war wieder dreimal stabil passend. Das ist ein PIE-Weltneustart im Editor; der echte Prozessneustart ist der cooked Nachweis oben.[^construction-proof]

**Abgewiesenen Save geschützt:** Ein absichtlich fremdgebundener Construction-Spielstand wurde abgewiesen. Nach **10 s Warmup und weiteren 4 s Wartezeit** blieb seine Datei bytegleich; der gültige gesicherte Stand wurde danach wiederhergestellt und sein vollständiger Auftrag identisch geladen. Der vorherige normale Foundations-Spielstand blieb ebenfalls bytegleich und wurde von der Probe nicht beschrieben. Das bestätigt die abgegrenzten Initialisierungs-/Autosave-Schutzfälle.[^construction-proof]

Vier unveränderte native Aufnahmen sind im Bericht und [in der Anleitung](guides/construction-lab.md) verknüpft: cooked Zwischenstand/Abschluss sowie normaler voller Puffer/pausierter Restore. Sie wurden visuell geprüft; es gibt **keinen automatischen Pixelvergleich**. Die **F5-Injektion bestätigte keinen Callback**. Alle Tastatur-/Fokusvarianten, eine pauschale menschliche Bedienabnahme und eine vollständige korrigierte uncooked Zwei-Prozess-Runde werden deshalb nicht behauptet. Der weitergehende [Architekturentwurf](reference/construction-and-terrain-architecture.md) enthält zusätzliche Produktionsaufträge, Wiederverwendung/Einbau und Untergrundthemen. Der kleine feste Prüfaufbau beweist keine freie Fahrzeugphysik, Maschinenwegfindung oder allgemeine Logistikwirtschaft.

## Gerenderte Navigation nach tatsächlicher Geländeänderung

Ein eigener uncooked Spielprozess bestand **11/11 Checks in 40,9 s**: Ein Bürger lief auf einem realen freien Plateau, eine breite **3 m tiefe** Grube änderte die native ShaderWorld-Kollision, der Bürger wartete unterstützt, nach Entfernen der Änderung erreichte derselbe Bürger das Ende seiner **20-m-Route**. **81 bestätigte Groundhits** decken ursprünglichen Boden, Grube und reparierten Boden mit je drei Durchläufen à neun Punkten ab; größter gemessener Grubenhöhenfehler rund **0,0027 cm**.[^navigation-proof]

Der Nachweis hat eine ausdrückliche Grenze: Der Harness ruft den Bürger kontrolliert selbst auf. Während das echte Managergate aussteht, darf sein Fortschritt nicht wachsen; nach dessen Freigabe hält der Harness weitere **zehn Ticks** bewusst an, bis seine unabhängigen erwarteten Höhenproben stabil sind. Das ist **keine automatische Produktions-Fertigmeldung** für beliebige ShaderWorld-Kollision und keine globale NavMesh-Abnahme. Gerendertes Warten vor der breiten Grube und Fortsetzen sind belegt; schmale-Gruben-Umwege besitzen kontrollierte native Tests, keinen zusätzlichen gerenderten Fall aus diesem Lauf.[^navigation-proof]

## Rodungsbenchmark: tatsächliche CPU-Aufrufzeiten, keine FPS-Zusage

Der [bereinigte Leistungsbericht](evidence/clearing-performance-test.json) bestätigt einen isolierten gerenderten **cooked Windows-Development-Prozess** mit fester Kamera und 200-m-Visitor. Der gestartete native EXE-Hash wurde geprüft; andere Projektbuilds und Rendergames waren vorher geschlossen. Nach **15,4 s** echter Bereitschaft folgten **acht Fenster à rund 8 s** für **0/1/10/100 reale Records**, jeweils Reapply allein und Reapply plus native Rayabfrage mit Zielrate 5 Hz. Insgesamt wurden **255 Reapply- und 153 Rayaufrufe** gemessen; alle Rayaufrufe fanden einen lebenden Baum. Die Prüfung ist bestanden, die nächste Optimierung noch nicht umgesetzt.[^clearing-benchmark]

| Records | Rayabfrage | Reapply ms, Mittel / p95 | Ray ms, Mittel / p95 | Besuchte Reapply-Slots je Aufruf |
| --- | --- | --- | --- | --- |
| 0 | Aus | 0,001 / 0,001 | – | 0 |
| 0 | An | 0,001 / 0,001 | 21,02 / 23,44 | 0 |
| 1 | Aus | 19,85 / 23,44 | – | 154997 |
| 1 | An | 20,44 / 24,30 | 20,43 / 23,90 | 154997 |
| 10 | Aus | 21,33 / 44,43 | – | 154997 |
| 10 | An | 21,47 / 27,84 | 20,84 / 24,65 | 154997 |
| 100 | Aus | 22,06 / 25,81 | – | 154997 |
| 100 | An | 21,72 / 25,48 | 20,99 / 24,44 | 154997 |

**Slots sind hier keine Baumzahl.** Der visuelle Pool hatte **152881 Slots**, aber zu Beginn nur **1410 nicht-null skalierte visuelle Instanzen**. Der Kollisionspool hatte 2116 Slots mit ebenfalls 1410 aktiven nicht-null Transforms. Bei positiven Recordzahlen besuchte Reapply beide vollständigen Pools, insgesamt **154997 Slots**, unabhängig davon, ob 1 oder 100 Records vorhanden waren. Die native Rayabfrage lief auch ohne Records teuer; sie liest laut Code den visuellen Puffer. Ihr tatsächlicher Rhythmus lag bei **4,74–4,85 Hz**, der Reapply-Rhythmus bei etwa 4 Hz. Eine interne Kostenaufteilung auf Kopie, Transformzerlegung, Ledger- und Boxtest fehlt; der Befund rechtfertigt eine gezielte Untersuchung von Live-/Raumindex, Poolfilter und konservativer Broadphase.[^clearing-benchmark]

In jedem Fenster blieben die gerodeten Ziele CPU-visuell und in aktiver Kollision bei **0/0**, der unabhängige Kontrollbaum bei **1/1** und gleichem Transform. Nach dem Versuch verlangte das native Erfolgsgate in drei aufeinanderfolgenden Beobachtungen die Rückkehr aller **101 ausgewählten visuellen Ressourcen** und die erhaltene Kontrolltransformation. Das ist ein visueller **CPU-Restore**, kein neuer GPU-Bildbeleg; die abschließende Kollision jedes zurückgeholten Baums wurde nicht gesondert als Erfolgskriterium protokolliert. Der eigene GameMode nutzt keine normale Stadt-Save-API; das native Flag bestätigt **normal_city_save_accessed = false**. Ein Vergleich der normalen Save-Dateihashes war nicht Teil dieses Fixtures.[^clearing-benchmark]

Gemessen wurde die **synchrone Game-Thread-Warte-/Aufrufzeit** einschließlich Pufferkopie, Locks, Dispatch und möglicher Betriebssystemplanung, keine Hardware-CPU-Zyklen oder GPU-Fertigzeit. Die gerenderten Tickintervalle entstanden mit **t.MaxFPS = 48**; sie sind keine Zusage erreichbarer FPS. Installation per einmaligem Record-Präfix, Bereitschaft, Inhaltsprüfungen und Restore lagen außerhalb der stationären Messfenster. Das ist kein Test von 100 nacheinander gedrückten C-Tasten; in den Messfenstern entstanden keine neuen Renderrefreshrequests. Vollständige Eingabe, Vorschauzeichnung, Bewegung/Streaming und Großweltlast sind ebenfalls nicht abgedeckt.[^clearing-benchmark]

Der frühere Startfehler durch einen Ground-Klassennamefilter lieferte vor Readiness/Messung **keine Werte** und wurde durch die Auswahl genau eines **GenerateCollision=true**-Actors korrigiert. Die jetzt gewonnenen Werte stammen ausschließlich aus dem anschließenden erfolgreichen Lauf. Eine Optimierung ist noch offen: volle Pufferdurchläufe reduzieren, ohne externen Restore, Regeneration, Indexwechsel und den gesonderten Kollisionsnachlauf zu verlieren; danach denselben Versuch wiederholen.

## Nächste Abnahmen für den City Builder

1. Nach bestandenem cooked Baugrubenabschluss und begrenzten normalen Schaltflächen-/Restore-/Autosave-Proben die übrigen Tastatur-/Fokusfälle gezielt prüfen; F5 und vollständige physische Eingaben bleiben offen. Die jetzt gemessenen vollen Rodungspool-Durchläufe gezielt optimieren und denselben isolierten Benchmark wiederholen, ohne Restore-/Kollisionsverträge zu verlieren. Die fünf Foundations-Biomprofile im vollständigen Spielbild vergleichen und Rodungsverwaltung mit großen Beständen messen; Einzelrodung und echte Regeneration sind jetzt im begrenzten Labor geprüft.
2. Manuelle F-/Mausbedienung des Laufmodus, weitere Fahrzeugprofile und speicherbare Tunnel.
3. Auftrieb mit einem definierten Physikobjekt und kontrollierten Wellenbedingungen.
4. Allgemeine Navigation nach Bauflächen-, Straßen- und Gebäudeänderungen; die getesteten lokalen Bürgerumwege ersetzen diese Abnahme nicht.
5. Nach der begrenzten verpackten Foundations-Abnahme weitere Karten und Konfigurationen sowie Leistung bei größerer Karte und vielen Änderungen prüfen.

Neue Versuche ergänzen die jeweilige Anleitung und ihren Beleg. Die Anleitung [Wissen pflegen](maintenance.md) beschreibt diesen Ablauf.

[^region-layer-api]: Separat lizenzierter ShaderWorld-4.1-Code gemäß Quellenbeschreibung; native API am 28. Oktober 2026 gelesen. Noch kein implementierter Layerpixel-Test.

[^build-controls]: Bereinigter [Kamera-/Werkzeugleistenbericht](evidence/build-controls-test.json), UE 5.8.4 und ShaderWorld 4.1, 28. Oktober 2026.

[^tree-fix]: [Bereinigter Rodungsbericht](evidence/tree-clearing-test.json): erfolgreiche Builds/zwölf native Tests, zwei neue cooked Datenprozesse und getrennte normale PIE-Backendbilder. Nachträgliche Nutzerbestätigung der ausprobierten korrigierten Rodung liegt vor; gelbe Vorschau/Fokusdetails und Paket-Pixelprüfung bleiben getrennt offen; CPU-Matches und Refreshanforderungen sind keine GPU-Fertigmeldung.

[^construction-lab]: [Baugrubenanleitung](guides/construction-lab.md); eigenes kleines Labor mit getrenntem Spielstand und expliziten Modellannahmen.
[^construction-proof]: [Bereinigter Baugrubenbericht](evidence/construction-lab-test.json); nach damaligem Construction-Fix native 22/22, cooked 14/14 und 15/15, normale abgegrenzte Schaltflächen-/Puffer-/Restore-/Autosave-Schutzproben und vier visuell geprüfte Originalbilder. Historischer 2-cm-Fehlversuch und offene Tastatur-/Fokusgrenzen sind separat erhalten.
[^navigation-proof]: [Gerenderter Navigationsnachweis mit Harnessgrenze](evidence/terrain-navigation-test.json).
[^height-quantization]: Gelesene native ShaderWorld-4.1-Höhenkodierung gemäß Quellenbeschreibung und im [Baugrubenbericht](evidence/construction-lab-test.json) gemessene Endhöhen; lokales 5-cm-Gate mit drei stabilen Durchläufen.
[^clearing-benchmark]: [Bereinigter CPU-Rodungsbenchmark](evidence/clearing-performance-test.json): acht erfolgreiche isolierte cooked Fenster und CPU-Restore mit klar getrennten Frame-/GPU-/Eingabegrenzen.

[^camera-tree]: [Bereinigter Kamerabaum-Bericht](evidence/camera-tree-test.json): aktuelle 25er-Suite, Build-/Repackageerfolg und historische Fixturekorrektur; normale ConstructionLab-Wiederherstellung separat bestätigt; keine neue physische oder cooked Kamerabedienabnahme.
