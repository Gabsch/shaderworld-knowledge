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
  at: "2026-10-28T03:41:40Z"
sources:
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
| Reference-Biom und Dreckstraße | Live-Ansicht und Actor-/Komponentenprüfung | Eigene Baumzustandsverwaltung offen; begrenzte Straßenmaske inzwischen im RoadLab geprüft |
| Ozean mit Wind und Schaum | [Ozeanbericht](evidence/ocean-report.json), Wind 18 m/s, Schaum aktiv, Rebuild beendet, sichtbare Schaumflächen | Keine Auftriebs-, Dedicated-Server- oder Mehrspielerabnahme |
| CityBasics-Tunnel und Testbuggy | [CityBasics-Bericht](evidence/citybasics-report.json): zwei eigenständige Spielstarts, je 65/65 Kollisionsproben und rund 259,48 m bodengebundene Durchfahrt | Eigene Fahrbahn-/Tunnelmeshes; CharacterMovement, keine Chaos-Fahrzeugphysik; F-/Mausbedienung manuell offen |
| Eigene Tunnelkomponente | [Komponentenbericht](evidence/tunnel-component-report.json): Build und zwei native Automationtests zu Profil/Lebenszyklus und echten WaterSubsystem-Abfragen bestanden | NullRHI mit kontrolliertem Wasserprovider; gespeicherte Karte und neues PIE zusätzlich per Eigenschaften geprüft, zusätzlich frischer Spielprozess mit 65/65 Kollisionsproben und rund 259,44 m Fahrt; neuer Sichtnachweis nur ein inspizierter PIE-Frame |
| RoadLab-Laufzeitstraßen | [RoadLab-Bericht](evidence/runtime-roads-report.json), zwei Prozesse mit je 72/72 Kollisionsproben; zwei Straßen und 16 Meshes identisch wiederhergestellt, Pflanzenursprünge 999 → 0 → 999 → 0 | 3,5-m-Kern und 10–30-m-Referenzbereich; keine Äste-/Überhang- oder GPU-Maskenmessung; R/Enter, Entwurfstasten, Q/E, K/L und PIE-Autoload geprüft; Kamera-/Aliastasten und Cook/Shipping offen |
| RoadLab-POM-Referenzebene | [Renderbericht](evidence/road-pom-render-report.json) und [Anleitung](guides/runtime-roads.md#nahsicht-boden-erscheint-durch-den-asphalt): reversibler 30-m-Bildvergleich, korrigierte 3-/100-m-Ansichten sowie gespeicherte Actor-Zuweisung nach Kartenneuladen/neuem PIE geprüft | Reguläre eigene Materialinstanz, POM/Relief bleiben an; PIE im selben Editorprozess, keine neue Standalone-Kollisions-/Cook-Abnahme |
| CityLoop: Straße, Grundstück, Haus und Bürger | [Spielschleifen-Bericht](evidence/cityloop-report.json): drei getrennte gerenderte Spielprozesse, Fortschritt unterwegs gespeichert und bis zur Haustür fortgesetzt, Ankunft nach weiterem Neustart erhalten; Grundstückskern 252 → 0 Pflanzenursprünge bei 2374 Referenzen | Sechs Terrain-Messpunkte wiederholt geprüft; straßengeführte Route mit Bodenkontakt, keine allgemeine NavMesh-/Cook-Abnahme; R/Enter/P/L, automatisches Speichern und normales PIE-Autoload zusätzlich geprüft; Kamera-/Aliastasten offen |
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

Wiederholtes Laden erzeugte keine zusätzlichen Häuser oder Bürger. Ein ungültiges Grundstück im Testspielstand wurde ohne Verlust der bestehenden Stadt abgewiesen; ein überlappendes neues Grundstück wurde wegen seiner Lage abgelehnt. Die neue eigene Speicherversion **3** enthält Grundstück, Hauszuordnung, Route, Fortschritt und Ankunft. Build und gespeicherte GameMode-/Materialzuweisung nach tatsächlichem Kartenreload sind bestätigt. Die [Anleitung](guides/city-builder-loop.md) grenzt weitere Bedienungs- und Cook-Nachweise ab. Die übrigen vereinbarten Themen bleiben in der [Roadmap](reference/city-builder-roadmap.md), einschließlich des ausdrücklich zurückgestellten allgemeinen Terraformings.

Die zusätzliche native Slate-Bedienprobe bestätigte **R/Enter**, **P** und **L** in der normalen Vorschau. Ohne manuelles K wurden eine zweite Straße und ein zweites Grundstück gespeichert; nach normalem Stop/Play erschienen beide Grundstücke mit gleichen IDs und zwei angekommenen Bürgern wieder. Kamera per ActorTools versetzt; WASD-/Mauseingaben und F5/F9 bleiben offen. Der [CityLoop-Bericht](evidence/cityloop-report.json) trennt diese Bedienprobe vom Drei-Prozess-Kaltstartnachweis.

Die [zusätzliche Regression mit Speicherversion 3](evidence/cityloop-regression-report.json) bestand anschließend in vier weiteren frischen Spielprozessen: RoadLab mit **18/18 und 19/19 Checks**, insgesamt **144/144** Terrain-/Asphalt-Kollisionsproben sowie Freiräumen und Nachwachsen; danach das ältere Pad-/Terrainstraßenlabor mit zwei Bauplätzen, zwei Trassen und je **26 ursprünglichen plus 26 geänderten** Terrainproben pro Prozess. Diese Wiederholung bestätigt die vorhandenen Wege nach der Speichererweiterung; sie ersetzt keine Prüfung eines verpackten Spiels.

## Nächste Abnahmen für den City Builder

1. Weitere Bauflächen-/Biomprofile und Verwaltung einzelner gefällter Bäume; die CityLoop-Abnahme gilt für ihren gemessenen Grundstückskern.
2. Manuelle F-/Mausbedienung des Laufmodus, weitere Fahrzeugprofile und speicherbare Tunnel.
3. Auftrieb mit einem definierten Physikobjekt und kontrollierten Wellenbedingungen.
4. NavMesh nach Bauflächen-, Straßen- und Gebäudeänderungen.
5. Verpackter Build und danach Leistung bei größerer Karte und vielen Änderungen.

Neue Versuche ergänzen die jeweilige Anleitung und ihren Beleg. Die Anleitung [Wissen pflegen](maintenance.md) beschreibt diesen Ablauf.
