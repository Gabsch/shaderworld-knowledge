---
type: Playbook
title: Nächste City-Builder-Bausteine
description: Die geprüften Foundations-Grundlagen von späteren Skalierungs-, Bauarbeits- und Produktionsaufgaben unterscheiden.
status: draft
tags: [shaderworld, citylab, city-builder, roadmap]
engine_version: "5.8.4"
plugin_version: "4.1"
generated: { by: codex/gpt-6, at: "2026-10-28T16:15:52Z" }
evidence_scope: Aktuelle Black-/Zero-Flow-Fassung uncooked und cooked mit je 29/29 und 12/12 Checks geprüft; normale kompilierte PIE-Paintbedienung mit Speichern/Laden und geschütztem Grundstück sichtbar geprüft. Keine separate verpackte Pixelabnahme oder Cook-Abnahme anderer Karten.
sources:
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

Foundations besitzt Planwerkzeuge, fünf Biomprofile und Einzelrodungszustände. **Die aktuelle Black-/Zero-Flow-Fassung bestand je 29/29 und 12/12 Checks in zwei frischen uncooked und zwei frischen cooked Prozessen.** Im normalen PIE blieb Snow nach T/F6/K/L sichtbar; das geschützte Grundstück blieb Sand und ohne nachgewachsenen Bewuchs im Bild. Frühere Spline-NoGrowth- und White-Datamap-Fehler sind getrennt dokumentiert. Diese Ergebnisse sind keine Cook-Abnahme anderer Karten und kein Großwelt- oder Leistungsnachweis.[^foundations]

## Vorhandene Grundlagen und aktueller Testbedarf

| Baustein | Stand | Noch offen |
| --- | --- | --- |
| Kamera und Werkzeugleiste | Elf native Tests, normale Slider-/Fokus-/Planbestätigung, Esc-Abbruch, Bauplatzvorschau, PIE-Preferences-Restore und finale lesbare Leiste belegt; verpackte Regression nach finalem Layoutbuild mit 29/29 und 12/12 Checks bestanden | Längere reale WASD/Shift/RMB-/Alt-Tab-Bedienung, persönliche Paket-Persistenz und neuer Paket-Pixeltest offen; Straßenentwurf teilweise Fixture[^build-controls] |
| Bestehendes CityLoop | Straße, gerodetes Grundstück, Haus und Bürger; erneute Format-4-Regression mit 24 Checks in drei frischen Prozessen | Allgemeine Stadtnavigation und Maschinen-/Materialwirtschaft |
| Fünf eigene Biome | Wald, Wiese, Fels, Strand, Meeresboden; fünf Profile und 19 Assets nach gespeichertem Kartenneuladen zurückgelesen | Alle sichtbaren Biomgrenzen und größere Welt; Meeresboden verwendet vorhandene Felsen statt neuer Meeresflora |
| Einzelrodung | Stabile Ressourcenkennung; früherer ausgewählter Baum nach echter Regeneration und Neustart entfernt, Kontrollbaum erhalten | Produktionsgrenze des Kollisionsnachlaufs, Reichweitenfahrt, viele Rodungen, Erträge und Rekultivierung |
| Planwerkzeuge | Anheben/Absenken/Ebnen/Material; inerte Planung und Wiederherstellung geprüft; frühere acht Foundations-Tests erfolgreich, neue Bedien-Suite insgesamt elf | Vollständige Eingabenrunde und Stadtsimulation; normale geprüfte T/F6/K/L-Paintbedienung ist ein begrenzter Ausschnitt |
| Materialmalerei | Quadratischer Black-Zero-Flow-Brush; native Kern-/Seitenmasken bleiben nach Paint, Regeneration und Laden frei; Snow nach normalem PIE-Laden sichtbar, geschütztes Grundstück bleibt Sand | Separate verpackte Pixelabnahme; Maskentestactors werden je Prozess neu erzeugt |
| Verpacktes Spiel | Aktuelle Fassung mit Cook/Stage und zwei echten cooked Prozessen geprüft; 29/29 und 12/12 Checks | Separate verpackte Pixel-/Bedienabnahme und größere Last |

Die getrennte Karte **`/Game/Maps/ShaderWorldFoundations`** verwendet den Slot **CityLabFoundations**. CityLoop und sein Slot bleiben erhalten. Die bisherige Acht-Test-Suite wurde für Kamera/Toolbar auf elf erfolgreiche native Tests erweitert; diese ersetzen weder sämtliche Tastatur-/Mausabläufe noch verpackte Pixelprüfungen.[^loop][^foundations]

## Abgeschlossen: Paintwirkung und normale Bedienung im geprüften Umfang

Der alte Paintbackend verwendete eine R-only-Spline. In einer normalen PIE-Probe wurde ein Hausgrundstück weiß, während Bäume und Gras im bemalten Bereich zurückkehrten. Der native Straßen-Layer-Pass wählte einen einzigen Road-Gewinner für alle Kanäle; dadurch wurde die NoGrowth-Maske verdrängt. Der Fehler lag nicht an einer falschen Biomkanalwahl im Dichtematerial.

Der neue `USW_LayerMaskBrushComponent` läuft vor dem strukturellen Road-/Pad-Pass. Seine Größe definiert den quadratischen Wirkbereich: 8 m bedeutet eine halbe Kantenlänge von 8 m, insgesamt 16 × 16 m. **Engine Black** ist ein konstanter Zero-Flow-Selektor, keine Flächenmaske. White wählte den deaktivierten Flow-Zweig und erzeugte keinen sichtbaren Snow-Auftrag; beide aktuellen Neustartprüfungen verlangen deshalb ausdrücklich Black. Straßen-/Pad-Material und NoGrowth haben in Kern **und** Seitenbereichen Vorrang. Uncooked und cooked blieben die geprüften NoGrowth-Bereiche nach Paint, echter Regeneration und je drei Loads frei. Die native Testmaske wird je Prozess neu erzeugt; dies beweist keine beliebige zusätzliche Maskenactorpersistenz. Die finale normale PIE-Probe bestätigte die kompilierte Fassung mit sichtbarem Snow nach Speichern und Laden sowie unverändert sandigem, bewuchsfreiem Grundstück im Bild.[^foundations]

Eine normale PIE-Probe bestätigte inerte Planung aus etwa 5 km Höhe, neun Bodenproben mit vier stabilen Durchläufen, Undo, getrennte Planauswahl und absolute Zielhöhe nach PIE-Neustart. Die aktuelle kompilierte Paintfassung bestand normale T/F6/K/L-Eingaben ohne nachträgliche Brushparameteränderung und einen qualitativen GPU-Sichtvergleich. Das ersetzt keine vollständige Tasten-/Mausprüfung oder gesonderte verpackte Pixelabnahme.[^foundations]

## Nach Kamera/Toolbar: begrenzte Bauarbeit statt sofortiger Weltvergrößerung

Die neue [Bedienfassung](../guides/build-controls.md) besitzt erste reale Eingabe-/Restore-Nachweise mit getrennten Plan-/Debugaktionen. Finale Leistenaufnahme und abgegrenzte Esc-/Straßenentwurfs-/Bauplatzproben sind geprüft. Die verpackte Regression bestand auch nach dem finalen Layoutbuild. Längere reale Kamerabedienung, persönliche Einstellungen im neuen Paketprozess und ein neuer Paket-Pixeltest bleiben getrennte offene Schritte. Danach ist folgende Reihenfolge ein Vorschlag, keine bereits implementierte Produktionsfunktion:[^build-controls][^construction]

1. **Ressourcenverwaltung absichern:** Den externen Restore-Vertrag und den Kollisionsnachlauf klären, dann visuelle Vollscans begrenzen. Initiale Rodung, Laden älterer Zustände, Indexwechsel und Kontrollbestand müssen korrekt bleiben.
2. **Kleinen Arbeits-/Materialkreislauf bauen:** Eine begrenzte Baugrube mit Baggerplatzhalter, erreichbaren Arbeitsschritten, endlichem Puffer, Transport auf vorgegebener Route, Lager und anschließender Aufschüttung. Planung bleibt inert; nur ausgeführte Arbeit verändert Ist-Gelände und Materialkonten gemeinsam. Dichten, Rasterung, Arbeitsraten und Bilanzierung sind noch zu entwerfen.
3. **Den halbfertigen Zustand neu starten:** Mit gefülltem Puffer oder beladenem Fahrzeug speichern und in einem neuen Prozess fortsetzen; mehrfaches Laden darf weder Masse noch Arbeitsschritte verdoppeln. Erst danach die Menge an Bauflächen, Rodungen und Brushes mit gemessenen Kosten erhöhen.

## Vor größerer Welt: den Rodungsnachlauf reduzieren

Die aktuelle Black-uncooked-Probe erfasst 55 Samples über 30,04 s. Der zuletzt gemeldete Rodungsscan kostete 0,9/15,9/39,4 ms (Minimum/Stichprobenmittel/Maximum) bei bis zu 153939 Instanzen. Die 56 cooked Samples über 30,25 s ergaben 2,6/15,2/23,1 ms. Der Verifier scannt zusätzlich selbst. Eine frühere Messung mit parallelem C++-Build hatte 177,9 ms Maximum. Diese Werte sind einzelne Scandiagnosen, keine vollständigen Framezeiten oder FPS-/Großweltbenchmarks.[^foundations]

Vor dem Überspringen periodischer visueller Vollscans muss der Vertrag für externe native `RestoreInstance`-Aufrufe geklärt werden: Sie können einen visuellen Transform außerhalb der Publishfilter ändern. Initiales Räumen, älterer Restore, Indexwechsel und Kollisionsnachlauf müssen erhalten bleiben. Diese Optimierung ist nicht eingebaut. Erst anschließend viele Rodungen, Straßen und Brushes sowie Speicher und Spielstandgröße belasten.

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

Die bestätigte Richtung bleibt: **Soll-Gelände planen, durch Arbeit am Ort das Ist-Gelände ändern und Aushub als Ressource erhalten.** Planung allein verändert und rodet nichts. F6 und C bleiben ausdrückliche Soforteingriffe des Labors. Maschinen, Arbeitsraten, Holz-/Aushuberträge und Materialkonten fehlen.[^construction]

Nach den Grundlagenprüfungen folgt als vorgeschlagener Versuch eine kleine Baugrube mit Baggerplatzhalter, begrenztem Puffer, Abtransport und Wiederverwendung. Volle Kapazität stoppt die Arbeit; ein Neustart mitten im Aushub prüft Geometrie, Mengen und Fortschritt gemeinsam. Dieser Kreislauf ist noch nicht implementiert.

Ein eigener früher 3D-Untergrundversuch bleibt nötig: Höhenfeld und Portalöffnungen beweisen weder frei ausgrabbares Erdreich noch TBM-Vortrieb. Die unterirdische Geometrie und Kollision benötigen einen eigenen Machbarkeitsnachweis.[^construction]

[^verification]: [Tatsächlicher Prüfstand](../verification.md).
[^foundations]: [Foundations: aktuelle Anleitung und Prüfgrenzen](../guides/foundations-lab.md).
[^build-controls]: [Neue Baukamera und Werkzeugleiste: aktueller Entwurf und ausstehende Abnahmen](../guides/build-controls.md).
[^loop]: [Bestehende CityLoop-Spielschleife](../guides/city-builder-loop.md).
[^construction]: [Zielarchitektur für Bauarbeit und Material](construction-and-terrain-architecture.md).
[^capabilities]: [Pluginfähigkeiten und Grenzen](versions-and-capabilities.md).
[^tunnel]: [Vorhandene trockene Tunnelkomponente](../guides/reusable-tunnel-component.md).
