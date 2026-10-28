---
type: Playbook
title: Nächste City-Builder-Bausteine
description: Die geprüften Foundations-Grundlagen von späteren Skalierungs-, Bauarbeits- und Produktionsaufgaben unterscheiden.
status: draft
tags: [shaderworld, citylab, city-builder, roadmap]
engine_version: "5.8.4"
plugin_version: "4.1"
generated: { by: codex/gpt-6, at: "2026-10-28T19:29:12Z" }
evidence_scope: Neue Baustellen-/Navigationssuite mit 22 nativen Tests bestanden; gerenderte Navigation 11/11; Baugrubenabschluss in zwei cooked Prozessen mit 14/14 und 15/15 Checks bestanden; normale PIE-Schaltflächen, voller Puffer, Stop/Play-Restore und Save-Abweisung mit Autosave-Schutz begrenzt geprüft; isolierter cooked Rodungsbenchmark mit acht CPU-Messfenstern bestanden, keine GPU-/FPS-Leistungszusage. Aktuelle Black-/Zero-Flow-Fassung uncooked und cooked mit je 29/29 und 12/12 Checks geprüft; normale kompilierte PIE-Paintbedienung mit Speichern/Laden und geschütztem Grundstück sichtbar geprüft. Keine separate verpackte Foundations-Pixelabnahme, vollständige Tastatur-/Fokusabnahme oder Cook-Abnahme anderer Karten.
sources:
  - id: fill-cycle
    resource: ../guides/closed-material-cycle.md
    title: Geschlossener Materialkreislauf und neuer Prüfstand mit 29 nativen Tests
  - id: construction-lab
    resource: ../guides/construction-lab.md
    title: Getrenntes Baugrubenlabor mit Baustellenmodell und begrenztem cooked Neustartabschluss
  - id: construction-proof
    resource: ../evidence/construction-lab-test.json
    title: 22 finale native Tests, cooked Baugrubenkreislauf und begrenzte normale PIE-Bedien-/Speicherproben
  - id: navigation-proof
    resource: ../evidence/terrain-navigation-test.json
    title: Gerenderte Gelände-/Bürgerprobe mit elf bestandenen Checks und ausdrücklichem Harness-Warteumfang
  - id: clearing-benchmark
    resource: ../evidence/clearing-performance-test.json
    title: Isolierter cooked 0/1/10/100-Record-Benchmark mit synchronen CPU-Aufrufzeiten und expliziten Grenzen
  - id: tree-clearing
    resource: ../evidence/tree-clearing-test.json
    title: Neue Baumkorrektur mit Code-/cooked Datenprüfungen und getrenntem normalem PIE-Backendbild
  - id: verification
    resource: ../verification.md
    title: Prüfstand und getrennte Abnahmen
  - id: foundations
    resource: ../guides/foundations-lab.md
    title: Aktueller Backendstand, historische Paintfehler und abgegrenzte native/PIE-Nachweise
  - id: build-controls
    resource: ../guides/build-controls.md
    title: Geprüfte Kamera-/Werkzeugleiste mit getrennten offenen Langbedienungsgrenzen
  - id: loop
    resource: ../guides/city-builder-loop.md
    title: Bestehende Stadtspielschleife mit eigenem Neustartnachweis
  - id: construction
    resource: construction-and-terrain-architecture.md
    title: Nutzerdesign und vorgeschlagener Maschinen-/Materialkreislauf
  - id: capabilities
    resource: versions-and-capabilities.md
    title: Pluginfähigkeiten und Bookkeeping-Grenze
  - id: tunnel
    resource: ../guides/reusable-tunnel-component.md
    title: Vorhandene trockene Tunnelkomponente
---
# Nächste City-Builder-Bausteine

Foundations besitzt Planwerkzeuge, fünf Biomprofile und Einzelrodungszustände. **Die Black-/Zero-Flow-Grundlage bestand je 29/29 und 12/12 Checks in zwei frischen uncooked und zwei frischen cooked Prozessen.** Die gesonderte Baumkorrektur ergänzte zwölf native Tests, erneute cooked Datenprozesse und getrennte normale PIE-Backendbilder; der Nutzer bestätigte anschließend die ausprobierte korrigierte Rodung; Vorschau-/Fokusdetails bleiben separat offen.[^tree-clearing] Im normalen PIE blieb Snow nach T/F6/K/L sichtbar; das geschützte Grundstück blieb Sand und ohne nachgewachsenen Bewuchs im Bild. Frühere Spline-NoGrowth- und White-Datamap-Fehler sind getrennt dokumentiert. Diese Ergebnisse sind keine Cook-Abnahme anderer Karten und kein Großwelt- oder Leistungsnachweis.[^foundations]

## Vorhandene Grundlagen und aktueller Testbedarf

| Baustein | Stand | Noch offen |
| --- | --- | --- |
| Kamera und Werkzeugleiste | Frühere elf native Tests, normale Slider-/Fokus-/Planbestätigung, Esc-Abbruch, Bauplatzvorschau, PIE-Preferences-Restore und finale lesbare Leiste belegt; verpackte Regression nach finalem Layoutbuild mit 29/29 und 12/12 Checks bestanden | Längere reale WASD/Shift/RMB-/Alt-Tab-Bedienung, persönliche Paket-Persistenz und neuer Paket-Pixeltest offen; Straßenentwurf teilweise Fixture[^build-controls] |
| Bestehendes CityLoop | Straße, gerodetes Grundstück, Haus und Bürger; erneute Format-4-Regression mit 24 Checks in drei frischen Prozessen | Allgemeine Stadtnavigation und Maschinen-/Materialwirtschaft |
| Fünf eigene Biome | Wald, Wiese, Fels, Strand, Meeresboden; fünf Profile und 19 Assets nach gespeichertem Kartenneuladen zurückgelesen | Alle sichtbaren Biomgrenzen und größere Welt; Meeresboden verwendet vorhandene Felsen statt neuer Meeresflora |
| Einzelrodung | Neue Builds und zwölf native Tests erfolgreich; Ray-/Meshbox-Geometrie geprüft, markierte Zielkrone nach Backendrodung und erneutem Backendladen im normalen PIE weg, blauer Kontrollbaum erhalten | Korrigierte Rodung vom Nutzer ausprobiert und bestätigt; gelbe Vorschau/Fokusdetails nicht gesondert bestätigt. Backendbilder sind keine C-Eingabeaufzeichnung oder Paket-Pixelabnahme. Kollisionsnachlauf, Reichweitenfahrt, viele Rodungen und Erträge offen[^tree-clearing] |
| Planwerkzeuge | Anheben/Absenken/Ebnen/Material; inerte Planung und Wiederherstellung geprüft; frühere acht Foundations-Tests erfolgreich, damalige Suite einschließlich Raygeometrie insgesamt zwölf; damalige Gesamtsuite mit Baustellen-/Navigationstests 22 | Vollständige Eingabenrunde und Stadtsimulation; normale geprüfte T/F6/K/L-Paintbedienung ist ein begrenzter Ausschnitt |
| Materialmalerei | Quadratischer Black-Zero-Flow-Brush; native Kern-/Seitenmasken bleiben nach Paint, Regeneration und Laden frei; Snow nach normalem PIE-Laden sichtbar, geschütztes Grundstück bleibt Sand | Separate verpackte Pixelabnahme; Maskentestactors werden je Prozess neu erzeugt |
| Verpacktes Spiel | Nach Baumkorrektur mit bestehenden cooked Assets neu verpackt; zwei neue cooked Prozesse mit 29/29 und 12/12 Checks in 120,5/70,8 s | Separate verpackte Pixel-/Bedienabnahme und größere Last |
| Neues ConstructionLab | Zwei frische cooked Prozesse bestanden 14/14 und 15/15 Checks in 24,7/113,8 s; vier Arbeitszellen, 18-t-Puffer/12-t-Laster/500-t-Lager, eigener Slot und Format 5; Abschluss mit exakt 172,8 t im Lager, Rest/Puffer/Laster leer und 0 g Modellbilanzfehler | Lokales 5-cm-/Drei-Pass-Höhengate; normale Schaltflächen-/Puffer-/Restore-/Autosave-Proben und vier Standbilder zusätzlich geprüft. Kein unabhängiges Meshvolumen, vollständiger korrigierter uncooked Pair oder allgemeiner Tastatur-/Fokus-/Pixelvergleich[^construction-lab][^construction-proof] |
| Geländeänderung vor laufendem Bürger | Gerenderter uncooked Versuch mit 11/11 Checks in 40,9 s: tatsächliche Grube, sicheres Warten, Reparatur und Ankunft desselben Bürgers | Harness hielt nach dem transienten Managergate zehn weitere Ticks bewusst an; keine allgemeine Produktions-Fertigmeldung oder NavMesh-Abnahme[^navigation-proof] |
| Damalige native Logik-/API-Suite | Nach letztem Initialisierungsfix 22/22 in 0,357 s erfolgreich, 20 ohne und zwei mit bekannten Warnungen, 0 fehlgeschlagen | NullRHI; getrennt vom bestandenen cooked Baugrubenabschluss und kein Ersatz für normale Bedienung oder Spielbilder[^construction-proof] |

Die getrennte Karte **`/Game/Maps/ShaderWorldFoundations`** verwendet den Slot **CityLabFoundations**. CityLoop und sein Slot bleiben erhalten. Die frühere Acht-Test-Suite wurde zunächst für Kamera/Toolbar und Raygeometrie auf zwölf und jetzt mit Baustellen-/Navigationstests auf 22 erfolgreiche native Tests erweitert; diese ersetzen weder sämtliche Tastatur-/Mausabläufe noch verpackte Pixelprüfungen.[^loop][^foundations]

**Aktueller Ausbau:** Der [geschlossene Materialkreislauf](../guides/closed-material-cycle.md) ergänzt eine zweite Baustelle mit Lager-Lkw und Zielpuffer. 29/29 native Tests sowie uncooked und cooked je zwei Prozessstarts mit 6/6 und 10/10 Checks bestanden: 172,8 t vollständig wieder eingebaut, 0 g Bilanzfehler, identischer gespeicherter Zwischenstand und drei weitere Loads. Freie Auftragswahl, mehrere konkurrierende Fahrzeuge, Verkehr, Verdichtung und Großweltleistung bleiben offen. Die älteren Zahlen oben sind historische Teilnachweise.

## Abgeschlossen: Paintwirkung und normale Bedienung im geprüften Umfang

Der alte Paintbackend verwendete eine R-only-Spline. In einer normalen PIE-Probe wurde ein Hausgrundstück weiß, während Bäume und Gras im bemalten Bereich zurückkehrten. Der native Straßen-Layer-Pass wählte einen einzigen Road-Gewinner für alle Kanäle; dadurch wurde die NoGrowth-Maske verdrängt. Der Fehler lag nicht an einer falschen Biomkanalwahl im Dichtematerial.

Der neue `USW_LayerMaskBrushComponent` läuft vor dem strukturellen Road-/Pad-Pass. Seine Größe definiert den quadratischen Wirkbereich: 8 m bedeutet eine halbe Kantenlänge von 8 m, insgesamt 16 × 16 m. **Engine Black** ist ein konstanter Zero-Flow-Selektor, keine Flächenmaske. White wählte den deaktivierten Flow-Zweig und erzeugte keinen sichtbaren Snow-Auftrag; beide aktuellen Neustartprüfungen verlangen deshalb ausdrücklich Black. Straßen-/Pad-Material und NoGrowth haben in Kern **und** Seitenbereichen Vorrang. Uncooked und cooked blieben die geprüften NoGrowth-Bereiche nach Paint, echter Regeneration und je drei Loads frei. Die native Testmaske wird je Prozess neu erzeugt; dies beweist keine beliebige zusätzliche Maskenactorpersistenz. Die finale normale PIE-Probe bestätigte die kompilierte Fassung mit sichtbarem Snow nach Speichern und Laden sowie unverändert sandigem, bewuchsfreiem Grundstück im Bild.[^foundations]

Eine normale PIE-Probe bestätigte inerte Planung aus etwa 5 km Höhe, neun Bodenproben mit vier stabilen Durchläufen, Undo, getrennte Planauswahl und absolute Zielhöhe nach PIE-Neustart. Die aktuelle kompilierte Paintfassung bestand normale T/F6/K/L-Eingaben ohne nachträgliche Brushparameteränderung und einen qualitativen GPU-Sichtvergleich. Das ersetzt keine vollständige Tasten-/Mausprüfung oder gesonderte verpackte Pixelabnahme.[^foundations]

## Nach Kamera/Toolbar: begrenzte Bauarbeit statt sofortiger Weltvergrößerung

Die neue [Bedienfassung](../guides/build-controls.md) besitzt erste reale Eingabe-/Restore-Nachweise mit getrennten Plan-/Debugaktionen. Finale Leistenaufnahme und abgegrenzte Esc-/Straßenentwurfs-/Bauplatzproben sind geprüft. Die verpackte Regression bestand auch nach dem finalen Layoutbuild. Längere reale Kamerabedienung, persönliche Einstellungen im neuen Paketprozess und ein neuer Paket-Pixeltest bleiben getrennte offene Schritte. Danach ist folgende Reihenfolge ein Vorschlag, keine bereits implementierte Produktionsfunktion:[^build-controls][^construction]

1. **Gemessene Rodungshotpaths begrenzen:** Der neue isolierte cooked 0/1/10/100-Record-Benchmark ist bestanden. Schon ein Record löst den Vollscan von 154997 Slots aus; die native Rayabfrage kostet auch ohne Rodungsrecords rund 21 ms. Zuerst Live-/Raumindex oder sichere versionierte Publish-Snapshots und Poolfilter untersuchen, danach konservative Broadphase für die Rayboxen. Vor dem Weglassen des visuellen Nachlaufs Restore-/Regenerations-/Kollisionsverträge klären. **Keine dieser Optimierungen ist eingebaut.** Nutzerbestätigung der korrigierten Rodung und offene Vorschau-/Fokusdetails bleiben getrennt.[^clearing-benchmark]
2. **Den kleinen Kreislauf gegen weitere Bedienrandfälle absichern:** [ConstructionLab](../guides/construction-lab.md) bestand vollständigen cooked Aushub/Abtransport sowie getrennte normale Schaltflächen-, Puffer-, Stop/Play- und Autosave-Schutzproben. Tastatur-/Fokusvarianten bleiben offen; die F5-Injektion bestätigte keinen Callback. Das lokale 5-cm-/Drei-Pass-Gate, Kollisionsretry und reale Bodenproben vor Erweiterungen beibehalten. Planung bleibt inert; Mengen und Ist-Gelände folgen ausgeführter Arbeit.[^construction-proof]
3. **Den Rückweg vom Lager ins Gelände ergänzen:** Modell-, Höhen- und cooked Neustartnachweis sowie begrenzte normale Bedienproben sind für das kleine Labor bestanden. Als nächsten Funktionsversuch Aufschüttung aus geliefertem Material sowie mehrere Bauaufträge mit eigenen Bilanz-/Restore-Prüfungen ergänzen. Anschließend Last von vielen Rodungen, Straßen und Brushes messen. Freie Maschinenwegfindung und größere Welt bleiben eigene Arbeiten.

## Vor größerer Welt: die gemessenen Rodungskosten senken

Ein einzelner isolierter **cooked Development-Prozess** bestand alle **acht 8-s-Messfenster** für 0/1/10/100 Records mit und ohne native Rayabfrage. Andere Projektbuilds und Rendergames waren vorher geschlossen. Ohne Records kostet Reapply rund **0,001 ms** und besucht keine Slots. Mit **1 bis 100 Records** liegen die Aufrufmittel bei **19,85–22,06 ms**, p95 bei **23,44–44,43 ms**. Die native Rayabfrage kostet bereits ohne Records rund **21,02 ms**, über alle vier Rayfenster **20,43–21,02 ms** pro Aufruf. Die tatsächlich erreichte Rayrate lag bei **4,74–4,85 Hz**.[^clearing-benchmark]

Wichtig ist die Unterscheidung zwischen **Slots und lebenden Bäumen**: Der visuelle Pool hatte **152881 Slots**, aber zunächst nur **1410 nicht-null skalierte Instanzen**; zusätzlich gab es 2116 Kollisionsslots. Reapply besuchte bei jeder positiven Recordzahl alle **154997 Slots in zwei Pools**. Das spricht für die Untersuchung von vollständigen Pufferkopien und -durchläufen; eine Aufteilung der Kosten auf Kopie, Transformzerlegung, Ledger- und Boxtest wurde nicht gemessen. Eine reine Ray-Broadphase beseitigt die vorgelagerte Kopie und Suche durch leere Slots noch nicht.

Die 100 entfernten Ressourcen blieben in den Messfenstern auf CPU-Seite visuell und kollisionsseitig entfernt, die Kontrolle bei **1/1** mit gleichem Transform. Nach dem Versuch verlangte der Erfolgsgate die Rückkehr aller **101 ausgewählten visuellen Ressourcen** und der Kontrolltransformation. Keine normalen Stadtspielstände wurden angesprochen. Das sind CPU- und Isolationsnachweise; keine neue Bildprüfung oder vollständige Kollisions-Restore-Abnahme. Renderrefreshkosten lagen außerhalb der stationären Messfenster.[^clearing-benchmark]

Die Zeiten messen synchrone Game-Thread-Aufrufe. Gerenderte Tickintervalle wurden unter **t.MaxFPS = 48** beobachtet; daraus werden weder GPU-Zeit noch erreichbare FPS abgeleitet. Der erste fehlgeschlagene Ground-Klassennameversuch lieferte vor dieser korrigierten Messung keine Werte. Frühere Verifier-Stichproben von bis zu 153939 Slots und ein Maximum bei gleichzeitigem C++-Build bleiben historische Scandiagnosen, keine zusätzlichen Benchmarkwiederholungen.[^foundations][^clearing-benchmark]

**Nächster Optimierungsschritt:** Live-Instanzen räumlich indizieren beziehungsweise einen sicher invalidierten Publikationsstand auswerten, unnötige volle Pooldurchläufe vermeiden und konservativ vor dem exakten Ray-Box-Test eingrenzen. Vor dem Überspringen periodischer visueller Scans muss der Vertrag externer nativer `RestoreInstance`-Aufrufe geklärt werden: Sie können Transforms außerhalb der Publishfilter verändern. Initiales Räumen, älterer Restore, Indexwechsel, Regeneration und Kollisionsnachlauf müssen erhalten bleiben. Danach denselben begrenzten Benchmark erneut ausführen; erst anschließend Welt und Zahl der Baustellen erhöhen. **Es wird noch keine Leistungsverbesserung behauptet.**

## Danach erhaltene Themen

| Thema | Geplantes Ergebnis | Abnahmeidee |
| --- | --- | --- |
| Ressourcenwirtschaft und Rekultivierung | Erträge, Arbeit und Neubepflanzung auf Einzelzuständen aufbauen | Mengen ohne doppelte Erträge, Wiederherstellung und gezielte Rücknahme |
| Vollständiger platzierbarer Tunnel | Tunnelkörper, Kollision, Öffnungen und Air Pocket gemeinsam verwalten | Platzieren, speichern, durchfahren und im Ozeaneinfluss trocken prüfen |
| Bauaufträge nachbearbeiten | Ungearbeitete Planung ändern; ausgeführte Arbeit über Gegen-/Rückbauaufträge behandeln | Teilbau, Mengen und Planrevision nach Neustart vergleichen |
| Allgemeine Navigation | Gültige Wege nach Straßen-, Gelände- und Gebäudeänderungen | Erreichbare und blockierte Ziele sowie dynamische NavMesh-Aktualisierung |
| Größere Welt | Viele Trassen und Brushes mit begrenzten Kosten | Framezeit, Speicher, Spielstandgröße und anschließend Streaming |
| Wasser, Auftrieb und Häfen | Belastbare Informationen für Schiffe und Küstenbauten | Definierte Physikobjekte, Wellenzustände und Küsten-/Tunnelbereiche |

Die eigene Ressourcenverwaltung ergänzt die [Plugin-Bookkeeping-Grenze](versions-and-capabilities.md#biome-und-vegetation-für-die-stadt). Sie ist ein anderer Vorgang als flächige NoGrowth-Maskierung. Lokale Korridorabfragen ersetzen weiterhin keine allgemeine Navigation.[^capabilities][^foundations][^tunnel]

## Spätere Bauwelt: Maschinenarbeit mit Materialbilanz

Die bestätigte Richtung bleibt: **Soll-Gelände planen, durch Arbeit am Ort das Ist-Gelände ändern und Aushub als Ressource erhalten.** Planung allein verändert und rodet nichts. F6 und C bleiben ausdrückliche Soforteingriffe des Labors. Ein erster eigener Baugrubenversuch implementiert jetzt Arbeitsraten und Materialkonten; eine vollständige Produktionswirtschaft, Holzgewinnung und freie Maschinenaufträge fehlen weiter.[^construction]

Das [ConstructionLab](../guides/construction-lab.md) ist der erste eigene kleine Arbeitsversuch, kein fertiges allgemeines Baustellensystem: **2 × 2 Zellen à 400 cm**, bis zur normalen Endtiefe von **150 cm**, analytisch **96 m³/172,8 t** bei den ausdrücklich angenommenen Dichten. Es verwendet den getrennten Slot **CityLabConstruction**, schreibt **Format 5** und hält Massen in ganzen Gramm. **18 t Puffer, 12 t Laster und 500 t Lager** begrenzen den Kreislauf; Planung ist pausiert und transportlos. Der vollständige Abschluss nach cooked Prozessneustart ist bestanden: exakt **172800000 g im Lager**, **0 g Restboden/Puffer/Laster und Modellbilanzfehler**. Vollständiger Modellhash und drei wiederholte Loads stimmten vor dem Weiterarbeiten überein. Die reale Endoberfläche wich maximal **2,000778 cm** vom 150-cm-Modellziel ab, bei **5 cm Toleranz**, **neun Punkten × drei stabilen Durchläufen**, **100 cm Kollisionsauflösung/129 Vertices je Patch**. Exakte Modellgramm sind keine unabhängig integrierte Masse des quantisierten Meshvolumens. Der frühere uncooked Versuch mit 2-cm-Gate endete im Kollisionswarte-Timeout; er bleibt als historischer Fehlversuch erhalten. Die normale Vorschau bestätigte einen automatisch gespeicherten pausierten Nullplan und reale Arbeit-/Transport-/Pauseaktionen. Bei Transport aus blieben 18-t-Puffer und Zellhöhen über weitere 57 Takte gleich; der pausierte **60-t-Stand = 12 t Puffer + 12 t Lkw + 36 t Lager** kam nach Stop/Play vollständig identisch und mit passender Kollision zurück. Ein absichtlich fremdgebundener Save blieb nach Abweisung über das Autosave-Zeitfenster bytegleich; danach wurde der gültige Stand wiederhergestellt. Vier native Standbilder sind visuell geprüft, keine pauschale menschliche Tastatur-/Fokusabnahme oder automatischer Pixelvergleich behauptet. Wiederverwendung für Aufschüttungen ist noch ein Folgeschritt.[^construction-lab][^construction-proof]

Ein eigener früher 3D-Untergrundversuch bleibt nötig: Höhenfeld und Portalöffnungen beweisen weder frei ausgrabbares Erdreich noch TBM-Vortrieb. Die unterirdische Geometrie und Kollision benötigen einen eigenen Machbarkeitsnachweis.[^construction]

[^verification]: [Tatsächlicher Prüfstand](../verification.md).
[^foundations]: [Foundations: aktuelle Anleitung und Prüfgrenzen](../guides/foundations-lab.md).
[^build-controls]: [Neue Baukamera und Werkzeugleiste: aktueller Entwurf und ausstehende Abnahmen](../guides/build-controls.md).
[^loop]: [Bestehende CityLoop-Spielschleife](../guides/city-builder-loop.md).
[^construction]: [Zielarchitektur für Bauarbeit und Material](construction-and-terrain-architecture.md).
[^capabilities]: [Pluginfähigkeiten und Grenzen](versions-and-capabilities.md).
[^tunnel]: [Vorhandene trockene Tunnelkomponente](../guides/reusable-tunnel-component.md).

[^tree-clearing]: [Bereinigter Rodungsbericht](../evidence/tree-clearing-test.json): zwölf native Tests und cooked Datenprüfung bestanden; Backend-Bilder mit erneutem Laden und nachträgliche Nutzerbestätigung der ausprobierten korrigierten Rodung; gelbe Vorschau/Fokusdetails bleiben separat offen.

[^construction-lab]: [Baugrube, Testbagger und Materialkreislauf](../guides/construction-lab.md), begrenztes eigenes Labor mit getrenntem Slot.
[^construction-proof]: [Bereinigter Baugrubenbericht](../evidence/construction-lab-test.json): 22 native Tests sowie cooked Create 14/14 in 24,705998 s und Resume 15/15 in 113,845061 s; exakte Modellbilanz und begrenzter physischer Höhennachweis. Historischer 2-cm-Fehlversuch bleibt separat.
[^navigation-proof]: [Gerenderter Navigationsbericht](../evidence/terrain-navigation-test.json): 11/11 Checks mit tatsächlichen Höhen; zusätzliche bewusste Harness-Wartezeit bleibt Teil des Nachweises.
[^clearing-benchmark]: [Bereinigter CPU-Rodungsbenchmark](../evidence/clearing-performance-test.json): acht cooked Messfenster, echte Slot-/Livezahlen und vollständiger visueller CPU-Restore; explizit kein GPU-/FPS-Leistungsnachweis.
