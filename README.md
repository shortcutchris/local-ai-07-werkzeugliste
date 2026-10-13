# local-ai-07-werkzeugliste

Demo zu **Local AI, Ausgabe 07: „Dein Einstieg in lokale KI?"**. Zählt, welche Einträge der Werkzeugliste
[awesome-local-ai](https://github.com/SeraphimSerapis/awesome-local-ai) für vier typische Rechner
ausdrücklich dokumentiert sind.

Keine Modelle, keine Grafikkarte, keine Netzverbindung beim Zählen. Nur Python 3 und eine Kopie der Liste.

## Schnellstart

```sh
git clone --depth 1 https://github.com/SeraphimSerapis/awesome-local-ai
python3 zaehlen.py awesome-local-ai
```

## Was gezählt wird

Für jeden Rechner prüft das Skript alle Datensätze unter `data/projects/`:

- **dokumentiert**: Betriebssystem und Hardware des Rechners stehen im Eintrag. Programme ohne
  Hardware-Angabe, die selbst kein Modell rechnen (`local-client`), zählen hier, wenn das
  Betriebssystem passt.
- **davon Modell betreiben**: dokumentierte Einträge mit dem Anwendungsfall `serve-models`.
- **unbekannt**: Betriebssystem oder Hardware sind leer. Leere Felder heißen laut Liste
  „unbekannt", nicht „läuft nicht".

Einträge mit `cloud-dependent` bleiben außen vor.

## Ergebnis vom 11.10.2026 (Commit b9a27d1)

| Rechner | dokumentiert | davon Modell betreiben |
|---|---|---|
| Büro-Laptop mit Windows, ohne Grafikkarte | 3 | 1 |
| Windows-Workstation mit NVIDIA-Karte | 4 | 2 |
| Mac mit Apple-Chip | 10 | 6 |
| DGX Spark | 17 | 7 |

Neun Einträge sind ausschließlich für den DGX Spark eingetragen. Vollständige Ausgabe:
[`ergebnisse/2026-10-11-commit-b9a27d1.txt`](ergebnisse/2026-10-11-commit-b9a27d1.txt).

## Grenzen

- Die Zählung gibt wieder, was in den Datensätzen steht. Sie sagt nichts darüber, ob ein Werkzeug
  auf einem nicht eingetragenen Rechner trotzdem läuft.
- Die Liste ist im Oktober 2026 gestartet und wächst schnell. Neue Zahlen bekommst Du, indem Du das
  Skript gegen den aktuellen Stand laufen lässt.
- Die Zählregeln sind meine. Wer sie anders setzen will, ändert `einordnen()` in `zaehlen.py`.

## Den eigenen Agenten fragen

Die Liste bringt eine Anleitung für Agenten mit (`AGENTS.md`). Dieser Prompt steht dort sinngemäß:

> Lies dieses Repository und hilf mir, ein lokales Setup für meinen Rechner auszuwählen. Frag zuerst
> nach Hardware und Anforderungen. Vergleiche passende Werkzeuge, zitiere ihre Dokumentation und
> trenne, was dokumentiert und was ungetestet ist. Installiere nichts.

## English

A small script for Local AI issue 07. It counts which entries of the awesome-local-ai catalog document
support for four typical machines: a Windows office laptop without a GPU (1 entry can run a model), a
Windows workstation with an NVIDIA card (2), a Mac with Apple silicon (6) and an NVIDIA DGX Spark (7).
Empty fields count as unknown, not as unsupported. Standard library only; run it against a fresh clone
to get current numbers.

## Lizenz

MIT
