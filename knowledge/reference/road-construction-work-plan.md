---
type: Playbook
title: Straßen als gespeicherte Bau- und Transportaufträge
description: Den ersten Straßenwerkzeug-Slice mit Vorschau, stabilem Netz, Maschinenarbeit und endlichen Materiallieferungen abgrenzen.
status: stable
tags: [shaderworld, citylab, roads, construction, logistics, savegame]
engine_version: "5.8.4"
plugin_version: "4.1"
generated:
  by: codex/gpt-6
  at: "2026-10-30T17:19:23+00:00"
evidence_scope: Vereinbarter begrenzter erster Slice umgesetzt; native 99, Editor12/Game7, Cook6, gerendertes Produktionspaar 35/61, normales F5/F9-Kaltstartpaar und separate sichtbare Übergabe bestanden. Zwei Originalbilder visuell geprüft; alte Fassungen/Fehlversuche getrennt. Physische Eingabe, gezielte POM-Nahsicht und Großweltprüfung offen.
sources:
  - id: road-native-evidence
    resource: ../evidence/road-construction-test.json
    title: Finale native 99-/Cook6-/Produktions35/61-/Normal-/Fensterbelege und erhaltene Fehlversuche
  - id: road-construction-guide
    resource: ../guides/road-construction-tools.md
    title: Abgenommene begrenzte Straßenanleitung mit zwei Originalbildern und expliziten späteren Grenzen
  - id: runtime-roads
    resource: ../guides/runtime-roads.md
    title: Vorhandener RCP-SplineMesh-Prototyp mit eigenem historischen Neustartnachweis
  - id: site-replan
    resource: ../guides/replan-building-sites.md
    title: Erhaltene Bodenarbeit und begrenzte Umplanung begonnener Bauplätze
  - id: scaping-plan
    resource: scaping-machine-work-plan.md
    title: Gespeicherte Sollpläne und tatsächliche Ausführung durch Maschinen
  - id: earth-materials
    resource: ../guides/earth-material-evaluation.md
    title: Unterscheidbare Boden-, Kies- und Bauschuttoberflächen mit eigener Importabnahme
  - id: earth-proof
    resource: ../evidence/earth-material-evaluation.json
    title: Bereinigter bestehender Materialnachweis; keine Straßenintegration
  - id: vehicle-assets
    resource: ../guides/vehicle-asset-evaluation.md
    title: Vorhandene Fahrzeugimporte mit getrennten Leistungs- und Herkunftsgrenzen
  - id: vehicle-proof
    resource: ../evidence/vehicle-asset-evaluation.json
    title: Bestehende Mesh-/Clip-Abnahme; keine allgemeine Fahr- oder Arbeitsfreigabe
  - id: city-loop
    resource: ../guides/city-builder-loop.md
    title: Frühere Grundstücks-, Haus- und Bürgerverbindung als getrennter Prototyp
  - id: save-binding
    resource: ../guides/stable-save-binding.md
    title: Strenge Profilbindung, erhaltene Altstände und ausdrückliche bekannte Übernahmen
  - id: local-inventory
    resource: "Lesendes Projektinventar vom 30. Oktober 2026: Content/ShaderWorldRoadLab, Content/EarthMaterialEvaluation, Content/VehicleEvaluation und die WheelLoader-Referenz in Source/UnrealMcpTest/CityLabEarthworks.cpp. Lizenzierte Unreal-Assets und Projektquellen sind nicht im öffentlichen Bundle enthalten."
    title: Tatsächlich vorhandene lokale Pakete und begrenzte Quellreferenz
---

# Straßen als gespeicherte Bau- und Transportaufträge

**Aktuelle Abgrenzung, 30. Oktober 2026:** Die volle Fahrzeugflotte mit einem tatsächlichen Depot, Disposition und allgemeiner fahrzeugabhängiger Wegsuche ist weiter ein **vereinbartes offenes Ziel**. Der PoC belegt begrenzte Start-/Lagerrouten und Materialübergaben, nicht bereits diesen gesamten Depotbetrieb. Historische Prüfbezeichnungen wie „Depotfahrt“ dürfen damit nicht gleichgesetzt werden. Der Nutzer vertagt die gemeldete Schwierigkeit, während eines Baus eine zweite Straße anzulegen; derzeit folgt die [RCP-Funktionsbesprechung und Integrationsplanung](road-creator-pro-runtime-plan.md), keine weitere Umsetzung. Die darunterstehenden 4.1-/RoadConstruction6-Nachweise behalten ihren damaligen Umfang; der aktuelle 4.2-Schnellstart steht in der [Straßenanleitung](../guides/road-construction-tools.md).

**Dieser erste Straßen-Slice ist umgesetzt und für den begrenzten RoadConstruction6-Ablauf abgenommen.** Straße zeichnen, Entwurf korrigieren, bestätigen, Material abholen und abschnittsweise bauen lassen; anschließend Hauszufahrt und Grundstück aus denselben gespeicherten Netz-/Arbeitszuständen. Diese Seite bewahrt den vereinbarten Vertrag und trennt die tatsächliche Abnahme von späterem Ausbau. Der vorhandene [RoadLab-Prototyp](../guides/runtime-roads.md) behält seinen eigenen engeren Prüfstand.[^runtime-roads]

Die [Straßenanleitung](../guides/road-construction-tools.md) erklärt Gerade/Kurve, Griffe, Bestätigen und Karte → **J → Leertaste → H**, eigene Karte/Slot, endliche Anfangsbestände und strenge passende Buildfassung. Bestätigte ungearbeitete Aufträge werden gespeichert; offene Maus-/Griffgesten bleiben transient. Die begrenzte Formbearbeitung ändert nur Griffe unbegonnener ungeteilter Straßen bei festen Endanschlüssen und gleichen Auftrags-/Abschnittskennungen. T-geteilte/begonnene Trassen sind geschützt. Produktions-Controllerpfade sind praktisch geprüft, physische Mausereignisse nicht behauptet.

Voraussetzung ist das eigene UnrealMcpTest mit Unreal **5.8.4**, ShaderWorld **4.1**, vorhandenem RCP-Mesh und Maschinen-/Speichergrundlage. Ein neues Assetpaket war für diesen PoC nicht erforderlich. Die finalen Nachweise stehen im [bereinigten Bericht](../evidence/road-construction-test.json); vorgeschlagene spätere Funktionen werden daraus nicht mit abgenommen.

## Was der erste Slice umfasst

| Bereich | Vereinbarter Umfang |
| --- | --- |
| Straßentyp | Bodennahe Straße mit zwei Fahrspuren und **8 m Breite**; Gelände folgt einem geplanten Höhenprofil. |
| Zeichnen | Gerade und kubische Kurve mit durchgehender Vorschau; Kontrollpunkte und ungearbeitete Entwürfe verschieben, bestätigen oder verwerfen. |
| Anschlüsse | An vorhandene Endpunkte einrasten; ein T-Anschluss erzeugt einen echten Netzknoten auf dem betroffenen Abschnitt. |
| Netz | Dauerhafte Knoten-, Kanten-, Anschluss- und Auftragskennungen; sichtbare Meshstücke werden aus diesem Zustand aufgebaut. |
| Häuser | Hauszufahrt an das Straßennetz anbinden; zugehörigen Bauplatz als Maschinenauftrag vorbereiten. |
| Arbeit | Rodung, Abtrag, Auffüllung, Kies und Asphalt als gespeicherte, abhängige Phasen. |
| Logistik | Begrenzte Start-/Lagerrouten, tatsächliche Lagerabholung, begrenzte Lkw-Ladung und Baustellenpuffer; getrennte Materialarten **Soil**, **Gravel**, **Asphalt**. Vollständiger Depotbetrieb bleibt offen. |
| Wiederaufnahme | Entwurf, Netz, geleisteter Boden, Phasenfortschritt, Bestand, Reservierungen und beladene Fahrten nach kaltem Neustart erhalten. |

Brücken, Tunnel, freie Offroad-Wege, allgemeine Fahrspur-KI und Umbau bereits arbeitender oder fertiger Straßen folgen später. Verschiebbare Entwürfe erlauben in diesem Slice kein nachträgliches Verschieben ausgeführter Erde oder fertiger Straßen. Die vorhandene begrenzte [Bauplatz-Umplanung](../guides/replan-building-sites.md) behält ihren eigenen Vertrag.[^site-replan]

## So soll der Werkzeugablauf aussehen

1. **Straße wählen.** Endpunkt oder befahrbaren Netzanschluss anklicken. Die Vorschau unterscheidet Gerade und Kurve; Länge, Höhenprofil und betroffene Baufläche bleiben erkennbar.
2. **Entwurf formen.** End- und Kurvenpunkte verschieben. Ein sichtbarer Fangpunkt zeigt Endpunkt oder T-Anschluss; ein nur optisches Kreuzen verbindet keine Straßen.
3. **Bau prüfen.** Vorschau zeigt Rodungsfläche, Abtrag, Auffüllung, Kies-/Asphaltbedarf und den tatsächlich erreichbaren Bauanfang. Zu enger Bogen, unzulässige Steigung, überlappende Anschlüsse, Wasser-/Tunnelbedarf oder geschützte Gebäude blockieren mit verständlichem Grund. Konkrete Grenzwerte werden als Bauprofil festgelegt und im Werkzeug angezeigt, nicht aus dem Meshnamen abgeleitet.
4. **Bestätigen.** Ein gespeicherter Auftrag entsteht; Planung und Bestätigung allein verändern weder Boden noch Bäume oder physische Materialkonten. Arbeit und Transport starten ausdrücklich.
5. **Am erreichbaren Anfang bauen.** Maschinen arbeiten von der vorhandenen Netzfront aus vor. Lieferungen verwenden nur tatsächlich freigegebene Zufahrten; ein entfernter Entwurf ist noch keine Straße.
6. **Haus anbinden.** Hauszufahrt und Bauplatzvorschau zeigen ihren Netzanschluss. Das Haus wird erst nach ausgeführter Rodung/Erdarbeit, passender lokaler Kollision und gebauter Zufahrt freigegeben. Ein nahes Straßenmesh allein genügt nicht.

Das ist ein Bedienentwurf ohne fest zugesagte neue Tastenbelegung. Er baut auf der Trennung zwischen inertem Plan und Maschinenwirkung im [Scaping-Arbeitsplan](scaping-machine-work-plan.md) auf.[^scaping-plan]

## Netz und Bauzustand sind verschiedene Dinge

Das geplante Netz beschreibt, **was verbunden werden soll**. Das befahrbare Netz beschreibt, **was jetzt tatsächlich erreichbar ist**. Eine Kante besitzt daher mindestens ihre stabile Identität, Kurvenbeschreibung, Anschlüsse und abschnittsweisen Bauzustand. Hauszufahrten beziehen sich auf echte Anschlüsse statt auf die zufällig nächstgelegene sichtbare Meshkante.

Ein T-Anschluss teilt die betroffene Netzkante logisch und erhält eine nachvollziehbare Zuordnung zu ihren bisherigen Abschnitten. Bereits ausgeführte Arbeit, Materialquittungen und aktive Routen dürfen dadurch nicht neu entstehen, verschwinden oder versehentlich ein zweites Mal abgerechnet werden. Unzulässige Änderungen werden vor der Übernahme vollständig abgewiesen. Freie Kreuzungen mit vier Armen und Straßenumbau sind kein versteckter Teil dieses ersten Anschlussumfangs.

Meshsegmente und ShaderWorld-Brushes sind Darstellungen beziehungsweise Ausführungswerkzeuge. **Der gespeicherte Graph und die Arbeitsquittungen sind die gemeinsame Grundlage** für Oberfläche, Gelände, Pflanzenfilter, Zufahrten und Transport. Der vorhandene RoadLab verwendet bereits eine gemeinsame Trasse für Gelände und RCP-SplineMeshes; daraus folgt noch keine allgemeine Netz- oder Baustellenlogik.[^runtime-roads]

## Erst roden und Erde bewegen, dann Oberfläche liefern

| Phase | Tatsächliche Wirkung | Voraussetzung für den nächsten Schritt |
| --- | --- | --- |
| Rodung | Gespeicherte Ressourcen im realen Arbeitskorridor entfernen; Kontrollbestand außerhalb erhalten. | Erforderliche Fläche tatsächlich frei; keine bloße Vorschaumaske als Rodung abrechnen. |
| Abtrag | Ausgangsboden schrittweise bis zum geplanten Profil senken und **Soil** in den begrenzten Abtragspuffer buchen. | Freier Puffer und erreichbare Abfuhr; bei vollem Puffer wartet die Arbeit. |
| Auffüllung | Tatsächlich gelieferten **Soil** verbrauchen und Gelände schrittweise anheben. | Passendes Material im Einbaupuffer, kein geplanter oder nur reservierter Aushub als Bestand. |
| Kies | Deklarierte Kieslage aus **Gravel** abschnittsweise einbauen und sichtbar machen. | Tragfähiger freigegebener Boden, reale Lieferung und bestätigte lokale Kollision. |
| Asphalt | Deklarierte Decklage aus **Asphalt** liefern und abschnittsweise fertigstellen. | Tatsächlich fertige Kiesunterlage und sichere Baustellen-/Rückfahrt. |

Fläche, Schichtdicke und Modell-Dichte bestimmen die Modellmengen; Buchung in Gramm. Aktuelles Laborprofil: 8 m Fahrbahnbreite, Kies20 cm/1.800 kg pro m³, Asphalt10 cm/2.300 kg pro m³, Erde1.600 kg pro m³; Lkw12 t und gemeinsamer Puffer18 t. 100/400/200 t endlicher deklarierter Anfangsbestand. Diese erste Kies-/Asphaltlage ist ein Bau-/Mengenmodell, keine nachgewiesene Körnerphysik, Verdichtung oder Baustoffproduktion.

Die ausgeführte Bodengeschichte bleibt erhalten: Ein neuer Abschnitt nimmt den tatsächlichen Boden als Ausgang, überschreibt keine bereits quittierte Erdarbeit und zählt überlappende Bauflächen nicht doppelt. Bereits gelöste Erhaltungsvorschriften der Bauplatz-Umplanung dienen als Grundlage; ihre früheren Tests ersetzen keine neue Straßenabnahme.[^site-replan]

## Depot, Lager und erreichbare Baufront

**Vereinbarte Zielregel, noch kein vollständiger Depotnachweis: Fahrzeuge beginnen im Depot mit gespeicherter Identität und leerer Ladung.** Benötigtes Material wird am tatsächlichen Lager abgeholt. Die erste Laborwelt erhält ausdrücklich deklarierte **endliche** Anfangsbestände und eine vorhandene, freigegebene Verbindung zwischen Depot und Lager. Weder ein spontaner voller Lkw noch ein unendliches Lager löst die Anfahrtsfrage.

Normale Straßen-Lkw fahren nur über fertiggestellte Straßen oder ausdrücklich als vorbereitet und befahrbar freigegebene Kiesabschnitte. Eine gezeichnete Linie, nur gerodeter Korridor oder blanke Planie ist keine solche Route. Sie fahren nicht automatisch über die Wiese zum nächsten Auftrag. Fehlt eine Verbindung, wartet der Auftrag mit angezeigtem Grund.

Damit eine Straße trotzdem wachsen kann, wird **von der erreichbaren Netzfront aus** gearbeitet und geliefert: Abtrag/Auffüllung/Kies bauen den nächsten begrenzten Arbeitsabschnitt; erst dessen reale Freigabe erweitert die Transportreichweite. Maschinenbewegung innerhalb des festgelegten lokalen Arbeitsbereichs ist gesondert zu prüfen und darf keine allgemeine Lkw-Offroad-Suche eröffnen. Eine kurze Zufahrt muss genauso gebaut und freigegeben sein wie eine lange.

Asphaltarbeit darf kein Fahrzeug auf einem inzwischen gesperrten Abschnitt einschließen. Vor Phasenwechsel und Graphänderung werden belegte Abschnitte sowie sichere Rückwege berücksichtigt; bei nicht erfüllbarem Ablauf wartet der nächste Schritt. Im PoC genügen nachvollziehbare gespeicherte Routen und Abschnittsbelegung. Freie Lenkphysik, Überholen, Kreuzungsampeln und vollständige Fahrspur-KI bleiben spätere Aufgaben.

## Drei Materialkonten und begrenzte Übergaben

| Materialkennung | Buchung im ersten Slice | Vorhandene passende Optik |
| --- | --- | --- |
| **Soil** | Tatsächlicher Erdabtrag, Lagerung und Wiedereinbau; vereinfachte gemeinsame Bodenart. | Ground Rubble als ausdrücklich gemischter, schutthaltiger Laborboden. |
| **Gravel** | Endlicher eigener Lagerbestand, Transport und Einbau der Kieslage. | Construction Gravel. |
| **Asphalt** | Endlicher eigener Lagerbestand, Transport und Einbau der Asphaltlage. | Vorhandene RCP-Straßenoberfläche; kein neues Oberflächenset erforderlich. |

**Construction Rubble ist Bauschutt und keine Asphaltquelle.** Auch Ground Rubble wird durch sein Aussehen weder zu reinem Mutterboden noch zu Gravel. Material-ID, sichtbares Material und physischer Bestand bleiben getrennt. Ein Typwechsel oder eine Herstellung aus Schutt wäre ein eigener Produktionsauftrag mit eigenen Rezepten und Verlusten.[^earth-materials]

Pro Typ muss jederzeit gelten: deklarierter Anfangsbestand plus tatsächlicher Zugang entspricht Lagerbestand plus Ladung plus Baustellenpuffern plus eingebauter beziehungsweise ausdrücklich abgeführter Menge. Reservierungen sind Verfügbarkeitsbindungen, keine zusätzliche physische Masse. Abholen verschiebt Bestand vom Lager in den Lkw, Abladen vom Lkw in einen freien passenden Puffer. Eine volle oder falsche Materialaufnahme wartet; dieselbe Übergabe darf nach Laden nicht erneut buchen. Die Lagerkapazität und die maximale Ladung beziehungsweise Pufferkapazität bleiben endlich.

Aushub fährt bei Platzmangel nicht unsichtbar weg. Freier Lagerraum, passende Fahrt und begrenzte Aufnahme sind erforderlich; andernfalls steht Abtrag still. Im PoC gibt es keine automatische Umwandlung zwischen Soil, Gravel und Asphalt und keinen kostenlosen Ersatzbestand bei Neustart.

## Vorhandene Assets und ihr genauer Zweck

Die folgenden **projektlokalen Pakete waren beim lesenden Inventar vorhanden**. Das öffentliche OKF liefert die Dateien nicht mit. Vorhandensein und frühere Assetabnahme belegen nicht ihre neue Straßenintegration.[^local-inventory]

| Aufgabe | Vorhandener Unreal-Paketpfad | Verwendung und Grenze |
| --- | --- | --- |
| Zweispuriger Asphalt | `/Game/ShaderWorldRoadLab/Meshes/SM_CityLab_RCP_TwoLane` | RCP-Kopie für Laufzeit-SplineMeshes; historische Anleitung verlangt CPU-Zugriff, passt etwa 9 m Quellbreite auf 8 m an. Editor-Construction-Script ist nicht der Spielbuilder. |
| Straßen-Terrainansicht | `/Game/ShaderWorldRoadLab/Materials/MI_RoadLab_Terrain` | Historisch geprüfte eigene POM-Referenzebene 1,0. Zuweisung auf der neuen Karte und Nahsicht erneut prüfen. |
| Gemischter Aushub | `/Game/EarthMaterialEvaluation/Materials/MI_GroundRubble` | Schutthaltiger Boden, keine allgemeine Bodenklassifikation. |
| Kies | `/Game/EarthMaterialEvaluation/Materials/MI_ConstructionGravel` | Heller Kies; Farbe/Belichtung in der Spielszene abstimmen. |
| Bauschutt | `/Game/EarthMaterialEvaluation/Materials/MI_ConstructionRubble` | Getrennter Bruch, kein Soil-/Gravel-/Asphalt-Rezept. |
| Haufen und Füllungen | `/Game/EarthMaterialEvaluation/Meshes/SM_pile_low`, `SM_pile_mid`, `SM_pile_high`, `SM_fill_low`, `SM_fill_mid`, `SM_fill_high` | Statische Vergleichsformen; Mengenanpassung und reale Fahrzeugfüllung sind kein vorhandener Automatismus. |
| Radlader | `/Game/VehicleEvaluation/WheelLoader/Meshes/SK_WheelLoader` und `SK_WheelLoader_Anim` | Bereits im Earthworks-Code referenziert; Demo-Rig/Clip ersetzen keine allgemeine Navigation oder Ladesimulation. |
| Bagger | `/Game/VehicleEvaluation/Liebherr956/Meshes/SK_Liebherr956` und `SK_Liebherr956_Anim` | Vorhandener Nahsicht-Technikimport; sehr hohe Geometrielast, nur LOD0. |
| Kipperversuch | `/Game/VehicleEvaluation/ElectroNick/Meshes/SK_ElectroNick` und `SK_ElectroNick_Anim` | Herkunft ungeklärt, Texturen unvollständig: lokaler Technikversuch, keine Produktions- oder öffentliche Weitergabefreigabe. |

Die importierten Fahrzeugclips wurden lokal als Demonstrationen erzeugt. Das frühere Assetlabor belegt Maße, gespeicherten Import, Posen und SIE-Ticken; es erzeugt keine Chaos-Fahrzeuge, Schaufelphysik oder beliebige Arbeitsbewegungen. Für den ersten Kreislauf reichen die bestehenden eigenen Laufzeitfahrzeuge beziehungsweise Platzhalter; Fahrzeugoptik kann getrennt zugeordnet werden, ohne Materialkonten oder Routenlogik an ein bestimmtes Modell zu binden.[^vehicle-assets][^vehicle-proof]

Die drei Erdmaterialien wurden unter Fab Standard License erworben, nicht CC0. Ihre frühere Materialprüfung umfasst 2K-Oberflächen und statische Laborformen; Displacement ist dort Referenz und nicht als geometrische Haufenverformung angeschlossen. Lizenzierte Rohtexturen, Modelle und Unreal-Pakete bleiben außerhalb des öffentlichen Doku-Repositories.[^earth-proof]

## Speichern und Wiederaufnehmen gehört zum ersten Ablauf

Der neue Straßenstand muss mindestens **bestätigte ungearbeitete Trassen und ihre Kurvenpunkte**, stabile Graphkennungen, T-Aufteilungen, Hauszufahrten und Bauplatzverknüpfungen, unveränderliche Bodenreferenzen/ausgeführte Abschnitte, Rodungszustand, Phasenquittungen, typisierte Grammkonten, Reservierungen, Fahrzeugzustand und Routenfortschritt enthalten. Material in einem fahrenden Lkw bleibt dieselbe konkrete Ladung; beim Wiederaufbau der Darstellung wird keine zweite erzeugt. Eine noch unbestätigte Mausgeste mit laufender Griffbearbeitung ist ausdrücklich transient und wird nicht gespeichert; sie muss vor dem Neustart bestätigt oder anschließend neu gezeichnet werden.

Ein kalter Start stellt zunächst den gespeicherten physischen Zustand und die zugehörige Darstellung her. Arbeit/Transport und ein eventuell blockierter Auftrag behalten ihre gespeicherten Schalter beziehungsweise Gründe. Automatischer Auftragsabschluss, Nachfüllen oder Neubeginn durch den Start ist unzulässig. Alte normale Slots und passende Archive bleiben erhalten; neue Datensätze brauchen einen eigenen geprüften Versions-/Profilvertrag statt stiller Lockerung der [bestehenden Savebindung](../guides/stable-save-binding.md).[^save-binding]

## Bestandene Abnahme und spätere Ausbaustufen

Die [finale native 99-Suite](../evidence/road-construction-test.json) besteht mit 97 sauberen Tests/zwei bekannten Warnungen, 20 neuen sauberen Straßentests / 114,922 s / Exit 0. Editor12/Game7 und Cook6 bestehen (58,97/73,27/81,55 s). Eigene Kartenübernahme mit rekursiv gleichem Zustand/Readback und unveränderten 1.066 geschützten Dateien/329 Saves/altem Profil, Manifest 411, ebenfalls bestanden. **Gerendertes Produktionspaar 35/61** umfasst kalte beladene Erdfahrt, drei normale Loads, echte Baufront/Boden-/Kies-/Asphaltarbeit, Hauszufahrt/Pad/Haus bis zur exakten 0-g-Endbilanz für alle drei Materialien. Normales zusätzliches F5/F9-Paar mit 4+2 vollständigen ExportText-Aufnahmen in zwei kalten Prozessen und separate sichtbare Übergabe bestehen. Zwei Originalbilder visuell geprüft. Alle acht Fehl-/Stoppversuche und früheren Fassungen bleiben erhalten.

Der vereinbarte Ablauf ist auf folgenden Ebenen geprüft; die Ebenen bleiben ausdrücklich getrennt:

- Native Modelle: Netz/Fangpunkte und atomare Ablehnung, endliche getypte Lager-/Puffer-/Transportkonten, Terrainabschnitte und begrenzte Bereitschaft. Leere/falsche Vorräte und Puffergrenzen sind Modellfälle, keine behauptete umfassende Störungsserie im gerenderten Großnetz.
- Gerenderte Produktions-Controller-APIs: inerte volle Vorschauen, T-/Kurven-/gespeicherte Griff- und Knotenänderungen, stabile Identität, Stornierung, nicht erreichbarer Start abgewiesen; echte Depotfahrt, schrittweise Rodung, Boden/Kies/Asphalt und Erweiterung nur ab vorbereiteter Netzfront.
- Gespeicherte beladene Innenfahrt: kalter zweiter Prozess und drei normale Loads erhalten alle vollständigen Gruppen; Fortsetzung beendet Straße, getrennte Hauszufahrt/Pad und genau ein Haus. Lokale Kollision in 39 akzeptierten Batches/382.173 wiederholten 50-cm-Proben bei 5-cm-Gate, maximal 2,431767 cm. Keine globale GPU-/Volumenmassenmessung.
- Normaler Modus: vier plus zwei vollständige ExportText-Snapshots über F5/F9-Funktionen und getrennten kalten Prozess, fünf Gruppen/übrige Metadaten exakt, Kamera 1e-8. Alte Saves/Paket unverändert.
- Grenzen: physische Maus-/Tasteneingaben und menschliche Spielprüfung, gezielte POM-/Kurven-/T-Naht-Nahsicht, gesonderte kalte Kies-/Asphaltladungscheckpoints sowie Großweltleistung bleiben offen. Die beiden qualitativen Bilder ersetzen diese Prüfungen nicht.

Danach folgen Straßenumbau unter erhaltener ausgeführter Arbeit, weitere Kreuzungen/Straßentypen, Fahrspur-KI/Verkehr und größere Netze. **Brücken, Tunnel und allgemeine Offroad-Wege** bleiben eigenständige spätere Slices. Untergrundansicht und echter Tunnelvortrieb behalten ihre bisherigen getrennten Grenzen. Der übergreifende [Fahrplan](city-builder-roadmap.md) führt die übrigen Themen weiter.

[^runtime-roads]: [Vorhandener Laufzeitstraßen-Prototyp](../guides/runtime-roads.md), eigener historischer Prüfstand.
[^site-replan]: [Begrenzte Bauplatz-Umplanung mit erhaltener Arbeit](../guides/replan-building-sites.md).
[^scaping-plan]: [Scaping als Maschinenaufträge](scaping-machine-work-plan.md).
[^earth-materials]: [Drei Erdmaterialfamilien und ihre Einsatzgrenzen](../guides/earth-material-evaluation.md).
[^earth-proof]: [Bestehender Materialprüfbericht](../evidence/earth-material-evaluation.json).
[^vehicle-assets]: [Vorhandene Fahrzeugimporte und ihre Grenzen](../guides/vehicle-asset-evaluation.md).
[^vehicle-proof]: [Bestehender Fahrzeugprüfbericht](../evidence/vehicle-asset-evaluation.json).
[^local-inventory]: Lesendes projektlokales Datei- und Quellreferenzinventar gemäß Quellenbeschreibung; keine neue Engine- oder Laufzeitprüfung.
[^save-binding]: [Strenge Savebindung und ausdrückliche bekannte Übernahmen](../guides/stable-save-binding.md).
