---
type: Playbook
title: Fehler gezielt eingrenzen
description: Typische ShaderWorld-Fehler anhand von sichtbaren Symptomen prüfen.
tags:
- shaderworld
- unreal-engine
- city-builder
status: stable
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: Beobachtete Fehlerbilder und ausdrücklich gekennzeichnete Codebefunde
generated:
  by: codex/gpt-6
  at: '2026-10-27T21:54:47Z'
sources:
- id: terrain-proof
  resource: ../evidence/terrain-report.json
  title: Terrainprüfung
- id: ocean-proof
  resource: ../evidence/ocean-report.json
  title: Ozeanprüfung
- id: hole-proof
  resource: ../evidence/hole-report.json
  title: Lochprüfung und Grenzen
- id: brush-doc
  resource: https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass
  title: Blueprint Brush System
---


# Fehler gezielt eingrenzen

Beginne beim sichtbaren Symptom. Ändere möglichst eine Ursache nach der anderen und kontrolliere danach das erwartete Ergebnis.

| Symptom | Zuerst prüfen | Erfolg erkennen |
| --- | --- | --- |
| Terrain oder Meer fehlen nach dem Laden | Shaderkompilierung beenden lassen, Editor/Viewport aktivieren und Realtime einschalten; bei Bedarf Play starten | Oberfläche wird nach gerenderten Frames aufgebaut |
| Gelände ist sichtbar, die Figur fällt hindurch | Generate Collision aktiv? Wird Kollision in der Nähe dieser Figur angefordert? | Die Figur bleibt nach fertiger Kollisionsgenerierung auf dem Terrain |
| Große Baukamera, aber Bodenabfragen fehlen | Darstellungsreichweite und Kollisionsreichweite getrennt betrachten; im CityLab gibt es einen eigenen Kollisionsanker | Terrain-Traces nahe dem Baugebiet treffen wirklich den Terrain-Actor |
| Schaum ist eingeschaltet, aber unsichtbar | Am Ocean-Actor Rebuild auslösen und einige Sekunden aktive Frames abwarten | Weiße Schaumflächen bilden sich auf Wellenkämmen |
| Schaum kommt trotz Rebuild nicht | Choppiness muss größer 0 sein; oceanfähiges Oberflächenmaterial verwenden | Schaum reagiert auf Faltung der Wellenkämme |
| Speichern/Laden reagiert nicht | In den PIE-Spielbereich klicken; CityLab-Karte und deren GameMode verwenden; K/L statt F5/F9 | HUD-/Log-Rückmeldung und sichtbare Rekonstruktion |
| Figur wird unter dem Gelände nach oben versetzt | An ihrer SW_Collision-Komponente Prevent Falling Under Terrain prüfen | Im Tunnelbereich verhindert diese Hilfsfunktion keinen Abstieg |

Die ersten Terrainfälle wurden beim Aufbau der Referenz beobachtet; Wind und Schaum wurden nach Parameter-Readback und Rebuild visuell bestätigt.[^terrain-proof][^ocean-proof] Die Tunnelzeile ist eine aus der aktuellen Komponente abgeleitete Prüfung, noch kein abgenommener Bergtunnel.

## Die rote Lumen-Meldung in unseren Bildern

Einige Viewport-Aufnahmen melden, dass **Lumen keine Ray-Tracing-Daten** besitzt. Im Projekt fehlen dafür geeignete Software-Distance-Field-Daten beziehungsweise aktiviertes Hardware-Ray-Tracing. Die dokumentierte Umstellung auf DX12/SM6 behob eine andere, zuvor beobachtete Nanite-Warnung. Die Lumen-Meldung ist weiterhin offen.

Die Bilder zeigen deshalb den beobachteten Terrain-/Wassereffekt, aber keine fertig abgestimmte Beleuchtung. Die Meldung einfach auszublenden wäre kein Renderer-Fix. Für eine spätere Rendererkonfiguration müssen Zielhardware und gewählte Lumen-Methode gemeinsam geprüft werden.

## Löcher treffen bei einem Trace trotzdem etwas

Unter der ausgeschnittenen Terrainfläche können separate Planes oder Tunnelmeshes liegen. Ein beliebiger Treffer beweist deshalb nicht, dass das Terrainloch geschlossen ist. Zur Prüfung muss erkennbar sein, **welcher Actor** getroffen wurde. Unsere Heightmap-Demo wurde visuell und anhand ihrer Komponenten untersucht; ein unabhängiger Loch-Kollisionsversuch steht noch aus.[^hole-proof]

## Ein Brush verändert nichts

Kontrolliere, ob der Brush aktiviert ist und zum richtigen Brush Manager beziehungsweise Layer gehört. Sein Einflussbereich muss die gewünschte Fläche vollständig umfassen. Die offizielle Brush-Anleitung beschreibt außerdem, dass Terrain, Kollision und Spawnables bei relevanten Änderungen neu berechnet werden.[^brush-doc]

## Falls eine ältere Anleitung andere Felder zeigt

Suche zuerst nach **Producers → Height**. Bei einem aktiven **Compute Producer** wird das Höhen-Generatormaterial ersetzt. Das ist insbesondere im aktuellen FFT-Ozean wichtig. Ein fehlender alter Materialverweis bedeutet dort nicht automatisch einen defekten Ozean. Siehe [Ozeanrezept](ocean-waves-and-foam.md) und [Versionsübersicht](../reference/versions-and-capabilities.md).

[^terrain-proof]: [Terrain-Prüfbericht](../evidence/terrain-report.json).
[^ocean-proof]: [Ozeanprüfung](../evidence/ocean-report.json).
[^hole-proof]: [Umfang der Lochprüfung](../evidence/hole-report.json).
[^brush-doc]: [Offizielles Brush-System](https://universgen.gitbook.io/shader-world/fundamentals/kick-start/blueprint-brush-system-landmass).
