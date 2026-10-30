---
type: Reference
title: CityLab-Quellen mit Git absichern
description: Vorschlag für ein eigenes privates Quellrepository mit getrennten Assets, Spielständen und öffentlicher OKF-Dokumentation.
status: draft
tags: [citylab, git, reproducibility, planning]
engine_version: "5.8.4"
plugin_version: "4.1"
generated:
  by: codex/gpt-6
  at: "2026-10-30T12:53:50.454522+00:00"
evidence_scope:
  source: Lesende Bestandsaufnahme des Projekts, der vorhandenen Ausschlussdatei und der getrennten OKF-Ablage. Kein Repository angelegt, keine Projektdateien versioniert oder veröffentlicht.
  runtime: Keine Spiel-, Build-, Wiederherstellungs- oder Lizenzprüfung durch diesen Plan.
sources:
  - id: local-inventory
    resource: "Lesende lokale Bestandsaufnahme am 30. Oktober 2026: kein eigenes .git am Unreal-Projekt; eigenes .git der OKF-Ablage. Die Projekt-.gitignore enthält bislang nur Binaries, DerivedDataCache, Intermediate, Saved und .vs. Source und Tools zusammen etwa 3,6 MB; vorhandene Road-Creator-, Fahrzeug- und Erdmaterialbestände zusammen etwa 1,55 GB. Diese Projektbestände und ihre Konfiguration werden nicht mitgeliefert."
    title: Lokaler Umfang und vorhandene Ausschlüsse, ausschließlich Dateibefund
  - id: maintenance
    resource: ../maintenance.md
    title: Öffentliches Wissen von privaten Projektdateien und lizenzierten Inhalten trennen
  - id: roads
    resource: road-construction-work-plan.md
    title: Straßen-Slice und bewusst getrennte spätere RCP-Integration
---
# CityLab-Quellen mit Git absichern

**Vorschlag, noch nicht eingerichtet:** CityLab erhält ein eigenes privates Quellrepository. Das öffentliche ShaderWorld-OKF bleibt ein eigenes Repository. Der Nutzer hat Git als nächstes Thema angesprochen; daraus wird hier keine bereits erfolgte Veröffentlichung oder Änderung der vorhandenen Repository-Struktur abgeleitet.[^local-inventory][^maintenance]

Die kleine Quellbasis und die großen importierten Assetpakete brauchen unterschiedliche Regeln. Der aktuelle RoadConstruction8-Straßenfix ist im begrenzten Umfang gebaut, im Spiel und nach kalten Neustarts geprüft; Git ist weiterhin der nächste eigenständige Schritt. Die vollständige Bestandsaufnahme von Road Creator Pro folgt anschließend als eigenes Thema.[^roads]

## Was in die erste Quellfassung gehört

| Bestandteil | Vorgeschlagene Behandlung |
| --- | --- |
| Eigener Code und Werkzeuge | `Source`, `Tools`, Projektbeschreibung und projektbezogene Agentenanweisungen aufnehmen. Vorher Dateiliste und Inhalt prüfen. |
| Projektkonfiguration | Nur geprüfte, benötigte Einstellungen aufnehmen. Zugangsdaten und rechnergebundene Werte vorher auslagern; eine bereinigte Vorlage und die Einrichtung beschreiben. |
| Eigene Karten und Assets | Benötigte selbst erstellte Inhalte einzeln auswählen. Für geeignete große Binärdateien Git LFS vor dem ersten Commit einrichten und den tatsächlichen Clone prüfen. |
| Zugekaufte oder separat bezogene Pakete | Eine Installationsliste mit Paketname, Version, Herkunft und benötigten Pfaden dokumentieren. Erst nach Prüfung der jeweiligen Weitergaberechte festlegen, welche Dateien überhaupt in das private Repository dürfen. |
| Öffentliche OKF-Dokumentation | Bestehendes Repository getrennt erhalten und per festem Commit oder dokumentierter Referenz zuordnen. Wissen weiterhin über PR pflegen. |
| Generierte Dateien und Spielstände | Buildprodukte, Caches, Logs, Paketarchive und persönliche Spielstände ausschließen. Testbelege gezielt und bereinigt dokumentieren. |

Die vorhandene `.gitignore` reicht als Veröffentlichungsregel noch nicht aus. Sie schließt die üblichen generierten Verzeichnisse aus, unterscheidet aber weder importierte Pakete noch rechnergebundene Konfiguration oder sensible Werte.[^local-inventory]

## Vorgehen für die erste abgesicherte Version

1. Das eigene Projekt-Repository klar vom übergeordneten Arbeitsverzeichnis und vom OKF-Repository abgrenzen. Vor jedem Commit muss die erfasste Dateiliste tatsächlich zum richtigen Repository gehören.
2. Ausschlussregeln und Konfigurationsvorlagen prüfen, bevor Dateien zur ersten Version hinzugefügt werden. Importierte Inhalte bleiben zunächst über die Installationsliste nachvollziehbar.
3. Die tatsächlich benötigten eigenen Karten und Binärdateien auswählen. Bei LFS prüfen, dass ein frischer Clone vollständige Dateien erhält und keine bloßen Zeigerdateien im Unreal-Content verbleiben.
4. Einen geprüften Ausgangsstand mit Engine-/Pluginversion, Buildbefehl und bestandenem Testumfang festhalten. Ein Commit allein belegt keinen funktionierenden Build.
5. In einem getrennten Checkout rekonstruieren, Abhängigkeiten einrichten und bauen. Erst dieser Versuch zeigt, ob der dokumentierte Ausgangsstand wiederherstellbar ist.
6. Künftige Änderungen auf Entwicklungsbranches und über PRs pflegen. Den passenden OKF-Commit mit dem getesteten Projektstand verknüpfen; normale Spielerdateien bleiben außerhalb von Git.

## Noch zu entscheiden und zu prüfen

- Name und Ziel des privaten CityLab-Repositories.
- Welche selbst erstellten Karten und importabhängigen Assets zur ersten reproduzierbaren Fassung gehören.
- Konkrete LFS-Auswahl sowie Ablage und Installation der separat bezogenen Pakete.
- Bereinigung und Einrichtung der benötigten lokalen Konfiguration.
- Erster vollständiger Wiederherstellungsversuch aus einem frischen Checkout.

Keine dieser Prüfungen ist durch diesen Entwurf erledigt. Insbesondere enthält das öffentliche OKF weder Projektkonfiguration noch Spielstände, Unreal-Binärassets oder Plugin-Quellen.[^maintenance]

[^local-inventory]: Beschriebene lokale Dateibestandsaufnahme; nur Umfang und vorhandene Ausschlüsse geprüft.
[^maintenance]: [Wartungs- und Veröffentlichungsregeln](../maintenance.md).
[^roads]: [Vereinbarter Straßenplan](road-construction-work-plan.md).
