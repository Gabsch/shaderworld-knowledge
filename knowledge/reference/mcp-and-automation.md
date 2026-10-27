---
type: Playbook
title: MCP und Automatisierung
description: Den nativen Unreal-MCP und die lokalen Laborwerkzeuge einordnen.
tags:
- shaderworld
- unreal-engine
- city-builder
status: stable
engine_version: 5.8.4
plugin_version: '4.1'
evidence_scope: Native MCP-Verbindung und Editoraktionen geprüft; kein Hersteller-MCP
  nachgewiesen
generated:
  by: codex/gpt-6
  at: '2026-10-27T21:55:15Z'
sources:
- id: epic
  resource: https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor
  title: Epic Unreal MCP
- id: terrain-proof
  resource: ../evidence/terrain-report.json
  title: Native Editorprüfung im Lernprojekt
---
# MCP und Automatisierung

Im ursprünglichen Lernprojekt ist der **native Unreal-MCP aus UE 5.8** eingerichtet. Epics Schnittstelle ist als **Experimental** eingeordnet. Die Projektkonfiguration aktiviert **Model Context Protocol** und **All Toolsets**. Er stellt allgemeine Editorwerkzeuge bereit, mit denen Actors, Eigenschaften, Materialien, Karten und PIE bedient werden können. Damit konnten wir ShaderWorld konfigurieren und Prüfungen ausführen.[^epic][^terrain-proof]

Ein öffentlich veröffentlichter ShaderWorld-eigener MCP wurde bei unserer Recherche vom 27. Oktober 2026 nicht nachgewiesen. Daraus folgt keine Aussage über private Discord- oder GitHub-Angebote.

## Was du ohne MCP machen kannst

Die Editor-Rezepte dieser Wissensbasis sind von Hand durchführbar. Du brauchst für Wind und Schaum, das Öffnen einer Map oder die Prüfung einer Einstellung keinen Agenten und keinen MCP. Die automatisierte Terrain-/Persistenzprüfung braucht dagegen die zusätzlichen Werkzeuge des ursprünglichen Lernprojekts.

## Vorhandene lokale Werkzeuge

Diese Dateien gehören zum ursprünglichen Unreal-Testprojekt, nicht zum öffentlichen Doku-Repository:

| Werkzeug unter Tools | Zweck |
| --- | --- |
| setup_shaderworld.py / verify_shaderworld.py | Flache Referenz vorbereiten, Editor/PIE und vier Kollisionstreffer prüfen |
| setup_citylab.py / verify_citylab.py | Hügel, Bauplatz und native Straßentrasse vorbereiten und prüfen |
| setup_persistence.py / verify_persistence.py | Separates Spielstandlabor und zwei unabhängige Spielprozesse |
| tour_shaderworld.py | Demo-Maps als Projektkopien laden, Actors lesen und Viewport aufnehmen |
| mcp_client.py | Verbindung zur lokalen Unreal-MCP-Schnittstelle |

Die bekannte lokale Adresse lautet `http://127.0.0.1:8000/mcp`. Ob dein Editor denselben Port verwendet, musst du an seiner MCP-Konfiguration prüfen. Die Skripte können Maps laden sowie PIE starten und beenden; eigene offene Versuche vorher speichern.

## Erkenntnisse für spätere Automatisierung

- Beim vorhandenen Actor-Werkzeug ersetzt `set_actor_transform` den ganzen Transform. Position, Rotation und Skalierung müssen gemeinsam übertragen werden.
- Nach dem Anheften einer Komponente kann eine zuvor bestehende Weltskalierung als relative Skalierung weiterwirken. Die CityLab-Straße brauchte explizit `(1,1,1)`.
- Die generische JSON-Zuweisung einer RootComponent an einen leeren Actor blockierte in unserem Versuch den Editor. Das Einrichtungsskript verwendet deshalb einen Actor mit vorhandener Scene-Root.
- GPU-Terrain und Kollisionsgenerierung arbeiten asynchron. Eine erfolgreiche API-Antwort ist noch kein Beleg für eine fertige Physikkollision.

Das sind Befunde unserer Werkzeugversion und unseres Projekts. Sie müssen bei Änderungen am Unreal-MCP erneut geprüft werden.

[^epic]: [Epic: Unreal MCP im Unreal Editor](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor).
[^terrain-proof]: [Terrain-Prüfbericht](../evidence/terrain-report.json).
