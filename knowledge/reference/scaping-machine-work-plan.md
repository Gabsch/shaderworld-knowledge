---
type: Playbook
title: Alle Scaping-Werkzeuge an Maschinenaufträge anbinden
description: Beschlossene Reihenfolge für Anheben, Absenken und weitere Bauarbeit mit gemeinsamer Materialbilanz, Speicherung und paralleler Untergrundansicht.
status: draft
tags: [shaderworld, city-builder, planning, machines, terraforming, underground, persistence]
engine_version: "5.8.4"
plugin_version: "4.1"
generated:
  by: codex/gpt-6
  at: "2026-10-29T02:49:32Z"
evidence_scope: Erster Slice nativ sowie uncooked und frisch verpackt mit je 10/10 und 12/12 Checks geprüft; normale Controller-/Queue-Kaltstartprobe und separate Editor-Ansicht mit lokalen Kollisionen bestanden. Physische Eingaben, verpackte Ansichtspixel und weitere Scaping-Werkzeuge offen.
sources:
  - id: machine-earthworks
    resource: ../guides/machine-earthworks.md
    title: Implementiertes Anheben und Absenken mit eigener Warteschlange und Speicherformat 6
  - id: machine-evidence
    resource: ../evidence/machine-earthworks-test.json
    title: Finale native Suite und begrenzte uncooked Erstabnahme
  - id: underground-view
    resource: ../guides/underground-view.md
    title: Eigene schematische Untergrunddarstellung mit getrenntem Nachweis
  - id: user-decision
    resource: "Direkte Nutzerentscheidung am 29. Oktober 2026: Plan in OKF festhalten; nach abgeschlossenem Asset-Import und Projektfreigabe Anheben/Absenken als Maschinenaufträge beginnen, parallel Untergrundansicht. Chat und Koordinationsnachrichten nicht im öffentlichen Bundle enthalten."
    title: Beschlossener Startpunkt und Reihenfolge
  - id: current-planner
    resource: ../guides/construction-planner.md
    title: Vorhandener begrenzter Planer und seine abgegrenzte Abnahme
  - id: world-edits
    resource: ../guides/foundations-lab.md
    title: Bestehende Scaping-Pläne und getrennte Sofort-Debugausführung
  - id: current-cycle
    resource: ../guides/closed-material-cycle.md
    title: Bereits geprüfter Materialkreislauf
  - id: underground
    resource: ../guides/underground-hybrid-probe.md
    title: Geprüfte Hybridkammer und offene Untergrundarbeit
  - id: storage
    resource: shaderworld-data-and-persistence.md
    title: Datenlayer, Projektkarte und dauerhafter Spielstand
  - id: own-source
    resource: "Gelesener eigener Projektcode: CityLabWorldEdits.h/.cpp, CityLabConstruction.h/.cpp, CityLabConstructionModel.h/.cpp, CityLabPersistence.h/.cpp und UndergroundProbe.h/.cpp. PlanEdit/RevisePlan/GetPreview und PreviewSite/ExpectedHeightAt/ProbeTerrain geprüft; Projektquellen nicht im öffentlichen Bundle enthalten."
    title: Vorhandene Bausteine und Grenzen des flachen Baustellenmodells
---
# Alle Scaping-Werkzeuge an Maschinenaufträge anbinden

**Ziel für alle regulären Scaping-Eingaben:** Ein gespeicherter Zielplan wird schrittweise von Maschinen ausgeführt. Das sichtbare Gelände zeigt den erreichten Bauzustand. Vorschau und ungearbeitete Bestätigung ändern noch keinen Boden, Bewuchs oder Materialbestand. Der erste getrennte Anheben-/Absenken-Slice ist implementiert und nativ sowie uncooked und verpackt geprüft; Ebnen, Oberflächenarbeit und die breite Umstellung der bisherigen Scaping-Werkzeuge folgen später.

Der erste Arbeitsblock **Anheben und Absenken als Maschinenauftrag** wurde nach abgeschlossenem Fahrzeug-Asset-Import und ausdrücklicher Projektfreigabe begonnen. Parallel entstand die **Untergrundansicht**. Während des Imports war allein abgestimmte Dokuarbeit freigegeben; Editor, PIE, Blender, Builds und Spielstände blieben beim Import. Diese Freigabe wurde abgewartet. Weitere gemeinsame Editor-/GPU-Läufe bleiben zeitlich zu koordinieren.[^user-decision] [Bedienung und Prüfgrenzen](../guides/machine-earthworks.md).

## So soll sich der Ablauf anfühlen

1. Werkzeug wählen und die gewünschte Form ziehen.
2. Zieloberfläche, tatsächlichen Ausgangsboden, Aushub, Einbaubedarf und Zugang prüfen. Ungültige Flächen mit verständlichem Grund markieren.
3. Auftrag bestätigen. Er ist gespeichert und zunächst pausiert; auf dem Gelände ist erst eine Plananzeige zu sehen.
4. Maschinenarbeit und Transport ausdrücklich starten. Begrenzte Puffer und tatsächlich verfügbare Lieferungen bestimmen den Fortschritt.
5. Pausieren, speichern und das Spiel schließen. Nach dem Neustart sind Pläne, ausgeführtes Gelände, Maschinen, Ladungen und Materialkonten wieder auf demselben Stand.

## Welche Aufträge die Werkzeuge erzeugen

| Werkzeug | Geplanter Auftrag und Materialwirkung |
| --- | --- |
| Absenken | Boden ausheben; genau einmal in Puffer, Fahrzeug oder Lager buchen; bei vollem Puffer warten. |
| Anheben | Material anliefern und einbauen; ohne Lieferung keine zusätzliche Höhe. |
| Ebnen | Zielhöhe festlegen; Aushub und Einbau getrennt berechnen, auch wenn sie innerhalb derselben Fläche auftreten. |
| Bodenmaterial auftragen | Flächenweise Oberflächenarbeit. Eine reine Material-ID beschreibt weder Masse noch Schichtdicke. Für physische Schichten Materialart, Dicke und Verbrauch vorher definieren. |
| Roden | Vorbereitungsarbeit mit dauerhaften Baumzuständen. Eine NoGrowth-Maske allein ist noch keine Holzbilanz; Erträge gesondert ergänzen. |
| Straße oder Grundstück vorbereiten | Abhängige Schritte aus Rodung, Erdarbeit und Oberflächenbau. Nur tatsächlich vorbereitete Abschnitte werden fertiggestellt beziehungsweise für Gebäude freigegeben. |

Die vorhandene Foundations-Sofortausführung bleibt bis zur Umstellung ausdrücklich ein Labor-Debugwerkzeug. Sie darf nicht unbemerkt die reguläre Maschinenarbeit umgehen.[^world-edits]

## Gemeinsame Regeln für Planung, Boden und Material

**Ein Plan besitzt eine stabile Identität und Revision.** Im neuen Earthworks-Pfad verweist `SourcePlanId` tatsächlich auf `Plan.Id`; der ausführende Job hat eine weitere stabile ID. Revisionen behalten Planidentität und Reihenfolge. Gespeichert werden Welt-/Generatorbindung, Ausgangs- und Referenzraster, Start-/Zielhöhen, Geländeversion und Operation. Der alte Construction-Pfad bleibt erhalten; seine unabhängig erzeugte SourcePlanId wurde dadurch nicht rückwirkend mit einem Scaping-Plan verbunden. Gemischte Aushub-/Einbaubereiche innerhalb eines Ebnenauftrags sind weiterhin Schritt B.[^own-source]

**Den echten Ausgangsboden erfassen.** Der frühere Construction-Planer setzte eine flache Basis voraus; seine Flachheitsprüfung war noch kein gespeichertes Ausgangsraster. Earthworks speichert nun dichte tatsächliche Kollisionsproben über der Einflussfläche und die Start-/Zielhöhe jeder Arbeitszelle. Zusätzlich enthält die Referenz dieselben Proben abzüglich bereits ausgeführter Earthworks-Höhenänderungen. Referenz plus sämtliche ausgeführten Beiträge erzeugen den erwarteten Boden, ohne die neue Baseline ein zweites Mal aufzutragen. Vor Arbeitsstart werden Fläche und Zugänge erneut geprüft. Ein veralteter ungearbeiteter Plan benötigt eine frische Revision. Ein beliebiges unebenes Feld samt gemischter Einebnung ist damit noch nicht abgenommen.

**Mengen aus derselben Form ableiten.** Gegensätzliche Höhenbeiträge dürfen sich nicht sichtbar aufheben, während trotzdem beide vollständigen Mengen als bewegt gelten. Aushub und Einbau werden getrennt integriert; Dichten, Zellauflösung und Rundung werden ausdrücklich festgelegt. Exakte Modellgramm sind von einer unabhängigen Vermessung des quantisierten Terrainmeshvolumens zu unterscheiden.

**Ein gemeinsamer Vorrat, mehrere Pläne.** Der erste Earthworks-Snapshot enthält eine Warteschlange, einen aktiven Auftrag, einen Lkw und genau ein Lager. Wartende Pläne besitzen weder Vorabgutschrift noch Reservierung. Anheben reserviert beim ausdrücklichen Start nur bereits vorhandenen vollständigen Bedarf; Absenken startet nur, wenn der gesamte verbleibende Aushub ins freie Lager passt. Der nächste Auftrag startet nicht automatisch. Das alte Gruben-/Aufschüttpaar bleibt ein separater Spezialfall mit eigenem Slot; seine Konten werden nicht automatisch mit Earthworks zusammengelegt.

**Ändern und Abbrechen bewahren die Arbeit.** Unbegonnene Aufträge dürfen verändert oder storniert werden. Nach dem ersten Erdschritt oder Materialtransfer bleiben ausgeführte Höhen, Verbrauch und Ladungen erhalten. Nach ausgeführter Arbeit benötigt ein neues Ziel einen weiteren Gegenauftrag; der erste Slice erlaubt dann weder Revision noch Storno des bisherigen Jobs. Undo löscht keine bereits ausgeführte Baugeschichte. Ein allgemeiner Abbruch mit Rücktransport beladener Fahrzeuge ist noch nicht implementiert.

**Ein Arbeitsschritt bildet einen konsistenten Speicherstand.** Materialbuchung, Zellfortschritt und ausgeführte Geometrieversion werden zusammen fortgeschrieben. Anschließend wird das Terrain daraus aufgebaut; weitere Erdarbeit wartet auf den lokalen Kollisionsnachweis. Nach dem Laden wird derselbe Stand rekonstruiert und geprüft, ohne Material erneut zu buchen. Speicherformat 6 ergänzt den Earthworks-Snapshot und erhält die bisherigen Felder einschließlich Constructionrecords. Native Schema-Fixtures prüfen diesen Datenvertrag; eine automatische Umwandlung alter Constructionaufträge in neue Earthworks-Jobs ist nicht enthalten. Die Migration jedes archivierten echten Binärsaves bleibt separat zu prüfen.[^current-cycle]

## Umsetzungsreihenfolge und erste Abnahme

### A: Anheben und Absenken

Ein Bodenmaterial, kleine zunächst ebene Flächen, feste geprüfte Wege, ein gemeinsames Lager, wartende Pläne und ein aktiver Maschinenzug. Die zentrale Probe lautet: **abtragen, lagern und dieselbe bearbeitete Fläche wieder auftragen**. Noch keine allgemeine Stadtlogistik, freie Routenwahl oder konkurrierende Erdmaschinen.

Abnahmekriterien:

- Vorschau, Bestätigung und ungearbeitete Revision verändern weder Terrain, Bewuchs noch Materialkonten.
- Veralteter Ausgangsboden blockiert den Arbeitsstart mit einer verständlichen Meldung.
- Der zweite Auftrag verwendet den tatsächlich ausgeführten Boden; keine doppelte Höhenprojektion oder Materialbuchung.
- Aushub und Einbau stimmen im definierten Modell; Gesamtbilanz **0 g**. Voller Puffer und fehlende Lieferung halten die Arbeit an.
- Mehrere wartende Pläne können denselben Lagerbestand nicht mehrfach verbrauchen.
- Revision, Storno und Undo bleiben vor Arbeit neutral. Nach erstem Erdschritt oder Materialtransfer dürfen sie weder Höhe noch Konten oder Ladungen zurücksetzen; Gegenarbeit benötigt einen neuen Auftrag.
- Neustart während beladener Fahrt und während ausstehender Kollisionsaktualisierung erhält den vollständigen Zustand vor weiterer Simulation. Drei weitere Loads erzeugen keine Duplikate.
- Unabhängige lokale Höhenproben, unbeeinflusste Kontrollflächen und alte Spielstände bleiben Teil der Prüfung. Physische Bedienung und gerenderte Form werden getrennt abgenommen.

### Prüfstand A nach der ersten Umsetzung

- **Nativ bestanden:** finale Suite 46/46, darunter sieben Earthworks-Tests und drei getrennte Untergrund-Datentests.
- **Uncooked und verpackt bestanden:** je zwei gerenderte Prozesse mit **10/10 + 12/12 Checks**. Auf derselben N2-/0,75-m-Fläche **86,4 t** ausheben, lagern und wieder einbauen; alle Bilanzen **0 g**. Beladene Fahrt und Kollisionswarte-Checkpoint exakt fortgesetzt, drei weitere Loads ohne Duplikat. Je Laufpaar 825 akzeptierte lokale Höhenproben, maximal 4 cm bei 5-cm-Gate. Neuer EarthworksLab-Cook/Stage/Archive erfolgreich; bekannte geerbte Level-Blueprint-Warnungen bleiben.
- **Normale APIs und Kaltstart bestanden:** eigener gespeicherter Kartenstand, Zielwahl, Bestätigung mit Autosave und drei logische Loads. Kalte Editorstarts laden den ungearbeiteten Plan mit identischem Zustand, Arbeit pausiert/Transport aus. Ein fehlender Slot bleibt bedienbar; normale Save-Dateien sind geschützt.
- **Ansicht getrennt bestanden:** vier Editorbilder für Oberfläche/Schnitt/Innenraum/Rückweg, Tiefenschritte, Laden aus Schnitt und invariant neun Terrain-/sechs Hüllen-Komponentenspuren je Ansicht. Der frühere Gras-zu-Sand-Fehler ist nach Korrektur der Live-Materialbindungen visuell nachgeprüft. [Eigener Ansichtsbericht](../evidence/underground-view-test.json).
- **Begrenzungen:** physische Eingaben, weitere normale Revisions-/Start- und Fehlerwege, Außenkontrollfelder und echte archivierte Altformat-Saves bleiben offen. Komponentenspuren sind keine Weltbewegungs- oder Wasserprobe; verpackte Ansichtspixel fehlen. Gemischtes Ebnen, breite Oberflächen-/Straßenanbindung und echter Tunnelvortrieb sind spätere Slices.

Der [bereinigte Maschinenbericht](../evidence/machine-earthworks-test.json) trennt native Modelle, uncooked ConstructionLab-Override, verpacktes EarthworksLab und normale APIs. Der erste Kreislauf ist einschließlich Neustart abgenommen; vor der breiten Bedienumstellung die verbleibenden Interaktionsfälle gezielt prüfen.

### B: Ebnen mit Aushub und Einbau

Ein kontrolliertes Buckel-/Muldenprofil auf eine absolute Zielhöhe bringen. Positive und negative Volumen getrennt anzeigen; zunächst denselben Materialtyp verwenden. Fehlmengen und Überschüsse sichtbar machen. Überlappende Änderungen und erneute Planung auf bereits bearbeiteter Fläche gezielt prüfen.

### C: Vorbereitungs- und Oberflächenarbeit

Rodung als Voraussetzung, anschließend definierter Oberflächenauftrag; danach Straßenabschnitte und Grundstücke. Materialmalerei erst nach fachlicher Festlegung von Fläche, Arbeitsleistung und gegebenenfalls Schichtverbrauch anbinden. Holz-, Verdichtungs- und Mehrmaterialwirtschaft bleiben eigene Erweiterungen.

## Parallel: Untergrundansicht

| Modus | Geplantes Verhalten |
| --- | --- |
| Oberfläche | Normale Stadtansicht und normale Bodenabfrage. |
| Schnittansicht | Ausgewählten Untergrundbereich lokal freilegen; später Tiefenregler mit absoluter Höhe und Tiefe unter dem örtlichen Boden. |
| Innenraum | Sichere Kameraposition im ausgewählten fertigen Abschnitt; eindeutige Rückkehr zur Oberfläche. |

Die Schnittansicht ist eine Darstellungsfunktion. Sie erzeugt keine Holebrushes, Erdbewegung, Rodung oder Wasserabdichtung. Auswahl und Kamera benötigen einen eigenen, zum sichtbaren Schnitt passenden Abfragepfad; Bürger, Fahrzeuge und Maschinen behalten ihre tatsächliche Kollision. Ausgeblendete Darstellung muss beim Verlassen, Laden und Beenden zuverlässig zurückgestellt werden.

Eine fertige bedienbare ShaderWorld-Cutaway-API wurde im untersuchten Bestand nicht gefunden. Eine eigene schematische Anzeige ist inzwischen implementiert. Drei native Datenprüfungen für Grenzen/Auswahl, Materialrückgabe und spielerbezogene Sichtbarkeit bestanden; GPU-Sichtbarkeit, Bewuchs, Schatten und weitere Kameras brauchen ihre eigene praktische Abnahme. [Bedienvertrag der Untergrundansicht](../guides/underground-view.md). Die erfolgreiche Hybridkammer ist die Grundlage für die erste Sichtprobe; ihre Existenz belegt keinen frei ausgrabbaren 3D-Untergrund.[^underground]

Erste Abnahme: alle drei Modi wechseln, dieselbe Kammer auswählen, sicher hin- und zurückfahren, unveränderte Physik/Materialkonten nachweisen und nach Neustart denselben Bauzustand sehen. Sichtprüfung und echte Maus-/Tastaturbedienung separat protokollieren. Zunächst keine fingierte Geologie anzeigen; Schnittflächen ohne Erdmodell sind als schematisch zu kennzeichnen.

## Danach: Tunnelbau und weitere Grundlagen

Unterirdischer Vortrieb braucht zusätzlich räumliche Boden-/Geologiedaten oder eine andere geeignete 3D-Geometriebeschreibung. Ein entnommener Bereich darf nicht zugleich als Oberflächenaushub und als Tunnelmaterial gezählt werden. Die heutige Hybridhülle wurde unter dem Höhenfeld eingesetzt und hat dadurch noch keinen Aushub erzeugt.

Der spätere Ablauf: Zugang herstellen, erreichbaren Abschnitt ausheben, Aushub abtransportieren, sichern/auskleiden, Kollision und Wasserabdichtung prüfen, Abschnitt freigeben. Portale, Trasse und Oberfläche werden abhängige Teilaufträge eines gemeinsamen Plans.

Fahrzeuge erhalten Fähigkeiten wie ausheben, laden, transportieren und verteilen. Modell, bewegliche Teile und Animation werden über Adapter an den Arbeitsfortschritt gebunden. Der [separate Fahrzeug-Importversuch](../guides/vehicle-asset-evaluation.md) belegt inzwischen gespeicherte Mesh-/Clips und Demoposen. Das bestätigt weder Schaufelphysik noch echte Fahrzeug-/Terrainkollision oder Produktionsleistung; die Arbeitsmengen bleiben Modellzustand.

Danach priorisieren: Bürger-/Maschinenwege nach Bodenänderungen, mehrere konkurrierende Baustellen, frischer Karten-Cook und verpackte Bedien-/Neustartabnahme; größere Welten und Streaming erst mit gezielten Leistungsnachweisen. Räumliche ShaderWorld-Layer werden als Projektion unseres Zustands erprobt, nicht vorab zum alleinigen Speicher erklärt.[^storage]

## Zuständigkeiten und weitere gemeinsame Prüfungen

- Hauptarbeit: offene Abnahmen der ersten Anheben-/Absenken-Runde schließen; danach denselben gemeinsamen Auftragsvertrag für gemischtes Ebnen erweitern.
- Parallelagent: isolierte Untergrunddarstellung mit eigenen Dateien und abgestimmtem Material-/Kameravertrag.
- Parallelagent: Mengen-/Restore-Review und unabhängige Abnahmefälle; später begrenzter Datenlayer-Neustartversuch.
- Editor, GPU-Abnahmen und Builds werden weiterhin zeitlich koordiniert. Parallelität bedeutet keine gleichzeitige Steuerung derselben Unreal-Sitzung.

[^user-decision]: Direkte Nutzerentscheidung laut Quellenbeschreibung; sie autorisiert die genannten nächsten Arbeiten nach der Freigabe, keinen vorzeitigen Editorzugriff.
[^current-planner]: [Vorhandener Baustellenplaner](../guides/construction-planner.md), mit seinen eigenen Eingabe- und Cookgrenzen.
[^world-edits]: [Foundations](../guides/foundations-lab.md), vorhandene Planungs- und Debugbausteine.
[^current-cycle]: [Geschlossener Materialkreislauf](../guides/closed-material-cycle.md), bestehender abgegrenzter Nachweis.
[^underground]: [Untergrund-Hybridversuch](../guides/underground-hybrid-probe.md), eigene Hülle und getrennte Kollisions-/Neustartprüfung.
[^storage]: [ShaderWorld-Daten und dauerhafter Spielstand](shaderworld-data-and-persistence.md).
[^own-source]: Eigener Projektcode laut Quellenbeschreibung; gelesen, nicht Teil dieses öffentlichen Bundles.
