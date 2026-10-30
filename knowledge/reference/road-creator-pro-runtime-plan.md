---
type: Plan
title: Road Creator Pro fast vollständig zur Spielzeit nutzen
description: Recherche und Vorschlag für RCP-Straßen, Ausstattung und Bauwerke mit CityLab-Aufträgen, ShaderWorld und dauerhaften Spielständen.
status: draft
tags: [citylab, road-creator-pro, roads, construction, runtime, planning]
engine_version: "5.8.4"
plugin_version: "4.2"
rcp_local_version: unbekannt
generated:
  by: codex/gpt-6
  at: "2026-10-30T17:21:47.484583+00:00"
evidence_scope:
  manual: Das Agententeam hat das vollständige offizielle 90-seitige RCP-Handbuch einschließlich relevanter Abbildungen und Roadmap gelesen; Herstellerfähigkeiten sind keine Laufzeitabnahme.
  local: Getrennte lesende Bestandszählung im vorhandenen Projekt; keine gesicherte RCP-Versionsnummer und kein Nachweis eines vollständigen aktuellen Imports.
  runtime: Reiner Entwurf. Kein neuer Spawn-, Materialwechsel-, Komponentenlebenszyklus-, Leistungs- oder Neustarttest für die hier geplante breite RCP-Integration.
sources:
  - id: rcp-manual
    resource: https://drive.google.com/file/d/1NYQA6k-qZHusso1npgAfEgGpnieeDRxt/view
    title: Offizielles Road-Creator-Pro-Handbuch, 90 Seiten, über den Dokumentationslink der Fab-Produktseite abgerufen am 30. Oktober 2026
  - id: rcp-fab
    resource: https://www.fab.com/listings/adc4696d-7ab7-4d79-9194-fd29fdc0edfa
    title: Road Creator Pro von lyoshko, Produktbeschreibung und Aktualisierungsliste
  - id: rcp-author
    resource: https://forums.unrealengine.com/t/lyoshko-road-creator-pro/2418882
    title: Offizieller Produktthread mit Autorenantworten zu Kreuzungen, Verkehr und Bearbeitungskosten
  - id: local-inventory
    resource: "Lesende projektlokale Bestandsaufnahme vom 30. Oktober 2026: 673 RCP-Inhaltspakete, davon 671 uasset und zwei umap. Gruppen: 49 Blueprints, 251 Meshes, 188 Materialien, 162 Texturen, 18 Demopakete und fünf Soundpakete. Ein Haupt-RoadCreator-Blueprint; Content-Assetpack, kein eigenes RCP-Plugin. Inventar, lizenzierte Assets und Blueprintquellen werden nicht öffentlich mitgeliefert. Versionsstand unbekannt; fehlende neuere Namen sind kein gesicherter Release-Zeitstempel."
    title: Lokaler RCP-Bestand, getrennt vom aktuellen Herstellerhandbuch
  - id: ue-construction
    resource: https://dev.epicgames.com/documentation/en-us/unreal-engine/construction-script-in-unreal-engine
    title: Epic UE5.8 Construction Script
  - id: ue-lifecycle
    resource: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-actor-lifecycle
    title: Epic UE5.8 Actor Lifecycle mit Spawn-, Construction- und Deferred-Spawn-Pfad
  - id: ue-materials
    resource: https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine
    title: Epic UE5.8 dynamische Materialinstanzen und nur zur Kompilierzeit wählbare statische Parameter
  - id: ue-save
    resource: https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine
    title: Epic UE5.8 SaveGame und Wiederherstellung eigener Spieldaten
  - id: sw-brush
    resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass
    title: Offizielle ShaderWorld-Brush-Dokumentation mit Terrain-, Kollisions- und Bewuchsaktualisierung
  - id: road-plan
    resource: road-construction-work-plan.md
    title: Bisheriger Straßen-Slice mit Bauphasen, endlichen Materialien und erreichbarer Baufront
  - id: current-road
    resource: ../guides/road-construction-tools.md
    title: Begrenzter bereits geprüfter Straßenprototyp; keine Abnahme dieser breiten Integration
  - id: machine-plan
    resource: scaping-machine-work-plan.md
    title: Sollpläne und tatsächliche Maschinenarbeit für ShaderWorld
---
# Road Creator Pro fast vollständig zur Spielzeit nutzen

**Ziel ist ein umfangreiches Straßenwerkzeug im Spiel:** RCP-Straßentypen, Kurven, Gehwege, Markierungen, Ausstattung, Kreuzungen, Brücken und Tunnel sollen sich planen, bauen und dauerhaft weiterverwenden lassen. Die Bedienung folgt unserem City Builder; den Editor-3D-Gizmo wollen wir nicht nachbauen. Diese Seite hält den Vorschlag zur Besprechung fest. Sie startet keine Implementierung.

**CityLab bleibt die maßgebliche Datenquelle.** RCP liefert Assets und geeignete geprüfte Funktionen für die Darstellung. ShaderWorld erzeugt Gelände, Bewuchs und Bodenkollision. Unsere Spielregeln bestimmen, was geplant, erreichbar, bezahlt, geliefert und tatsächlich gebaut ist. Der [bestehende Prototyp](../guides/road-construction-tools.md) ist ein begrenzter Ausgangspunkt, keine Bestätigung sämtlicher nachfolgender Funktionen.

## Was untersucht wurde und was tatsächlich vorhanden ist

Die Handbuchrecherche umfasst **alle 90 Seiten** im Agententeam. Seitenverweise in dieser Planung beziehen sich auf genau diese Ausgabe: PDF-Metadaten vom 29. Oktober 2026, Aktualisierungsliste bis Oktober 2026, abgerufen am 30. Oktober. SHA-256 der untersuchten PDF: `b588d729f04def350b37f31a9860d54f6a010e9e870cdeb91d4ca3dd06f001e2`. Original-PDF, Vendor-Screenshots und lizenzierte Assets werden nicht in dieses öffentliche Repository kopiert.[^rcp-manual]

Die **lokale Bestandszählung** ist ein anderer Nachweis: **673 Pakete**, davon **671 `.uasset` und zwei `.umap`**. Erfasst wurden 49 Blueprint-, 251 Mesh-, 188 Material-, 162 Textur-, 18 Demo- und fünf Soundpakete. Darunter liegt ein Haupt-RoadCreator-Blueprint. RCP ist hier ein **Content-Assetpack und kein eigenes RCP-Plugin**.[^local-inventory]

Mehrere im heutigen Handbuch beschriebene neuere Helfer, Parking-Area-, Map-Backdrop-, Utility-Poles-, Low-Poly-, Mirage- und Gebäude-Bausteine fehlen im lokalen Bestand namentlich. Das kann ein älterer Bestand oder eine unvollständige Migration sein. **Die lokale RCP-Version ist unbekannt.** Aus der Engine-Serializer-Version eines Assets lässt sich das RCP-Release nicht zuverlässig datieren. Deshalb zuerst Bestand und Abhängigkeiten mit der verfügbaren lizenzierten Distribution abgleichen; keine automatische Aktualisierung aus dieser Planung ableiten.

## Was RCP für uns liefert

RCP ist ein **parametrisierter Meshbaukasten**: Straßen werden entlang von Splines verformt; Ausstattung wird als Spline Mesh, instanzierte Meshes oder einzelne Actors angeordnet. Viele sichtbare Funktionen lassen sich dadurch übernehmen. Kreuzungsflächen und Kreisverkehre verwenden teilweise vorbereitete Meshes. Das Handbuch verspricht keinen allgemeinen Solver für beliebige Kreuzungstopologien.[^rcp-manual]

Die folgende Matrix trennt die Rollen. **Assets** meint lizenzierte Modelle, Materialien, Texturen und Blueprints, soweit lokal vorhanden. **Adapter** meint unseren ausdrücklichen Aufruf und die Rekonstruktion zur Spielzeit. **Spiellogik** meint Zustände und Regeln, die CityLab selbst verantwortet. Keine Tabellenzeile ist bereits eine neue Laufzeitabnahme.

| Bereich und PDF-Seiten | RCP-Assets und dokumentierte Fähigkeiten | Erforderlicher Runtime-Adapter | Eigene CityLab-Spiellogik |
| --- | --- | --- | --- |
| Straßenquerschnitte, S.3–5, 11, 19, 85 | Mehrspurige Varianten, Gesamt- und Fahrbahnbreite, Doppelstraßen, Mittelabstand; Zusatzspur als Custom Part. Die Produktseite beschreibt ein bis acht Spuren. Gerade Basismeshes sind 12 m lang, Standardspur 4 m. | Stil in passenden Mesh-/Materialsatz und Splinequerschnitt übersetzen; Breiten und UVs konsistent halten. | Gespeicherte Straßenprofile, Netzkennungen, Kurven, erlaubte Breiten und Umbaugrenzen. |
| Gehwege und Fahrbahnränder, S.7–9, 11, 41 | Links/rechts/mittig, schmal/breit, Höhen, Materialien, farbige Bordsteine, Kiesstreifen, unregelmäßige Asphaltkante. | Seitenteile mit Anschlussaussparungen aufbauen; kurze Gehwegteile nur bei nötiger Krümmung. | Begehbare Flächen, Zugänge und Baukosten; Randänderung wird ein Auftrag. |
| Leitplanken und Schutzwände, S.6, 8, 14–15 | Spline- oder 4-m-ISM-Leitplanken, alte/gebrochene Varianten, Betonbarrieren, Stützwände, Lärm- und Blendschutz. | Qualität und Instanzierung wählen; Lücken und Endstücke an Knoten behandeln. | Baufreigabe, Zustand/Schäden und eventuelle spätere Reparaturen. |
| Custom Parts, S.18–19 | Mesh, Spline/ISM, Abstand, Seiten-/Höhenoffset, Start-/Endoffset, Skalierung, Rotation/Zufall, Neigung, Material, Spiegelung. | Wiederverwendbarer Teileverteiler mit stabilen Seeds und begrenzten Aktualisierungen. | Stil und Platzierungsabschnitte speichern; zusätzliche Teile benötigen eigene Bauanforderungen. |
| Straßensnapping, S.20 | Enden an Straßen oder Mesh-Sockets, Tangentenanpassung, Standardsuche 250 cm. | Socket- und Netzanschlüsse in einer gemeinsamen Vorschau prüfen. | Gemeinsame Knoten statt optischem Überlappen; genaue Bestätigung und Abbruch. |
| Autobahn, Rampen und Übergänge, S.67–68 | New-Road-/Transition-/New-Lane-Meshes, zusätzliche Spur mit 12/24/48-m-Einlauf; Anleitung für zusammengesetzte Anschlüsse. | Zu Profilen passende Übergangs- und Einfädelmodule mit Socket-/Nahtprüfung. | Rampengeometrie, tatsächliche Spurwechsel-/Abbiegeverbindungen und Bauzugang; kein belegter automatischer Autobahnknoten-Generator. |
| Steigung und Kurven, S.21 | Steigung, vertikaler/horizontaler Radius, Geschwindigkeits- und Farbhilfen. | Geeignete Berechnung prüfen und im Spiel anzeigen. | Verbindliche Baugrenzen und verständliche Ablehnungsgründe festlegen. |
| Bearbeitung, S.25–29 | Teilen, links/rechts trennen, umkehren, versetzen, zusammenführen, Stil übernehmen; Splineimport über Editorhelfer. | Geeignete Geometriefunktionen aus Editoraktionen lösen oder kontrolliert ersetzen. | Atomare Netzänderung; begonnene Arbeit, Identitäten und bereits verbrauchte Materialien erhalten. |
| Kreuzungen, S.26–27, 55–57 | Vorbereitete Kreuzungs-/Abzweig-/Übergangsmeshes, Junction Placer, Gehwege, abgesenkte Bordsteine, Flächen und Decals. | Passende Prefabs mit Sockets einsetzen; Zuschnitt, Höhen und Nähte prüfen. Für freie Formen gegebenenfalls eigene Flächen erzeugen. | Abbiegebeziehungen, Vorfahrt, Bauabschnitte, Zugänge und später Verkehrsfreigabe. |
| Kreisverkehr, S.42–43 | Große Varianten, modularer kleiner Kreisverkehr und 50-m-Variante; kleiner modularer Kreisverkehr und 50-m-Variante erlauben variable Zufahrten/Winkel, mit jeweils passenden Anschlussmeshes. | Kreis-/Zufahrtsmodule, Material-/Gehwegnähte und Socketzuordnung. | Gerichtete Fahrbeziehungen und Erreichbarkeit; kein allgemeiner Kreuzungssolver mitgeliefert. |
| Asphalt und Fahrbahnlinien, S.33–40 | Asphalt, Risse, Schmutz, Feuchte/Pfützen, reparierte/farbige Spur; Randlinien, drei Trenner, Schraffuren, Breite, Versatz, Strichmuster, Farbe/Alpha, Retroreflexion. | Mesh-UV-Vertrag nutzen; dynamische Parameter und vorzukompilierende Materialvarianten unterscheiden. | Gespeicherte Stilwerte; Markierung ist Darstellung, kein automatisch erzeugter Fahrspurgraph. |
| Schotter und Pflaster, S.69–70 | Schotterstraßentyp und passendes Abzweigmesh; Pflasteroptik über Pavement-Material. | Material-/Meshvarianten aus dem Straßenprofil wählen und passend anschließen. | Getrennte Straßenqualität, Verbrauch und Baufortschritt; ein Materialwechsel erzeugt keinen neuen gebauten Untergrund. |
| Weitere Markierungen und Schäden, S.44–49 | Gerade/Spline-Liniendecals, Text, Pfeile, Schraffuren, Reparatur-/Bremsspuren, Schächte, Leck-/Graffitidecals, POM-Schlaglöcher. | Decals kontrolliert projizieren und aus Parametern rekonstruieren. | Platzierung/Zustand speichern; ein POM-Schlagloch ist keine physische Grube. |
| Brücken und Stützwände, S.12–14, 23–24, 50–52 | 20 Stützenmeshes, Reihenanzahl, Abstände/Offsets/Skalierung, Material, kurvenfolgende Stützen; Pylone/Kabel, Widerlager, Fugen samt Geräusch. | Brückensegmente, Stützen und Auflager aus dem Plan anordnen. | Spannweiten-/Durchfahrtregeln, Bauphasen, Kosten und Zufahrten; keine belegte automatische Statik. |
| Tunnel, S.12, 23 | Portale, Hülle, Beleuchtung, längenabhängig 0/4/8 Lüfter. | Tunnelteile, Portale und Beleuchtung mit eigener Tunnelkomponente koppeln. | Tatsächliche Öffnung, befahrbare Hülle, AirPocket, Sicherheit der Übergänge und später echter Vortrieb. |
| Leuchten und Tageszeit, S.13, 22, 50–52, 76, 81 | Straßen-/Tunnelleuchten, Kabel, Billboards, Hindernislicht, Lichtinterface; Tageszeit/Breitengrad/Jahreszeit. | Geprüfte Lichtfunktionen anbinden; sichtbare Lichtquellen budgetieren. | Gespeicherter Lichtzustand und gegebenenfalls spätere Energieversorgung. UDS ist eine externe Integration, keine Voraussetzung dieses Plans. |
| Ampeln, S.58–60 | EU-/US-/Fußgängerformen, Richtungen A–D, Phasen, abschaltbare Richtungen und manuelle Steuerereignisse. | Ampelgruppen und Zeitsteuerung an unsere Knoten anbinden. | Konfliktfreie Bewegungsfreigaben und Verkehrs-KI; sichtbare Ampeln lenken noch keine Fahrzeuge. |
| Schranken, S.53–54 | Öffnen/Schließen, Sensor, Zeitablauf, gekoppelte Schranken, Unterbrechung; im Handbuch als multiplayerfähig beschrieben. | Ereignisse und Kollisionen prüfen und an Aufträge/Zufahrten anbinden. | Berechtigungen, Warteschlange und dauerhafter Zustand; Multiplayer/Save nicht durch Handbuch übernommen. |
| Parken, S.63–66, 89 | Straßenrand- und Flächenparkplätze, Winkel/Abmessungen/Markierungen, dekorative Belegung; ein Standardautotyp, erweiterbare Meshliste, EV-Ausstattung. | Parkplatzflächen und Stellplatzdaten aus Profilen aufbauen. | Reservierung, Zufahrt, Einparken, Belegung und Ladevorgang; dekorative Autos sind keine Simulation. |
| Schilder und Straßenmöbel, S.10, 61–62, 71–74, 88 | EU-/US-Schilder, Zieltexte, Pfosten, umfahrbare Teile, Bänke/Mülleimer und ISM-Prop-Verteiler; neun Zaunarten. | Platzierung, Instanzen, Texte und gegebenenfalls Physikersatz verwalten. | Regelwirkung, persistente Schäden und Ressourcen; Deko wird nicht automatisch Verkehrsregel. |
| Versorgungstrassen, S.17, 61–62 | Masten, automatisch angeordnete Kabel, Hochspannungsleitungen und Transformator-Mesh. | Spline-/Mast-/Kabelaufbau separat oder entlang der Straße. | Eigener Versorgungsgraph, Anschluss/Leistung und Versorgungsausfall bleiben separate Systeme. |
| Optik und Gebäude, S.35–37, 75, 77 | Nahdetail, Low-Poly-Stil, Hitzeflimmern/Heat Haze; neun Gebäudemeshes und Licht-/Fenstereinstellungen. | Vorhandene Materialvarianten prüfen; Gebäude und Lichtparameter instanzieren. | Grundstück, Bewohner und Nutzung stammen aus unserem Bausystem; Gebäudeassets sind keine Stadtwirtschaft. |
| Hilfswerkzeuge und Optimierung, S.28–30, 78–83 | Messen, Kartenbild als Entwurfsunterlage, ISM/Spline-Aufteilung, Scalability, statisches Zusammenführen. | Sinnvolle Mess-/Profilwerkzeuge als Spiel-UI anbieten; Editorwerkzeuge nicht voraussetzen. | Streaming-/Speicher-/Lichtbudgets messen. Map Backdrop ist laut Autor keine Funktion für das fertige Produkt. |

[^rcp-manual]: [Offizielles RCP-Handbuch](https://drive.google.com/file/d/1NYQA6k-qZHusso1npgAfEgGpnieeDRxt/view), untersuchte 90-seitige Ausgabe; die Seitenzahlen stehen direkt in der Matrix.

## Wichtige Grenzen für die Integration

**Construction Script ist kein grundsätzliches Laufzeitverbot.** Auf Seite 27 formuliert das RCP-Handbuch den Ausschluss für ein verpacktes Spiel zu pauschal. Epic dokumentiert bei gespawnten Actors ausdrücklich `ExecuteConstruction`/`OnConstruction` und bei Deferred Spawn die Fertigstellung über diesen Pfad. Davon zu unterscheiden sind bereits vorbereitete Level-Actors, Editor-Rekonstruktion und nachträgliche Parameteränderungen. Daraus folgt noch kein funktionierender Refreshvertrag des konkreten RCP-Blueprints.[^ue-construction][^ue-lifecycle]

Wir prüfen deshalb vor einer Zusage zum Wiederverwenden des vollständigen RoadCreator-Actors: verfügbare Laufzeitfunktionen, Editorabhängigkeiten, Materialwechsel, synchrone Assetladevorgänge, Komponentenabbau und Kosten wiederholten Neuaufbaus. Geeignete Funktionen dürfen bleiben. Was nur über Editor Utility, Merge Actors oder Landscape-Editorpfade funktioniert, erhält einen eigenen Adapter oder bleibt ein Vorbereitungswerkzeug. Hinweise zur Komponentenverwaltung und teuren Spline-Rekonstruktion im [Autorenforum](https://forums.unrealengine.com/t/lyoshko-road-creator-pro/2418882) sind Anlass zur Messung, kein nachgewiesener Leak unserer Installation.

**Markierung und Fahrspurgraph sind verschieden.** Die Asphaltlinien entstehen über die UVs des Straßenmeshes; freie Linien, Pfeile und Texte nutzen zusätzlich Decals. Randlinien und drei Trenner sind fünf Markierungskanäle, kein Beleg für fünf beliebig erzeugte Fahrspuren. Überhöhung beziehungsweise Banking wird aus den bloßen Neigungs-/Skalierungsoptionen ebenfalls nicht als fertige oder geprüfte Funktion zugesagt. Statische Materialparameter werden laut Epic zur Kompilierzeit festgelegt. Benötigte Varianten müssen deshalb vor dem Verpacken verfügbar sein; dynamische Parameter und die tatsächliche RCP-Parameterbelegung werden getrennt geprüft.[^ue-materials]

**Frei geformte Netzknoten sind eine eigene Aufgabe.** Das Handbuch zeigt vorbereitete Kreuzungen, Platzieren an Straßenseiten und zusammengesetzte Flächen. Unterschiedlich gewinkelte Zufahrten am 50-m-Kreisverkehr beweisen keinen allgemeinen Kreuzungssolver. Der Socket-Snapwinkel unter 90° auf Seite 20 betrifft die Orientierung des Anschlussendes und ist keine 90°-Grenze für Kreuzungsarme. Die Roadmap auf Seite 90 behandelt einen allgemeinen beliebig gewinkelten Junction-Generator weiter als mögliche Zukunft; durchgestrichene andere Roadmappunkte sind bereits umgesetzt und dürfen nicht als fehlende Features gezählt werden.[^rcp-manual]

**Landscape-Deformation wird nicht unverändert übernommen.** RCP beschreibt auf Seiten 31–32 ein Unreal-Landscape-Verfahren mit Edit-/Paint-Layern, Böschung, Zusatzbreite und Vorschau. Es nennt selbst Speicher-/Blendingprobleme bestimmter Edit-Layer-Kombinationen. Unser Gelände ist ShaderWorld. Wir übernehmen sinnvolle Zielprofile und Böschungsparameter, führen sie aber über eigene gespeicherte Maschinenaufträge und ShaderWorld-Brushes aus. Die offizielle Brushbeschreibung nennt betroffene Terrain-, Kollisions- und Bewuchsaktualisierungen; sie ersetzt weder unsere Persistenz noch ein Fertigstellungsprotokoll.[^sw-brush][^machine-plan]

## Gelände, Brücke und Tunnel folgen derselben Trasse

Für eine **Bodenstraße** beschreibt die Trasse Fahrbahn, Seitenräume und Böschungen. Wir leiten daraus Abtrag, Auffüllung und Rodungsbedarf ab; nur ausgeführte Maschinenarbeit verändert ShaderWorld und gibt den befahrbaren Untergrund frei. Die im Handbuch gezeigte adaptive Böschung ist dafür ein gutes Vorbild: Bei festem Böschungswinkel wächst ihre Breite mit der Höhe des Damms.

Eine **Brücke** besitzt eine eigene Fahrbahnhülle und Stützen. Das Gelände unter der Spannweite wird nicht automatisch bis zur Fahrbahn aufgeschüttet; Fundamente und Zufahrten sind getrennte Bodenarbeiten. Ein optisches Kreuzen auf unterschiedlicher Höhe erzeugt keinen Netzknoten.

Ein **Tunnel** braucht neben den RCP-Portalen und -Meshes eine tatsächliche ShaderWorld-Öffnung sowie eine eigene Hülle mit Boden, Wänden, Decke und Kollision. RCP verlangt beim UE Landscape selbst ein separates Sichtbarkeitsloch; der Meshaufbau gräbt keinen Berg aus. Unsere AirPocket ist der Wasserausschluss, der verhindert, dass das Ozeanmaterial durch den Tunnelboden sichtbar wird. Sie ersetzt weder die Hülle noch die Geländekollision. Echter maschineller Vortrieb bleibt eine spätere Aufgabe.[^rcp-manual]

## Vorgeschlagenes Datenmodell

Ein **Straßenprofil** enthält stabile Kennung und Profilversion, Querschnitt, Breiten, Material-/Markierungsstil sowie die gewählten Gehwege, Randteile, Leuchten und sonstigen Custom Parts. Profile verweisen auf einen geprüften Assetkatalog. Ein neuer Vendorimport darf diese Bedeutung nicht stillschweigend verändern.

**Knoten und Kanten** halten gemeinsame Anschlüsse, Verlauf, Höhen und Verkehrsbeziehungen. Splinepunkte, Tangenten, Breitenverlauf und Typgrenzen sind ausdrücklich gespeicherte Daten. Straße, Brücke und Tunnel werden nötigenfalls in verbundene Segmente mit passenden Anschlüssen aufgeteilt; ein Typ gilt im dokumentierten RCP-Actor für dessen ganze Länge.

**Soll, Ist und Vorschau bleiben getrennt:**

- Die temporäre Vorschau beschreibt die aktuelle Mausgeste. Sie verändert weder Gelände noch Lager oder gebaute Straßen.
- Bestätigen erzeugt einen gespeicherten Sollplan mit geprüften Anschlüssen, Ausgangsboden und Mengen. Arbeit startet weiterhin ausdrücklich.
- Der Istzustand enthält bereits gerodete Flächen, ausgeführtes Terrain, eingebaute Straßenabschnitte und Materialkonten. Nur tatsächliche Maschinenarbeit verändert ihn.
- Umplanen eines begonnenen Vorhabens erhält ausgeführte Arbeit und Konten. Zusätzlicher Abtrag, Einbau, Ausstattungstausch oder Rückbau wird als neue verbleibende Arbeit geplant; ein Materialwechselknopf darf keinen fertig gebauten Gegenstand kostenlos ersetzen.

Die Darstellung baut sich aus diesen Daten wieder auf. **Wir speichern keine erzeugten SplineMesh-/ISM-Komponenten als maßgeblichen Spielstand.** Stattdessen speichern wir Profilkennungen, Geometrie, Baufortschritt, Seeds und nötige Einzelzustände und rekonstruieren die Komponenten kontrolliert. Lampen, Ampeln, Schranken und Schäden erhalten nur die tatsächlich benötigten dauerhaften Zustände. Epic stellt mit SaveGame den Speichermechanismus bereit; unser Spiel legt die Daten und Wiederherstellung fest.[^ue-save]

## Bau, Transport und Erreichbarkeit bleiben echte Spielregeln

Das gemeinsame Lager, tatsächliche Lkw-Ladungen und begrenzte Baustellenpuffer bleiben maßgeblich. Ein neuer RCP-Stil erzeugt weder Anfangsbestand noch kostenlosen Asphalt. Breitere Fahrbahn, Gehweg, Brücke oder Tunnel brauchen definierte Mengen und Bauphasen. Welche zusätzlichen Baustoffarten sinnvoll sind, legen wir beim jeweiligen Ausbau fest; das vorhandene Erd-/Kies-/Asphaltmodell wird nicht heimlich um beliebige Ersatzmaterialien erweitert.[^road-plan]

Der vorhandene begrenzte Maschinenzug und seine geprüfte Baufront sind keine allgemeine Stadtlogistik. **Depotflotte, allgemeine Fahrzeugsuche, freie Arbeitszuweisung und umfassende Baustellenzufahrten bleiben offen.** RCP-Meshes liefern auch keine vollständige Fahrzeugnavigation. City Traffic Pro ist eine gesonderte Integration; wir entscheiden später, ob eigene Verkehrslogik oder ein zusätzliches System passt.[^rcp-author]

Der Nutzer meldet außerdem ein **UI-Problem beim Arbeiten mit mehreren Aufträgen**. Es ist ausdrücklich vertagt und wird durch diese Recherche weder behoben noch als getestet markiert. Bei der späteren Bedienung müssen Werkzeugwahl, Entwurf, bestätigter Auftrag und aktiver Maschinenauftrag klar erkennbar sein.

## Sinnvolle Reihenfolge zur Besprechung

1. **Bestand und kleinsten Laufzeitpfad klären.** Fehlende aktuelle Assetgruppen und Abhängigkeiten feststellen. In einem getrennten gekochten Versuch einen RCP-Actor beziehungsweise geeigneten Builder spawnen, Geometrie/Material ändern, mehrfach rekonstruieren und vollständig entfernen. Komponentenanzahl, Kollision, Ladehänger und Speicher über Wiederholungen prüfen. Erst danach Wiederverwendung des ganzen Actors zusagen.
2. **Profile, Darstellung und Speicherung erweitern.** Zunächst vorhandene gerade und gekrümmte Straße über denselben Asset-/Teileadapter erzeugen. Gehwege und Markierungen als erste sichtbare Erweiterung; Soll/Ist unverändert erhalten. Kalter Neustart rekonstruiert denselben Zustand ohne doppelte Teile, Kosten oder Lagerbestände.
3. **Anschlüsse und echte Planung vertiefen.** Mehrere Querschnitte, Übergänge, Endpunkt-/T-/Kreuzungsanschlüsse und Kreisverkehr mit Kurvenvorschau. Terrainprofil und Maschinenmengen aus derselben bestätigten Geometrie ableiten. Geneigte Knoten, Nähte und Kollision gesondert prüfen.
4. **Ausstattung und Steuerung hinzufügen.** Leitplanken, Leuchten, Schilder, Ampeln, Schranken und Parkplätze. Zuerst konsistente Platzierung/Speicherung, dann ihre tatsächlichen Verkehrs- und Nutzungsregeln. Das vertagte Mehrfachauftragsproblem vor breiter Bedienabnahme erneut behandeln.
5. **Brücken und Tunnel als Bauwerke aufbauen.** Anschlüsse, Stützen/Portale, Durchfahrten, eigene Tunnelhülle und AirPocket. Gespeicherte Bauphasen und Materialversorgung; echter Tunnelvortrieb bleibt eine eigene Ausbauetappe.
6. **Dichte, Wiederaufbau und große Netze messen.** Instanzierung, Straßen-/Teilequalität, Materialvarianten, Lichtbudget, Streaming und Ladezeiten anhand unseres Spiels entscheiden. Herstellerangaben zu Performance sind keine gemessene CityLab-Leistung.

Diese Reihenfolge ist ein Vorschlag, keine Freigabe für einen großen Gesamtumbau. Als erste praktische Abnahme zählt ein kleiner gekochter Versuch mit tatsächlichem Laufzeitaufbau, Stilwechsel und sauberem Komponentenlebenszyklus. Danach legen wir den nächsten sichtbaren Spielfunktions-Slice gemeinsam fest.

## Prüfstatus und offene Entscheidungen

**Erledigt:** vollständige Handbuchrecherche im Team, getrennte lokale Bestandszählung und dieser Integrationsentwurf. **Nicht erfolgt:** breite RCP-Runtime-Integration, neue gekochte RCP-Actor-/Lifecycle-Abnahme, Leistungsnachweis, Save-Migration oder Nutzerabnahme der geplanten Funktionen.

Noch festzulegen sind der zu vervollständigende lizenzierte RCP-Bestand, das erste Profilset, der gewünschte Umfang freier Kreuzungsformen und die Grenze zwischen reiner Ausstattung und echter Verkehrs-/Versorgungssimulation. Das bestehende Straßenlabor und seine Spielstände behalten ihren eigenen [begrenzten Prüfstand](../guides/road-construction-tools.md).

[^local-inventory]: Getrennte lesende lokale Bestandsaufnahme; Details und Aussagegrenzen im Quellenobjekt `local-inventory`.
[^ue-construction]: [Epic: Construction Script](https://dev.epicgames.com/documentation/en-us/unreal-engine/construction-script-in-unreal-engine).
[^ue-lifecycle]: [Epic: Actor Lifecycle](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-actor-lifecycle), besonders Spawning und Deferred Spawn.
[^ue-materials]: [Epic: Material Instances](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine), Static Parameters und Material Instance Dynamic.
[^ue-save]: [Epic: Saving and Loading Your Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine).
[^sw-brush]: [ShaderWorld: Blueprint Brush System](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass).
[^road-plan]: [Straßenbau-Arbeitsplan](road-construction-work-plan.md).
[^machine-plan]: [Scaping als Maschinenaufträge](scaping-machine-work-plan.md).
[^rcp-author]: [Offizieller Produktthread mit Autorenantworten](https://forums.unrealengine.com/t/lyoshko-road-creator-pro/2418882); kein mitgelieferter Verkehrs- oder Runtime-Abnahmenachweis.
