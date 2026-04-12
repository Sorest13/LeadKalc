# LeadKalc — Teljes Végrehajtási Terv
**Dátum:** 2026. április 12.
**Cél:** 10 alapítói partner szerzése 30 napon belül

---

## ERŐFORRÁSAID

| Eszköz | Tartalom |
|---|---|
| 1 495 cég (master lista) | 848 napelem + 651 klíma/hőszivattyú, email + telefon |
| Landing page (LIVE) | leadkalc.hu — alapítói ár, SEO, mobil fix, minden kész |
| 3 widget demó (LIVE) | widget-solar.html, widget-hvac.html, widget-heatpump.html |
| Cold email szekvencia | 3 lépéses, HUF árazással, outreach mappában |
| Cold calling script | Ellenvetés-kezelés, napi rutin, HUF kommunikáció |
| Facebook posztok | 6 kész sablon + ütemezés |

---

## 1. HETI TERV — Összefoglaló naptár

### 1. HÉT (ápr. 12–18): INDÍTÁS

| Nap | Délelőtt (8:00–12:00) | Délután (13:00–16:00) | Este (20:00–21:00) |
|---|---|---|---|
| **Szombat (ma)** | — | Frostbite regisztráció + email fiók | Facebook csoportokhoz csatlakozás |
| **Vasárnap** | — | Email szekvencia beállítás Frostbite-ban (klíma + napelem) | Első Facebook poszt (#5 — kérdés) |
| **Hétfő** | 50 KLÍMA hívás | Demók tartása + follow-up emailek | Email kampány statisztika nézés |
| **Kedd** | 50 KLÍMA hívás | Demók + Facebook poszt (#1) | Frostbite statisztikák |
| **Szerda** | 50 KLÍMA hívás | Demók | — |
| **Csütörtök** | 50 KLÍMA hívás + Facebook poszt (#3) | Demók | Heti kiértékelés |
| **Péntek** | 50 KLÍMA hívás | Demók + Frostbite optimalizálás | — |

### 2. HÉT (ápr. 19–25): KLÍMA FOLYTATÁS + NAPELEM INDÍTÁS

| Nap | Délelőtt | Délután |
|---|---|---|
| Hétfő–Szerda | 50 KLÍMA hívás (lista folytatás) | Demók + napelem email kampány indítás |
| Csütörtök–Péntek | 50 NAPELEM hívás (top priority lista) | Demók + Facebook poszt (#2 esettanulmány ha van adat) |

### 3–4. HÉT: NAPELEM + HŐSZIVATTYÚ + OPTIMALIZÁLÁS

Kéthetente váltás a listákon, az email kampány automatán megy mindkettőre párhuzamosan.

---

## 2. MA ELVÉGZENDŐ — Frostbite Setup (Szombat)

### 2.1 — Email fiók (10 perc)

Hozz létre egy dedikált email fiókot az outreach-hez. Két opció:

**A) Ha van domain (leadkalc.hu):** Használd az `info@leadkalc.hu` vagy `marcell@leadkalc.hu` címet.
**B) Ha nincs domain email:** Hozz létre egy `leadkalc.outreach@gmail.com`-ot.

A domain email professzionálisabb, de a Gmail is megteszi az elején.

### 2.2 — Frostbite.ai regisztráció (15 perc)

1. Nyisd meg: **frostbite.ai**
2. Regisztrálj a dedikált email fiókkal
3. Kösd össze az SMTP-vel (az outreach email fiókod SMTP adatai)
4. Napi küldési limit beállítás: **50 email/nap** (első hét — later emelhető)

### 2.3 — Klíma email kampány beállítás (20 perc)

**Frostbite-ban létrehozandó szekvencia:**

**Szekvencia neve:** "LeadKalc — Klíma szezon 2026"

**Lista importálás:** Töltsd fel a `lista-8-frostbite-klima.csv` fájlt (651 cég).
- Merge tagek: `{cégnév}` → cégnév oszlop, `{email}` → email oszlop

**Email 1 (azonnali küldés):**

Tárgy: `{cégnév} — egy ötlet a klímaszezonra`

Szöveg:
```
Kedves Kolléga,

A klímaszezon közeleg — az érdeklődők már most keresik a szerelőket.

Fejlesztettem egy klíma kalkulátor widgetet, amit a weboldalra lehet tenni. A látogató beírja a szoba méretét, kiválasztja a klímát, és kiszámolja a költséget — közben automatikusan megadja az elérhetőségét.

Egy sor kód a weboldalra, és az érdeklődők maguktól jönnek.

Most indítom az Alapítói Partner Programot: az első 10 cég havi 24 ezer forintért kapja — ez napi 800 Ft. Ez az ár nekik örökre ennyi marad.

Ha érdekli, szívesen megmutatom 5 percben: [demó link]

Üdvözlettel,
Garamszegi Marcell
LeadKalc — leadkalc.hu
+36 30 356 2888
```

**Email 2 (4 nap múlva):**

Tárgy: `RE: {cégnév} — egy ötlet a klímaszezonra`

Szöveg:
```
Kedves Kolléga,

Csak röviden: az első ügyfelem, egy klímás cég, a widget beépítése óta folyamatosan kap megkereséseket a weboldalán — hirdetés nélkül.

A kalkulátor azért működik, mert a látogató aktívan részt vesz. Nem egy "Kérjen ajánlatot" gomb, amit senki nem nyom meg.

Az Alapítói Programban még van szabad hely — 14 napig kockázatmentesen kipróbálható.

Üdvözlettel,
Marcell
```

**Email 3 (7 nap múlva):**

Tárgy: `Utolsó üzenet — {cégnév}`

Szöveg:
```
Kedves Kolléga,

Ez az utolsó üzenetem. Az Alapítói Partner Programból már csak pár hely maradt.

Ha most nem aktuális, itt megnézheti a demót bármikor: [demó link]

Sok sikert a klímaszezonra,
Marcell
+36 30 356 2888
```

**Ütemezés:** Hétköznap 8:00–9:00 között küld, max 50/nap.

### 2.4 — Napelem email kampány (külön szekvencia)

**Szekvencia neve:** "LeadKalc — Napelem 2026"

**Lista:** `lista-7-frostbite-napelem.csv` (848 cég)

A szövegek a `cold-email-szekvencia.md` fájlban vannak — azok napelem-specifikusak.
Ezt a kampányt **1 héttel a klíma után** indítsd, hogy ne terhelje túl a Frostbite limitet.

---

## 3. COLD CALLING — NAPI RUTIN

### Első napok: KLÍMA lista

**Használandó fájl:** `lista-4-klima-szezon-priority.csv` (615 cég)
**Script:** `cold-calling-script.md` (már tartalmazza a HUF árazást)

**FONTOS MÓDOSÍTÁS KLÍMA HÍVÁSHOZ:**

A script hook-ját így mondd klímásoknak:

> "Klímaszerelő cégeknek fejlesztek egy kalkulátor widgetet a weboldalra. A látogató beírja a szoba méretét, és kiszámolja melyik klíma kell neki — közben megadja a telefonszámát. A klímaszezon előtt most érdemes beüzemelni."

**Napi beosztás (hétfőtől):**

| Idő | Teendő |
|---|---|
| 7:30–8:00 | 50 cég kiválasztása a CSV-ből + weboldalak gyorsellenőrzése |
| 8:00–12:00 | **50 hívás** (script alapján) |
| 12:00–12:30 | "Küldjön emailt" válaszokra személyes email küldés |
| 12:30–13:00 | Google Sheet frissítés: cégnév, dátum, eredmény |
| 14:00–16:00 | Demók tartása |

### 2. héttől: NAPELEM lista

**Használandó fájl:** `lista-1-napelem-top-priority.csv` (355 cég)

A script hook-ját így mondd napelemeseknek (ahogy az eredeti scriptben van):

> "Energetikai kivitelező cégeknek fejlesztek egy kalkulátor widgetet a weboldalra. A látogató kiszámolja a megtérülést, és közben megadja a telefonszámát."

### HÍVÁS PRIORITÁS

1. **Első:** Akik megnyitották az emailt de nem válaszoltak (Frostbite statból)
2. **Második:** A klíma szezon lista (615 cég) — most a legmelegebb
3. **Harmadik:** Napelem top priority (355 cég)
4. **Negyedik:** Napelem website havers (533 cég)
5. **Ötödik:** Hőszivattyú lista (352 cég)

---

## 4. FACEBOOK — HETI RUTIN

### Csoportok (csatlakozz MA)

1. **Napelem és napenergia és hőszivattyús hűtés-Fűtés** — facebook.com/groups/napelemneked
2. **Magyar Napelem Napkollektor Szövetség** — facebook.com/groups/MNNSZfelhasznaloi
3. **Napelem szerelők és kivitelezők portálja** — facebook.com/groups/1093630727971032
4. **Klímaszerelő kereső** — facebook.com/groups/400295567944726

### Posztolási ütemezés

A kész posztok a `facebook-posztok.md` fájlban vannak.

| Hét | Kedd | Csütörtök |
|---|---|---|
| 1. hét | #5 (kérdés — vasárnap este) | #1 (statisztika) |
| 2. hét | #3 (provokáció) | #4 (tanácsadó) |
| 3. hét | #2 (esettanulmány) | #6 (alapítói program) |
| 4. hét+ | Rotáció + új posztok eredmények alapján | |

### Facebook szabályok
- SOHA ne hirdessd közvetlenül a linket — kitiltanak
- Értéket adj, kérdést tegyél fel, beszélgetést indíts
- Kommentelj naponta 5-10 másik posztra értelmesen
- Ha privátban kérdeznek → telefonszámot kérj és küldj demó linket

---

## 5. EREDMÉNY KÖVETÉS

### Google Sheet (hozz létre MA)

**1. fül: "Hívások"**

| Dátum | Cégnév | Típus | Eredmény | Következő lépés | Megjegyzés |
|---|---|---|---|---|---|
| 2026-04-14 | XY Klíma Kft | klíma | demó időpont | demó 04.15 14:00 | érdekelődik |

**Eredmény oszlop értékei:**
- `demó időpont` — sikeres időpont egyeztetés
- `email kérés` — "küldjön emailt" → személyes email megy
- `visszahívás` — "hívjon X-kor" → emlékeztető
- `nem érdekli` — levesszük 6 hónapra
- `nem vette fel` — max 3x próba
- `nincs weboldal` — weboldal+widget csomag lenne ha kínálod

**2. fül: "Pipeline"**

| Cégnév | Fázis | Ár | Widget típus | Várható zárás |
|---|---|---|---|---|
| Klíma Audit Kft | szerződés | 59 EUR | klíma + szivárgás | ápr. 15 |

**Fázisok:** lead → demó → ajánlat → szerződés → aktív

**3. fül: "Heti számok"**

| Hét | Hívás | Email küldve | Demó | Lezárás | Bevétel |
|---|---|---|---|---|---|
| 1. hét | 250 | 350 | ? | ? | ? |

---

## 6. KONVERZIÓS CÉLOK

| Mutató | Cél | Magyarázat |
|---|---|---|
| **Hívás → Demó** | 8-12% | 50 hívásból 4-6 demó időpont |
| **Demó → Lezárás** | 25-35% | 5 demóból 1-2 fizetős ügyfél |
| **Email megnyitás** | 30-50% | Ha alacsonyabb → tárgysor csere |
| **Email válasz** | 3-8% | Ha alacsonyabb → szöveg csere |
| **Heti új ügyfél** | 2-4 | Első 10 = alapítói, utána normál ár |
| **30 napos cél** | 10 alapítói partner | Teljes program betöltve |

---

## 7. MI FUT AUTOMATÁN (nem kell csinálnod)

| Rendszer | Mit csinál | Mikor |
|---|---|---|
| **Frostbite email** | Napi 50-100 email a klíma/napelem listára | Hétköznaponként 8:00 |
| **Frostbite follow-up** | 4 és 7 napos automatikus follow-up | Automatán |
| **Landing page** | Leadek gyűjtése EmailJS-sel | 24/7 |
| **Widget demók** | Élő demó linkek a weboldalon | 24/7 |
| **SEO** | Google indexelés az új meta tagekkel | Folyamatos |

---

## 8. MÉRFÖLDKÖVEK

| Dátum | Mérföldkő | Hatás |
|---|---|---|
| **Ápr. 12 (ma)** | Frostbite setup + Facebook csatlakozás | Rendszer kész |
| **Ápr. 14 (hétfő)** | Első 50 klíma hívás + email kampány indul | Első kontaktok |
| **Ápr. 18 (péntek)** | 250 hívás + 350 email → első demók | Pipeline épül |
| **Ápr. 21** | Napelem email kampány indítás | Második vertikális |
| **Ápr. 25** | 500+ hívás kész → első 2-3 fizetős ügyfél várható | Bevétel indul |
| **Máj. 1** | Esettanulmány készítés (ha van adat) | Social proof |
| **Máj. 12** | 30 nap letelt → 10 alapítói partner cél | Program betöltve |
| **Máj. 15+** | Normál árazás (90-199 EUR) bevezetés | Recurring revenue nő |

---

## 9. HA ELAKADSZ

| Probléma | Megoldás |
|---|---|
| Alacsony email megnyitás (<20%) | Tárgysor csere — próbáld: "{cégnév} klímaszezon" |
| Sok "nem érdekel" válasz | Hook csere a scriptben — teszteld más megnyitóval |
| Senki nem veszi fel a telefont | Hívj 14:00-16:00 között is (nem csak reggel) |
| Demóról nem zárod le | Kérdezd: "Mi kell ahhoz hogy holnap elkezdjük?" |
| Frostbite technikai probléma | Váltás Instantly.ai-ra (ingyenes tier) |
| Klíma scraper újrafuttatás kell | `python3 scraper_klima.py` a terminálban |
| Napelem scraper újrafuttatás | `python3 scraper.py` a terminálban |
| CSV újraszűrés | `python3 csv_szuro.py` a terminálban |

---

## FÁJL TÉRKÉP — Gyors referencia

```
LeadKalc landing1.0/
├── index.html                          ← LIVE landing page (GitHub)
├── index-3.html                        ← Lokális másolat
├── og-image.jpg                        ← Social media megosztó kép
├── widget-solar.html                   ← Napelem demó widget
├── widget-hvac.html                    ← Klíma demó widget
├── widget-heatpump.html                ← Hőszivattyú demó widget
├── aszf.html                           ← ÁSZF
├── sitemap.xml                         ← SEO
└── outreach/
    ├── VEGREHAJTASI-TERV.md            ← EZ A FÁJL
    ├── cold-email-szekvencia.md        ← 3 lépéses napelem email szöveg
    ├── cold-calling-script.md          ← Hívás forgatókönyv + napi rutin
    ├── facebook-posztok.md             ← 6 kész poszt + ütemezés
    ├── prospect-lista-forrasok.md      ← Források, linkek
    │
    ├── scraper.py                      ← Napelem scraper (Napenergia Plusz)
    ├── scraper_klima.py                ← Klíma scraper (NKVH F-gáz)
    ├── csv_szuro.py                    ← Egyesített priorizáló
    │
    ├── prospect-osszes-megye.csv       ← 6086 napelem nyers adat
    ├── prospect-klima-hoszivattyu.csv  ← 653 klíma/hőszivattyú nyers adat
    │
    ├── lista-1-napelem-top-priority.csv    ← 355 — fő napelem cold calling
    ├── lista-2-napelem-website-havers.csv  ← 533 — napelem weboldalas
    ├── lista-3-klima-osszes.csv            ← 651 — összes klíma/hőszivattyú
    ├── lista-4-klima-szezon-priority.csv   ← 615 — split-klíma telepítők
    ├── lista-5-hoszivattyu-priority.csv    ← 352 — hőszivattyú cégek
    ├── lista-6-nagy-halak-napelem.csv      ← 129 — napelem 500+ kivitelezés
    ├── lista-7-frostbite-napelem.csv       ← 848 — napelem email import
    ├── lista-8-frostbite-klima.csv         ← 651 — klíma email import
    └── lista-9-master-all.csv              ← 1495 — MINDEN egyben
```

---

**Az egyetlen dolog amit most kell csinálnod: nyisd meg a frostbite.ai-t és regisztrálj.**
**Minden más kész. A rendszer vár rád.**
