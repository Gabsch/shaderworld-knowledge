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
  at: "2026-10-30T22:29:19.274182+00:00"
evidence_scope:
  manual: Das Agententeam hat das vollständige offizielle 90-seitige RCP-Handbuch einschließlich relevanter Abbildungen und Roadmap gelesen; Herstellerfähigkeiten sind keine Laufzeitabnahme.
  local: Aktualisierter Bestand mit 907 Paketen, 18 eigenen vorbereiteten Meshkopien, tatsächlicher Klassenreflexion und statischen Tunnel-/Brückengeometriemessungen; Releasekennung und Vollständigkeit des neuesten Releases bleiben ungeklärt.
  runtime: Historische Stage1 mit gekochtem Deferred-Spawn, negativer Raw20-Route und begrenzt bestandener Eigenadapter20-Probe getrennt von Native2 mit 128 Modell-/API-Tests. Nachfolgende Stage2 besteht Create32/Resume95 über die Produktionsmanager-API einschließlich Kaltstart; neue normale Bediengesten, Stage3, Import und Stage4 sind damit nicht abgenommen.
sources:
  - id: stage2-proof
    resource: ../evidence/rcp-toolkit-integration.json
    title: Begrenzte Stage2-Maschinen-/Kaltstartabnahme und getrennte Folgefehler
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
    resource: ../evidence/rcp-toolkit-stage1.json
    title: Bereinigter Stage1-Beleg mit 907 Paketen, nativer Klassenreflexion, 18 vorbereiteten Kopien, Geometriemessungen und getrennten Native2-Tests
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

**Ziel ist ein umfangreiches Straßenwerkzeug im Spiel:** RCP-Straßentypen, Kurven, Gehwege, Markierungen, Ausstattung, Kreuzungen, Brücken und Tunnel sollen sich planen, bauen und dauerhaft weiterverwenden lassen. Die Bedienung folgt unserem City Builder; den Editor-3D-Gizmo wollen wir nicht nachbauen. Der Nutzer hat die Umsetzung inzwischen in vier Stufen beauftragt. Diese Seite hält Architektur, aktuellen Bestand und offene Abnahmen fest; sie ist noch keine Anleitung für vollständig verfügbare Spielfunktionen.

**CityLab bleibt die maßgebliche Datenquelle.** RCP liefert Assets und geeignete geprüfte Funktionen für die Darstellung. ShaderWorld erzeugt Gelände, Bewuchs und Bodenkollision. Unsere Spielregeln bestimmen, was geplant, erreichbar, bezahlt, geliefert und tatsächlich gebaut ist. Der [bestehende Prototyp](../guides/road-construction-tools.md) ist ein begrenzter Ausgangspunkt, keine Bestätigung sämtlicher nachfolgender Funktionen.

## Was untersucht wurde und was tatsächlich vorhanden ist

Die Handbuchrecherche umfasst **alle 90 Seiten** im Agententeam. Seitenverweise in dieser Planung beziehen sich auf genau diese Ausgabe: PDF-Metadaten vom 29. Oktober 2026, Aktualisierungsliste bis Oktober 2026, abgerufen am 30. Oktober. SHA-256 der untersuchten PDF: `b588d729f04def350b37f31a9860d54f6a010e9e870cdeb91d4ca3dd06f001e2`. Original-PDF, Vendor-Screenshots und lizenzierte Assets werden nicht in dieses öffentliche Repository kopiert.[^rcp-manual]

Nach dem vom Nutzer durchgeführten Update enthält der **lokale Bestand 907 Pakete: 905 `.uasset` und zwei `.umap`**. Der frühere 673-Paket-Bestand bleibt die historische Ausgangszählung. Die Gruppen sind Verzeichnisse und enthalten beispielsweise auch Enums und Strukturen; 80 Blueprintpakete bedeuten daher nicht 80 Actor-Klassen. Ein Haupt-`BP_Road_Creator` ist vorhanden. RCP liegt hier als **Content-Assetpack ohne eigenes RCP-Plugin** vor.[^local-inventory]

| Ordnergruppe | Vor dem Update | Aktuell |
| --- | ---: | ---: |
| Blueprints und zugehörige Typen | 49 | 80 |
| Meshes | 251 | 352 |
| Materialien | 188 | 241 |
| Texturen | 162 | 209 |
| Demo | 18 | 18 |
| Sound | 5 | 7 |
| Gesamt | 673 | 907 |

Nun sind Helper, Tape Measure, Parking Area, Map Backdrop, Utility Poles/Transmission Line, LowPoly-/Mirage-Materialfunktionen und das Gebäudeset namentlich vorhanden. Das korrigiert die frühere Fehlstellenliste. **Die genaue RCP-Releasekennung und ein vollständig aktueller Import sind weiter nicht belegt.** Im Bridge-Ordner liegen neun Meshes; die im neueren Handbuch beschriebenen vielen auswählbaren Stützen lassen sich daraus nicht vollständig bestätigen. Ein vorhandener Name ist außerdem noch kein funktionierendes Laufzeitfeature. Die Engine-Serializer-Version eines Assets datiert das RCP-Release nicht.[^local-inventory]

### Was die echte Bestandsprüfung zusätzlich zeigt

Die AssetRegistry meldet **sechs nicht vorhandene Paketverweise in sechs Materialpaketen**: vier Texturpfade aus `Street_Props`, einen aus `Backyard_Pool` und einen aus `Restroom_Basic_Pack`. Der [bereinigte Beleg](../evidence/rcp-toolkit-stage1.json) nennt die genauen relativen Assetpfade. Die unmittelbaren `/Game`-Abhängigkeiten des Haupt-RoadCreator-Blueprints sind dagegen vorhanden. Das ist keine Entwarnung für sämtliche transitiven Zubehörmaterialien und noch kein beobachteter Fehler im verpackten Bild. Vor Nutzung betroffene Materialien zuordnen und ausdrücklich reparieren oder durch eigene Varianten ersetzen; keine stillen Änderungen am Vendorbestand.[^local-inventory]

Die geladene Klasse besitzt **196 Vendor-Eigenschaften und 47 Vendor-Funktionen**. Darunter ist `UserConstructionScript` ohne Parameter. Keine dieser Eigenschaften oder Funktionen trägt ein `EditorOnly`-Flag. Gerade auch Landscape-/Editorhelfer zeigen, warum dies allein keine Laufzeitzusage erlaubt: indirekte Aufrufe müssen im verpackten Spiel geprüft werden. Im Klassenstandard ist `Road Settings.RoadMesh` noch `None`; die Zuordnung des Straßentyps erfolgt durch eine Funktion. Der Katalog darf sie deshalb erst nach tatsächlichem Komponentenaufbau als Laufzeitmapping bestätigen.[^local-inventory]

Am Haupt-Asphaltmaterial wurden **37 statische Schalter, 57 skalare und fünf Vektorparameter** gelesen. `MI_Asphalt_MAIN_Reflective_Mirage` ist als eigene vorhandene Variante für Retroreflexion und Mirage identifiziert. Statische Schalter werden nicht als frei schaltbare Laufzeitregler ausgegeben: Die passenden Varianten müssen gekocht sein, dynamische Werte und tatsächliche Materialzuweisung bleiben separat zu prüfen.[^local-inventory][^ue-materials]

Die lokalen Basismeshes ergeben geometrische Breiten von rund **5 / 9 / 13 / 17 / 20 m** für ein-, zwei-, drei-, vier- und geteilt vierspurig; der Kiesweg misst rund **5,977 m**. Die geraden Elemente sind etwa 12 m lang. Das sind gemessene Meshgrenzen, keine nutzbaren Fahrspurbreiten oder bereits bestätigten Runtime-Skalierungen. Der Adapter muss Profil, Randteile und Bodenziel daran gemeinsam ausrichten; der bisherige 8-m-Prototyp ist kein universeller RCP-Querschnitt.[^local-inventory]

### Eigene vorbereitete Meshes und gemessene Bauwerksgeometrie

Für den eigenen Adapter wurden **18 getrennte Meshkopien** vorbereitet und CPU-Zugriff an diesen Kopien zurückgelesen: sechs Straßenprofile, fünf Brückentypen, Tunnel und Portal, eine Stütze sowie vier Ausstattungsteile. Die untersuchten Vendor-Meshes bleiben unverändert und besitzen weiterhin deaktivierten CPU-Zugriff. Diese Vorbereitung ist kein Beleg für später korrekt gekochte Spline-Kollision.[^local-inventory]

Die statische Geometriemessung begrenzt bereits wichtige Annahmen:

- Im Tunnel wurde ein mittiger **8 m breiter und 4 m hoher Korridor** an 729 Proben bestätigt. Sein lokaler Boden liegt bei +10 cm, der untersuchte innere Dachbereich mindestens bei rund +527,38 cm. Das beweist weder das gesamte Gewölbe noch massive Boden-/Wandstärke, Kollision oder eine Durchfahrt.
- Das Portal besitzt einen anderen lokalen Bodenbezug, hier 0 cm. Wir richten Fahrbahn und Öffnung nach dokumentierten Bezugshöhen aus; die jeweilige Bounding Box genügt dafür nicht.
- Am zweispurigen Brückenchassis fanden 81 zentrale Proben keine Fläche auf oder über der lokalen Z=0-Ebene. Aus dessen Umhüllung wird daher keine geschlossene Fahrbahnplatte abgeleitet: Fahrbahn und nötige deckende/kollidierende Hülle müssen separat erhalten und geprüft werden.
- Eine große rechteckige AirPocket um das ganze Tunnelgewölbe ist noch nicht freigegeben. Sie kann über die Rundung in offene Bereiche reichen; vollständige Geländeabdeckung, Portalabschluss, Wasserbild und Neustart sind eigene Tests.

Es wurden nur Messzusammenfassungen übernommen. Lizenzierte Meshes, OBJ-Exporte, vollständige Geometrie und Vendorquellcode bleiben außerhalb dieses öffentlichen Bundles.[^local-inventory]

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

## Beauftragte Stufen und ursprüngliche Reihenfolge

Die Umsetzung ist in **vier abgegrenzte Arbeitspakete** gebündelt: zuerst Inventar und tatsächlicher RCP-Laufzeitpfad; dann Profile und mehrere gespeicherte Planungen; danach Anschlüsse/Knoten/Kreisverkehr; schließlich Brücken und Tunnel mit Wasser-, Material- und Neustartprüfung. Der bestehende geprüfte Starter bleibt RoadConstruction11, bis eine neue Abnahme einen Wechsel rechtfertigt. Der isolierte erste Cook erhält keine pauschale Freigabe alter Saveprofile.

Die folgende ausführlichere Reihenfolge bleibt die fachliche Orientierung:

1. **Bestand und kleinsten Laufzeitpfad klären.** Fehlende aktuelle Assetgruppen und Abhängigkeiten feststellen. In einem getrennten gekochten Versuch einen RCP-Actor beziehungsweise geeigneten Builder spawnen, Geometrie/Material ändern, mehrfach rekonstruieren und vollständig entfernen. Komponentenanzahl, Kollision, Ladehänger und Speicher über Wiederholungen prüfen. Erst danach Wiederverwendung des ganzen Actors zusagen.
2. **Profile, Darstellung und Speicherung erweitern.** Zunächst vorhandene gerade und gekrümmte Straße über denselben Asset-/Teileadapter erzeugen. Gehwege und Markierungen als erste sichtbare Erweiterung; Soll/Ist unverändert erhalten. Kalter Neustart rekonstruiert denselben Zustand ohne doppelte Teile, Kosten oder Lagerbestände.
3. **Anschlüsse und echte Planung vertiefen.** Mehrere Querschnitte, Übergänge, Endpunkt-/T-/Kreuzungsanschlüsse und Kreisverkehr mit Kurvenvorschau. Terrainprofil und Maschinenmengen aus derselben bestätigten Geometrie ableiten. Geneigte Knoten, Nähte und Kollision gesondert prüfen.
4. **Ausstattung und Steuerung hinzufügen.** Leitplanken, Leuchten, Schilder, Ampeln, Schranken und Parkplätze. Zuerst konsistente Platzierung/Speicherung, dann ihre tatsächlichen Verkehrs- und Nutzungsregeln. Das vertagte Mehrfachauftragsproblem vor breiter Bedienabnahme erneut behandeln.
5. **Brücken und Tunnel als Bauwerke aufbauen.** Anschlüsse, Stützen/Portale, Durchfahrten, eigene Tunnelhülle und AirPocket. Gespeicherte Bauphasen und Materialversorgung; echter Tunnelvortrieb bleibt eine eigene Ausbauetappe.
6. **Dichte, Wiederaufbau und große Netze messen.** Instanzierung, Straßen-/Teilequalität, Materialvarianten, Lichtbudget, Streaming und Ladezeiten anhand unseres Spiels entscheiden. Herstellerangaben zu Performance sind keine gemessene CityLab-Leistung.

Als erste praktische Abnahme zählt der getrennte gekochte Versuch mit tatsächlichem Laufzeitaufbau, Stilwechsel und sauberem Komponentenlebenszyklus. Mindestens 20 echte Umbau-/Abbauzyklen müssen tatsächliche registrierte Instanzen, Straßenkollision, Profil/Ausstattung/Material sowie Komponentenabbau prüfen. Fehler bleiben Fehler, auch wenn die übrigen Zyklen für die Diagnose weiterlaufen. Prozessspeicher wird gemessen; Engine- und Assetcaches erlauben daraus allein keine Leakfreiheit abzuleiten.

## Prüfstatus und offene Entscheidungen

**Nachfolgende Stage2 begrenzt bestanden:** Die eigene Produktionsmanager-API besteht zwei gekochte Prozesse mit 32 Create-/95 Resume-Prüfungen, drei zusätzlichen gespeicherten Profilplänen während Erdarbeit und einem kalten beladenen Fertigteiltransport. Vollständige Zustände und drei normale Loads bleiben exakt; nur der Hauptauftrag wird fertig, vier Materialbilanzen sind 0 g. Neue Bediengesten und allgemeine Depot-/Flottenlogik sind damit nicht geprüft. Die [Baukastenanleitung](../guides/rcp-road-toolkit.md) bleibt Entwurf und erklärt die ursprünglichen Bilder samt UI-Grenzen.[^stage2-proof]

Der erste echte Stage3-Versuch scheitert an der Erstzuweisung eines Kostenträgers am bestehenden Startknoten; Korrektur und erneute gekochte Knoten-/Nahtprüfung bleiben offen. Der erste gepinnte Legacy-Import scheitert getrennt am alten ausgelassenen Standardfeld Version1. Editor16 sowie eine reine eigene Materialgraphprüfung sind im Nachfolgestand bestanden, keine neue GPU-/Spiel-/Stage4-Abnahme. Historische Stage1-Nachweise darunter behalten ihren engen Umfang.[^stage2-proof]

**Belegt:** vollständige 90-Seiten-Handbuchrecherche, neuer 907-Paket-Bestand mit unveränderten Vendorbytes und Saves während der Prüfung, echte Klassen-/Materialreflexion, 18 vorbereitete eigene Kopien und abgegrenzte statische Geometriemessungen. Native2 besteht **128 CityLab-Modell-/API-Tests: 126 sauber, zwei bekannte Warnungen, null Fehler**. Das sind keine 128 verpackten RCP-Actor- oder Fahrtests.[^local-inventory]

**Gekochter Rohversuch:** Der frische isolierte Cook und ein Deferred-Spawn des Haupt-Blueprints funktionieren. Die anschließenden **20 direkten `UserConstructionScript`-Aufrufzyklen sind fehlgeschlagen**: Im ersten Actor wuchsen registrierte Komponenten von 7 über 10 auf 19, während nur zwei tatsächliche Zweispur-Meshinstanzen verblieben. Der angeforderte Profil-/Material-/Zubehörwechsel wurde nicht dargestellt; alle drei realen Szene- und Body-Rays verfehlten die Straße. Die Splineform änderte sich, und nach Destroy/GC blieben in allen Zyklen null eigene schwache Objektreferenzen übrig. Es gab keine Engine-Fehlerzeilen; Vendorpakete, Probequellen, gekochte Dateien und alle 362 vorhandenen Spielstände blieben unverändert. Das ist ein negatives Ergebnis für **diese direkte UCS-Aufrufroute**, keine Behauptung, Construction Scripts oder sämtliche RCP-Laufzeitpfade könnten grundsätzlich nicht funktionieren.[^local-inventory]

**Eigener Adapter, erster Versuch:** Die separat gebaute native Surface-/Accessories-Route führt alle 20 Zyklen aus. Tatsächliche Profil-/Material-/Zubehöridentitäten, wiederholter Neuaufbau, Clear und vollständige Destroy/GC-Bereinigung passen. Der Lauf scheitert jedoch ehrlich an einer physischen Naht: Beim geraden 60-m-Stück mit sechs Slices verfehlt der unveränderte mittlere Messstrahl genau den inneren Stoß; Szene und Body liefern dort jeweils nur 2/3 Treffer. Der gekrümmte Neuaufbau trifft 3/3. Die begrenzte gemeinsame Render-/Kollisionsüberlappung an inneren Slices ist im Produktionscode korrigiert und im zweiten getrennten Cook bestanden. Die Messpunkte und Treffergates blieben unverändert. An Splinepunkten ist dies eine höchstens 0,5 cm weite Fortsetzung des jeweiligen Segmentpolynoms, keine Gleichheitsbehauptung für unterschiedliche Nachbarkurven. Eigenständige 8-m-Outputactor-Grenzen brauchen zusätzlich einen expliziten Anschlussvertrag und eigene Nahtproben.[^local-inventory]

Der erste eigene Prüfläufer schrieb außerdem seine Berichte versehentlich unter `Tools/runs` und verletzte damit seinen Quell-/Werkzeugschutz. Dieser fehlgeschlagene Nachweis bleibt erhalten; der korrigierte Läufer schreibt ausschließlich unter `Saved`. Kein Schutz wurde dafür ausgeklammert.

**Eigener Adapter, zweite Abnahme bestanden:** Alle **20 gekochten Zyklen** bestehen ohne Beobachtungsfehler: Zweispur → Vierspur, Kurve/Höhe, exakter Main-/ReflectiveMirage-Materialwechsel, Leitplanken, wiederholter Aufbau, Clear und Neuaufbau. Die fünf befüllten Zustände pro Zyklus ergeben **300 echte Szene- und 300 Bodytreffer**, einschließlich des unveränderten mittleren Nahtstrahls. Registrierte Komponenten bleiben bei 9 für die gerade Straße und 21 mit Leitplanken; Clear lässt nur drei Fixturekomponenten zurück. Nach Destroy/vollständigem GC sind alle eigenen schwachen Referenzen in jedem Zyklus ungültig. Der konkrete Leitplanken-Materialoverride ist für diese isolierte Probe Beton, keine Abnahme aller Vendor-Metallmaterialien. Vendor-/eigene Pakete, Quellen/Werkzeuge, Konfigurationshashes, gekochte Dateien und alle 362 vorhandenen Saves blieben während der Probe exakt unverändert. Native Laufzeit 58,67 s; Speicher- und Einzelbauzeiten stehen im [Beleg](../evidence/rcp-toolkit-stage1.json). Prozessspeicher einschließlich Engine-/Assetcaches ist kein eigenständiger Leak- oder Stadtleistungsnachweis.[^local-inventory]

**Noch offen:** weitere Profil-/Kollisions-/Leistungsgrenzen, Nähte zwischen eigenständigen Outputactoren, weitere Profile-/Netz-/Bauwerksabnahmen und ihre normale Bedienung; Stage2 hat inzwischen nur die oben abgegrenzten Produktionsmanager-/Kaltstartfälle bestanden. Vorhandene Funktionen und Spielstände behalten ihren eigenen [begrenzten Prüfstand](../guides/road-construction-tools.md).

Die Herkunft aller benötigten optionalen Materialien, der vollständige aktuelle Vendorumfang und die Grenze zwischen Ausstattung und Simulation bleiben ausdrücklich zu klären. Depotflotte, allgemeine Fahrzeugsuche und das vertagte Mehrfachauftragsproblem sind durch Stage1 nicht erledigt.

[^local-inventory]: Getrennte lesende lokale Bestandsaufnahme; Details und Aussagegrenzen im Quellenobjekt `local-inventory`.
[^ue-construction]: [Epic: Construction Script](https://dev.epicgames.com/documentation/en-us/unreal-engine/construction-script-in-unreal-engine).
[^ue-lifecycle]: [Epic: Actor Lifecycle](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-actor-lifecycle), besonders Spawning und Deferred Spawn.
[^ue-materials]: [Epic: Material Instances](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine), Static Parameters und Material Instance Dynamic.
[^ue-save]: [Epic: Saving and Loading Your Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine).
[^sw-brush]: [ShaderWorld: Blueprint Brush System](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass).
[^road-plan]: [Straßenbau-Arbeitsplan](road-construction-work-plan.md).
[^machine-plan]: [Scaping als Maschinenaufträge](scaping-machine-work-plan.md).
[^rcp-author]: [Offizieller Produktthread mit Autorenantworten](https://forums.unrealengine.com/t/lyoshko-road-creator-pro/2418882); kein mitgelieferter Verkehrs- oder Runtime-Abnahmenachweis.

[^stage2-proof]: [Bereinigter Stage2-Beleg](../evidence/rcp-toolkit-integration.json); Folgefehler und noch offene Runtime-/UI-/Starterprüfungen sind gesondert erfasst.
