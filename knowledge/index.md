---
okf_version: "0.2"
---

# ShaderWorld für den City Builder lernen

Diese Wissensbasis begleitet konkrete Editor-Versuche mit Unreal **5.8.4** und ShaderWorld **4.1**. Beginne mit Einrichtung und Beispielwelten. Danach kannst du einzelne Rezepte unabhängig durcharbeiten.

## Einstieg

- [Terrain und Kollision einrichten](guides/setup-terrain.md) – eine flache Welt anzeigen und begehbaren Boden vorbereiten.
- [Beispielwelten vergleichen](reference/example-maps.md) – Reference, Heightmap und OceanOnly finden und sinnvoll nutzen.
- [Fehler gezielt eingrenzen](guides/troubleshooting.md) – Projektzuordnung und Konvertierungsdialog, leere Vorschau, fehlende Kollision, Lumen-Meldung und ausbleibender Schaum.

## Ausprobieren und bauen

- [Grundstück durch Rodung und Erdarbeit vorbereiten](guides/site-preparation.md) – Slice C mit Rodung vor Erdarbeit und Hausfreigabe in getrennter SitePreparation-V2-Map/eigenem Slot; explizite Biomregeln, Legacywelt erhalten, V2-Uncooked- und Cooked-Neustarts bestanden; versiegelte Demo vorbereitet, sichtbarer Start noch offen.

- [Unebenen Boden durch Maschinen ebnen](guides/flatten-machine-earthworks.md) – begrenzter Slice B stable: 52 native Tests, Uncooked/frisches Development-Cooked je 12/12 + 16/16, Controller-API 15/15 und sichtbare getrennte Demo mit Slate-Bild bestanden. Physische Eingaben und menschliche Prüfung nicht erfolgt.
- [Anheben und Absenken durch Maschinen](guides/machine-earthworks.md) – mehrere gespeicherte Pläne, gemeinsames Lager und ein Maschinenzug; 46 native Tests und je zwei uncooked/verpackte Kreislaufprozesse bestanden, 86,4 t und 0 g. Normale Controller-APIs und kalter Queue-Restore geprüft; physische Eingaben bleiben offen.
- [Untergrundansicht bedienen](guides/underground-view.md) – Oberfläche, schematischer Schnitt und Innenraum als getrennte Darstellung; vier frühere Editorbilder, lokale Kollisionsinvarianz und Kamerarückkehr geprüft; freie Kamera und Schnittfenster über aktuelle gemeinsame APIs/Editorbilder erneut auf EarthworksLab geprüft; normale V2-Demo vorbereitet. Physische Eingaben und verpackte Schnitt-/Innenraumpixel offen.

- [Kostenlose Fahrzeugassets prüfen](guides/vehicle-asset-evaluation.md) – Liebherr, Radlader und Lkw mit neuen Democlips; gespeicherter Import, Einheiten, gerenderte Posen und SIE geprüft, Produktionsgrenzen offen.
- [Baustellen selbst planen](guides/construction-planner.md) – Grube/Aufschuettung mit Formvorschau, Mengen, ausdruecklichem Arbeitsstart und je vier gerenderten Neustartprozessen uncooked/cooked.
- [Rodungscache und Messgrenzen](guides/clearing-cache-and-performance.md) – weniger visuelle Instanzscans, stabile Baumkennungen und getrennte native/CityLab-Wiederherstellung.
- [Unterirdische Hybridkammer](guides/underground-hybrid-probe.md) – eigener Hohlraum unter unveraenderter Oberflaeche; getrennte Kollisions-/Neustartabnahme, kein freies 3D-Graben.

- [CityBasics: Insel, Wald, Berg und Tunnel](guides/city-basics-lab.md) – den farbigen Laboraufbau und den bodengebundenen Testbuggy verstehen.
- [Wind und Schaum einstellen](guides/ocean-waves-and-foam.md) – den Ozean von 10 auf 18 m/s Wind umstellen und Schaum sichtbar machen.
- [Bauplätze und Straßen verändern](guides/building-pads-and-roads.md) – die Lernkarte bedienen und Gelände, Material und Straßenmesh unterscheiden.
- [Vom Straßenbau zum bewohnten Testhaus](guides/city-builder-loop.md) – verbundene Spielschleife mit Grundstück, Haus, Bürger und bestandenem Drei-Prozess-Neustartnachweis.
- [Baukamera und Werkzeugleiste bedienen](guides/build-controls.md) – geprüfte Regler/Planbestätigung und neuer selektiver Baum-Kamerafilter mit 25/25 nativen Tests; bisherige Toolbar-/Restorebelege getrennt. Normales ConstructionLab-Wiederladen mit passendem Boden und Kamerapose zusätzlich belegt; physische Kameraeingaben und aktuelle cooked Kamerafahrt bleiben offen.
- [Foundations: planen, Biome und Einzelrodung](guides/foundations-lab.md) – aktuelle Black-/Zero-Flow-Fassung mit uncooked und verpacktem Neustartnachweis; sichtbares Snow nach normalem PIE-Laden und geschütztes Grundstück mit Bildern belegt; Rodungsfix mit separater Vorher-/Nachher-/Ladebildprobe, Rodung vom Nutzer nach dem Fix ausprobiert und bestätigt; gezielte Abnahme aller Vorschau-/Fokusfälle bleibt offen.
- [Baugrube, Testbagger und Materialkreislauf](guides/construction-lab.md) – schrittweise Erdarbeit mit 18-t-Puffer, 12-t-Lkw und eigenem Spielstand; cooked Neustart und Abschluss mit 172,8 t im Lager/0 g Modellbilanzfehler bestanden. Lokale Höhenprüfung, normale Erstplanung/Puffer/Transport und exaktes PIE-Wiederladen belegt; Tastatur-/Fokusfälle und Pixelvergleich bleiben begrenzt.
- [Aushub wieder einbauen: geschlossener Materialkreislauf](guides/closed-material-cycle.md) – zweiter Standort, Lager-Lkw und Zielpuffer; 29 native Tests, uncooked/cooked Neustart während beladener Fahrt und vollständiger Wiedereinbau mit 0 g Bilanzfehler bestanden.
- [Straßen zur Laufzeit bauen und speichern](guides/runtime-roads.md) – RoadLab mit gemeinsamer Terrain-/Mesh-Spline; Neustart, Kollision, Pflanzenursprünge und die POM-Nahsichtkorrektur verstehen.
- [Änderungen speichern und laden](guides/save-and-load.md) – unsere CityLab-Spielstände einschließlich eines echten Neustarts prüfen.
- [Löcher und Bergtunnel verstehen](guides/holes-and-mountain-tunnels.md) – Holebrush-Beispiele ansehen und einen Tunneleingang planen.
- [Tunnelkomponente mit eingebautem Wasserausschluss](guides/reusable-tunnel-component.md) – eigener Baustein mit bestandenen nativen API-Tests; gespeicherte Karte, neues PIE und frische Durchfahrt geprüft.

## Nachschlagen

- [Scaping als Maschinenaufträge: vereinbarter Ausbau](reference/scaping-machine-work-plan.md) – erster Anheben-/Absenken-Slice nativ, uncooked und verpackt geprüft; gemischtes Ebnen nativ, uncooked, frisch verpackt und mit sichtbarer Demo geprüft; historische Bauvorbereitungs-/API-Nachweise erhalten; getrennte SitePreparation-V2-Map mit eigenem Slot und expliziten Biomregeln eingerichtet; Uncooked- und Cooked-Neustarts bestanden, versiegelte Demo vorbereitet, sichtbarer Start noch offen. Physische Eingaben und Oberflächenarbeit folgen.
- [ShaderWorld-Datenlayer und Spielstand](reference/shaderworld-data-and-persistence.md) – räumliche Terrain-Daten, Mapassets und dauerhafte Zustände unterscheiden; Quellbefund zu unvollständigen Speicherfunktionen in 4.1.
- [Bauarbeit, Gelände und Material](reference/construction-and-terrain-architecture.md) – gesetzte Designregeln, geprüfter kleiner Baugrubenkreislauf und Vorschläge für weitere Maschinen-/Materialarbeit.
- [Nächste City-Builder-Bausteine](reference/city-builder-roadmap.md) – erhaltene Themen, Baufortschritt statt freiem Terraforming und offene Abnahmen.
- [Versionen und Fähigkeiten](reference/versions-and-capabilities.md) – alter UE-5.5-Bestand, aktuelle Erweiterungen, Biome, PCG und offene Grenzen.
- [MCP und Automatisierung](reference/mcp-and-automation.md) – was der native Unreal-MCP im Lernprojekt übernimmt.
- [Quellen und Bildherkunft](reference/sources.md) – offizielle Dokumentation, eigener Nachweis und Bildverzeichnis.
- [Prüfstand und offene Tests](verification.md) – aktuelle 46 native Tests, uncooked/verpackte Maschinen-Erdarbeit und separate Editor-Ansichtsprüfung; ältere 36er-Planer/Cache/Hybridnachweise sowie historische 29 native Tests, frühere 12er-/22er-Suiten, der getrennte gerenderte Navigationsversuch, cooked Baugrubenabschluss, geschlossener Materialkreislauf und acht CPU-Rodungsmessfenster mit ihren Grenzen.

## Wissensbasis pflegen

- [Neue Erkenntnisse eintragen](maintenance.md) – Metadaten, Quellen, Prüfstatus und technische Dokuprüfung.
- [Änderungsverlauf](log.md) – inhaltliche Aktualisierungen nach Datum.

Die öffentlichen Dateien enthalten die Anleitungen und Belege. Die projektlokalen CityLab-Karten und die eigene SaveGame-Implementierung liegen im ursprünglichen Unreal-Testprojekt; sie werden hier als Voraussetzung benannt und nicht als mitgelieferte Pluginfunktion dargestellt.
