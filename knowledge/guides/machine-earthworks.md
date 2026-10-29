---
type: Guide
title: Anheben und Absenken als gespeicherte Maschinenarbeit
description: Mehrere Erdaufträge planen, vorhandenen Boden ausheben und wieder einbauen sowie Ladungen und Arbeitsfortschritt speichern.
tags: [shaderworld, city-builder, earthworks, construction, persistence]
status: draft
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: 46 native Tests; je zwei gerenderte uncooked und frisch verpackte Prozesse mit 10/10 und 12/12 Checks. Normale Controller-APIs, drei exakte Loads und kalter Queue-Restore geprüft. Separate Editor-Ansicht mit Bildern und lokalen Kollisionen belegt; physische Eingaben und verpackte Ansichtspixel offen.
generated:
  by: codex/gpt-6
  at: "2026-10-29T11:00:12Z"
sources:
- id: own-earthworks
  resource: "Eigener Projektcode CityLabEarthworksModel, CityLabEarthworks und CityLabEarthworksGameMode sowie Tools/setup_earthworks_lab.py; nicht im öffentlichen Bundle enthalten"
  title: Gespeicherte Erdaufträge, Mengenmodell, ShaderWorld-Projektion und Bedienung
- id: own-persistence
  resource: "Eigener Projektcode CityLabPersistence und CityLabEarthworksTests; nicht im öffentlichen Bundle enthalten"
  title: Speicherformat 6, Snapshot-Prüfung und bestandene native Modelltests
- id: machine-evidence
  resource: ../evidence/machine-earthworks-test.json
  title: Finale native Suite und gerenderte uncooked sowie verpackte Neustartproben
- id: work-plan
  resource: ../reference/scaping-machine-work-plan.md
  title: Vereinbarter Ausbau der Scaping-Werkzeuge zu Maschinenaufträgen
- id: storage-contract
  resource: ../reference/shaderworld-data-and-persistence.md
  title: Terrain-Daten und dauerhaften Spielzustand unterscheiden
- id: previous-planner
  resource: construction-planner.md
  title: Vorheriges Planerlabor mit genau einem Gruben-Aufschüttungspaar
---

# Anheben und Absenken als gespeicherte Maschinenarbeit

Im neuen **Erdarbeitslabor** sollst du mehrere kleine Anhebungen und Absenkungen planen können. Ein gemeinsamer Maschinenzug arbeitet jeweils einen ausdrücklich gestarteten Auftrag ab. Absenken gewinnt Erde, der Lkw bringt sie ins Lager, und eine spätere Anhebung verbraucht diesen tatsächlichen Bestand. Auch eine bereits bearbeitete Fläche kann einen neuen Auftrag erhalten, sobald Boden und Zufahrt erneut geprüft sind.

**Anheben, Absenken und Neustart sind uncooked und im frisch verpackten Spiel geprüft.** Je zwei getrennte Spielprozesse bestanden **10/10 und 12/12 Checks**. Auf derselben Fläche wurden **86,4 t** ausgehoben, eingelagert und wieder eingebaut; alle beobachteten Materialbilanzen blieben **0 g**. Die finale native Suite bestand 46 Tests. Normale Controller-APIs und ein kalter Start mit ungearbeitetem Plan sind zusätzlich geprüft. Physische Maus-/Tasteneingaben und verpackte Ansichtspixel bleiben offen; deshalb bleibt die Anleitung ein Entwurf. [Bereinigter Prüfbericht](../evidence/machine-earthworks-test.json). Frühere Nachweise aus dem [Planerlabor](construction-planner.md) gelten weiterhin für dessen eigene Fassung.

## Voraussetzungen und Einstieg

Benötigt werden Unreal **5.8.4**, ShaderWorld **4.1** und der neu kompilierte CityLab-Code im ursprünglichen Projekt. Die Karte und ihre eigenen Materialien sind bereits gespeichert und frisch gecookt. Das öffentliche Wissensbundle liefert keine Unreal-Karte, Spielstände oder lizenzierten Fahrzeugassets mit.

1. Im **Content Browser** den Ordner **Content → Maps** öffnen und **ShaderWorldEarthworksLab** doppelklicken. Der vollständige Kartenpfad ist **/Game/Maps/ShaderWorldEarthworksLab**; sie verwendet **CityLabEarthworksGameMode**.
2. **Play** starten. Gerenderte Frames, Shader und Bodenkollision abwarten. Der normale Slot heißt **CityLabEarthworks**; Construction, Planner und Foundations behalten ihre getrennten Slots.
3. Ohne vorhandenen Slot beginnt das Labor leer. Ein gültiger vorhandener Slot wird geladen. Im aktuellen normalen Laborstand wartet ein ungearbeiteter Absenkplan; Arbeit ist pausiert und Transport aus. Es wird kein Beispielauftrag beim Start erzeugt.

### Karte bei Bedarf neu einrichten oder reparieren

Diese Folge ist nur für die Einrichtung nötig; die vorhandene Karte kannst du direkt öffnen.

1. Eigene Editoränderungen speichern und **Play/PIE beenden**. Die Editor-Sitzung darf keinen anderen Auftrag abarbeiten.
2. In Unreals **Python-Konsole** die feste Bridge anhängen:

   ```python
   import runpy, unreal
   runpy.run_path(unreal.Paths.project_dir() + "Tools/earthworks_editor_session.py", run_name="__main__")
   ```

3. Nach der Logmeldung **CITYLAB_EARTHWORKS_EDITOR_BRIDGE_READY** binnen **120 Sekunden** in einer externen PowerShell im Projektordner ausführen:

   ```powershell
   python Tools/setup_earthworks_lab.py
   ```

4. Die Bestätigung **EarthworksLab eingerichtet und gespeichert zurückgelesen** abwarten. Erst anschließend Karte öffnen und Play starten. Der private Bericht liegt unter **Saved/McpDiagnostics/earthworks-map-setup.json**.

Der Client startet keinen Editor und sendet genau eine feste Setup-Anfrage. Die Bridge richtet ihre eigene Karte, GameMode, Haupt-/Fernmaterial und Schnittmaterialien ein; sie schreibt keine Spielstände. Bei einem Timeout nicht blind wiederholen: Der Editor kann noch arbeiten. Ergebnis und Bericht zuerst prüfen. Eine bewusste neue Anfrage benötigt eine frisch angehängte Bridge. Der externe Client ist mit neun Offline-Protokollfällen geprüft; die tatsächliche Editor-Einrichtung wurde über dieselbe feste Bridge-Aktion direkt abgenommen. Die [Untergrundanleitung](underground-view.md#voraussetzungen-und-einrichtung) beschreibt die Materialgrenzen.

Für eigene Neustartversuche einen isolierten Test-Spielstand verwenden und den normalen Spielstand erhalten.

## Erst absenken und Erde einlagern

1. **Absenken [1]** wählen und die Maus über ein freies Arbeitsfeld bewegen. Zunächst auf der ebenen Laborfläche beginnen. Eine gültige Vorschau erscheint **cyan**, eine ungültige **rot**. Die Anzeige beschreibt den Grund einer Ablehnung. Noch wird kein Boden verändert.
2. Mit **Linksklick** den Ort fixieren. Danach kannst du die Maus zum Bedienfeld bewegen. Ziehen mit rechter Maustaste bleibt eine Kameraaktion.
3. **Groesse -/+** beziehungsweise **Komma/Punkt** stellt **1 bis 3 Zellen je Seite** ein. **Hoehe -/+** beziehungsweise **Bild ab/auf** ändert den Betrag in **0,25-m-Schritten** zwischen **0,5 und 2 m**. Die Vorschau zeigt die vollständig vorgesehene Endform.
4. Geplantes Volumen, Masse und freien Lagerplatz lesen. **Plan bestaetigen + speichern [Enter]** legt den Auftrag in der Warteschlange ab. Der tatsächliche Boden, Puffer, Lagerbestand und Materialkonten bleiben dabei unverändert.
5. Der neue Auftrag ist ausgewählt. **Arbeit starten / Pause [Space]** prüft ihn erneut, aktiviert ihn und schaltet Maschinenarbeit ein. **Transport an / aus [H]** schaltet den Lkw getrennt ein.
6. Beobachten, wie der Boden schrittweise zur Sollform wird. Ohne Transport füllt sich der Aushubpuffer; bei vollem Puffer wartet die Maschine. Erst die tatsächliche Lkw-Entladung erhöht den Lagerbestand.

Das normale Profil sieht **18 t Puffer**, **12 t Lkw-Ladung** und **500 t Lagerkapazität** vor. Diese Größen und die Arbeitsgeschwindigkeit sind Laborwerte. Der Radlader ist eine Fahrzeugdarstellung; Bewegungen und Mengen folgen dem eigenen Arbeitsmodell und festen geprüften Wegen.

Absenken lässt sich nur starten, wenn **der gesamte noch vorgesehene Aushub ins freie Lager passt**. Diese Prüfung verhindert, dass der einzige Maschinenzug mit vollem Lager feststeckt. Sie schreibt keine Erde gut und reserviert keinen zukünftigen Ertrag für andere Pläne.

## Die Erde wieder zum Anheben verwenden

1. Den Absenkauftrag einschließlich aller Lieferungen abschließen lassen. Die restliche Arbeit, Puffer und Lkw müssen leer sein; der Lkw steht anschließend wieder am Lager.
2. **Anheben [2]** wählen. Eine freie Fläche oder dieselbe zuvor abgesenkte Fläche auswählen, den Ort fixieren und Größe sowie Betrag einstellen. Die Anzeige zeigt Bedarf, freien tatsächlichen Lagerbestand und gegebenenfalls fehlende Masse.
3. Den Plan bestätigen. Auch ein noch nicht finanzierter Anhebeplan darf zunächst gespeichert warten. Er erhält dadurch keine Erde und blockiert keinen Lagerbestand.
4. **Space** startet den ausgewählten Auftrag erst, wenn der gesamte Bedarf im gemeinsamen Lager vorhanden ist. Jetzt wird diese vorhandene Masse für ihn reserviert. **H** schaltet seine Lieferfahrten ein.
5. Der Lkw lädt am Lager, fährt zum Arbeitsfeld und entlädt in dessen begrenzten Puffer. Nur Material aus diesem Puffer kann die Maschine einbauen und damit den tatsächlichen Boden anheben.

Nach jedem Auftrag bleibt der nächste Plan inert. Mit **Naechsten waehlen [Tab]** wählst du den gewünschten gespeicherten Auftrag und startest ihn ausdrücklich. Es gibt **einen aktiven Auftrag und einen gemeinsamen Lkw**; die Warteschlange ist noch keine allgemeine Stadtlogistik.

**Arbeitspause und Transportpause sind unabhängig.** Bei pausierter Maschinenarbeit kann der Lkw weiter liefern. Auch eine solche Lieferung gehört bereits zur verbindlichen Materialhistorie.

## Welche Menge bedeutet die Form?

| Zellen je Seite | Abstand der Zellmitten | Gesamter Höheneinfluss | Integrale Fläche für die Mengenrechnung |
| --- | --- | --- | --- |
| 1 | 4 m | 8 × 8 m | 16 m² |
| 2 | 4 m | 12 × 12 m | 64 m² |
| 3 | 4 m | 16 × 16 m | 144 m² |

Jede Zelle besitzt eine weich auslaufende Form mit dreieckigem Verlauf entlang beider Achsen. Benachbarte Formen überlappen sich. Die Mengenrechnung verwendet dasselbe Modell wie die Höhenprojektion: **Zellenzahl × 16 m² × Höhenbetrag**.

Bei **2 × 2 Zellen und 0,75 m** ergeben sich **48 m³ Boden beziehungsweise 86,4 t** bei der angenommenen In-situ-Dichte von **1.800 kg/m³**. Der äußerste Einfluss ist dabei 12 × 12 m groß. Ein Einzelzellauftrag bildet eine Spitze beziehungsweise Mulde; für eine größere mittlere Fläche zwei oder drei Zellen je Seite verwenden. Freie Böschungsprofile, Verdichtung und mehrere Bodenarten folgen später.

Die Materialkonten rechnen in ganzzahligen **Gramm**. Für den Aushub gilt im Modell:

> Anfangsbestand im Lager + tatsächlich ausgegrabene Erde = aktuelles Lager + Puffer + Lkw-Ladung + tatsächlich eingebaute Erde.

Eine Reservierung ist eine Zuordnung innerhalb des tatsächlichen Lagerbestands. Erst das Beladen des Lkw bucht diese Masse aus dem Lager aus. Gespeicherte Warteschlangenpläne besitzen keine Vorabgutschrift und keine Reservierung.

## Warum ein zweiter Auftrag auf derselben Fläche funktioniert

Jeder neue Plan erfasst den **wirklich vorhandenen Ausgangsboden**. Die Aufnahme enthält ein dichtes Raster über die ganze Einflussfläche und die Start- sowie Zielhöhe jeder Arbeitszelle. Unmittelbar vor dem Arbeitsstart werden Ausgangsboden, Maschinenstände und feste Zufahrt erneut geprüft.

Daneben merkt sich der Plan eine **Referenzoberfläche**: den aufgenommenen Boden abzüglich der bereits ausgeführten Höhenänderungen unserer Erdaufträge. ShaderWorld erhält anschließend nur die tatsächlich ausgeführten zusätzlichen Höhenänderungen aller Aufträge. Der eingefrorene Ausgangsboden wird dadurch beim nächsten Auftrag kein zweites Mal aufgetragen.

Ideales Rechenbeispiel an einer Zellmitte: Ausgangshöhe **3 m**, um **0,75 m** abgesenkt ergibt **2,25 m**; eine gleich große Anhebung führt wieder auf **3 m**. Im wirklichen Lauf erfasst der zweite Plan erneut die tatsächliche Kollision: Seine Startwerte lagen bei rund **2,240 m** und seine Zielwerte bei **2,990 m**. Die quantisierte Terrainoberfläche ist keine beliebig genaue mathematische Fläche. Die Darstellung ergibt sich aus der ursprünglichen Referenzhöhe plus beiden ausgeführten Änderungen, ohne die abgesenkte Basis zusätzlich aufzutragen. Der zweite Auftrag verbraucht die zuvor wirklich eingelagerte Erde.

Ändert sich die Fläche zwischen Planung und Start, kann der Auftrag **NeedsReplan** anzeigen. Dann den gespeicherten Auftrag auswählen, eine frische Vorschau auf dem gewünschten Ort fixieren und **Ungearbeitet revidieren** verwenden. Eine unabhängige Änderung an anderer Stelle muss den Plan nicht unbrauchbar machen; entscheidend sind die erneut gemessene Fläche und ihre Zugänge.

Technisch bleiben die **Plan-ID** und ihre Reihenfolge bei einer Revision erhalten; die Revisionsnummer steigt. Der ausführende **Job** hat eine eigene stabile ID und verweist auf diesen gespeicherten Plan. `SourcePlanId` bezeichnet hier dieselbe Identität wie `Plan.Id`. Ein gespeicherter Fingerabdruck prüft die innere Konsistenz der eingefrorenen Proben und Zielwerte; er ist kein Sicherheitsnachweis gegen absichtliche Manipulation.

## Verwerfen, revidieren und stornieren

- **Vorschau verwerfen [Esc]** entfernt nur die noch nicht bestätigte Vorschau.
- **Ungearbeitet revidieren** ersetzt die Vorgaben eines wartenden, noch ungearbeiteten Plans durch eine frisch geprüfte Vorschau. Zuvor den gewünschten Auftrag mit **Tab** auswählen und einen Zielort fixieren.
- **Ungearbeitet stornieren** beziehungsweise **Entf** storniert einen Auftrag, der noch keine Erde bewegt und keinen Materialtransfer ausgeführt hat. Eine bloße, noch unbenutzte Reservierung wird dabei freigegeben.
- Nach dem ersten Erdarbeitsschritt **oder Materialtransfer** bleiben tatsächliche Höhen, Ladungen und Konten erhalten. Eine spätere Korrektur benötigt einen neuen Gegenauftrag mit eigenem Bedarf und eigener Arbeit.

Abgeschlossene Aufträge bleiben als Arbeits- und Materialhistorie gespeichert. Ein Plan-Undo darf keine bereits ausgeführte Erde oder Lieferung zurücksetzen. Die bisherigen Foundations-Tasten für Plan-Undo und sofortige Debug-Ausführung sind in diesem Erdarbeitslabor keine allgemeinen Erdarbeitswerkzeuge.

## Speichern und mitten während der Arbeit fortsetzen

**F5/K** speichert ausdrücklich, **F9/L** lädt. Planbestätigung, Revision und Arbeits-/Transportschalter lösen ebenfalls Speichern aus; laufende Änderungen werden mit begrenzter Rate automatisch gesichert. Die unbestätigte Mausvorschau bleibt flüchtig.

Der gemeinsame Snapshot enthält die Warteschlange mit Baseline und Referenz, stabile Identitäten und Revisionen, ausgeführte Gramm je Zelle, aktive Maschinenzelle und Fahrt, Lkw-Phase und Position entlang der Route, Ladung, Puffer, Lager, Reservierung sowie kumulative Materialkonten. Arbeits- und Transportschalter bleiben gespeichert. Beim Laden werden Terrain-Darstellung und Bewuchsmasken daraus rekonstruiert; passende lokale Kollision muss die weitere Arbeit freigeben. Es gibt keine Offline-Nachholung.

Das eigene CityLab-**Speicherformat 6** ergänzt diese Erdarbeitsdaten. Die bisherigen Felder für Straßen, Bauplätze, Bürger, WorldEdits, Rodung und Construction-Aufträge bleiben erhalten. Formate **1 bis 5** unterliegen weiterhin ihren jeweiligen Schema- und Weltbindungsprüfungen. Daraus folgt keine pauschale Migration bei veränderter Karte, Generator- oder Terrainkonfiguration. Alte Construction-Aufträge werden auch nicht automatisch in die neue Warteschlange umgewandelt.

**Noch kein Spielstand vorhanden** ist ein behebbarer Hinweis: weiterplanen und den ersten Plan bestätigen. Genau dieser Fall blieb im normalen PIE bedienbar und führte zur erfolgreichen Bestätigung mit Autosave. Wird dagegen ein vorhandener Spielstand als ungültig abgewiesen, bleiben Speichern und Autosave gesperrt. Bei einem fehlgeschlagenen manuellen Laden hält die implementierte Fassung zusätzlich die Erdarbeitssimulation an. Den Fehler zuerst klären und einen gültigen Spielstand ausdrücklich erneut laden. Ein abgewiesener Spielstand soll durch keinen leeren Ersatz überschrieben werden. Die Abweisung eines ungültigen vorhandenen Saves und seine vollständigen normalen Fehler-/Wiederanlaufwege benötigen weiterhin eine eigene praktische Abnahme.

## Wenn es nicht weitergeht

| Anzeige oder Verhalten | Nächster Schritt |
| --- | --- |
| Boden, Shader oder Kollision noch nicht bereit | Gerenderte Frames abwarten und die Kamera in der Nähe des Felds lassen. Nach einer Höhenänderung wartet die nächste Arbeit auf lokale Kollisionsproben. |
| Ausgangsboden verändert / NeedsReplan | Frische Vorschau aufnehmen und den ausgewählten ungearbeiteten Plan revidieren. Bereits bearbeitete Aufträge bleiben erhalten. |
| Zu wenig freier Lagerplatz für Absenken | Zuerst vorhandene Erde mit einem finanzierten Anhebeauftrag verbrauchen oder einen kleineren Absenkauftrag planen. |
| Fehlende Masse für Anheben | Erst tatsächlichen Aushub einlagern. Ein wartender Absenkplan allein erzeugt keinen Bestand. |
| Puffer voll / Maschine wartet | Transport einschalten und die Ladungs-/Lieferkette beobachten. Maschinenpause stoppt den Lkw nicht automatisch. |
| Zufahrt oder Maschinenstand ungeeignet | Arbeitsfeld versetzen. Die festen Wege und Außenstände müssen frei und eben sein; ein freier Routenplaner fehlt noch. |
| Arbeitsfeld berührt Straße, Grundstück, Haus oder Tunnel | Freien Standort wählen. Bestehende Bauobjekte und gespeicherte Zufahrten sind geschützt. |
| Sollboden zu nah am Meer | Höher gelegenen Standort oder geringeren Absenkbetrag wählen. Der Abstand zum mittleren Meeresspiegel ist keine Wellen- oder Grundwassersimulation. |
| Noch kein Erdarbeits-Spielstand vorhanden | Ersten Plan bestätigen oder ausdrücklich speichern. Dieser Hinweis sperrt die weitere Planung nicht. |
| Speichern nach abgewiesenem Laden gesperrt | Fehler prüfen und einen passenden gültigen Spielstand erneut laden. Den normalen Slot erhalten. |

Die Arbeitsvorbereitung unterdrückt generierten Bewuchs bei beginnendem Aushub beziehungsweise beim ersten Materialbezug eines Anhebeauftrags. Dabei entstehen noch keine gespeicherten Holzerträge. Die dauerhafte Einzelrodung bleibt ein eigener Vertrag.

Das Bedienfeld enthält außerdem **Oberflaeche [3]**, **Schnitt [4]** und **Innenraum [5]** für die getrennte [Untergrundansicht](underground-view.md). Diese schematische Ansicht erzeugt keine Erdarbeit und keinen Aushub. Die frühere [Hybridkammerprobe](underground-hybrid-probe.md) hat eigene Nachweise; freie 3D-Ausgrabung ist ein späteres Thema.

## Prüfstand und nächste Schritte

| Umfang | Tatsächlicher Nachweis |
| --- | --- |
| Native Gesamtsuite | **46/46 erfolgreich** in der letzten Suite nach der Live-Biom-Korrektur in rund 2,21 s; 44 ohne und zwei mit bekannten Warnungen aus alten Testpfaden. Darunter sieben neue Earthworks-Tests für Warteschlange, Reservierungen, vollständigen Lagerplatz, Kreislauf, Neustart, Revision/Transfer, beschädigte Snapshots und N3-Formintegral. |
| Untergrund-Datenvertrag | Drei native Tests bestanden; getrennte Editorbilder bestätigen Oberfläche/Schnitt/Innenraum/Rückkehr. Neun Terrain- und sechs Hüllen-Komponentenspuren je Ansicht bleiben gleich. [Eigener Bericht](../evidence/underground-view-test.json); keine echte Ausgrabung oder verpackte Ansichtspixel. |
| Gerenderter uncooked Kreislauf | Zwei getrennte Prozesse: **10/10 Create** und **12/12 Resume**. N2/0,75 m: 48 m³ beziehungsweise **86,4 t** ausgehoben, eingelagert und auf derselben Fläche wieder eingebaut. Am Ende Lager, Reservierung, Puffer und Lkw leer; sämtliche 1.011 beobachteten Materialbilanzen **0 g Fehler**. |
| Speichern während Arbeit | **12 t im fahrenden Lkw** exakt wiederhergestellt. Zweiter Checkpoint während ausstehender Kollision mit **6 t bereits eingebaut und 6 t im Puffer** ebenfalls exakt wiederhergestellt; drei weitere Loads ohne Verdopplung. Vollständige Recordhashes stimmen vor Weiterarbeit überein. |
| Tatsächliche lokale Bodenhöhe | **300 + 525 akzeptierte Kollisionsproben**, je 25 Punkte und drei stabile Durchläufe pro Prüfphase. Unabhängige Sollrechnung aus gespeicherter Referenz und ausgeführten Mengen; **5-cm-Gate**, maximal **4 cm** passender Fehler. Unfertige oder unpassende Anlaufproben wurden als Wartephasen behandelt. |
| Normale Controller-/Saveprobe | **EarthworksLab im normalen PIE**, Verifier aus: fehlender Slot als Hinweis, danach gültiges Ziel, Bestätigung und nativer Autosave. Drei Loads mit identischem kanonischem SHA-256 des Earthworks-Zustands; ein ungearbeiteter Plan bleibt pausiert, Transport aus. Diese drei Loads sind logische Restores. Zusätzlich bestätigten kalte Editorstarts denselben ungearbeiteten Plan, Pause und Transport aus mit gleichem Zustandshash. |
| Karte und Darstellungsassets | Eigene Karte gespeichert und zurückgelesen, Earthworks-Modus sowie tatsächliches Haupt-/Fernmaterial bestätigt; normale PIE-API-Probe auf dieser Karte. Schnittmaterial eingerichtet und grüne Biomoberfläche beim Wechsel und Rückweg visuell bestätigt. Neuer Karten-/Material-Cook und Start im verpackten Spiel bestanden. |
| Uncooked Neustartumfang | Zwei isolierte Prozesse auf **ConstructionLab mit Earthworks-Spielmodus**, `-game` und Offscreen-Rendering; normale Save-Dateien dabei unverändert. Davon getrennt neuer Cook und verpackter Kreislauf auf EarthworksLab bestanden; keine physische Eingabe-, Shipping- oder verpackte Pixelabnahme. |
| Frisch verpackter Kreislauf | **10/10 Create in 97,9 s + 12/12 Resume in 95,4 s** auf EarthworksLab. 965 Bilanzbeobachtungen mit **0 g**, 86,4 t Kreislauf; 300 + 525 akzeptierte Höhenproben, maximal 4 cm. Beladene Fahrt und Kollisionswarte-Checkpoint exakt erhalten, drei weitere Loads ohne Duplikate. Normale Saves unverändert. |

Der [bereinigte Bericht](../evidence/machine-earthworks-test.json) enthält Checks, Konten, Hashes und Messgrenzen. Der Lauf verwendete ein **beschleunigtes Prüfprofil**; seine rund 151 s/134 s Laufzeit sind keine Angabe zur normalen Baugeschwindigkeit. Die native Modellrechnung prüft N1/N3, Kapazitätsgrenzen und konkurrierende wartende Pläne zusätzlich; diese Fälle wurden nicht alle gerendert wiederholt.

Die Laufzeitprobe wies eine **veraltete Vorschau beim Bestätigen** atomar ab. Ein bereits gespeicherter Plan mit nachträglich verändertem Boden beim Arbeitsstart sowie die normale Revisionsbedienung benötigen noch ihre eigene Spielabnahme. Inerte Planung ist durch Konten, fehlende Höhenbrushes und lokale Bodenproben belegt; eine getrennte Bewuchs-Bildprüfung fehlt. Der Neustart wurde uncooked und cooked mit beladener Fahrt und ausstehender Kollision geprüft. Kalte normale Editorstarts bestätigten zusätzlich den ungearbeiteten wartenden Plan. Für den Restore hielt der Prüfaufbau weitere Simulation ausdrücklich bis zu seinen unabhängigen Proben an.

Exakte Modellgramm sind keine unabhängige Vermessung des Terrainmeshvolumens. Die Höhenproben betreffen das lokale Arbeitsfeld; unbeeinflusste Kontrollflächen außerhalb der Form wurden nicht separat gemessen. Native Altformat-Fixtures und unveränderte normale Saves sind keine pauschale Migration aller archivierten echten Spielstände. Die allgemeine unabhängige Read-only-Snapshotprobe erreichte in der normalen Controllerprobe ihr Komponentenlimit; direkte Controller-/Backenddaten und kanonische Earthworks-Hashes sind die dortigen Beobachtungspfade. Der frühere Grass-zu-Sand-Fehler ist durch Übernahme der tatsächlichen Live-Materialbindungen korrigiert und im Editor sichtbar nachgeprüft. [Bilder und Ansichtsprüfung](underground-view.md#der-geprüfte-ansichtswechsel) bleiben getrennt von physischen Maus-/Tastaturfällen; private Spielstände, Benutzerpfade, Projekt-/Pluginquellen und lizenzierte Assets gehören nicht in dieses Bundle.

Der fachliche Ausbau **Ebnen mit getrennten Abtrags- und Einbaumengen** ist nativ und im vollständigen gerenderten Uncooked-Neustartlauf geprüft (12/12 + 16/16 Checks). Die normale Ebnen-Controller-API bestand zusätzlich 15/15 Checks mit einem tatsächlichen alten Version-1-Absenkstand, inertem 325-cm-Zielplan und drei exakten Loads. Auch der frische Development-Cook/Stage/Archive und das anschließende verpackte Laufpaar dieser Erweiterung bestanden (12/12 + 16/16); Mengen und Endkonten stimmten mit Uncooked überein. Die separate normale sichtbare Ebnen-Demo mit agentengeprüftem Slate-Bild ist ebenfalls abgenommen (12/12 native + 9/9 externe Checks). Die [eigene Ebnenanleitung](flatten-machine-earthworks.md) ist für diesen begrenzten Vertrag stable; physische Eingaben und menschliche Prüfung sind nicht erfolgt. Die bisherigen 46er- und Kreislaufergebnisse auf dieser Seite gelten für Anheben und Absenken. Vor einer breiten Werkzeugumstellung die physischen Bedienfälle und zusätzliche Start-/Revisionsfälle prüfen. Der begrenzte erste Kreislauf ist einschließlich frischem Cook und Paket-Neustart abgenommen. Danach können Materialauftrag und Baugrund-/Straßenwerkzeuge an dieselbe Maschinenverwaltung angeschlossen werden. Bodenarten, Verdichtung, Holzressourcen, freie Logistik, mehrere gleichzeitige Maschinenzüge und Untergrund-Aushub sind weiterhin offen. Der [vereinbarte Scaping-Plan](../reference/scaping-machine-work-plan.md) hält diese Reihenfolge und ihre Abnahmegrenzen fest.

Der frische Build/Cook/Stage/Archive endete erfolgreich in rund **157,4 s**. Fünf geerbte nichtfatale Level-Blueprint-Warnungen zu ungültigen Actor-Verweisen bleiben dokumentiert; sie wurden in diesem Slice nicht repariert. Neue Karte, Schnittmaterialien und Radlader sind im Staging belegt. Der ungeklärte ElectroNick-Lkw und der schwere Liebherr sind dort nicht enthalten. Der Radlader bleibt eine animierte Darstellung ohne Chaos-Fahrzeugphysik oder geprüfte Schaufelinteraktion.
