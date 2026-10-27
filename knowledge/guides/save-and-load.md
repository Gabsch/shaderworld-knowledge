---
type: Guide
title: Bauplätze und Straßen nach einem Spielneustart laden
description: Das eigene CityLab-Spielstandlabor bedienen und den nachgewiesenen Umfang der Persistenz verstehen.
tags: [shaderworld, savegame, persistence, citybuilder, runtime, collision]
engine_version: "5.8.4"
plugin_version: "4.1"
status: draft
generated: { by: codex/gpt-6, at: "2026-10-27T21:49:03Z" }
evidence_scope:
  tested: Zwei getrennte gerenderte Spielprozesse mit zwei Bauplätzen und zwei Straßentrassen sowie Kollisionsproben
  observed: Tastaturbedienung und verzögertes automatisches Laden nach einem Editor-Neustart im ursprünglichen Testprojekt
  not_tested: Verpackter Shipping-Build, Navigation, Multiplayer, Gebäude, Rodung und große Änderungsmengen
sources:
  - id: persistence-proof
    resource: ../evidence/persistence-report.json
    title: Neustartnachweis des Spielstandlabors
  - id: citylab-view
    resource: ../assets/images/citylab-terrain.png
    title: Illustration der verwandten CityLab-Geländeversuche
  - id: lab-implementation
    resource: "Originales Testprojekt UnrealMcpTest: CityLabPersistence.h/.cpp, CityLabGameMode.h/.cpp und CityLabVerification.h/.cpp; nicht in diesem Dokumentations-Repository enthalten"
    title: Projektlokale Laufzeit-, Bedienungs- und Testimplementierung
  - id: shaderworld-brush-docs
    resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass
    title: Offizielle Erklärung der Laufzeitaktualisierung von Brushes
---
# Bauplätze und Straßen nach einem Spielneustart laden

Im Testprojekt lassen sich während des Spiels Bauplätze ebnen und Straßentrassen anlegen, speichern und in einem neuen Spielprozess wiederherstellen. Das ist durch einen Test mit zwei getrennten Prozessen und echten Terrain-Kollisionsabfragen belegt.[^persistence-proof]

Die Speicherfunktion ist eine **eigene C++-Erweiterung des Testprojekts**. Sie ist kein allgemeiner ShaderWorld-Menüpunkt und wird durch das Aktivieren des Plugins allein nicht verfügbar. ShaderWorld liefert die verformbaren Terrain- und Straßenbausteine; das Projekt speichert die logischen Stadtänderungen und baut sie beim Laden neu auf.[^lab-implementation]

## Was du zum Nachmachen brauchst

Du benötigst das ursprüngliche, lauffähig kompilierte Projekt **UnrealMcpTest** mit Unreal Engine 5.8.4, ShaderWorld 4.1 und der Karte `/Game/Maps/ShaderWorldPersistenceLab`. In deren World Settings muss der projektlokale **CityLabGameMode** verwendet werden.

Dieses öffentliche Repository enthält ausschließlich Wissen und ausgewählte Nachweise. Das Unreal-Projekt, das native Runtime-Modul, die Karte und ihre Materialien werden hier nicht mitgeliefert. Ein Klon dieses Repositories reicht deshalb nicht aus, um das Labor zu starten.

![Illustration: Gelände, Baufläche und Trasse der verwandten CityLab-Versuche](../assets/images/citylab-terrain.png)

Die Abbildung illustriert die verwandte **CityLab**-Geländekarte. Sie ist keine Aufnahme des Neustarttests und ersetzt dessen Messdaten nicht.[^citylab-view]

## Das Labor starten und bauen

1. Öffne im ursprünglichen Projekt den Content Browser und dort **Content → Maps → ShaderWorldPersistenceLab**.
2. Prüfe in **World Settings → GameMode Override**, dass **CityLabGameMode** eingestellt ist. Starte **Play** und klicke in das Spielfenster, damit es Tastatureingaben erhält.
3. Warte, bis das Gelände sichtbar und unter dem Mauszeiger erreichbar ist. Ein vorhandener Spielstand wird erst geladen, wenn die Grundwelt erzeugt wurde. Notiere die bereits angezeigte Anzahl an Bauplätzen und Straßen.
4. Zeige auf eine freie Stelle und drücke **P**. Der Bauplatz wird auf die getroffene Bodenhöhe plus den angezeigten Höhenversatz geebnet.
5. Für eine deutliche Höhenänderung drücke beispielsweise zweimal **E** und setze an einer anderen Stelle einen weiteren Bauplatz. **Q** senkt den Versatz wieder um jeweils einen Meter.
6. Für eine Straße zeige auf den Anfang und drücke **R**. Bewege den Mauszeiger zum Ende und drücke erneut **R**. Die beiden Punkte müssen mindestens einen Meter auseinanderliegen. Ihre Höhen bestimmen die Steigung.
7. Warte nach jeder Änderung, bis Gelände und Kollision nachgezogen haben. Prüfe die Statusmeldung und die angezeigten Objektzahlen.

Die Bedienung verwendet folgende Tasten:[^lab-implementation]

| Eingabe | Wirkung |
| --- | --- |
| **P** | Bauplatz am Mauszeiger anlegen. |
| **R**, dann **R** | Anfang und Ende einer geraden Straßentrasse setzen. |
| **Q / E** | Höhenversatz für anschließend gesetzte Punkte um 1 m senken / erhöhen. |
| **K** | Aktuellen Zustand im Slot `CityLabCity` speichern. |
| **L** | Gespeicherten Zustand laden und die aktuell verwalteten Änderungen ersetzen. |
| **WASD** | Kamera verschieben. |
| **Rechte Maustaste + Maus** | Blick drehen. |
| **Mausrad** | Zoomen. |

**Q/E verschiebt bereits gesetzte Objekte nicht.** Der Versatz wird zu einem neuen Bodenhit addiert; er ist keine absolute Welthöhe. Ein Bauplatz verwendet einen Brushbereich mit 10 m Radiusparameter und einen ebenen Kern von 12 × 12 m. Die Straßenbedienung erzeugt einen 8 m breiten ebenen Streifen mit je 4 m Übergang. Sichtbarer Asphalt, Kreuzungen und Verkehr entstehen dadurch noch nicht.[^lab-implementation]

## Speichern und Laden selbst prüfen

**K überschreibt den festen Slot `CityLabCity`.** Neue Änderungen werden nicht automatisch gespeichert. Im Development-Labor liegt der Slot projektbezogen unter `Saved/SaveGames/CityLabCity.sav`.[^lab-implementation]

1. Baue einen gut erkennbaren Bauplatz und eine Straße. Merke dir Position, Höhe und die angezeigten Objektzahlen.
2. Drücke **K** und prüfe die Meldung **Stadt gespeichert**.
3. Lege einen zusätzlichen Bauplatz an und speichere ihn noch nicht. Drücke **L**. Nach der Aktualisierung soll dieser zusätzliche Bauplatz wieder verschwunden sein; die zuvor gespeicherte Stadt soll zurückkehren. **L verwirft damit ungespeicherte Änderungen.**
4. Beende Play. Schließe anschließend den Editor vollständig und öffne das ursprüngliche Projekt erneut. Öffne dieselbe Persistenzkarte und starte Play.
5. Warte auf **Gespeicherte Stadt wiederhergestellt**. Prüfe erneut Anzahl, Positionen und Höhen. Das automatische Laden geschieht verzögert nach der ShaderWorld-Grunderzeugung, damit dieselben Generator- und Seed-Identitäten verfügbar sind.
6. Drücke testweise noch einmal **L**. Die Anzahl darf sich dadurch nicht verdoppeln.

Das Speichern des Editor-Levels ersetzt **K** nicht. Der Spielstand beschreibt die Laufzeitstadt; die Map enthält die Ausgangswelt und die Spieleinrichtung.[^lab-implementation]

## Was der vorhandene Nachweis tatsächlich belegt

Der automatisierte Lauf erzeugte zwei Bauplätze und zwei Straßentrassen, schrieb einen Spielstand und lud ihn nach Ende des ersten Prozesses in einem zweiten Prozess. IDs, Geometrie und Änderungsreihenfolge blieben erhalten. Pro Prozess wurden 26 Terrainproben vor und 26 nach der Änderung beziehungsweise Wiederherstellung geprüft. Die Toleranz betrug 3 cm; der größte gemessene Fehler nach den Änderungen einschließlich unveränderter Kontrollpunkte lag bei rund 0,63 cm.[^persistence-proof]

| Geprüfter Fall | Ergebnis im Labor |
| --- | --- |
| Neuer Prozess lädt gespeicherte Änderungen | Bauplätze und Straßentrassen samt geprüfter Terrainkollision wiederhergestellt. |
| Erneut denselben Spielstand laden | Keine Duplikate; IDs, Geometrie und Reihenfolge erhalten. |
| Fehlenden Slot laden | Aktuelle leere oder bereits geladene Stadt bleibt erhalten. |
| Spielstand mit falscher Formatversion laden | Vorhandene Stadt bleibt erhalten. |

Diese Prüfungen liefen als **uncooked Development-Editor-Laufzeit** mit `UnrealEditor.exe -game -RenderOffscreen` und gerenderten Frames. Das belegt einen vollständigen Neustart des Spielprozesses. Ein verpackter Shipping-Build wurde dabei nicht getestet.[^persistence-proof]

## Wie die Speicherung funktioniert

Gespeichert werden Bauplatzmittelpunkte und Radiusparameter sowie Straßenkontrollpunkte, Breiten, Übergänge und Tiefe. Jedes Objekt erhält eine stabile ID; eine gemeinsame Reihenfolge steuert die Priorität überlappender Änderungen. Beim Laden erzeugt das Projekt daraus neue native ShaderWorld-Brushes und Straßenkomponenten.[^lab-implementation]

Der Spielstand trägt eine Formatversion und Identitäten für Karte, Generator und Terrainkonfiguration einschließlich relevanter Materialparameter und Seeds. Das Projekt prüft diese Angaben und die Geometrie, bevor es die aktuelle Stadt ersetzt. Ein anderes Terrain oder eine geänderte Generatorbasis benötigt später eine bewusste Migration. Die Identitätsprüfung ist keine vollständige Versionsverwaltung aller abhängigen Assets.[^lab-implementation]

Eine erfolgreiche Ladebestätigung bedeutet zunächst, dass die Daten übernommen wurden. GPU-Gelände und Physikkollision aktualisieren sich anschließend. Die automatische Bereitschaftsprüfung ist keine vollständige Fertigmeldung der Physik; der automatisierte Test wartet deshalb zusätzlich auf passende Kollisionstreffer. Auch die Herstellerdokumentation beschreibt Terrain-, Kollisions- und Spawnable-Aktualisierung als Folge einer Brush-Änderung.[^lab-implementation][^shaderworld-brush-docs]

## Wenn etwas nicht klappt

| Beobachtung | Als Nächstes prüfen |
| --- | --- |
| P/R/K/L tun nichts | Läuft Play, hat das Spielfenster Fokus und ist CityLabGameMode aktiv? |
| Kein Boden unter dem Mauszeiger | Shader und Terrainaufbau abwarten; Generate Collision und die lokale Kollisionsabdeckung prüfen. |
| Straße fehlt nach dem ersten R | Den zweiten Endpunkt mit R setzen, mindestens einen Meter entfernt. |
| Neue Änderungen fehlen nach Neustart | Wurde nach diesen Änderungen K gedrückt und dieselbe Persistenzkarte geöffnet? |
| L meldet inkompatiblen Spielstand | Karte, Generator, Seeds oder Terrainkonfiguration mit der gespeicherten Basis vergleichen. Die aktuelle Stadt wird bei Ablehnung nicht ersetzt. |
| Gelände sieht geladen aus, Bodenhit stimmt noch nicht | Weitere gerenderte Frames und Kollisionsaktualisierung abwarten. |

Gebäude, entfernte Vegetation, Verkehrsnetz, Navigation, Tunnel und Multiplayerzustand gehören noch nicht zu diesem kleinen Spielstandmodell. Sie benötigen eigene gespeicherte Daten und eigene Abnahmen. Für die geometrischen Grenzen eines Tunnels siehe [Löcher im Gelände und Bergtunnel](holes-and-mountain-tunnels.md).

[^persistence-proof]: [Bereinigter Bericht des Neustarttests](../evidence/persistence-report.json), mit ausgewählten Prüfungen und Messwerten aus dem ursprünglichen Testprojekt.
[^citylab-view]: [Illustration der CityLab-Geländeversuche](../assets/images/citylab-terrain.png); andere Karte als das Persistenzlabor.
[^lab-implementation]: Geprüfte projektlokale Implementierung in `CityLabPersistence.h/.cpp`, `CityLabGameMode.h/.cpp` und `CityLabVerification.h/.cpp` sowie das Bedienungsprotokoll des ursprünglichen Testprojekts. Diese Dateien sind nicht Bestandteil des öffentlichen Dokumentationsbundles.
[^shaderworld-brush-docs]: [ShaderWorld: Blueprint Brush System – Landmass](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass).
