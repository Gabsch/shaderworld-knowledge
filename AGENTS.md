# Arbeiten an dieser Wissensbasis

Lies zuerst `knowledge/index.md`, `knowledge/verification.md` und `knowledge/maintenance.md`.

- Schreibe verständliche deutsche Anleitungen für Leser ohne C++-Kenntnisse. Ziel, Voraussetzungen, Editor-Schritte, erwartetes Ergebnis und Fehlerhilfe gehören zusammen.
- Das OKF-Bundle liegt ausschließlich unter `knowledge/`. Nutze OKF 0.2; kanonische Spezifikation: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md.
- Kennzeichne Herstellerangaben, Codebefunde und praktische Tests getrennt. Ein Linktest bestätigt keinen Spielablauf. `human:` in `verified` nur nach dokumentierter menschlicher Prüfung verwenden.
- Nenne UE-/ShaderWorld-Versionen und verlinke Quellen sowie Belegdateien. Erfinde keine erfolgreichen Tests und keine beobachteten Editor-Klicks.
- Vor Änderungen Zeilenenden prüfen und beibehalten. Neue Textdateien in diesem Windows-Projekt: UTF-8, CRLF, keine gemischten Zeilenenden.
- Keine lokalen Benutzerpfade, Zugangsdaten, `.sav`-Dateien, Unreal-Projektdateien, Plugin-Quellen, `.uasset`- oder `.umap`-Dateien veröffentlichen.
- Bilder gezielt übernehmen, visuell prüfen und ihre Herkunft in `knowledge/evidence/image-manifest.json` erfassen. Technische Warnungen nicht als gelöst darstellen.
- Kleine Aktualisierungen in `knowledge/log.md` festhalten; Index und Querverweise aktuell halten.
- Vor Veröffentlichung `python tools/validate_knowledge.py` ausführen, Git-Diff/Dateiliste auf private Daten prüfen und ausschließlich dieses Repository stagen. Das übergeordnete Unreal-Projekt gehört nicht in den Commit.
