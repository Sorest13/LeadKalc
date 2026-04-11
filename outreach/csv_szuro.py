#!/usr/bin/env python3
"""
LeadKalc CSV Prioritizáló és Szűrő v2
======================================
Most MINDKÉT forrást kezeli:
- prospect-osszes-megye.csv (6086 napelem cég → 848 egyedi)
- prospect-klima-hoszivattyu.csv (653 klíma/hőszivattyú cég)

Kimeneti listák:
- lista-1-napelem-top-priority.csv  (fő napelem cold calling)
- lista-2-napelem-website-havers.csv (cold email napelem)
- lista-3-klima-osszes.csv          (összes klíma/hőszivattyú)
- lista-4-klima-szezon-priority.csv (split-klíma telepítés, klímaszezon fókusz)
- lista-5-hoszivattyu-priority.csv  (csak hőszivattyús cégek)
- lista-6-nagy-halak.csv            (volumen alapján)
- lista-7-frostbite-napelem.csv     (email lista napelem kampányhoz)
- lista-8-frostbite-klima.csv       (email lista klíma kampányhoz)
- lista-9-master-all.csv            (minden együtt, tipus oszloppal)

Használat:
    python3 csv_szuro.py
"""

import csv
import os
from collections import Counter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_NAPELEM = os.path.join(SCRIPT_DIR, "prospect-osszes-megye.csv")
INPUT_KLIMA = os.path.join(SCRIPT_DIR, "prospect-klima-hoszivattyu.csv")


def load_csv(path):
    """CSV betöltése szótárak listájába."""
    if not os.path.exists(path):
        print(f"  ⚠ {path} nem létezik, átugorva")
        return []
    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        return list(reader)


def is_valid_website(url):
    if not url or url.strip() == "":
        return False
    return url.strip().lower().startswith("http") and "." in url


def parse_int(s):
    try:
        return int(s) if s else 0
    except (ValueError, TypeError):
        return 0


def has_email(ceg):
    email = (ceg.get("email") or "").strip()
    return email and "@" in email


def dedupe_by_email(cegek):
    """Email alapján deduplikál."""
    seen = set()
    unique = []
    for ceg in cegek:
        email = (ceg.get("email") or "").strip().lower()
        if email and email not in seen:
            seen.add(email)
            unique.append(ceg)
    return unique


def save_csv(cegek, filename, fieldnames=None):
    path = os.path.join(SCRIPT_DIR, filename)
    if not cegek:
        return 0

    if fieldnames is None:
        # Az összes előforduló mezőt összeszedi
        all_fields = set()
        for c in cegek:
            all_fields.update(c.keys())
        fieldnames = sorted(all_fields)

    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(cegek)
    return len(cegek)


def unify_klima_format(ceg):
    """Klíma cég rekord → napelem-kompatibilis közös formátum."""
    return {
        "cégnév": ceg.get("cégnév", ""),
        "kapcsolattartó": "",
        "mobil": ceg.get("telefon", ""),
        "email": ceg.get("email", ""),
        "weboldal": "",  # NKVH-ban nincs weboldal
        "válaszidő_nap": "",
        "ajánlatszám": "",
        "kivitelezés": "",
        "megye": ceg.get("megye", ""),
        "település": ceg.get("település", ""),
        "irányítószám": ceg.get("irányítószám", ""),
        "cím": ceg.get("cím", ""),
        "tevékenységek": ceg.get("tevékenységek", ""),
        "típus": "klíma/hőszivattyú",
    }


def unify_napelem_format(ceg):
    """Napelem cég rekord → közös formátum."""
    return {
        "cégnév": ceg.get("cégnév", ""),
        "kapcsolattartó": ceg.get("kapcsolattartó", ""),
        "mobil": ceg.get("mobil", ""),
        "email": ceg.get("email", ""),
        "weboldal": ceg.get("weboldal", ""),
        "válaszidő_nap": ceg.get("válaszidő_nap", ""),
        "ajánlatszám": ceg.get("ajánlatszám", ""),
        "kivitelezés": ceg.get("kivitelezés", ""),
        "megye": ceg.get("megye", ""),
        "település": "",
        "irányítószám": "",
        "cím": "",
        "tevékenységek": "Napelem",
        "típus": "napelem",
    }


def main():
    print("=" * 60)
    print("  LeadKalc Priorizáló és Szűrő v2")
    print("  Napelem + Klíma + Hőszivattyú")
    print("=" * 60)
    print()

    # BETÖLTÉS
    napelem_raw = load_csv(INPUT_NAPELEM)
    klima_raw = load_csv(INPUT_KLIMA)

    print(f"Napelem lista betöltve: {len(napelem_raw)} sor")
    print(f"Klíma lista betöltve:   {len(klima_raw)} sor")
    print()

    # DEDUPLIKÁCIÓ email alapon
    napelem_unique = dedupe_by_email(napelem_raw)
    klima_unique = dedupe_by_email(klima_raw)
    print(f"Napelem egyedi (email): {len(napelem_unique)}")
    print(f"Klíma egyedi (email):   {len(klima_unique)}")
    print()

    # ============ NAPELEM LISTÁK ============

    # Top priority: van weboldal + gyors válaszidő + komoly volumen
    napelem_top = [
        c for c in napelem_unique
        if is_valid_website(c.get("weboldal"))
        and 1 <= parse_int(c.get("válaszidő_nap")) <= 7
        and parse_int(c.get("kivitelezés")) >= 50
    ]

    napelem_website = [
        c for c in napelem_unique
        if is_valid_website(c.get("weboldal"))
    ]

    # ============ KLÍMA LISTÁK ============

    # Összes klíma cég
    klima_osszes = klima_unique

    # Klímaszezon prioritás: split-klíma telepítők (ők a nyári lakossági piac)
    klima_szezon = [
        c for c in klima_unique
        if "Split-klíma telepítés" in (c.get("tevékenységek") or "")
    ]

    # Hőszivattyús cégek
    hoszivattyu = [
        c for c in klima_unique
        if "hőszivattyú" in (c.get("tevékenységek") or "").lower()
    ]

    # ============ NAGY HALAK (volumen alapú) ============
    nagy_halak_napelem = [
        c for c in napelem_unique
        if parse_int(c.get("kivitelezés")) >= 500
        and is_valid_website(c.get("weboldal"))
    ]

    # ============ FROSTBITE IMPORT ============
    frostbite_napelem = [c for c in napelem_unique if has_email(c)]
    frostbite_klima = [c for c in klima_unique if has_email(c)]

    # ============ MASTER LISTA (mind) ============
    master = []
    for c in napelem_unique:
        master.append(unify_napelem_format(c))
    for c in klima_unique:
        master.append(unify_klima_format(c))

    # Master email deduplikáció (ha egy cég mindkét listán van)
    master_deduped = {}
    for c in master:
        email = (c.get("email") or "").strip().lower()
        if not email:
            continue
        if email in master_deduped:
            # Összevonjuk a típusokat
            existing = master_deduped[email]
            if c["típus"] not in existing["típus"]:
                existing["típus"] = existing["típus"] + " + " + c["típus"]
                existing["tevékenységek"] = existing["tevékenységek"] + " | " + c["tevékenységek"]
        else:
            master_deduped[email] = c
    master_final = list(master_deduped.values())

    # ============ MENTÉS ============
    print("-" * 60)
    print("SZŰRT LISTÁK:")
    print("-" * 60)

    lists = [
        (napelem_top, "lista-1-napelem-top-priority.csv",
         "NAPELEM fő cold calling: weboldal + gyors válaszidő + ≥50 kivitelezés"),
        (napelem_website, "lista-2-napelem-website-havers.csv",
         "NAPELEM összes weboldalas: cold email fő lista"),
        (klima_osszes, "lista-3-klima-osszes.csv",
         "KLÍMA/HŐSZIVATTYÚ összes F-gáz regisztrált cég"),
        (klima_szezon, "lista-4-klima-szezon-priority.csv",
         "KLÍMA szezon: split-klíma telepítők (lakossági)"),
        (hoszivattyu, "lista-5-hoszivattyu-priority.csv",
         "HŐSZIVATTYÚ cégek (háztartási + ipari)"),
        (nagy_halak_napelem, "lista-6-nagy-halak-napelem.csv",
         "NAGY HALAK: 500+ kivitelezés/év napelem cégek"),
        (frostbite_napelem, "lista-7-frostbite-napelem.csv",
         "NAPELEM email kampány a Frostbite-ba"),
        (frostbite_klima, "lista-8-frostbite-klima.csv",
         "KLÍMA/HŐSZIVATTYÚ email kampány a Frostbite-ba"),
        (master_final, "lista-9-master-all.csv",
         "MINDEN cég egyben, típus oszloppal (email szerint egyedi)"),
    ]

    for cegek, fname, desc in lists:
        n = save_csv(cegek, fname)
        print(f"  [{fname}]")
        print(f"     {n:4d} cég — {desc}")
        print()

    # STATISZTIKA
    print("-" * 60)
    print("ÖSSZESÍTETT STATISZTIKÁK:")
    print("-" * 60)
    print()
    print(f"  Napelem összes (egyedi email):     {len(napelem_unique):5d}")
    print(f"  Napelem weboldallal:               {len(napelem_website):5d}")
    print(f"  Napelem top priority:              {len(napelem_top):5d}")
    print()
    print(f"  Klíma/hőszivattyú összes:          {len(klima_unique):5d}")
    print(f"  Split-klíma telepítők (szezon):    {len(klima_szezon):5d}")
    print(f"  Hőszivattyús cégek:                {len(hoszivattyu):5d}")
    print()
    print(f"  TELJES PIAC (master egyedi):       {len(master_final):5d} cég")
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
