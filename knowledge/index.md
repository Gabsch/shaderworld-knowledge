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
- [Änderungen speichern und laden](guides/save-and-load.md) – unsere CityLab-Spielstände einschließlich eines echten Neustarts prüfen.
- [Löcher und Bergtunnel verstehen](guides/holes-and-mountain-tunnels.md) – Holebrush-Beispiele ansehen und einen Tunneleingang planen.
- [Tunnelkomponente mit eingebautem Wasserausschluss](guides/reusable-tunnel-component.md) – eigener Baustein mit bestandenen nativen API-Tests; gespeicherte Karte, neues PIE und frische Durchfahrt geprüft.

## Nachschlagen

- [Versionen und Fähigkeiten](reference/versions-and-capabilities.md) – alter UE-5.5-Bestand, aktuelle Erweiterungen, Biome, PCG und offene Grenzen.
- [MCP und Automatisierung](reference/mcp-and-automation.md) – was der native Unreal-MCP im Lernprojekt übernimmt.
- [Quellen und Bildherkunft](reference/sources.md) – offizielle Dokumentation, eigener Nachweis und Bildverzeichnis.
- [Prüfstand und offene Tests](verification.md) – welche Aussage durch welchen Versuch gedeckt ist.

## Wissensbasis pflegen

- [Neue Erkenntnisse eintragen](maintenance.md) – Metadaten, Quellen, Prüfstatus und technische Dokuprüfung.
- [Änderungsverlauf](log.md) – inhaltliche Aktualisierungen nach Datum.

Die öffentlichen Dateien enthalten die Anleitungen und Belege. Die projektlokalen CityLab-Karten und die eigene SaveGame-Implementierung liegen im ursprünglichen Unreal-Testprojekt; sie werden hier als Voraussetzung benannt und nicht als mitgelieferte Pluginfunktion dargestellt.
