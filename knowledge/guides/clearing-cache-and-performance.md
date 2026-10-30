---
type: Guide
title: Dauerhafte Rodung mit weniger Instanzscans verstehen
description: Den visuellen Rodungscache, seine Invalidierung und die getrennten Grenzen von Ressourcenidentität, Kollision und nativer Wiederherstellung nachvollziehen.
status: stable
tags: [shaderworld, citylab, vegetation, clearing, performance, persistence]
engine_version: "5.8.4"
plugin_version: "4.1"
generated:
  by: codex/gpt-6
  at: "2026-10-28T23:12:53Z"
evidence_scope:
  implementation: Projektcode und native ShaderWorld-4.1-Schreibpfade gelesen; kompakte unveränderliche Live-Snapshots nur für eigene visuelle Resource-HISMs implementiert
  native_tests: 36/36 native Tests bestanden, 34 ohne und zwei mit bekannten Warnungen; sechs Vegetationstests einschließlich echtem nativem Remove/Restore, Sparsecache, Legacyfallback und vollständigem CityLab-Ledger-Restore erfolgreich
  cooked_performance: Ein isolierter gerenderter cooked Windows-Development-Prozess mit acht Fenstern à etwa acht Sekunden und 0/1/10/100 Records bestanden; 248 Nachläufe und 156 erfolgreiche native Rayabfragen
  measured_speedup: Positive Rodungsnachläufe im Mittel 0,816–1,251 ms gegenüber historischen 19,850–22,061 ms; native Rayabfragen 0,315–0,548 ms gegenüber 20,433–21,025 ms, gleiche Laborszene und begrenzte Messkonfiguration
  not_tested: Neue GPU-Pixelabnahme, vollständige C-Vorschau-/Fokuseingabe, Streamingfahrt, große Rodungsbestände und Großweltlast
sources:
  - id: cache-proof
    resource: ../evidence/clearing-cache-test.json
    title: Bereinigter neuer Cachebenchmark, Vergleichszahlen und bestandene native Restoretests
  - id: baseline
    resource: ../evidence/clearing-performance-test.json
    title: Historischer isolierter cooked CPU-Benchmark vor dem visuellen Cache
  - id: implementation
    resource: "Originales Testprojekt UnrealMcpTest: Source/UnrealMcpTest/CityLabVegetationState.h/.cpp und CityLabVegetationTests.cpp; eigene Projektdateien nicht im öffentlichen Wissensbundle enthalten"
    title: Visueller Cachevertrag, stabile Ressourcenkennungen und vorbereitete native Regressionstests
  - id: benchmark
    resource: "Originales Testprojekt UnrealMcpTest: Source/UnrealMcpTest/CityLabClearingBenchmark.cpp und Tools/benchmark_clearing.py; eigener Benchmark mit additiven Cachezählern, Projektdateien nicht im öffentlichen Wissensbundle enthalten"
    title: Begrenzte Messfenster und getrennte Zähler für Live-Kandidaten und rohe Pufferplätze
  - id: native-contract
    resource: "Lizenzierte ShaderWorld-4.1-Installation: Source/ShaderWorld/Public/Component/SWHISMComponent.h, Private/Component/SWHISMComponent.cpp und Private/Component/SWFoliageInstancedSMeshComponent.cpp; Pluginquellen nicht im öffentlichen Wissensbundle enthalten"
    title: Virtuelle visuelle Publish-/Updatepfade, nichtvirtueller Kollisionsbatch und native FormerScale-Wiederherstellung
  - id: foundations
    resource: foundations-lab.md
    title: Bedienung und bisherige getrennte Bild-/Neustartnachweise der Einzelrodung
---

# Dauerhafte Rodung mit weniger Instanzscans verstehen

Der neue Cache reduziert die regelmäßige CPU-Baumprüfung und die native Auswahl unter dem Mauszeiger in unserer festen Laborszene deutlich: Rodungsnachläufe mit Records liegen im Mittel bei **0,82–1,25 ms**, zuvor bei rund **20–22 ms**. **Welche Bäume dauerhaft gerodet sind, bleibt weiterhin eine eigene gespeicherte CityLab-Liste.** Der Cache hält nur eine wiederverwendbare Sicht auf die gerade lebenden visuellen Instanzen. Native Tests und der isolierte cooked Vergleich sind bestanden; GPU-/Bedienungsgrenzen bleiben unten ausdrücklich getrennt.[^cache-proof]

## Warum diese Änderung nötig ist

Der bisherige [CPU-Benchmark](../evidence/clearing-performance-test.json) fand einen visuellen Pool mit **152.881 reservierten Plätzen**, aber nur **1.410 lebenden Bauminstanzen**. Zusammen mit dem Kollisionspool wurden bei vorhandenen Rodungsrecords regelmäßig **154.997 Plätze** gelesen und durchlaufen. Das kostete in diesem begrenzten Versuch rund **19,85–22,06 ms pro Rodungsnachlauf**; die native Rayauswahl lag bei rund **20,43–21,02 ms pro Aufruf**. Diese historischen Werte sind synchrone CPU-Aufrufzeiten aus genau einem Laborlauf.[^baseline]

Viele reservierte Plätze tragen eine Nullskalierung und zeigen keinen Baum. Bisher musste die Auswahl sie dennoch immer wieder kopieren und untersuchen. Der neue Cache liest einen geänderten visuellen Pool einmal und behält danach nur seine gültigen, nicht-null skalierten Transforms. Wiederholte Abfragen verwenden diese kompakte Liste. Ein Cacheaufbau liest weiterhin den ganzen Quellpuffer; häufige Regeneration kann diese Arbeit erneut auslösen.[^implementation]

## Was der Cache zuverlässig unterscheiden muss

Ein **HISM-Index** ist die aktuelle Nummer eines Platzes im Instanzpuffer. ShaderWorld kann diesen Platz nach Regeneration für einen anderen Baum verwenden. Deshalb ist er keine gespeicherte Ressourcenkennung.

Eine **CityLab-Ressourcen-ID** bindet Welt, Generator, Terrainprofil, Spawnable-/Meshasset und den ursprünglichen horizontalen Stammort. Eine reine Änderung der Bodenhöhe verändert diese Identität nicht. Der Cache speichert HISM-Indizes ausschließlich als flüchtige Zugriffsorte. Auch beim Cachetreffer prüft die Rodungslogik weiterhin die logische Ressourcenidentität; es wird keine Indexliste als Spielstand gespeichert.[^implementation]

Die kompakte Liste ist unveränderlich: Eine laufende Abfrage behält ihre bisherige Momentaufnahme, während eine folgende Abfrage nach einer Änderung eine neue erhält. Neue Daten dürfen nicht versehentlich über eine alte Liste ausgewählt oder unterdrückt werden.

| Änderung | Verhalten des eigenen visuellen Resource-HISM |
| --- | --- |
| Neue native visuelle Instanzen oder ein Batch mit geänderten Transforms | `SWNewAddInstances` beziehungsweise `SWNewBatchUpdateCountInstanceData` machen die alte Momentaufnahme ungültig. Der bestehende Incomingfilter unterdrückt weiterhin gespeicherte Rodungen vor diesem Publish. |
| Einzelner Transform wird geändert | Das virtuelle `UpdateInstanceTransform` macht die Momentaufnahme ungültig. Das erfasst auch den visuellen Owner-Aufruf aus nativem `RemoveInstance` und `RestoreInstance`. |
| `ClearInstances` wird angefordert | Der Cache wird ungültig. Bei einem verzögerten nativen Clear ist die Anforderung noch keine Zusage, dass alle Puffer bereits leer sind. |
| Nativer Speicherblock, Arrayadresse oder Anzahl der Plätze wechselt | Die nächste Abfrage baut eine frische Liste auf. Gleiche Platzzahl allein reicht nicht für einen Cachetreffer. |
| Unveränderter nativer visueller Puffer | Die nächste Abfrage verwendet die kompakte Liste erneut. |
| Alter, unversionierter Legacy-Puffer oder getrennter Proximity-Kollisionspool | Weiterhin frischer konservativer Read; diese Puffer erhalten keine Wiederverwendungszusage. |

Radiusauswahl, Rayauswahl und regelmäßiger Rodungsnachlauf nutzen dieselbe visuelle Momentaufnahme. Diagnose-Vollprüfungen und das Wiederherstellen eines älteren Rodungsledgers lesen dagegen weiterhin vollständige Puffer. Diese Änderung ist kein allgemeiner Raumindex für eine ganze Stadt.[^implementation][^native-contract]

## Was sich beim Spielen ändern soll

Die Bedienung bleibt wie in [Foundations](foundations-lab.md): **C** rodet den frisch entlang des Mausstrahls gewählten getaggten Baum, **K/F5** speichert und **L/F9** lädt. Die gelbe Zielbox ist eine Näherung über die transformierte Meshbox. Nur eigene getaggte Baumressourcen gehören zu diesem Werkzeug.

Für einen gezielten Sichttest nach erfolgreichem Build:

1. Öffne **Content → Maps → ShaderWorldFoundations**, starte **Play** und warte auf das tatsächlich gerenderte Terrain und den Bewuchs.
2. Wähle einen eindeutig erkennbaren Baum und eine benachbarte Kontrolle. Drücke **C**. Der gewählte Baum soll verschwinden; die Kontrolle soll erhalten bleiben.
3. Speichere mit **K/F5** und lade mit **L/F9**. Die Rodung soll erhalten bleiben.
4. Prüfe anschließend mit einem eigenen isolierten Teststand echte Vegetationsregeneration und einen frischen Spielprozess. Eine unveränderte Kamera oder ein erfolgreicher Speicherdialog ersetzt diese Probe nicht.

Dieser Ablauf ist hier eine Prüfanleitung. Er ist noch keine neue manuelle oder GPU-Abnahme der Cachefassung. Normale Spielstände bei automatisierten Tests erhalten; isolierte Messungen greifen auf keinen normalen CityLab-Slot zu.[^foundations][^benchmark]

## Native Wiederherstellung und unser vollständiger Ledger-Restore

ShaderWorld 4.1 speichert im nativen Collectable-Pfad bei `RemoveInstance` nur die frühere **Skalierung**. Durch das Schreiben einer Nullskalierung geht die ursprüngliche Rotation in dieser Matrix verloren. `RestoreInstance` liest diese Matrix und setzt die alte Skalierung zurück. Im kontrollierten nativen Test wurde aus **34° ursprünglicher Drehung eine native Restore-Drehung von 0°**. Der Cache stimmte dabei mit dem frisch gelesenen nativen Puffer bei einer Toleranz von **0,000001** überein. Quellbefund und Beobachtung zeigen, warum dieser native Pfad keinen vollständigen Originaltransform verspricht. Der Cache muss den tatsächlichen nativen Puffer abbilden; er repariert diese fremde Wiederherstellung nicht.[^native-contract]

Unser persistenter Rodungsrecord enthält dagegen den **vollständigen ursprünglichen Transform**. Beim Laden eines älteren CityLab-Zustands, in dem der Baum noch nicht gerodet war, stellt der Ledger-Restore Position, Rotation und Skalierung aus diesem Record wieder her. Der eigene native Test mit gedrehtem Zielbaum und unabhängigem, nichtuniform skaliertem Kontrollbaum ist bestanden. Er lädt einen Rodungsrecord, wärmt den versteckten Cache auf und lädt danach den älteren leeren Ledger: Der vollständige Originaltransform kehrt zurück, Kontrolle und zuvor gehaltene Momentaufnahme bleiben erhalten. Den nativen Slot-Aufruf `RestoreInstance` nicht mit dieser gespeicherten Ressourcenwiederherstellung gleichsetzen. Diese neue Abnahme ist ein kontrollierter **In-Memory-Recordrestore**, kein zusätzlicher Spielneustart mit normaler Save-Datei.[^implementation][^cache-proof]

Ein externer nativer Restore löscht außerdem keinen bestehenden CityLab-Rodungsrecord. Der nächste Rodungsnachlauf kann die wieder eingeblendete Ressource deshalb erneut unterdrücken. Die Invalidierung verhindert einen unbemerkt alten Cache, macht aus einem fremden Slot-API aber keine dauerhafte Buchhaltung.

## Technische Grenzen für die weitere Entwicklung

- **Game Thread:** Auswahl, Cachelesen und normale HISM-Änderungen gehören auf Unreals Game Thread. Die atomare Revision und Datenlocks erlauben keine beliebige gleichzeitige Änderung von Welt, Komponenten und logischem Rodungsledger durch Worker.
- **Direkte Pufferänderungen:** Wer die öffentlichen Pluginpuffer außerhalb der erfassten Methoden direkt überschreibt, muss am eigenen Resource-HISM ausdrücklich `InvalidateResourceSnapshot()` auslösen. Ein Überschreiben derselben Plätze bei gleicher Arrayadresse und -länge ist sonst nicht zuverlässig erkennbar. Neue Schreibpfade brauchen eine eigene Prüfung.
- **Kollision:** Die native Proximity-Kollision nutzt einen getrennten, nichtvirtuellen Batchpfad und wird weiter periodisch bereinigt. Eine vorübergehende unsichtbare Baumkollision bleibt möglich. Das Prüfintervall von **0,25 s** ist keine zugesagte obere Latenzgrenze.
- **Rendering:** `SWUpdateTree` stößt die native Renderaktualisierung an. Ein Refreshzähler oder korrekter CPU-Puffer belegt keinen fertigen GPU-Frame.
- **Leistung:** Der Cacheaufbau kann weiterhin einen großen Puffer scannen und dessen Datenlock belegen. Der stationäre Fall ersetzt keine Messung während Fahrt, Streaming oder vieler Änderungen. Große Rodungsbestände, vollständige UI-Vorschau und Gesamtframezeit bleiben getrennte Aufgaben.

## Prüfstand und Messwerte

| Nachweis | Stand dieser Fassung |
| --- | --- |
| Cache-/Invalidierungsvertrag im Projektcode und relevante native Schreibpfade | Gelesen und implementiert; kein Pluginpatch |
| Erneute native Suite einschließlich echtem nativen Remove/Restore und vollständigem Ledger-Restore | **36/36 bestanden**, 34 ohne und zwei mit bekannten Warnungen; alle sechs Vegetationstests ohne Warnung/Fehler |
| Isolierter cooked Benchmark mit 0/1/10/100 Rodungsrecords, jeweils ohne und mit nativer Rayauswahl | **Acht Fenster bestanden**, 248 Rodungsnachläufe und 156/156 erfolgreiche native Rays |
| Gemessene Beschleunigung gegenüber dem historischen Vollscan | Positiver Nachlauf **0,816–1,251 ms**, native Rayauswahl **0,315–0,548 ms** im Mittel; Einzelvergleich unten |
| Neue Sicht-/GPU-Abnahme der Einzelrodung und vollständigen C-Vorschau | Offen |

Der [neue bereinigte Bericht](../evidence/clearing-cache-test.json) bestätigt dieselben 152.881 visuellen und 2.116 Kollisionsslots mit anfangs je 1.410 lebenden Instanzen. In jedem positiven stationären Fenster wurde **ein visueller Cache wiederverwendet**, **kein visueller Snapshot neu aufgebaut** und nur der **2.116-Slot-Kollisionspuffer frisch gelesen**. Die lebenden Kandidaten aus Visual- und Kollisionspool zusammen betrugen 2.818, 2.800 und 2.620 für 1, 10 und 100 Rodungsrecords.[^cache-proof]

| Records | Rayauswahl | Nachlauf vorher → jetzt, Mittel in ms | Nachlauf jetzt, p95 in ms | Ray vorher → jetzt, Mittel in ms | Ray jetzt, p95 in ms |
| --- | --- | --- | --- | --- | --- |
| 0 | Aus | 0,001 → 0,001 | 0,001 | – | – |
| 0 | An | 0,001 → 0,001 | 0,001 | 21,025 → 0,410 | 0,351 |
| 1 | Aus | 19,850 → 1,105 | 1,297 | – | – |
| 1 | An | 20,437 → 0,816 | 0,996 | 20,433 → 0,315 | 0,395 |
| 10 | Aus | 21,329 → 1,251 | 1,635 | – | – |
| 10 | An | 21,468 → 1,235 | 1,568 | 20,843 → 0,501 | 0,582 |
| 100 | Aus | 22,061 → 1,179 | 1,430 | – | – |
| 100 | An | 21,715 → 1,185 | 1,369 | 20,985 → 0,548 | 0,636 |

Vorher und jetzt sind je **ein Durchlauf** auf derselben Laborszene; es gibt keine Wiederholungsstatistik oder Vertrauensintervalle. Im Nullrecord-Rayfenster lag ein Spitzenwert bei **5,151 ms**. Dadurch kann der Mittelwert über p95 liegen. Ein kalter Cacheaufbau wurde nicht gesondert instrumentiert; die Werte garantieren keine maximale Latenz.

Alle acht Fenster hielten gerodete Ziele CPU-visuell und in aktiver Kollision bei **0/0**, den unabhängigen Kontrollbaum bei **1/1** und unverändertem Transform. Der Abschluss bestätigte in drei unabhängigen Beobachtungen den CPU-visuellen Restore aller **101 ausgewählten Ressourcen**. Das ist kein neuer Pixelbeleg und keine separate abschließende Kollisionsabnahme jedes wiederhergestellten Baums. Ein normales Stadt-Save wurde nicht verwendet.[^cache-proof]

Der Lauf dauerte einschließlich ausgeschlossener Bereitschaft, Einschwingen und Restore rund **102,2 s**, davon **15,4 s** bis zur ersten echten Bereitschaft. Die tatsächlichen Aufrufraten lagen bei **3,87 Hz** für den Nachlauf und **4,87 Hz** für die native Rayauswahl. Das Profil zielte auf 4 beziehungsweise 5 Hz und holte verpasste Intervalle nicht in Bursts nach. Die vorgegebene 48er Framebegrenzung ist ein Messparameter, kein Leistungsversprechen.

Die Zähler unterscheiden ausdrücklich die Arbeit pro **Rodungsnachlauf**:

| Berichtsfeld | Bedeutung |
| --- | --- |
| `native_scanned_instances` bei `instance_visit_semantics = compact_live_candidates.v1` | Besuchte lebende Kandidaten; nicht mehr dieselbe Zählweise wie die vollständigen reservierten Slots im historischen Bericht. |
| `native_snapshot_source_slots` | Rohe Pufferplätze, die während dieses Rodungsnachlaufs für einen neuen Snapshot oder einen konservativen Fallback gelesen wurden. |
| `native_snapshot_cache_hits` | Wiederverwendete visuelle Snapshots während dieses Rodungsnachlaufs. |
| `native_snapshot_rebuilds` | Neu erzeugte Snapshots eigener visueller Resource-HISMs während dieses Rodungsnachlaufs. |
| `reapply_call_ms` und `ray_call_ms` | Gemessene synchrone CPU-Aufrufzeit des Nachlaufs beziehungsweise der nativen Rayauswahl. |

Die Quellslot-/Cachezähler erfassen den Rodungsnachlauf. Ein Cacheaufbau durch eine separate Rayauswahl liegt in deren CPU-Zeit und ist kein zusätzlicher Eintrag in diesen Nachlaufzählern. Insbesondere bedeuten null Nachlauf-Slots bei null Rodungsrecords nicht, dass die Rayauswahl keine Arbeit verrichtet. Historische und neue Zahlen erst nach Prüfung dieser Zählweise vergleichen.[^benchmark]

Dieser bestandene Vergleich ist ein begrenzter CPU-Nachweis mit fester Kamera und vorgegebenem Framecap. Er ist keine FPS-, GPU-Fertigstellungs- oder Großweltgarantie. Neue Regeneration, Fahrt, Eingaben und hohe Änderungsraten brauchen ihre eigenen Messungen; die offenen Sichtprüfungen sind nicht durch diese Zahlen ersetzt.

[^baseline]: [Historischer bereinigter Rodungsbenchmark](../evidence/clearing-performance-test.json), UE 5.8.4 und ShaderWorld 4.1; ein isolierter gerenderter cooked Windows-Development-Prozess vor dieser Optimierung.
[^implementation]: Eigene projektlokale Vegetationsverwaltung laut Quellenbeschreibung; sechs aktuelle Vegetationstests innerhalb der bestandenen 36er-Suite, Scope im neuen Cachebericht.
[^benchmark]: Eigener begrenzter Benchmark und Launcher laut Quellenbeschreibung; additive Cachezähler, strikte Reportvalidierung und erfolgreich beendeter isolierter cooked Lauf.
[^native-contract]: Gelesene lizenzierte native ShaderWorld-4.1-APIs laut Quellenbeschreibung; kein mitgelieferter Pluginquellcode.
[^foundations]: [Foundations-Anleitung](foundations-lab.md) mit bisherigen getrennten Bedienungs-, Bild- und Neustartnachweisen.

[^cache-proof]: [Neuer bereinigter Cachebericht](../evidence/clearing-cache-test.json), UE 5.8.4 und ShaderWorld 4.1; 36 native Tests und ein isolierter gerenderter cooked Windows-Development-Prozess mit acht Messfenstern.
