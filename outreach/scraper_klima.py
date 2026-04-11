#!/usr/bin/env python3
"""
LeadKalc Klíma + Hőszivattyú Scraper
=====================================
Forrás: Nemzeti Klímavédelmi Hatóság (NKVH) F-gáz nyilvántartás
URL: https://nemzetiklimavedelmihatosag.kormany.hu/kereso.php

Legyűjti az ÖSSZES magyar klíma- és hőszivattyú-kivitelezőt akik
F-gáz regisztrációval rendelkeznek (ez kötelező!).

Tevékenységek amiket scrape-elünk:
  1  — Split-klímák Telepítés (fő cél — lakossági klíma)
 17  — Split-klímák Szerviz
 27  — Háztartási hőszivattyúk Telepítés
 28  — Háztartási hőszivattyúk Szerviz
  4  — Klímarendszerek Telepítés (ipari/VRV)
 20  — Klímarendszerek Szerviz
  2  — Kis méretű hűtőberendezések Telepítés
 18  — Kis méretű hűtőberendezések Szerviz

Kimenet: prospect-klima-hoszivattyu.csv
"""

import requests
import json
import csv
import re
import time
import os
import warnings
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore")

BASE_URL = "https://nemzetiklimavedelmihatosag.kormany.hu/kereso.php"

TEVEKENYSEGEK = {
    1:  "Split-klíma telepítés",
    17: "Split-klíma szerviz",
    27: "Háztartási hőszivattyú telepítés",
    28: "Háztartási hőszivattyú szerviz",
    4:  "Klímarendszer telepítés (VRV)",
    20: "Klímarendszer szerviz (VRV)",
    2:  "Kis hűtőberendezés telepítés",
    18: "Kis hűtőberendezés szerviz",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    "Accept-Language": "hu-HU,hu;q=0.9,en;q=0.5",
}

CSV_FEJLEC = [
    "cégnév", "tevékenységek", "település", "megye", "irányítószám",
    "cím", "telefon", "email", "lat", "lng", "megye_label",
]


def fetch_tevekenyseg(tevekenyseg_id):
    """Egy tevékenységre lekéri az összes cég adatot országosan."""
    params = {
        "internet": "",
        "tevekenyseg_id": str(tevekenyseg_id),
        "terulet_tipus": "1",  # Országos
        "terulet_id": "",
    }
    try:
        resp = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=60)
        resp.raise_for_status()
        resp.encoding = "utf-8"
        return resp.text
    except requests.RequestException as e:
        print(f"  HIBA: {e}")
        return None


def extract_places_json(html):
    """Kinyeri a 'var places = [...]' JSON tömböt a HTML-ből."""
    # A JavaScript így kezdődik: var places = [{"tevekenyseg_csoport_id":...
    m = re.search(r"var\s+places\s*=\s*(\[.*?\]);", html, re.DOTALL)
    if not m:
        return []

    json_text = m.group(1)
    try:
        return json.loads(json_text)
    except json.JSONDecodeError as e:
        print(f"  JSON parse hiba: {e}")
        return []


def normalize_ceg(raw, tevekenyseg_nev):
    """Egy nyers cég rekordot normalizál a CSV fejléchez."""
    # None-safe: minden mezőre default empty string
    postcode = (raw.get("postcode") or "").strip()
    telepules = (raw.get("settlements_name") or "").strip()
    megye = (raw.get("megye") or "").strip()
    address = (raw.get("address") or "").strip()

    telefon = (raw.get("telefon") or "").strip()
    email = (raw.get("email") or "").strip().lower()

    # Telefon normalizálás (06... → +36...)
    if telefon.startswith("06"):
        telefon = "+36" + telefon[2:]
    telefon = re.sub(r"[\s\-/]", "", telefon)

    return {
        "cégnév": (raw.get("customers_cegnev") or "").strip(),
        "tevékenységek": tevekenyseg_nev,
        "település": telepules,
        "megye": megye,
        "irányítószám": postcode,
        "cím": address,
        "telefon": telefon,
        "email": email,
        "lat": str(raw.get("lat", "")),
        "lng": str(raw.get("lng", "")),
        "megye_label": megye,
    }


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    kimenet = os.path.join(script_dir, "prospect-klima-hoszivattyu.csv")

    # Gyűjtés: cégnév+email kulccsal, összevonva a tevékenységeket
    osszes_ceg = {}  # (cégnév, email) → ceg dict

    print("=" * 60)
    print("  LeadKalc Klíma + Hőszivattyú Scraper")
    print("  Forrás: Nemzeti Klímavédelmi Hatóság F-gáz regisztráció")
    print("=" * 60)
    print()

    for tev_id, tev_nev in TEVEKENYSEGEK.items():
        print(f"[{tev_id:2d}] {tev_nev}...", end=" ", flush=True)

        html = fetch_tevekenyseg(tev_id)
        if not html:
            continue

        places = extract_places_json(html)
        print(f"→ {len(places)} találat")

        for raw in places:
            ceg = normalize_ceg(raw, tev_nev)
            if not ceg["cégnév"] or not ceg["email"]:
                continue

            key = (ceg["cégnév"].lower(), ceg["email"])
            if key in osszes_ceg:
                # Már van, csak hozzáfűzzük a tevékenységet
                existing = osszes_ceg[key]
                if tev_nev not in existing["tevékenységek"]:
                    existing["tevékenységek"] = existing["tevékenységek"] + " | " + tev_nev
            else:
                osszes_ceg[key] = ceg

        time.sleep(1.5)

    # Mentés
    print()
    print("-" * 60)

    if osszes_ceg:
        cegek_lista = list(osszes_ceg.values())

        # Rendezés megye szerint, majd cégnév szerint (None-safe)
        cegek_lista.sort(key=lambda c: (c.get("megye") or "", c.get("cégnév") or ""))

        with open(kimenet, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FEJLEC, delimiter=";")
            writer.writeheader()
            writer.writerows(cegek_lista)

        print(f"✓ KÉSZ! {len(cegek_lista)} egyedi cég mentve")
        print(f"  Fájl: {kimenet}")

        # Statisztika
        from collections import Counter
        megyek = Counter(c["megye"] for c in cegek_lista)
        print()
        print("Megyénkénti bontás:")
        for megye, count in sorted(megyek.items(), key=lambda x: -x[1]):
            print(f"  {megye:30s} {count:4d} cég")

        print()
        tevekenysegek_count = Counter()
        for c in cegek_lista:
            for t in c["tevékenységek"].split(" | "):
                tevekenysegek_count[t] += 1
        print("Tevékenységenkénti megoszlás (cégek több tevékenységet is végezhetnek):")
        for tev, count in sorted(tevekenysegek_count.items(), key=lambda x: -x[1]):
            print(f"  {tev:40s} {count:4d} cég")
    else:
        print("✗ Nem sikerült cégeket kinyerni.")

    return len(osszes_ceg)


if __name__ == "__main__":
    main()
