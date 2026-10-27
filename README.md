# ShaderWorld Wissen für einen City Builder

Praktische deutsche Anleitungen für **Unreal Engine 5.8.4 und ShaderWorld 4.1**. Die Wissensbasis erklärt Einrichtung, Bauplätze, Straßen, Spielstände, Terrainlöcher und Ozeanwellen anhand eines untersuchten Testprojekts. Sie verwendet **Open Knowledge Format 0.2** und bleibt als normales Markdown lesbar.

**[Hier mit dem Lernpfad beginnen](knowledge/index.md)** · [Prüfstand und offene Tests](knowledge/verification.md) · [Doku ergänzen](knowledge/maintenance.md)

![Reference-Welt mit Wald, Küste und Straßentrasse](knowledge/assets/images/reference-overview.png)

Die rote Lumen-Meldung und die Drahtkästen gehören zur untersuchten Editoransicht. Die Meldung ist ein offener Renderer-Konfigurationspunkt; das Bild ist keine vollständig abgestimmte Beleuchtungsreferenz.

## Was du hier bekommst

- Genaue Editor-Schritte, Einstellungen, erwartete Bilder und Hilfe bei typischen Fehlern.
- Quellen und einen fachlichen Prüfstatus je Thema: Herstellerangabe, Codebefund, Editor/PIE oder Neustarttest.
- Ausgewählte, von lokalen Dateipfaden bereinigte Prüfberichte und unveränderte eigene Viewport-Aufnahmen.
- Einen lokalen Prüfer für Metadaten, Links und Bilddateien.

Dieses Repository ist eine **inoffizielle, projektbezogene Ergänzung** zur [ShaderWorld-Dokumentation](https://universgen.gitbook.io/shader-world). Es enthält weder das kostenpflichtige Plugin noch dessen Quellcode, Assets oder ein ausführbares Unreal-Projekt. Für die allgemeinen Beispielanleitungen ist eine eigene ShaderWorld-Installation nötig. Die CityLab-Anleitungen setzen zusätzlich das im ursprünglichen Lernprojekt implementierte Labor voraus; dessen besondere Tastenbelegung gehört zu unserem Projekt.

## Schnell einsteigen

1. [Terrain und Kollision einrichten](knowledge/guides/setup-terrain.md).
2. [Die drei Beispielwelten kennenlernen](knowledge/reference/example-maps.md).
3. [Wind und Schaum ausprobieren](knowledge/guides/ocean-waves-and-foam.md).
4. [Bauplätze und Straßen verstehen](knowledge/guides/building-pads-and-roads.md) und [Speichern/Laden prüfen](knowledge/guides/save-and-load.md).
5. [Löcher und Bergtunnel richtig einordnen](knowledge/guides/holes-and-mountain-tunnels.md).

## Lokal lesen und prüfen

Öffne `knowledge/index.md` in einem Markdown-Editor oder direkt auf GitHub. Ein Google-Konto, Cloud-Katalog oder zusätzlicher Server ist zum Lesen nicht nötig.

Für die technische Dokuprüfung mit Python 3.11 oder neuer:

```powershell
python -m pip install -r requirements.txt
python tools/validate_knowledge.py
```

GitHub Actions führt dieselbe Prüfung bei Pushes nach main und bei Pull Requests aus. Der Prüfer prüft die Wissensbasis, führt keine Unreal-Simulation aus und bestätigt keine Spielszenarien. Mehr zum Format, Quellenmodell und Aktualisieren steht unter [Wartung](knowledge/maintenance.md).

Stand: **27. Oktober 2026**. Neue Pluginversionen benötigen eine bewusste Nachprüfung der betroffenen Rezepte.
