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
  at: "2026-10-29T00:01:27Z"
evidence_scope: Nutzerbeschlossener Umsetzungsplan vom 29. Oktober 2026 und Quellprüfung; keine Umsetzung oder neue Laufzeitabnahme der beschriebenen Erweiterungen.
sources:
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

**Beschlossen, noch nicht umgesetzt:** Alle regulären Scaping-Eingaben erzeugen einen gespeicherten Zielplan. Maschinen führen ihn schrittweise aus. Das sichtbare Gelände zeigt den erreichten Bauzustand. Die Vorschau darf zukünftige Arbeit zeigen, aber noch keinen Boden, Bewuchs oder Materialbestand ändern.

Der erste Arbeitsblock ist **Anheben und Absenken als Maschinenauftrag**, parallel dazu eine **Untergrundansicht**. Die Umsetzung startet erst nach abgeschlossenem Fahrzeug-Asset-Import und ausdrücklicher Projektfreigabe durch den Import-Chat. Die reine OKF-Dokuarbeit ist währenddessen abgestimmt; Editor, PIE, Blender, Builds und Spielstände bleiben beim Import. Eine fehlende Abschlussmeldung gilt nicht als Freigabe.[^user-decision]

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

**Ein Plan besitzt eine stabile Identität und Revision.** Seine Arbeitsaufträge verweisen auf diese Identität. Die bisherige unabhängig erzeugte SourcePlanId im Construction-Pfad ist noch keine echte Verknüpfung zu einem Scaping-Plan. Der neue Auftrag speichert Weltbindung, Ausgangsraster, Zielraster, regionale Geländeversion, Operation und getrennte Aushub-/Einbaumengen.[^own-source]

**Den echten Ausgangsboden erfassen.** Der jetzige Baustellenplaner nimmt eine flache Basis an. Die neun Punkte der Scaping-Vorschau beziehungsweise lokalen Kollisionsabnahme ersetzen kein allgemeines Volumenraster; auch die dichtere Flachheitsprüfung der Construction-Vorschau mit 25/49/81 Punkten je nach Größe erzeugt noch kein gespeichertes Ausgangsraster. Für bearbeiteten oder unebenen Boden müssen Vorschau, Mengenrechnung und ausgeführte Geometrie dieselbe Beschreibung verwenden. Bereits enthaltene Änderungen dürfen beim nächsten Auftrag nicht erneut aufaddiert werden. Wird die Ausgangsfläche vor Arbeitsbeginn verändert, wartet der Auftrag mit **Plan erneut prüfen**.

**Mengen aus derselben Form ableiten.** Gegensätzliche Höhenbeiträge dürfen sich nicht sichtbar aufheben, während trotzdem beide vollständigen Mengen als bewegt gelten. Aushub und Einbau werden getrennt integriert; Dichten, Zellauflösung und Rundung werden ausdrücklich festgelegt. Exakte Modellgramm sind von einer unabhängigen Vermessung des quantisierten Terrainmeshvolumens zu unterscheiden.

**Ein gemeinsamer Vorrat, mehrere Pläne.** Zunächst eine gespeicherte Warteschlange und ein aktiver Erdauftrag beziehungsweise Maschinenzug. Das vorhandene Gruben-/Aufschüttpaar bleibt ein geprüfter Spezialfall. Lagerbestände und Reservierungen gehören einmal zur Welt; jeder Auftrag darf denselben Vorrat nicht erneut als frei zusagen. Überlappende aktive Einflussbereiche werden zunächst ausgeschlossen. Wartende Pläne werden vor Beginn erneut geprüft.

**Ändern und Abbrechen bewahren die Arbeit.** Unbegonnene Aufträge dürfen verändert oder storniert werden. Nach dem ersten Erdschritt oder Materialtransfer bleiben ausgeführte Höhen, Verbrauch und Ladungen erhalten. Ein neues Ziel erzeugt eine Folgerevision mit Rest- oder Gegenarbeit. Undo löscht keine bereits ausgeführte Baugeschichte. Beim Abbruch bleiben Ladungen erhalten oder werden durch einen ausdrücklichen Rücktransport behandelt.

**Ein Arbeitsschritt bildet einen konsistenten Speicherstand.** Materialbuchung, Zellfortschritt und ausgeführte Geometrieversion werden zusammen fortgeschrieben. Anschließend wird das Terrain daraus aufgebaut; weitere Erdarbeit wartet auf den lokalen Kollisionsnachweis. Nach dem Laden wird derselbe Stand rekonstruiert und geprüft, ohne Material erneut zu buchen. Neue Daten benötigen eine versionierte Save-Erweiterung mit geprüfter Übernahme alter Constructionrecords.[^current-cycle]

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

Eine fertige bedienbare ShaderWorld-Cutaway-API wurde im untersuchten Bestand nicht gefunden. Ein kompatibles eigenes Anzeigematerial ist ein zu prüfender Ansatz, einschließlich Bewuchs, Schatten und weiterer Kameras. Die erfolgreiche Hybridkammer ist die Grundlage für die erste Sichtprobe; ihre Existenz belegt keinen frei ausgrabbaren 3D-Untergrund.[^underground]

Erste Abnahme: alle drei Modi wechseln, dieselbe Kammer auswählen, sicher hin- und zurückfahren, unveränderte Physik/Materialkonten nachweisen und nach Neustart denselben Bauzustand sehen. Sichtprüfung und echte Maus-/Tastaturbedienung separat protokollieren. Zunächst keine fingierte Geologie anzeigen; Schnittflächen ohne Erdmodell sind als schematisch zu kennzeichnen.

## Danach: Tunnelbau und weitere Grundlagen

Unterirdischer Vortrieb braucht zusätzlich räumliche Boden-/Geologiedaten oder eine andere geeignete 3D-Geometriebeschreibung. Ein entnommener Bereich darf nicht zugleich als Oberflächenaushub und als Tunnelmaterial gezählt werden. Die heutige Hybridhülle wurde unter dem Höhenfeld eingesetzt und hat dadurch noch keinen Aushub erzeugt.

Der spätere Ablauf: Zugang herstellen, erreichbaren Abschnitt ausheben, Aushub abtransportieren, sichern/auskleiden, Kollision und Wasserabdichtung prüfen, Abschnitt freigeben. Portale, Trasse und Oberfläche werden abhängige Teilaufträge eines gemeinsamen Plans.

Fahrzeuge erhalten Fähigkeiten wie ausheben, laden, transportieren und verteilen. Modell, bewegliche Teile und Animation werden über Adapter an den Arbeitsfortschritt gebunden; ihre tatsächliche Eignung wird erst aus dem separaten Importbericht übernommen. Keine erfolgreiche Fahrzeuganimation vorwegnehmen.

Danach priorisieren: Bürger-/Maschinenwege nach Bodenänderungen, mehrere konkurrierende Baustellen, frischer Karten-Cook und verpackte Bedien-/Neustartabnahme; größere Welten und Streaming erst mit gezielten Leistungsnachweisen. Räumliche ShaderWorld-Layer werden als Projektion unseres Zustands erprobt, nicht vorab zum alleinigen Speicher erklärt.[^storage]

## Zuständigkeiten nach der Projektfreigabe

- Hauptarbeit: gemeinsamer Auftragsvertrag, tatsächlicher Ausgangsboden, Materialkonten und Save-Migration; Integration der ersten Anheben-/Absenken-Runde.
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
