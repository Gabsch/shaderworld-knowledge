---
type: Playbook
title: Nächste City-Builder-Bausteine
description: Die vereinbarten nächsten Funktionen und ihre noch offenen Abnahmen nach dem ersten Straßen- und Tunnelversuch festhalten.
status: draft
tags: [shaderworld, citylab, city-builder, roadmap]
engine_version: "5.8.4"
plugin_version: "4.1"
generated: { by: codex/gpt-6, at: "2026-10-28T03:14:36Z" }
evidence_scope: Vereinbarte Planung vom 28. Oktober 2026; keine Abnahme der hier vorgeschlagenen Funktionen.
sources:
  - id: verification
    resource: ../verification.md
    title: Tatsächlicher Prüfstand und offene Tests
  - id: capabilities
    resource: versions-and-capabilities.md
    title: Gelesene Pluginfähigkeiten und Grenzen
  - id: loop
    resource: ../guides/city-builder-loop.md
    title: Erste zusammenhängende Spielschleife
  - id: tunnel
    resource: ../guides/reusable-tunnel-component.md
    title: Vorhandene Tunnelkomponente mit Wasserausschluss
---
# Nächste City-Builder-Bausteine

Diese Liste hält die gemeinsam besprochenen nächsten Themen fest. **Die anschließenden Ausbauschritte sind geplant oder offen.** Die erste kleine Spielschleife hat inzwischen ihren abgegrenzten Drei-Prozess-Nachweis bestanden. Die vorhandenen Nachweise stehen im [Prüfstand](../verification.md); eine Empfehlung ist keine bereits verfügbare Spielfunktion.

## Jetzt: Eine zusammenhängende kleine Spielschleife

Eine Straße zur Laufzeit ziehen, daneben ein Grundstück ebnen und roden, ein Testhaus setzen und einen Bürger zum Haus laufen lassen. Nach Speichern und einem echten Spielneustart sollen Straße, Grundstück, Haus und Bürgerzustand wiederhergestellt sein. Die [Spielschleifen-Anleitung](../guides/city-builder-loop.md) beschreibt Aufbau und tatsächlichen Prüfstand.

Dafür genügen zunächst die vorhandenen Road-Creator-Assets, ShaderWorld und einfache UE-Grundformen für Haus und Bürger. Weitere Assetpakete sind für die Funktionsprüfung nicht vorgesehen. Gebäudevarianten, Figurenmodell und Animationen können später die Platzhalter ersetzen.

## Danach erhaltene Themen

| Thema | Geplantes Ergebnis | Woran wir es prüfen wollen |
| --- | --- | --- |
| Eigene Biomvorlagen | Verständliche Vorlagen für Wald, Wiese, Fels, Strand und Meeresboden; Höhen-, Hang- und Bebauungsmasken nachvollziehbar einstellen | Passende Vegetation über und unter Wasser, freie Bauflächen und unveränderte Referenzbereiche nach Neustart |
| Einzelne Ressourcen dauerhaft verwalten | Gefällte Bäume und abgebaute Ressourcen bleiben entfernt; gezielte Rücknahme ist möglich | Zustand nach Verlassen der Generationsreichweite, Rückkehr und Spielneustart vergleichen |
| Vollständiger platzierbarer Tunnel | Ein Actor verwaltet Tunnelkörper, Kollision, Terrainöffnungen und die vorhandene Air Pocket gemeinsam; Laufzeitänderungen werden gespeichert | Im Editor setzen, zur Laufzeit wiederherstellen, durchqueren und im Ozeaneinfluss trocken prüfen |
| Bauflächen nachbearbeiten | Grundstücke verschieben, gezielt entfernen und Änderungen rückgängig machen | Höhen, Bewuchs und gespeicherte Reihenfolge nach jeder Operation sowie nach Neustart vergleichen |
| Navigation nach Änderungen | Bürger finden gültige Wege nach Straßen-, Gelände- und Gebäudeänderungen | Erreichbare und blockierte Ziele, Umwege und dynamische NavMesh-Aktualisierung prüfen |
| Baukamera und Geländeabfragen | Bauen funktioniert auch aus großer Höhe und beim schnellen Bewegen der Kamera | Bodentreffer, angeforderte Kollisionsbereiche, Terrainbereitschaft und Fehlermeldungen messen |
| Verpackter Build und größere Welt | Dieselbe Spielschleife läuft außerhalb des Editors mit vielen Trassen und Brushes | Cook/Start, Speichern/Neustart, Framezeit und Speicher erfassen; anschließend Streaming untersuchen |
| Wasserabfragen, Auftrieb und Häfen | Schiffe, schwimmende Objekte und Küstenbauten erhalten belastbare Wasserinformationen | Definierte Physikobjekte, mehrere Wellenzustände und Küsten-/Tunnelbereiche gezielt testen |

Einzelne Ressourcen zu speichern ist eine andere Aufgabe als die flächige NoGrowth-Maske eines Grundstücks. Die [Fähigkeitenübersicht](versions-and-capabilities.md#biome-und-vegetation-für-die-stadt) erläutert die bisher gefundene Bookkeeping-Grenze. Ebenso ersetzt eine festgelegte Bürgerroute noch keine allgemeine Navigation.

## Terraforming bleibt bewusst offen

Anheben, Absenken, Ebnen und Bodenmaterial auftragen sollen später unter einem einheitlichen Werkzeug mit Vorschau, Rückgängig und Speicherung zusammenkommen. **Dieser Ausbau ist zurückgestellt, weil der Nutzer dafür eine eigene Überraschung angekündigt hat.** Die aktuelle Spielschleife darf ihre Grundstücke ebnen; sie legt damit kein allgemeines Terraforming-Bedienkonzept fest.

## Reihenfolge überprüfen

Die kleine Spielschleife besitzt jetzt ihren beschriebenen uncooked Neustartnachweis. Als nächste technische Absicherung früh einen verpackten Build versuchen, bevor viele Assets, PCG-Varianten oder große Welten hinzukommen. Aus der Liste wird erst dann ein umgesetzter Baustein, wenn seine Anleitung und sein abgegrenzter Nachweis ergänzt sind.
