# Änderungen an der Wissensbasis

## 2026-10-28

- Neue native PIE-Aufnahme nach Komponentenwechsel und Kartenneuladen inspiziert: sichtbarer Tunnelinnenraum trocken, nur ein Frame; Langzeit-/GPU-Prüfung offen.
- Eigenen Guide zur CityLab-Tunnelkomponente mit integriertem Air Pocket angelegt: Editor-Bedienung, Passagemaße und Platzierung beschrieben. Eigene Komponente implementiert, Build und zwei native Automationtests bestanden; Gespeicherte Karte tatsächlich neu geladen und Eigenschaften im neuen PIE bestätigt; frischer Spielprozess bestand 65/65 Proben und rund 259,44 m bodengebundene Durchfahrt. Bisherige separate Box bleibt als früherer Sichtnachweis erhalten.

- Waldfilter über eigenes Landbiom und drei Spawnable-Kopien auf Min 150 cm gesetzt; Plugin-Originale unverändert. Wellendämpfung 1,0 gespeichert und im laufenden PIE bestätigt.
- Nutzer grenzte verbleibende Wellen auf den Tunnel ein: Hole-Sentinel wird vom Ozean als große Wassertiefe gelesen; eigene Fahrbahn ist nicht Teil der Terrainquelle.
- Native Air-Pocket-Box für Tunnel und Portale gespeichert und nach PIE-Neustart zurückgelesen; Nutzer meldete anschließend an der betroffenen Stelle „Bisher trocken“. Langzeit-/GPU-Prüfung weiterhin offen.

- Küsten-/Biomfragen lesend untersucht: Ground/Ocean-Verknüpfung vorhanden, Restwellendämpfung und vorbereitete Air-Pocket-Materialmaske dokumentiert; gemeldeter Wellendurchbruch noch nicht reproduziert.
- Alte negative Pflanzen-Höhenfilter nach der Meereshöhenänderung als Ursache für erlaubten Wald unter Wasser eingeordnet; OceanMap-Biom als Landvegetation erklärt.
- Straßenherkunft präzisiert: native ShaderWorld-Drecktrassen, eigene Asphalt-/Markierungsmeshes, Road-Creator-Kopplung weiterhin offen.

- Zufahrten korrigiert: Nach direkten JSON-Splineänderungen fehlte die passende Längentabelle; Tangenten und vollständige Weglängen nun gemeinsam erzeugt.
- Zwei native PIE-Editorbilder mit freier Dreckstraße und Portalzufahrt ergänzt.
- Neue CityBasics-Kollisions- und Durchfahrtsbelege mit Quellen und offenen Bedien-/Cook-/SaveGame-Grenzen verknüpft.

## 2026-10-27

- Eigenes CityBasics-Labor mit Reference-Bodenmaterialien/Biom, Insel, Ozean, Bergbrush, Portalstempeln und Tunnelkörper angelegt.
- Datenmaskenfehler am Berg dokumentiert: Ein unterirdischer Spline mit deaktivierter Höhenverformung schreibt weiterhin Material-/Biomwerte auf die obere Terrainfläche; die durchgehende Maske wurde deaktiviert.
- Eigene Buggy-/Laufbedienung ergänzt; den tatsächlichen Nachweis hält die CityBasics-Anleitung fest.
- OKF-0.2-Wissensbasis für Unreal 5.8.4 und ShaderWorld 4.1 im Projekt angelegt.
- Anleitungen für Terrain/Kollision, Beispielwelten, Pads/Straßen, SaveGame, Löcher/Tunnel und Ozean zusammengeführt.
- Sieben unveränderte Viewport-Aufnahmen und sechs bereinigte Nachweis-/Manifestdateien aufgenommen.
- Wind 18 m/s und aktivierten Schaum nach erforderlichem Ozean-Rebuild dokumentiert.
- Herstellerangaben, Codebefunde, Editor-/PIE-Prüfungen und echten Prozessneustart getrennt ausgewiesen.
