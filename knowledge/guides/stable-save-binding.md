---
type: Guide
title: Bauplatz nach einem neuen Build weiterbauen
description: Bekannte Bauplatzstände ausdrücklich in einen getrennten Format-8-Slot übernehmen, den Arbeitsstand prüfen und bei Problemen sicher zur alten Fassung zurückkehren.
status: stable
tags: [shaderworld, city-builder, persistence, migration, site-preparation]
engine_version: "5.8.4"
plugin_version: "4.1"
generated:
  by: codex/gpt-6
  at: "2026-10-30T00:05:16.235520+00:00"
evidence_scope:
  source: Gelesener Projektvertrag für getrennte Inhaltsprüfung und erhaltene Spielstandskennungen; kein mitgelieferter Quellcode.
  cpu: Früherer Profilstand mit 70 nativen Tests, davon 68 sauber und 2 bekannte Warnungen; 7 Datei-Kopie-Ablehnungstests im früheren und erneut 7 im korrigierten Profilstand bestanden.
  runtime: Drei bekannte Checkpoints je 16 Bridge-, 30 B2- und 30 C2-Checks bestanden; strenge physische C2-Fortsetzung, getrennte Nutzermigration und normales No-CSV-Speicher-/Lade-/Kaltstartpaar bestanden; sichtbarer normaler Start durch Betriebssystemfenster und Kartenlog belegt.
  limit: Bekannte Format-7-Stände der SitePreparation-V2-Karte; Herkunftsflags bleiben begrenzt. Normale Controller-APIs geprüft, keine physische Tasten- oder menschliche Pixelabnahme.
sources:
  - id: binding-contract
    resource: "Gelesene eigene Projektimplementierung zum SaveGame, zum expliziten Upgrade, zum Inhaltsprofil und zur geschützten Übernahme des ursprünglichen Kennungsraums; Projektquellen nicht im Bundle enthalten"
    title: Savebindung als gelesener Implementierungsvertrag
  - id: cook-versions
    resource: "Gelesene separat lizenzierte ShaderWorld-4.1-Implementierung für PreSave und Version von Biom und Spawnable; Quellen nicht im Bundle enthalten"
    title: Flüchtige Cook-Versionen und tatsächliche Inhalte
  - id: legacy-proof
    resource: "Gelesene Unreal-5.8-Asset-Registry- und Cook-Metadatenverträge für SavedHash, alte Package-GUID und CookedHash; Enginequellen nicht im Bundle enthalten"
    title: Aussagegrenzen der historischen Quellrevision
  - id: evidence
    resource: ../evidence/save-binding-test.json
    title: Bereinigte CPU-, Cook-, Physik- und normale Lebenszyklusnachweise
  - id: site-guide
    resource: site-preparation.md
    title: Bauplatz bedienen und bisherige Neustarttests einordnen
  - id: maintenance
    resource: ../maintenance.md
    title: Quellenbefund, praktischen Test und menschliche Prüfung unterscheiden
---
# Bauplatz nach einem neuen Build weiterbauen

Deine Rodung, bewegte Erde, Lkw-Ladung und das Haus sollen nach einer neuen Paketfassung erhalten bleiben. Dieser Ausbau ermöglicht dafür ein **ausdrückliches Übernehmen in einen neuen Spielstand** für die hier geprüften bekannten Bauplatzstände. Das alte Spiel und sein gespeicherter Stand bleiben gemeinsam erhalten.[^binding-contract]

**Aktueller Stand: Die begrenzte Savebindung ist abgenommen.** Drei bekannte Referenzstände bestehen je 16 Bridge-, 30 B2- und 30 C2-Checks in zwei neuen vollständigen Cooks. Die gesonderte physische Fortsetzung endet mit 21 entfernten Bäumen, erhaltenem Kontrollbaum, passendem Boden, genau einem physisch getroffenen Haus, 176,4 t Lager und drei weiteren Loads. Der normale Nutzerstand wurde getrennt übernommen. Auch Speichern und Laden über die normalen Controller-APIs und ein frischer Prozess ohne CSV bestehen: sechs Snapshots mit acht vollständigen Laufzeit-Datengruppen exakt gleich, beide Prozesse Exit 0. Der normale neue Start zeigt ein antwortendes eigenes Fenster und die richtige Karte. Menschliche Pixelbestätigung und physische Tasteneingaben bleiben offen.[^evidence]

## Ziel und Geltungsbereich

Der erste Ausbau gilt für **`/Game/Maps/ShaderWorldSitePreparationLab`**, unsere getrennte V2-Bauplatzkarte. Hier schreibt die neue Implementierung Format 8. Andere Labore behalten ihren bisherigen Schreibvertrag. Es gibt keinen allgemeinen Konverter für beliebige alte Welten, andere Seeds, geänderte Assets oder neuere Plugin-Versionen.[^binding-contract]

Das neue **Inhaltsprofil** prüft die tatsächliche Grundlage der Welt. Die ursprünglichen Kennungen des Spielstands halten ihre Geschichte zusammen: bereits entfernte Bäume, Bauaufträge, Materialkonten und festgehaltene Arbeitsreihenfolgen. Diese Kennungen bleiben erhalten.[^binding-contract]

## Voraussetzungen

- Unreal Engine 5.8.4 und ShaderWorld 4.1 in der hier beschriebenen Projektfassung.
- Der bekannte alte Format-7-Spielstand zusammen mit seiner passenden alten Paketfassung und den vorhandenen Prüfmetadaten.
- Das korrigierte Inhaltsprofil einschließlich nativer Standardassets. CPU-Vorprüfung, ausdrückliche Übernahme und natives Laden in zwei neuen vollständigen Cooks sind bestanden; die strenge physische Fortsetzung ist ebenfalls bestanden. Normales Speicher-/Lade-/Neustartpaar und normaler Fenster-/Kartenstart sind ebenfalls separat bestanden.
- Ein neuer Ziel-Slot in einer getrennten Datenablage. Alte Quelle und vorhandene Ziele werden nicht ersetzt.
- Die nachgewiesene neue C2-Paketfassung und der dafür freigegebene normale Startpfad; andere Paketfassungen benötigen eine eigene Prüfung.[^binding-contract][^evidence]

## So verwendest du den übernommenen Stand

Die Übernahme ist zunächst ein Werkzeug für die Projektbetreuung, noch kein Knopf im Bau-Menü. Ein Agent bereitet den geprüften neuen Stand vor. Du musst dafür keine C++-Dateien lesen oder Hashes bearbeiten.

1. **Im alten Spiel speichern und schließen.** `F5` ist der bestehende Speicherbefehl. Erst nach Ende der Sitzung wird die Quelle unveränderlich gesichert. Auch die passende alte Anwendung bleibt erhalten.
2. **Die Übernahme abwarten.** Das Werkzeug läuft getrennt mit Kopien der passenden alten Cook-Inhalte. Es prüft den alten Stand und schreibt ausschließlich einen neuen Format-8-Slot. Ein normaler Ladeversuch führt keine stille Konvertierung aus.
3. **Nach Freigabe die neue Demo öffnen.** Dafür dient `Tools/launch_stable_site_preparation_demo.ps1`; der aktuelle geprüfte Start verwendet die [überarbeitete UI2-Fassung](site-preparation.md#neue-baustellenleiste) bei unverändertem Terrainprofil. Der C2-Nachweis bleibt die erhaltene Migrations-/Physikgrundlage; **-PreviousBuild** startet diese bewahrte Fassung. Die neue UI2-Abnahme bestätigt zusätzlich alle acht vollständigen Recordgruppen des bestehenden v8-Nutzerstands über normale F5/F9-Funktionen und kalten Neustart. Der Startpfad benutzt eine eigene Datenablage und verweigert den Start, solange seine erforderlichen echten Abschlussbelege fehlen. Der bisherige Startpfad bleibt der alten passenden Demo zugeordnet.
4. **Den Zustand vergleichen.** Stimmen Arbeitsfortschritt, verbleibende Bäume, Ladung, Lager und Haus mit dem gesicherten Ausgangspunkt überein? Bei Teilrodung muss nur die Restarbeit übrig sein. Ein beladener Lkw darf seine Ladung nicht verlieren.
5. **Weiterbauen, speichern und neu starten.** Arbeit und Transport wie in der [Bauplatzanleitung](site-preparation.md) starten. Mit `F5` speichern, das Spiel schließen und über denselben neuen Startpfad erneut öffnen. `F9` ist der bestehende Ladebefehl innerhalb der laufenden Sitzung.[^binding-contract][^site-guide]

Die Speicher- und Ladefunktionen hinter `F5` und `F9` wurden über die normalen Controller-APIs ausgeführt und anschließend in einem zweiten normalen Prozess geprüft. Das bestätigt keine physischen Tastendrücke. Der freigegebene Startpfad wurde ohne Computer Use geöffnet; sein eigenes Fenster antwortete und der Kartenlog bestätigte die richtige Spielkarte. Eine menschliche Pixel- und Eingabenprüfung steht separat aus.[^evidence]

## Was die bisherigen Übernahme- und Ladeprüfungen zeigen

Drei bekannte Ausgangsstände wurden getrennt geprüft: **Teilrodung, beladener Transport und fertiges Haus**. Die Bridge nutzt die neue native Anwendung mit Kopien der passenden alten Cook-Inhalte. Sie schreibt jeweils einen neuen Format-8-Slot mit Schema 1 und tatsächlichem Inhaltsprofil. Alle drei Übernahmen bestehen je 16 Prüfungen; die logischen Nutzdaten außerhalb der drei Hüllfelder und die kopierten Quellen bleiben unverändert.[^evidence]

Anschließend wurden die drei neuen Stände im **frisch vollständig gecookten Build B** geladen. Cook, Stage und Archivierung bestanden in 158,65 Sekunden BuildCookRun-Zeit, ohne Wiederverwendung des alten Cooks. Die nativen Ladeprüfungen bestehen je 30 Checks: vollständiger logischer Zustand, drei wiederholte Loads desselben Ursprungs und unveränderte geprüfte Dateien. Zwei ungültige Stände lassen die leere Welt mit ihren ursprünglichen Bindungen zurück. Vier weitere Fälle werden bei vorhandenem logischem Zustand atomar abgewiesen: falsches Profil, fremde Karte, falsches Schema und anderer Weltursprung.[^evidence]

Auch der zweite vollständige Cook **C** bestand: 103,79 Sekunden BuildCookRun, Exit 0. Alle drei Stände bestehen erneut je 30 native Prüfungen einschließlich Ladeablehnungen und wiederholter Loads. Zwischen B und C änderten sich alle 13 beobachteten nativen Biom-/Spawnable-Versionen tatsächlich; das reale Inhaltsprofil und die vollständigen logischen Daten blieben gleich. Die geprüften Ziel-Dateihashes stimmen über Bridge, B und C überein, normale Slots blieben unverändert. Dies bestätigt den vorgesehenen Unterschied zwischen flüchtigen Cook-Kennungen und gebundener Weltgrundlage für diese bekannten Referenzstände.[^evidence]

Zusätzliche Proben zeigten: Geänderte Kollisions- und Pflanzendichtewerte ändern das Profil; Zurückstellen liefert das ursprüngliche Profil wieder. Ein nicht erfasstes flüchtiges Material wird abgewiesen. Der gesonderte physische Lauf hat inzwischen beide Arbeitswege bis zum Ende fortgesetzt: 21 gerodete Ressourcen sind weder sichtbar noch kollidierend, der Kontrollbaum bleibt erhalten, Boden und Haus sind physisch geprüft. Beide Endzustände und drei zusätzliche Loads erhalten dieselbe alte geprüfte Geschichte. Die normale Nutzerdemo bleibt davon getrennt.[^evidence]

## Erwartetes Ergebnis und Sicherheitsnetz

Der neue Stand enthält dieselben logischen Daten: ursprünglicher Weltursprung, Kennungen der Aufträge und Ressourcen, eingefrorene Baumreihenfolge, bereits gerodeter Anfang dieser Reihenfolge, Plan-Fingerprints und Materialmengen in Gramm. Bei der ausdrücklichen Übernahme ändern sich nur drei Hüllfelder: Formatversion, Bindungsschema und Kompatibilitätsprofil. Auch der gespeicherte ursprüngliche Prozessnachweis bleibt erhalten.[^binding-contract]

Ein fehlerhafter Stand soll vollständig abgewiesen werden, bevor er eine laufende Welt verändert. Einen anderen Weltursprung darf nur eine noch leere Sitzung übernehmen. Normales erneutes Laden desselben Ursprungs bleibt auch bei laufender Arbeit vorgesehen.[^binding-contract]

**Zur alten Fassung zurückkehren:** Die neue Testsitzung schließen und die bewahrte alte Demo mit ihrer alten Datenablage öffnen. Den neuen Slot nicht über die alte Quelle kopieren. Eine automatische Rückkonvertierung von Format 8 nach Format 7 gehört nicht zu diesem Ausbau.

## Warum ein neuer Cook bisher störte

Ein **Cook** bereitet Assets für das verpackte Spiel auf. ShaderWorld erzeugt dabei neue interne `Version`-Kennungen für Biome und Spawnables. Diese Kennungen waren Teil unserer bisherigen Geländebindung. Dadurch konnte ein neuer Cook einen alten Stand ablehnen, obwohl seine maßgeblichen Projektassets unverändert waren. Frühere Neustarterfolge bleiben Nachweise für ihre jeweils geprüfte Paketfassung.[^cook-versions][^site-guide]

Die neue semantische Prüfung nimmt ausschließlich diese zwei bekannten nativen `Version`-Felder aus. Tatsächlicher Seed, Terrain-, Kollisions-, Dichte-, Generator- und Materialzustand bleiben gebunden. Das Profil liest die wirklichen aktuellen Assets auch nach Übernahme der alten Spielstandskennungen. Es darf seine Kompatibilität nicht aus übernommenen Kennungen selbst ableiten.[^binding-contract]

Zusätzlich erhalten die erfassten aktuellen Quellassets samt Begleitdaten und den vorgesehenen Code-, Shader- und Konfigurationsgrundlagen einen SHA256-Nachweis. Ein unveränderter Assetpfad reicht damit nicht: Auch eine neue Textur oder Materialfunktion am gleichen Pfad wird erkannt. Der Dateivergleich ist konservativ; schon erneutes Speichern kann Bytes ändern und eine gesonderte Kompatibilitätsentscheidung nötig machen.[^binding-contract]

## Was wir über die alte Fassung belegen können

Die historischen Cook-Metadaten enthalten sowohl moderne Inhalts-Hashes als auch ältere Revisions-GUIDs. Eine gleiche alte GUID bezeichnet die bekannte serialisierte Revision unter normalem Speichern und Reimport in Unreal. Sie ist **kein kryptografischer Beweis aller historischen Quelldateibytes**. Absichtliche Byteänderungen unter Beibehaltung einer alten GUID deckt dieser historische Nachweis nicht ab.[^legacy-proof]

Für wenige bereits gebackene Editorquellen, ein Editor-Icon und das beim Kompilieren verwendete Standardmakro gibt es gesonderte begrenzte Regeln. Der Makrofall benötigt zusätzlich den tatsächlichen Vergleich der kompilierten Verbraucher in den alten und neuen Laufzeitfassungen. Dieser begrenzte Vergleich ist über die übereinstimmenden tatsächlichen Profile von alter Bridge, B2 und C2 für die drei Referenzstände belegt; die Manifestgeneration allein führt ihn nicht aus. Das korrigierte Profil erfasst 366 aktuelle Zukunftspakete. 346 historische Quellrevisionen passen: 56 moderne Inhalts-Hashes und 290 alte GUIDs. Weitere 18 gebackene Editorquellen, ein Icon und ein Makropaket bleiben ausdrücklich begrenzte Sonderfälle. Die zwei kompilierten Makroverbraucher sind im geprüften Laufzeitvertrag enthalten.[^evidence]

Die Prüfung der Engine-, Plugin- und Shadergrundlage verankert die feste initiale Codebasis dieser bekannten, vertrauenswürdig unveränderten Sitzung. Ein vollständiger historischer Byte-Nachweis des Herstellerquellcodes wurde dadurch nicht nachträglich gewonnen. Die Herkunftsflags bleiben entsprechend eingeschränkt. Die ausgeführten nativen und physischen Tests der alten Referenzstände ergänzen diesen begrenzten Herkunftsnachweis; sie ergeben keine allgemeine Migrationsgarantie.[^binding-contract][^evidence]

## Ein sicher abgewiesener Testaufbau

Beim ersten C-Prüflauf war ein absichtlich ungültiger Test-Slot aus der B-Phase noch vorhanden. Die Schutzprüfung brach mit `negative_slot_is_new_and_private` ab; dies war ein Fehler der isolierten Testeinrichtung, kein abweichender Weltinhalt. Der Fehlbericht bleibt erhalten. Die Wiederholung nutzte eine neue private Datenablage mit bytegleichen Quell- und Zielkopien, denselben Slotnamen und unveränderten gespeicherten Kennungen. C++-Code, Profil und Pakete wurden dafür nicht geändert. Danach bestanden alle drei C-Fälle. Normale Spielstände werden für diesen Testfehler nicht gelöscht oder umgeschrieben.[^evidence]

## Physische Wiederaufnahme und früherer Fehlversuch

Im ersten physischen Versuch konnten beide Arbeitswege fertiggestellt werden; Boden, Bäume und Materialbilanz bestanden ihre strengen Prüfungen. Beim zweiten wiederholten Load war genau ein Haus vorhanden und der logische Zustand unverändert, sein Kollisionsnachweis schlug jedoch fehl. Der gesamte Lauf bleibt deshalb **fehlgeschlagen**. Ein vorhandener Actor allein beweist kein physisch fertiges Haus.[^evidence]

Laut Untersuchung der Projektimplementierung wartet die Produktion nach dem Laden bereits auf drei erfolgreiche Bodenprüfungen, bevor sie die Hauskollision freigibt. Der Prüfer hatte dieses bestehende Gate an zwei Stellen nicht abgewartet. Seine neue Fassung wartet darauf und behält alle bisherigen physischen Prüfbedingungen bei. Game 4 bestand den Build in 97,04 Sekunden; anschließend wurden B2 und C2 vollständig neu gecookt und die nativen Daten-/Ladeprüfungen erneut bestanden. Der erneute C2-Lauf bestand danach tatsächlich: zwölf strenge Checks in 291,34 Sekunden, Prozess-Exit 0 und drei wiederholte Loads. Alle acht alten historischen Modellhashes passen; das Lager endet mit exakt 176.400.000 g, Puffer und Lkw leer, alle 2.149 beobachteten Modellbilanzen mit 0 g Fehler. 24 von 28 Bodenabfragesätzen wurden akzeptiert: 6.936 Messungen an 289 Positionen, maximal 1,00023 cm Höhenabweichung. Vier frühere Sätze mit fehlendem Bodentreffer beziehungsweise laufender Aktualisierung wurden wiederholt und zählen nicht als Erfolg. Das ist eine örtliche Stichprobe, keine gesamte Oberflächen- oder unabhängige Meshmassenprüfung. Frühere B/C-Erfolge und der Fehlversuch bleiben getrennt erhalten.[^evidence]

## Normales Speichern, Laden und erneutes Öffnen

Nach der getrennten Übernahme wurde eine einmalige neue Startkopie erzeugt. Zwei weitere normale Prozesse prüften deren Kopien ohne CSV und ohne Prüfactor: zuerst Speichern und Laden über die normalen Controller-Funktionen, anschließend ein kalter Neustart. Vier plus zwei Snapshots enthalten dieselben acht vollständigen Rohdatengruppen, jeweils 0 g Modellbilanzfehler. Beide Prozesse endeten sauber mit Exit 0; die alten normalen Spielstände, die vorbereitete Demoquelle und das Paket blieben unverändert. Der Vergleich von SaveGame und Laufzeit nutzt den vorhandenen Parser mit Standardwertbehandlung; dies ist keine neue Aussage zur binären Fließkommapräzision.[^evidence]

Ein erster Prüftreiber hatte trotz sauberem Spielprozess nur den erwarteten Log-Marker nicht gefunden. Sein Gesamtfehler bleibt bestehen. Ausschließlich die private Prüfer-Logkonfiguration wurde ergänzt; der vollständige neue Zwei-Prozess-Lauf bestand danach. Der frühere CSV-bezogene späte Exitfehler wird dadurch nicht als gelöst umgewertet. Der abschließende normale Launcherstart erfolgte ohne Computer Use und ohne Offscreenmodus. Betriebssystem und Kartenlog belegen das antwortende eigene Fenster und die richtige Karte; das Spiel blieb zum Ausprobieren geöffnet. Das ist keine menschliche Bild- oder physische Tastaturabnahme.[^evidence]

## Fehlerhilfe

| Beobachtung | Was tun? |
| --- | --- |
| Altstand verlangt ausdrückliches Upgrade | Alte passende Demo und Quelle behalten; den getrennten Übernahmeweg verwenden lassen. Nicht den normalen Slot löschen. |
| Falsche Karte, Seed oder Weltgrundlage | Richtige Ausgangsfassung prüfen. Kennungen und Hashes nicht von Hand ersetzen. |
| „Asset fehlt“ in der geprüften Save-Abhängigkeit | Die Projektbetreuung muss zusätzlich zu Registry-Verweisen die nativen Konstruktor-Standardassets als Profilwurzeln erfassen und ihre historische Quellrevision erneut gegen den alten Nachweis prüfen. Keine Saves umhashen und keine Kennungen ersetzen. Danach Profil, Vorprüfung und Laufzeitprobe wiederholen. |
| Prozess endet mit 0, Bericht meldet einen Fehler | Den nativen Fehler klären; Exit 0 allein genügt nicht. Die erste Bridge-Vorprüfung zeigte genau diesen Unterschied. |
| Neuer Ziel-Slot existiert bereits | Einen weiteren neuen Ziel-Slot verwenden. Vorhandene Dateien bleiben erhalten. |
| Fremder Weltursprung trifft laufende Arbeit | Den Stand in einer frischen Sitzung öffnen. Die laufende Arbeit darf nicht verdrängt werden. |
| Asset-, Plugin-, Engine- oder Terrainlogik geändert | Änderung gesondert bewerten und ihre Migration planen. Dieses Werkzeug gibt Änderungen nicht pauschal frei. |
| Daten geladen, aber Bewuchs oder Kollision noch nicht bereit | Die vorhandenen örtlichen Bereitschaftsprüfungen abwarten. Gültige Daten beweisen keine allgemeine GPU- oder Streaming-Bereitschaft. |
| Später Absturz beim instrumentierten Beenden | Rohbericht behalten; der frühere CSV-bezogene Spätabsturz ist hier nicht als gelöst bestätigt. Neue Tests ohne CSV-Instrumentierung getrennt auswerten. |

## Nachweise und ihre Grenzen

Die aktuellen Cook-Zeiten unten gehören den abschließenden Archiven **B2/C2** mit Game 4. Frühere B/C-Archive und ihre Datenprüfungen bleiben historische Belege; ihre Zeiten werden nicht der neuen EXE zugeschrieben.

Der [bereinigte Beleg](../evidence/save-binding-test.json) enthält die konkreten CPU-Ergebnisse und ihre Profilfassung. Deren Umfang darf nicht mit einer später geänderten Inhaltsmenge gleichgesetzt werden.

| Prüfebene | Vorliegendes Ergebnis |
| --- | --- |
| Gelesene Implementierung | Trennung von Inhaltsprofil und ursprünglichen Kennungen; ausdrücklicher neuer Ziel-Slot; geschützte Übernahme und Ablehnung. |
| Nativer CPU-Satz | 70 Tests: 68 sauber, 2 bekannte Warnungen, keine fehlgeschlagenen oder offenen Tests. Zugehörige Editorfassung im Beleg abgegrenzt. |
| Datei-Kopie-Negativtests | Je 7 von 7 Änderungen im früheren 365- und korrigierten 366-Pakete-Profil abgewiesen; Originalquellen unverändert. Das ist kein neuer Cook- oder physischer Nachweis. |
| Erste Laufzeit-Vorprüfung | Fehlgeschlagen vor der Migration: fehlendes natives Standardmaterial; Bericht `success=false` trotz Prozess-Exit 0. |
| Korrigiertes Profil | Generation und unabhängige CPU-Vorprüfung bestanden: 366 Pakete, davon 346 passende historische Quellrevisionen. Native Standardmaterial-Wurzel ergänzt. |
| Begrenzte A7→8-Bridge-Probe | Teilgerodeter bekannter Stand: 16/16 native Checks, Prozess-Exit 0, Quelle und Nutzdaten erhalten. Weiterhin alte kopierte Cook-Inhalte; kein Laden in neuem Cook. |
| A7→neuer-Cook-B8: native Nutzdaten und Laden | Drei getrennte Referenzstände bestanden: je 16 Bridge- und 30 B-Checks, Gesamtprüfer Exit 0. Das ist noch keine physische Fortsetzung. |
| Zwei neue vollständige Cooks | B 158,65 s und C 103,79 s, beide Exit 0 ohne SkipCook. Drei Checkpoints je 30 B- und 30 C-Checks, 13/13 beobachtete native Versionen B→C geändert; Inhaltsprofil und logische Daten gleich. |
| Physische Wiederaufnahme | Finaler C2-Lauf bestanden: zwölf Checks, beide Restarbeiten abgeschlossen, 21 Ressourcen, Kontrollbaum, Boden, Hauskollision und drei Loads; 176,4 t Lager/0 g Modellbilanzfehler. Erster Hausbereitschaftsfehler bleibt historisch. |
| Ungültige Stände über den echten Ladeweg | In B und C bestanden: je Referenzstand zwei Ablehnungen mit exaktem Rückweg der leeren Welt und vier atomare Ablehnungen bei vorhandenem logischem Zustand. |
| Normaler Nutzerstand | Getrennte ausdrückliche Übernahme 16/30 bestanden, alte Quelle/andere Saves/Archiv unverändert, einmalige neue Startkopie vorbereitet. |
| Neue normale Demo und Neustart | Normale Controller-APIs für Speichern/Laden sowie kalter zweiter Prozess ohne CSV bestanden; vier plus zwei Snapshots mit acht vollständigen Rohdatengruppen identisch, 0 g Bilanzfehler, beide Prozesse sauber Exit 0. Erster fehlgeschlagener Log-Harnesslauf bleibt separat erhalten. |
| Sichtbarer normaler Start | Freigegebener C2-Launcher ohne Offscreenmodus: eigenes antwortendes Hauptfenster, richtige Karte und keine Startupfehler belegt; keine menschliche Pixel- oder physische Eingabenabnahme. |

Gleiche Modell-Hashes beweisen keine sichtbaren Bäume oder passende Kollision. Ein physisch erfolgreicher Neustart allein beweist wiederum keinen Wechsel zwischen zwei neuen Cooks. Diese Nachweise bleiben getrennt; menschliche Prüfung wird erst nach einer tatsächlichen dokumentierten Bestätigung eingetragen.[^maintenance]

[^binding-contract]: Gelesener eigener Projektvertrag; ausgeführte begrenzte Laufzeitprüfungen und verbleibende Bediengrenzen im Beleg getrennt ausgewiesen.
[^cook-versions]: Gelesene separat lizenzierte ShaderWorld-4.1-Implementierung, nicht im Wissensbundle enthalten.
[^legacy-proof]: Gelesener Unreal-5.8-Asset-Registry-Vertrag; eine alte Revisions-GUID ist kein historischer Byte-Hash.
[^evidence]: Bereinigte CPU-, Profil-, Cook-, physische und normale Lebenszyklusnachweise; fehlgeschlagene Vorversuche bleiben erhalten, menschliche Eingabenprüfung ist nicht erfolgt.
[^site-guide]: Bestehende Bauplatzanleitung mit ihren historischen, jeweils begrenzten Prüfungen.
[^maintenance]: Regeln dieser Wissensbasis für nachprüfbare Aussagen und tatsächliche menschliche Bestätigungen.
