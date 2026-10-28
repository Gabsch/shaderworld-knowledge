---
okf_version: "0.2"
---

# ShaderWorld für den City Builder lernen

Diese Wissensbasis begleitet konkrete Editor-Versuche mit Unreal **5.8.4** und ShaderWorld **4.1**. Beginne mit Einrichtung und Beispielwelten. Danach kannst du einzelne Rezepte unabhängig durcharbeiten.

## Einstieg

- [Terrain und Kollision einrichten](guides/setup-terrain.md) – eine flache Welt anzeigen und begehbaren Boden vorbereiten.
- [Beispielwelten vergleichen](reference/example-maps.md) – Reference, Heightmap und OceanOnly finden und sinnvoll nutzen.
- [Fehler gezielt eingrenzen](guides/troubleshooting.md) – leere Vorschau, fehlende Kollision, Lumen-Meldung und ausbleibender Schaum.

## Ausprobieren und bauen

- [CityBasics: Insel, Wald, Berg und Tunnel](guides/city-basics-lab.md) – den farbigen Laboraufbau und den bodengebundenen Testbuggy verstehen.
- [Wind und Schaum einstellen](guides/ocean-waves-and-foam.md) – den Ozean von 10 auf 18 m/s Wind umstellen und Schaum sichtbar machen.
- [Bauplätze und Straßen verändern](guides/building-pads-and-roads.md) – die Lernkarte bedienen und Gelände, Material und Straßenmesh unterscheiden.
- [Vom Straßenbau zum bewohnten Testhaus](guides/city-builder-loop.md) – verbundene Spielschleife mit Grundstück, Haus, Bürger und bestandenem Drei-Prozess-Neustartnachweis.
- [Baukamera und Werkzeugleiste bedienen](guides/build-controls.md) – geprüfte Regler/Planbestätigung und neuer selektiver Baum-Kamerafilter mit 25/25 nativen Tests; bisherige Toolbar-/Restorebelege getrennt. Normales ConstructionLab-Wiederladen mit passendem Boden und Kamerapose zusätzlich belegt; physische Kameraeingaben und aktuelle cooked Kamerafahrt bleiben offen.
- [Foundations: planen, Biome und Einzelrodung](guides/foundations-lab.md) – aktuelle Black-/Zero-Flow-Fassung mit uncooked und verpacktem Neustartnachweis; sichtbares Snow nach normalem PIE-Laden und geschütztes Grundstück mit Bildern belegt; Rodungsfix mit separater Vorher-/Nachher-/Ladebildprobe, Rodung vom Nutzer nach dem Fix ausprobiert und bestätigt; gezielte Abnahme aller Vorschau-/Fokusfälle bleibt offen.
- [Baugrube, Testbagger und Materialkreislauf](guides/construction-lab.md) – schrittweise Erdarbeit mit 18-t-Puffer, 12-t-Lkw und eigenem Spielstand; cooked Neustart und Abschluss mit 172,8 t im Lager/0 g Modellbilanzfehler bestanden. Lokale Höhenprüfung, normale Erstplanung/Puffer/Transport und exaktes PIE-Wiederladen belegt; Tastatur-/Fokusfälle und Pixelvergleich bleiben begrenzt.
- [Straßen zur Laufzeit bauen und speichern](guides/runtime-roads.md) – RoadLab mit gemeinsamer Terrain-/Mesh-Spline; Neustart, Kollision, Pflanzenursprünge und die POM-Nahsichtkorrektur verstehen.
- [Änderungen speichern und laden](guides/save-and-load.md) – unsere CityLab-Spielstände einschließlich eines echten Neustarts prüfen.
- [Löcher und Bergtunnel verstehen](guides/holes-and-mountain-tunnels.md) – Holebrush-Beispiele ansehen und einen Tunneleingang planen.
- [Tunnelkomponente mit eingebautem Wasserausschluss](guides/reusable-tunnel-component.md) – eigener Baustein mit bestandenen nativen API-Tests; gespeicherte Karte, neues PIE und frische Durchfahrt geprüft.

## Nachschlagen

- [Bauarbeit, Gelände und Material](reference/construction-and-terrain-architecture.md) – gesetzte Designregeln, geprüfter kleiner Baugrubenkreislauf und Vorschläge für weitere Maschinen-/Materialarbeit.
- [Nächste City-Builder-Bausteine](reference/city-builder-roadmap.md) – erhaltene Themen, Baufortschritt statt freiem Terraforming und offene Abnahmen.
- [Versionen und Fähigkeiten](reference/versions-and-capabilities.md) – alter UE-5.5-Bestand, aktuelle Erweiterungen, Biome, PCG und offene Grenzen.
- [MCP und Automatisierung](reference/mcp-and-automation.md) – was der native Unreal-MCP im Lernprojekt übernimmt.
- [Quellen und Bildherkunft](reference/sources.md) – offizielle Dokumentation, eigener Nachweis und Bildverzeichnis.
- [Prüfstand und offene Tests](verification.md) – aktuelle 25 native Tests, frühere 12er-/22er-Suiten, der getrennte gerenderte Navigationsversuch, cooked Baugrubenabschluss und acht CPU-Rodungsmessfenster mit ihren Grenzen.

## Wissensbasis pflegen

- [Neue Erkenntnisse eintragen](maintenance.md) – Metadaten, Quellen, Prüfstatus und technische Dokuprüfung.
- [Änderungsverlauf](log.md) – inhaltliche Aktualisierungen nach Datum.

Die öffentlichen Dateien enthalten die Anleitungen und Belege. Die projektlokalen CityLab-Karten und die eigene SaveGame-Implementierung liegen im ursprünglichen Unreal-Testprojekt; sie werden hier als Voraussetzung benannt und nicht als mitgelieferte Pluginfunktion dargestellt.
