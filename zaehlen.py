"""Zählt, welche Einträge von awesome-local-ai für vier typische Rechner dokumentiert sind.

Aufruf: python3 zaehlen.py <pfad-zur-kopie-von-awesome-local-ai>
Nur Standardbibliothek, keine Modelle, keine Netzverbindung.
"""

import glob
import json
import os
import sys

RECHNER = {
    "Büro-Laptop mit Windows, ohne Grafikkarte": ("windows", {"cpu"}),
    "Windows-Workstation mit NVIDIA-Karte": ("windows", {"nvidia-gpu", "cpu"}),
    "Mac mit Apple-Chip": ("macos", {"apple-silicon", "cpu"}),
    "DGX Spark": ("linux", {"dgx-spark"}),
}


def laden(root):
    pfade = sorted(glob.glob(os.path.join(root, "data", "projects", "*.json")))
    if not pfade:
        sys.exit(f"Keine Datensätze unter {root}/data/projects gefunden.")
    return [json.load(open(p, encoding="utf-8")) for p in pfade]


def einordnen(eintrag, plattform, hardware):
    """dokumentiert, unbekannt oder None. Leere Felder heißen laut Liste 'unbekannt'."""
    plattformen, hw = set(eintrag["platforms"]), set(eintrag["hardware"])
    spark = "dgx-spark" in hardware and "dgx-spark" in hw
    plattform_ok = plattform in plattformen or spark
    hw_ok = bool(hw & hardware)
    if plattform_ok and (hw_ok or (not hw and eintrag["local_mode"] == "local-client")):
        return "dokumentiert"
    if (plattform_ok or not plattformen) and (hw_ok or not hw):
        return "unbekannt"
    return None


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    eintraege = laden(sys.argv[1])
    lokal = [e for e in eintraege if e["local_mode"] != "cloud-dependent"]
    print(f"Einträge gesamt: {len(eintraege)}, davon lokal: {len(lokal)}\n")
    for name, (plattform, hardware) in RECHNER.items():
        gruppen = {"dokumentiert": [], "unbekannt": []}
        for e in lokal:
            klasse = einordnen(e, plattform, hardware)
            if klasse:
                gruppen[klasse].append(e)
        modell = [e["name"] for e in gruppen["dokumentiert"] if "serve-models" in e["use_cases"]]
        print(name)
        print(f"  dokumentiert: {len(gruppen['dokumentiert'])}  {', '.join(e['name'] for e in gruppen['dokumentiert'])}")
        print(f"  davon Modell betreiben: {len(modell)}  {', '.join(modell)}")
        print(f"  unbekannt (leere Felder): {len(gruppen['unbekannt'])}  {', '.join(e['name'] for e in gruppen['unbekannt'])}\n")
    nur_spark = [e["name"] for e in eintraege if e["hardware"] == ["dgx-spark"]]
    print(f"Nur für DGX Spark eingetragen: {len(nur_spark)}  {', '.join(nur_spark)}")
    print(f"Benannte Einschränkungen: {sum(len(e['limitations']) for e in eintraege)}")
    print(f"Quellenangaben: {sum(len(e['sources']) for e in eintraege)}")
    print(f"Ohne klare Lizenz: {', '.join(e['name'] for e in eintraege if not (e.get('license') or {}).get('spdx'))}")


if __name__ == "__main__":
    main()
