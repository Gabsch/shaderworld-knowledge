# Änderungen an der Wissensbasis

## 2026-10-28

- Kameraabhängigen Bodenfleck durch RoadLab-Asphalt auf den aktiven POM-Pfad eingegrenzt: 6-cm-Anhebung bleibt bei kleiner Bildschirmparallaxe ohne Tiefenversatz sichtbar. Eigene MI_RoadLab_Terrain mit **POM: Reference Plane = 1,0**, POM/Relief weiter aktiv, bestand den reversiblen 30-m-Bildvergleich und zusätzliche 3-/100-m-Sichtproben. Gespeicherte Actor-Zuweisung nach echtem Kartenneuladen/neuem PIE mit drei geladenen Straßen bestätigt; gleicher Editorprozess, kein Standalone-/Cook-Test. Bloßen Instanzsave von dauerhafter Kartenzuweisung unterschieden. Frühere Legacy-Displacement-Hypothese verworfen, erfolglose 1-cm-Overrides entfernt. Gescheiterte Live-MID-/Graphdiagnosen getrennt erfasst; Kollisionsprüfungen erfassen diese Materialeffekte nicht.

- Native Slate-Bedienprobe im RoadLab bestanden: R/Enter, Backspace, X, Q/E, K/L und normales PIE-Autoload mit identischen IDs, Splinepunkten/Tangenten und Einstellungen. Kamera per ActorTools versetzt; Bewegungstasten, Maustasten/Zoom und F5/F9 bleiben offen. Neue normale Auto-Load-Aufnahme ins Manifest aufgenommen. Unabhängige Bauplatz-/Terrainstraßen-Regression mit Format 2 und zwei frischen Prozessen bestanden.

- RoadLab-Zwei-Prozess-Nachweis bestanden: 18/18 und 19/19 Checks, je 72/72 Kollisionsproben, identische zwei Straßen/16 Meshsegmente. Gemessene Pflanzenursprünge 999 → 0 → 999 → 0 bei 8615 Referenzen und drei gleichen Matrix-Fingerprints je Phase. Bereinigten Bericht und zweite native Aufnahme mit Herkunft/Hash ergänzt; synthetisches Format-1-Fixture, fehlende UI-/Cook-/Überhang-/GPU-Abnahme getrennt benannt.

- Zweiter RoadLab-Lauf passiert das korrigierte Pflanzen-Baseline-Gate nach rund 31 s und erzeugt zwei Straßen mit 16 Meshes. Danach blockierte unser Manager wegen unnötiger Pad-Shader-Abhängigkeit ohne Pad-Instanz vor Kollisionsproben. Projektintegration auf vorhandene Pads begrenzt; neuer Test läuft, Neustart-/Vegetationswirkung weiterhin offen.

- Erstes RoadLab-Timeout auf unser ungeeignetes Pflanzen-Testgate eingegrenzt: Grundterrain und Pflanzen waren vorhanden. Async-Build-Zustand plus drei stabile Transform-Fingerprints ersetzen die bisherige IsTreeFullyBuilt-Annahme; Straßen-/Neustart- und Maskenwirkung weiterhin offen.

- RoadLab-Guide als draft vorbereitet: gemeinsame ShaderWorld-/SplineMesh-Trasse, RCP-Meshkopie, Punktbedienung und logisches Saveformat 2 dokumentiert. Build bestanden und erste unveränderte PIE-Aufnahme inspiziert: sichtbare Laufzeit-Beispielstraße, noch kein Bedienungs-/Zwei-Prozess-/Pflanzen-/Cook-Nachweis.

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
