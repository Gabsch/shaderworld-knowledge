---
type: Guide
title: Grundstück durch Rodung und Erdarbeit zum Bauplatz vorbereiten
description: Einen Bauplatz planen, Bäume dauerhaft roden lassen, Erde über das gemeinsame Lager bewegen und anschließend das Testhaus setzen.
status: stable
tags: [shaderworld, city-builder, site-preparation, clearing, earthworks, persistence]
engine_version: "5.8.4"
plugin_version: "4.1"
generated:
  by: codex/gpt-6
  at: "2026-10-30T01:30:33Z"
verified:
  by: codex/gpt-6
  at: "2026-10-30T01:30:33Z"
  scope: Format-9-Ergänzung gegen gelesene Projektverträge, getrennte Create-/Resume-/Migrationsberichte und normalen Spieler-F5/F9-/Kaltstartbericht geprüft; historische Nachweise ihren Fassungen zugeordnet. Normaler sichtbarer Fenster-/Kartenstart separat bestätigt; keine physischen Eingaben oder menschliche Abnahme.
evidence_scope:
  source: Neue Auftragskarten und auf das aktive Spiel begrenzter Tab-Prozessor; getrennte V2-Laborkarte mit BlueAndBounds1-Biomkopien und eigenem Slot eingerichtet; aktueller Controller- und Setupvertrag gelesen. Altassets und bisherige Spielstände bleiben erhalten.
  prior_verification: Vorheriger Quellstand bestand Uncooked-Neustartpaar, native 60er-Suite und normale Controller-/Kamera-API. Diese Ergebnisse und Bilder sind historisch genau diesem Stand zugeordnet.
  runtime: V2-Einrichtung mit elf neuen Assets und unveränderten Legacydateien geprüft; native V2-Suite und wiederholte Einrichtung bestanden; vollständige Uncooked-/Cooked-Neustartpaare bestanden; normale V2-Startdaten exakt wiederhergestellt; separate normale Prozesse ohne CSV-Instrumentierung sauber beendet. CSV-instrumentierter Exit bleibt fehlgeschlagen; passender Demo-Startspielstand und sechs Paketdateien versiegelt vorbereitet; normaler Launcherstart mit reagierendem eigenem Fenster und korrekter Spielkarte bestanden; physische Eingaben und menschliche Pixelabnahme offen. Historische Nachweise gelten ihrer früheren Sourcebasis.
  ui_runtime: UI2 mit einem nativen Eingabetest, 38 plus 40 echten Slate-Checks und vier plus zwei exakten normalen Nutzerstand-Snapshots geprüft; beide UI-Originalbilder vom Agenten visuell geprüft.
  replan_player_lifecycle: Übernommener aktueller Format-9-Spielerstand über normale F5/F9-Funktionen und kalten zweiten Prozess geprüft; vier plus zwei vollständige Rohdaten-Snapshots mit acht exakt gleichen Gruppen, zwei reguläre Exits 0 ohne CSV oder Verifikationsmodus.
  limit: Keine globale GPU-/Bewuchs-Fertiggarantie, keine physische Eingabe- oder menschliche Abnahme. Holz und allgemeine Logistik offen; die hier geprüfte UI2-Fassung besitzt noch keinen expliziten Replanpfad nach begonnener Rodung. Format 9 besitzt einen getrennten Umplanungsnachweis mit 17/18 gerenderten Checks und zehn bekannten UI2-Migrationschecks; frühere UI2-Nachweise bleiben historisch.
sources:
  - id: replan-guide
    resource: replan-building-sites.md
    title: Begrenzte Format-9-Umplanung mit Create-, Resume- und bekannter UI2-Migrationsprüfung
  - id: ui-proof
    resource: ../evidence/earthworks-ui-test.json
    title: Neue Auftragsleiste, tatsächliche Slate-Ereignisse und unveränderter Nutzerstand über Neustart
  - id: tab-focus
    resource: "Nutzermeldung mit blau fokussiertem Kameraregler am 29. Oktober 2026; eigener gelesener Source/UnrealMcpTest/CityLabEarthworksGameMode.cpp: SCityLabEarthworksPanel, BlocksKeys, KeysAllowed, SetupInputComponent, SelectNextJob und QueueText; Unreal Slate NavigationConfig und SlateApplication. Private Aufnahme und separat lizenzierte Quellen nicht im Bundle enthalten"
    title: Historischer gemeldeter Tab-Fokusfehler und damaliger Maus-Workaround
  - id: stable-save-guide
    resource: stable-save-binding.md
    title: Bekannte Referenzstände ausdrücklich übernehmen und über neue Cooks laden
  - id: stable-save-evidence
    resource: ../evidence/save-binding-test.json
    title: Getrennte CPU-, Bridge-, B2/C2-, Physik- und normale Lebenszyklusnachweise
  - id: own-site-model
    resource: "Eigene gelesene Projektimplementierung: Source/UnrealMcpTest/CityLabSitePreparationModel.h/.cpp, CityLabSitePreparation.h/.cpp, CityLabEarthworksGameMode.h/.cpp, CityLabEarthworks.h/.cpp und CityLabPersistence.h/.cpp. Projektquellen nicht im Bundle enthalten"
    title: Bauvorbereitung, Controller, lokaler Bewuchsrestore und Speicherdaten als eigener Quellvertrag
  - id: v2-biome-contract
    resource: "Eigene gelesene Tools/setup_site_preparation_lab.py und Tools/repair_city_biome_density.py sowie privater Setupreport b2ee64eabcd74f13836d182ea5915351: elf frische Assets, vollständige Erhaltung der Legacydateien/Metadaten und Spielstände. Separat lizenzierte native ShaderWorld-Funktionen nur als lesender Quellbefund; Projekt-/Pluginassets und Quellcode nicht im Bundle enthalten"
    title: BlueAndBounds1, getrennte Map und feste Erhaltungsgrenzen
  - id: build-bound-save-source
    resource: "Gelesene ShaderWorld-4.1-Installation: Source/ShaderWorld/Private/Data/ShaderWorld_Biom.cpp und ShaderWorld_Spawnable.cpp, beide PreSave erzeugen Version neu; Public/Data zugehörige Version-Properties. Eigene CityLabPersistence.cpp bindet Biome-/Spawnable-Versionen ausdrücklich sowie über ObjectSettings/CPF_Edit in TerrainSettingsIdentity. Separat lizenzierte Quellen nicht im Bundle enthalten"
    title: Quellbefund zur derzeitigen Savebindung an den Cook
  - id: biome-rules
    resource: foundations-lab.md
    title: Bestehende Höhen- und Hangregeln der fünf Projektbiome
  - id: proof
    resource: ../evidence/site-preparation-test.json
    title: Aktuelle V2-Neustartnachweise, begrenzter normaler Launcherstart und getrennte historische Belege
  - id: clearing
    resource: clearing-cache-and-performance.md
    title: Dauerhafte Ressourcenkennungen und NoGrowth unterscheiden
  - id: flatten
    resource: flatten-machine-earthworks.md
    title: Getrennte Aushub-/Einbauphasen, Materiallager und begrenzte Erdarbeit
  - id: plan
    resource: ../reference/scaping-machine-work-plan.md
    title: Vereinbarter Slice C und noch folgende Oberflächenarbeit
---
# Grundstück durch Rodung und Erdarbeit zum Bauplatz vorbereiten

Im getrennten **SitePreparationLab** bereitest du einen Bauplatz als zusammenhängenden Auftrag vor: **planen → roden → Erde bewegen → Boden prüfen → Testhaus setzen**. Die neue Karte hat eigene Biomkopien und einen eigenen Spielstand. Einrichtung, native Tests und vollständige Uncooked- sowie Development-Cooked-Neustartpaare dieser V2-Fassung sind geprüft. Die aktuelle gemeinsame Controller-/Kamera-API ist separat auf der erhaltenen EarthworksLab-Karte geprüft. Die normalen Startdaten werden korrekt geladen; getrennte normale Starts ohne CSV-Instrumentierung enden sauber. Ein später Exitfehler des CSV-Prüflaufs bleibt offen. Ein passender Startspielstand und die versiegelte Demo sind vorbereitet. Der normale Launcherstart mit reagierendem eigenem Fenster und korrekter Spielkarte ist ebenfalls bestanden. Die Anleitung ist für diesen begrenzten PoC **stable**; physische Eingaben und menschliche Pixelabnahme stehen separat aus.[^v2-biome-contract][^proof]

**Neuer Format-9-Ausbau getrennt geprüft:** [Einen begonnenen Bauplatz umplanen](replan-building-sites.md) erhält feste Fläche, Rodung, ausgeführte Erde und Material. Die neue Fassung besteht 17 Create- und 18 Resume-Checks samt kaltem Start und drei normalen Loads. Die ausdrückliche bekannte UI2-Kopiermigration in ein neues Ziel besteht zehn Checks. Die folgenden V2-/UI2-Nachweise bestätigen weiterhin ihre jeweiligen früheren Fassungen.[^replan-guide]

## Voraussetzungen

Benötigt werden CityLab mit Unreal **5.8.4**, ShaderWorld **4.1**, dem aktuellen Projektmodul und **/Game/Maps/ShaderWorldSitePreparationLab**. Öffne diese vorbereitete Karte und starte **Play**. Das öffentliche Wissensbundle enthält Anleitung und Nachweise; Karte, Projektquellen und lizenzierte Assets liegen im ursprünglichen Projekt.

Die neue Karte verwendet **CityLabSitePreparation** als normalen Speicher-Slot. Sie startet bei dessen erster Verwendung frisch mit **0 t Lagerbestand**: zuerst abtragen und einlagern, danach Material einbauen. Das bisherige **ShaderWorldEarthworksLab** mit Slot **CityLabEarthworks**, seinen fünf Aufträgen und rund 6,4 t bleibt getrennt erhalten. Alte Saves werden nicht umgebunden oder ersetzt. Eine verpackte V2-Demo bekommt außerdem einen eigenen UserDir; ein alter Spielstand mit anderer Welt-/Materialbindung wird sicher abgewiesen.[^own-site-model][^v2-biome-contract]

**Wichtig für alte Spielstände:** Alte Quelle und passende Paketfassung gemeinsam erhalten. Die bisherige Demo bleibt ihrer Format-7-Fassung zugeordnet. Die [ausdrückliche Übernahme bekannter V2-Stände nach Format 8](stable-save-binding.md) ist nativ über zwei neue vollständige Cooks, mit strenger physischer Wiederaufnahme und mit normalem Speicher-/Lade-/Kaltstartpaar bestanden. Der neue normale C2-Start zeigt ein antwortendes eigenes Fenster und die richtige Karte. Frühere Fehler bleiben im Beleg; menschliche Pixelbestätigung und physische Tasten sind separat offen. Der normale Ladebefehl konvertiert Altstände nicht stillschweigend.

## Geprüfte Fassungen und neuer Startpfad

**Der gewöhnliche Format-9-Spieler-Lebenszyklus ist bestanden:** Normale F5/F9-Funktionen und ein kalter zweiter Prozess erhalten alle acht vollständigen Gruppen in vier plus zwei Snapshots exakt; beide Prozesse enden regulär mit Exit 0. Der sichtbare normale Fensterstart ist separat mit antwortendem Hauptfenster, richtiger Karte und eigener neuer Datenablage bestanden; Pixel des normalen Fensters, physische Eingaben und menschliche Spielabnahme werden daraus nicht abgeleitet. **Tools/launch_stable_site_preparation_demo.ps1** wählt die neue **SiteReplan3**-Fassung mit ihrem geprüften eigenen Abschlussbeleg und der übernommenen Format-9-Datei in **Saved/SiteReplanDemoUser**. Ohne diesen Beleg gibt der Startpfad die neue Fassung nicht frei. Ein vorhandener Stand wird nicht neu besät.[^replan-guide]

Die bisherige UI2-Fassung verwendet weiter **Saved/SaveBindingDemoUser** und bleibt über **-PreviousUiBuild** erreichbar. **-PreviousBuild** behält die bewahrte C2-Fassung. **F5** speichert und **F9** lädt; für einen kalten Neustart denselben zur jeweiligen Fassung gehörenden Startpfad verwenden. Die [Speicheranleitung](stable-save-binding.md) erklärt die historischen Übernahmen und den Rückweg; die [Umplanungsanleitung](replan-building-sites.md) grenzt die neue bekannte UI2-Übernahme ab.

## Historische vorgeplante Format-7-Demo starten

Im Projektordner startet **Tools/launch_site_preparation_demo.ps1** die vorbereitete verpackte V2-Fassung mit eigener Datenablage **Saved/SitePreparationDemoUser**. Der Launcher prüft die sechs Paketdateien gegen das Manifest und schützt gegen doppelte Starts derselben Demo. Die Startdatei ist exakt die geprüfte Cooked-Ready-Datei; bestehender Spielfortschritt wird nicht automatisch neu besät. Der normale Launcherstart ist separat bestanden: Am **29. Oktober 2026 um 18:12:47 UTC** bestätigten Prozess-/Fensterabfrage und natives Startlog ein reagierendes eigenes Hauptfenster, die richtige Spielkarte und einen Start ohne Offscreen-Modus oder protokollierten Startup-Error. Seeddatei und Paketmanifest stimmten mit den vorbereiteten SHA256-Werten überein. Dieser Nachweis enthält keine Pixelprüfung, Computer-Use-Bedienung, physischen Eingaben oder menschliche Bestätigung und keinen abschließenden Exitnachweis.[^proof]

In dieser Demo ist **ein Bauplatz bereits geplant und pausiert**: **Arbeit starten [Space]**, danach **Transport an [H]** verwenden. Zuerst wird gerodet, dann Erde bewegt. Sobald **Bauplatz bereit** erscheint, mit **B** das Haus setzen. **7** brauchst du erst für einen neuen Standort. Die Demo verwendet das ausdrücklich beschleunigte Prüfprofil; das ist keine realistische Maschinenleistung.

## Neue Baustellenleiste

**+ Neuen Bauplatz planen [7]** erzeugt einen neuen Entwurf. Die **anklickbaren Auftragskarten** wählen vorhandene Pläne; **AUSGEWAEHLT** und die farbige Karte zeigen das Ziel für Arbeit, Transport und Hausbau. Darunter stehen Phase, Restarbeit und der nächste Schritt. Kameraregler, Untergrund und technische Auftragsdetails sind anfangs eingeklappt.[^ui-proof]

![Neue Auftragskarten mit genau einem ausgewählten Auftrag](../assets/images/site-preparation-order-cards.png)

Das unveränderte Originalbild zeigt zwei pausierte Absenk-Testaufträge im neuen verpackten Spiel. Beide ursprünglichen 1600 × 1000-Aufnahmen wurden vom Agenten visuell geprüft.[^ui-proof]

## Einen eigenen Bauplatz vorbereiten

Die neue Leiste ist im verpackten Spiel über echte Slate-Ereignisse geprüft. Einzelne Höhenvorgaben sind zusätzlich als Quellvertrag beschrieben; physische menschliche Bedienung bleibt eine getrennte Abnahme.[^ui-proof]

1. **+ Neuen Bauplatz planen [7]** wählen. Den Mauszeiger außerhalb der Leiste auf geeigneten Boden bewegen und den Ort mit einem kurzen Linksklick fixieren. Der Testhaus-Bauplatz hat einen festen **12 × 12 m** großen ebenen Kern.
2. Die Zielhöhe wählen. **Auf Bodenhoehe**, **50 cm tiefer**, **1 m tiefer** und **50 cm hoeher** beziehen sich auf die Bodenhöhe am fixierten Klickpunkt. **Hoehe − 25 cm / Hoehe + 25 cm** beziehungsweise **Bild ab / Bild auf** erlauben weitere Schritte. Die Zielhöhe bleibt eine feste Höhe für den gesamten ebenen Kern.
3. Vorschau lesen: **ABTRAGEN** und **AUFFUELLEN** nennen getrennte Volumen- und Massenmengen; zusätzlicher Lagerbedarf und nutzbarer Bestand stehen daneben. Kurz stillhalten, bis die Baumerfassung einschließlich Zufahrt stabil ist. Ein ebener Bauplatz benötigt keine tiefe Grube: An einem Hang können Abtrag und Einbau zusammen nötig sein; nahezu passender Boden kann nur wenig Erdbewegung erfordern.
4. **Plan bestaetigen + speichern [Enter]** wählen. Eine Auftragskarte erscheint, der Entwurf endet und der neue Auftrag ist gewählt. Bestätigen speichert zunächst die Absicht; Bäume, Boden und Materialkonten werden dadurch noch nicht bearbeitet. **Entwurf verwerfen [Esc]** beendet nur den Entwurf.
5. Die gewünschte Auftragskarte anklicken und auf **AUSGEWAEHLT** achten. Alternativ ist **Tab** für den nächsten und **Shift+Tab** für den vorherigen vorhandenen Auftrag vorgesehen. Auch fertige Aufträge bleiben auswählbar. **Tab erstellt keinen neuen Bauplatz.** Für einen weiteren Standort wieder oben **+ Neuen Bauplatz planen [7]** verwenden.
6. Für den gewählten Auftrag **Arbeit starten [Space]**, danach **Transport anfordern [H]** verwenden. Erneutes Betätigen pausiert die Arbeit beziehungsweise stoppt den Transport. Zuerst wird gerodet; der Transportwunsch wird währenddessen vorgemerkt. Erst nach vollständiger Rodung folgt die Erdarbeit mit Lager, Puffer und Lkw. Es gibt einen gemeinsamen Maschinenzug; andere Aufträge warten.
7. Auf **Bauplatz bereit** und die lokale Bodenfreigabe warten. Dann **Haus auf fertigen Bauplatz setzen [B]** wählen. Die Schaltfläche ist nur bei freigegebenem ausgewähltem Bauplatz verfügbar. Boden und freier Hausbereich werden erneut geprüft; wiederholtes Auslösen erzeugt kein zweites Haus.[^own-site-model]

**Speichern [F5]** und **Laden [F9]** gelten für die gemeinsame Kette. Erfolgreiche Plan- und Schalteraktionen speichern ebenfalls; geänderter Fortschritt wird ungefähr alle zwei Sekunden automatisch gesichert. Vor einem gezielten Neustart ausdrücklich speichern. Die hier geprüfte UI2-Überarbeitung ändert weder SaveGameformat noch Kompatibilitätsprofil oder Erdarbeitsmodell.[^own-site-model][^ui-proof]


| Phase | Bedeutung |
| --- | --- |
| Geplant | Gespeicherte Absicht; noch keine Maschinenarbeit. Revision/Storno nur ungearbeitet. |
| Rodung | Gespeicherter Baumbestand wird schrittweise dauerhaft entfernt. |
| Erdarbeit | Rodung vollständig; getrennte Aushub-/Einbauphasen mit Materialtransport. |
| Bauplatz bereit | Erde fertig und Hausboden über neun lokale Punkte in drei stabilen Durchläufen geprüft. |
| Haus gebaut | Genau das zugeordnete Testhaus steht am freigegebenen Ort. |
| Storniert | Ungearbeiteter Auftrag neutral beendet. Geleistete Arbeit wird nicht zurückgedreht. |

## Bekannter Eingabefehler: Tab landet auf den Kamerareglern

Die Meldung vom 29. Oktober 2026 gilt der früheren Oberfläche. Sie war ein Fokusfehler und keine Begrenzung auf einen Bauplatz. Die Korrektur behandelt **Tab / Shift+Tab** vor der Slate-Navigation im eigenen aktiven Spiel, wählt genau einmal pro Druck und stellt danach den Weltfokus wieder her. Gehaltenes Tab schaltet nicht mehrfach. Andere Fenster und beabsichtigte Reglerbedienung behalten ihre eigene Navigation.[^ui-proof]

Im neuen Paket **EarthworksUi2** bestanden ein nativer Slate-Test sowie **38 + 40 Checks** in zwei normalen gerenderten Spielprozessen: echte Kartenklicks, Tab aus beiden fokussierten Kamerareglern, Shift+Tab, Wiederholung, neuer Entwurf per Knopf und 7, Escape, F5/F9 und kalter Neustart. Eine separate Kopie des tatsächlich erhaltenen Spielerstands bestand zusätzlich normales Speichern/Laden und einen kalten zweiten Prozess mit allen acht vollständigen Recordgruppen. Die Originalstände bleiben unverändert. Das ist eine programmatisch geroutete Slate-Abnahme; eine menschliche physische Tastenprüfung wird daraus nicht abgeleitet.[^ui-proof]

## Aktuelle Werkzeugleiste im normalen verpackten Spiel

**Historisches Bild:** Der folgende Beleg zeigt die frühere Format-7-Leiste. Für die neue Oberfläche gilt das Bild der Auftragskarten oben.

Diese unveränderte **888 × 500-SHOWUI-Aufnahme** zeigt den normalen V2-Controller mit einem bereits geplanten, pausierten Bauplatz im Wald. Acht native Snapshots bestätigten separat den exakten ungearbeiteten Ready-Zustand. Der grüne Framezähler gehört zur CSV-Prüfung; deren später Exitfehler bleibt offen. Ein getrennter normaler Start desselben Builds mit demselben Save, ohne CSV, endete sauber. Das Bild belegt keine physischen Eingaben.[^proof]

![Normales V2-Spiel mit geplanter Baustelle und Werkzeugleiste](../assets/images/site-preparation-normal-cooked-controls.png)

## Getrennter gemeinsamer Werkzeugleistenbeleg im Editor

Die unveränderte Aufnahme zeigt die Bauplatzvorschau mit dem aktuellen Controller auf der erhaltenen EarthworksLab-Karte. Die Slate-Leiste ist innerhalb des gesamten **1310 × 750-Editorrahmens** klein sichtbar. Normale API-Aufrufe sind geprüft; das Bild belegt keine physischen Tasten und noch keine normale V2-Cooked-Demo.

![Bauplatzvorschau mit aktueller gemeinsamer Werkzeugleiste auf EarthworksLab](../assets/images/site-preparation-editor-preview.png)

## So sieht der geprüfte Ablauf im verpackten Spiel aus

Die folgenden unveränderten Aufnahmen stammen aus dem erfolgreichen Development-Cooked-Lauf auf der neuen V2-Karte.

**Teilrodung:** Die Terrainaufnahme zeigt noch Wald. Ein erster Rodungsschritt ist gespeichert; einzelne Ressourcenkennungen sind aus dem Bild allein nicht abzulesen.

![Wald während der gespeicherten Teilrodung](../assets/images/site-preparation-cooked-partial-clearing.png)

**Abschluss:** Nach Rodung, Erdarbeit und Bodenfreigabe stehen Testhaus und geschlossenes Dach auf dem abgesenkten freien Bauplatz. Die Zufahrt bleibt frei; blaue Hilfslinien gehören zum Labor.

![Fertiger freier Bauplatz mit Testhaus und Zufahrt](../assets/images/site-preparation-cooked-completed.png)

Die unveränderten Bilder wurden vom Agenten visuell geprüft und im [Bildmanifest](../evidence/image-manifest.json) erfasst. Sie zeigen Terrain und Haus, keine Slate-Werkzeugleiste oder physische Bedienung.[^proof]

## Explizite Biomregeln im neuen Labor

Die neue Karte verwendet fünf getrennte **SitePreparationV2**-Profile: **Wald, Wiese, Fels, Strand und Meeresboden**. Ihre bestehenden Höhen- und Hanggrenzen bleiben erhalten; die gemeinsam genutzten Spawnassets werden nicht verändert.[^biome-rules][^v2-biome-contract]

Die neue Dichtematerialregel **BlueAndBounds1** wertet die ausdrücklich gewählte Biom-ID im blauen Datenkanal und ShaderWorlds native Zellgrenzen aus. Der rote Kanal bestimmt das Bodenmaterial. **GrassAlt** als sichtbarer Bodenwert erzeugt dadurch keine zusätzliche versteckte Pflanzensperre. Die bewuchsfreie **Biom-ID 3** bleibt in dieser eigenen Konfiguration ausdrücklich für NoGrowth reserviert. Eine solche Maske ersetzt weiterhin keine gespeicherte Rodung.[^v2-biome-contract][^clearing]

Dafür wurden **zehn neue Biom-/Dichtematerialassets und eine neue Karte** angelegt. Die Originaldateien der Biome und der alten Welt bleiben unverändert; ihre zur Laufzeit berechnete Bindung kann sich beim Cook dennoch ändern. Das ist eine versionierte Labortrennung, keine automatische Migration bestehender Welten.

## Speichern und Wiederaufnahme

Gespeichert werden die verbundenen Aufträge, eingefrorenen Baumkennungen, Rodungsfortschritt, Phase, Pause, Transportwunsch, ausgeführte Erde, Materialkonten, Lkw-Ladung und Hausidentität. **NoGrowth ersetzt das Rodungsregister nicht:** Die Maske verhindert neuen Bewuchs; das Register hält fest, welche Ressourcen tatsächlich entfernt wurden. Holz besitzt in diesem Slice noch kein eigenes Konto.[^own-site-model][^clearing]

Die hier ursprünglich abgenommene Demo schreibt ausdrücklich **Format 7**. Die getrennte neue stabile V2-Fassung schreibt **Format 8** mit Schema 1; ihr begrenzter Übernahme-/B/C-Nachweis steht in der [neuen Speicheranleitung](stable-save-binding.md). Ältere unterstützte Formate werden innerhalb ihrer Welt-/Generatorbindung geprüft; ein nativer Binärtest erhält auch den alten ausgelassenen Versionswert 6. Das ist keine universelle Altsave-Migration. Widersprüchliche Records oder eine andere Welt-/Generator-/Terrainbindung werden vor Anwendung abgewiesen. Die erfolgreichen kalten Restarts verwenden jeweils dieselbe Paketfassung; sie bestätigen keine Kompatibilität nach erneutem Cook.[^proof][^build-bound-save-source]

Nach dem Laden kann **Bewuchs nach Laden: native Neuberechnung abwarten** erscheinen. Die Runtime fordert den lokalen Boden selbst an und lässt die beteiligten nativen Baumquellen in ihrer begrenzten Region fertig rechnen, bevor weitere Arbeit folgt. Sie erfindet keine Instanzen und verändert dafür keine Rodungs- oder Materialbuchung. Lokale Bodenbereitschaft ist trotzdem keine globale GPU-/Bewuchs-Fertiggarantie für beliebige Biome oder Streaminglagen.[^own-site-model][^proof]

## Stand der aktuellen Prüfung

**Neue UI2-Abnahme:** ein nativer Slate-Test, 38/38 + 40/40 tatsächliche Slate-Checks, zusätzliche 4 + 2 vollständige normale Nutzerstand-Snapshots und eigenes antwortendes Spielfenster bestanden. Die folgenden V2-Terrain- und Maschinenbelege sind die erhaltene frühere Prüfbasis.[^ui-proof]

Die Einrichtung mit elf neuen Assets, native V2-Suite und Wiederholung ohne neue Assets sind bestanden. **Uncooked und Development-Cooked bestanden jeweils mit zwei frischen Prozessen:** Teilrodung und beladene Fahrt wurden exakt fortgesetzt; beide Pfade endeten mit 21 gerodeten Ressourcen, erhaltenem Kontrollbaum, genau einem Haus, 176,4 t Lager und 0 g Bilanzfehler. Drei weitere Loads erzeugten keine Duplikate. Die aktuelle gemeinsame Controller-/Kamera-API bestand separat 38 Checks auf der erhaltenen EarthworksLab-Karte. Die normale V2-Startprüfung bestätigt zusätzlich acht vollständig gleiche native Snapshots des ungearbeiteten Plans. Dennoch liefert der Prozess nach sauber protokollierter CSV-Finalisierung einen späten Nichtnull-Exit; dasselbe passiert mit dem passenden alten Archivpaket. Das ist kein vollständiger normaler Demo-PASS. Drei getrennte normale Starts ohne CSV-Instrumentierung bestanden inzwischen mit Exit 0: neue V2-Karte mit demselben Ready-Save, passende alte Foundations-Karte und leere Entry-Karte. Sie bestätigen saubere normale Prozessbeendigung; die instrumentierten Fehlversuche bleiben erhalten. Die versiegelte Demo mit identischer privater Ready-Datei ist vorbereitet: 106 Quelldateien und sechs Paketdateien geprüft, 170 zuvor vorhandene Save-Dateien unverändert; genau eine neue private Startdatei hinzugefügt. Der tatsächliche normale Launcherstart bestand anschließend die begrenzte Fenster-/Kartenprüfung mit unveränderter Seed- und Manifestbindung. Physische Eingaben, Computer-Use-Bedienung und menschliche Pixelabnahme bleiben offen; der Start ergänzt keinen weiteren Exitnachweis.[^proof]

Der [Prüfbericht](../evidence/site-preparation-test.json) erhält die früheren Erfolge, die gescheiterten Kontrollbaumversuche und deren Diagnose getrennt. Diese historischen Ergebnisse und Bilder werden nicht auf V2 übertragen. Boden- und Baumgates bleiben streng; keine Ersatzbäume, zusätzlichen Rodungsbuchungen oder nachträglich angepassten Savebindungen.

## Fehlerhilfe und Grenzen

| Beobachtung | Vorgehen |
| --- | --- |
| Nach Bestätigung passiert nichts | Richtigen Queueauftrag mit **Tab** wählen, dann **Arbeit starten / Pause**. Bestätigen allein startet keine Arbeit. |
| Baumerfassung oder Wiederaufnahme wartet | Standort unverändert lassen und gerenderte Frames zulassen. Bodenbereitschaft allein bestätigt keine fertigen Baumquellen; Status lesen. |
| Der Lkw fährt nicht | Erst Arbeit starten, danach für denselben Bauplatz **H** verwenden. Während Rodung wird der Transportwunsch nur vorgemerkt. |
| Das Haus bleibt gesperrt | Fertige Erdarbeit und aktuellen Kollisionsnachweis abwarten; den Hausbereich freihalten. |
| Ein Baum scheint ungerodet zu fehlen | Native Nullskalierung und dauerhaften Rodungsrecord unterscheiden. Ein fehlender sichtbarer Kandidat darf nicht als zusätzlich gefällter Baum gebucht werden. |
| Alter Save wird nach neuem Cook abgewiesen | Quelle mit passender alter Paketfassung bewahren. Für die bekannten V2-Stände den [ausdrücklichen Format-8-Weg](stable-save-binding.md) nutzen lassen; dessen native B2/C2-Abnahme und separate physische Fortsetzung gelten für bekannte Stände bei unveränderter Grundlage. Beliebige Inhaltsänderungen benötigen eine eigene Migration. Keine Bindungen umhashen. |
| Ausgangsboden ändert sich während Rodung extern | Der spätere Erdstart kann **NeedsReplan** blockieren. Rodungsfortschritt bleibt erhalten; ein expliziter Replanpfad nach begonnener Rodung fehlt noch. |

Es gibt weiterhin **einen Maschinenzug**, feste geprüfte Wege und ein Erdmaterial. Holztransport, allgemeine Bürger-/Fahrzeugnavigation, Oberflächenarbeit und das Ändern bereits geleisteter Aufträge folgen später. Die [Untergrundansicht](underground-view.md) ist eine getrennte Darstellungsfunktion.

[^own-site-model]: Gelesene eigene Implementierung gemäß Quellenbeschreibung.
[^proof]: [Prüfbericht mit aktueller V2-Grenze und getrennten historischen Nachweisen](../evidence/site-preparation-test.json).
[^clearing]: [Dauerhafte Ressourcenkennungen und Rodungscache](clearing-cache-and-performance.md).
[^flatten]: [Erdarbeit, Lager und getrennte Aushub-/Einbauphasen](flatten-machine-earthworks.md).
[^plan]: [Vereinbarter Scaping-Ausbau](../reference/scaping-machine-work-plan.md).
[^v2-biome-contract]: Eigene gelesene V2-Setup-/Dichtewerkzeuge und erfolgreicher begrenzter Einrichtungsbericht gemäß Quellenbeschreibung; vollständige V2-Uncooked-/Cooked-Neustartpaare separat im Prüfbericht.
[^biome-rules]: [Bestehende Höhen- und Hangregeln](foundations-lab.md).

[^build-bound-save-source]: Gelesene native PreSave-Versionierung und eigene Terrainidentität gemäß Quellenbeschreibung; keine Änderung am Vendorcode oder nachträgliche Save-Normalisierung.

[^tab-focus]: Historische Nutzermeldung und lesende Prüfung der damaligen Tab-/Slider-Navigation. Der aktuelle Fix und seine getrennte Eingabeabnahme stehen im neuen UI-Prüfbericht.

[^ui-proof]: [Prüfbericht zur neuen Oberfläche mit getrenntem nativen Test, tatsächlichem Slate-Spielpfad und normalem Nutzerstand-Neustart](../evidence/earthworks-ui-test.json).
