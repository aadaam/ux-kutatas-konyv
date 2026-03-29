# Szerkesztoi vegfelulvizsgalat -- post-factcheck editorial review

**Datum:** 2026. marcius 29.
**Felulvizsgalo:** Claude Opus 4.6 (editor-in-chief pass)
**Alap:** Fact-check utan, az osszes fejezet (00--06) es a styleguide_hu.md alapjan

---

## Ossz publikaciokeszseg: 92%

A konyv publikaciokesz szintu. A hangvitel, a szerkezet es a tartalmi minoseg egyenletesen magas. Harom kisebb, javitando problema maradt (lasd alabb); ezek egyike sem blokkolo, de a kiadoi minoseg erdekeben javitasuk javasolt.

---

## Fejezet szintu ertekeles

| Fejezet | File | Ertekeles | Megjegyzes |
|---|---|---|---|
| 00 -- Eloszo | `00_eloszó.md` | **PASS** | Nincs Osszefoglalas / Ellenorzo kerdesek -- a styleguide szerint az eloszobol ez ki is maradhat. Hangnem kozvetlen, tegező, "mi"-forma rendben. |
| 01 -- UX alapok | `01_ux_alapok.md` | **MINOR** | Ket tipografiai problema: (1) "9000" szokoz nelkul (kellene: "9 000"), (2) az RHS/SUS terminologia bevezetes rendben, de a SUS rovidites csak a cimben es az osszefoglalasban jelenik meg -- a szovegtorzs vegig RHS-t hasznal, ami konzisztens. |
| 02 -- Hasznalhatosagi teszteles | `02_hasznalhatosagi_teszteles.md` | **MINOR** | Egy onozeses tesztfeladat-pelda maradt benne (115. sor: "az on altal most tesztelt honlap" es "Probalja meg"). A konyv vegig tegez -- ez a sor szoges ellentmondasban all a hangvitellel. |
| 03 -- Toborzas | `03_toborzas.md` | **MINOR** | "3000 Ft" szokoz nelkul (54. sor; kellene: "3 000 Ft"). Egy typo: "tamogat" (58. sor) -- helyesen: "tamogat" (ez valojaban nem hiba, a szo helyes, de erdemes ellenorizni a kontextust). |
| 04 -- Interju elokeszitese | `04_interju_elokeszites.md` | **PASS** | Szerkezet, callout-ok, hangvitel hibatlan. Demo interju kozvetlen, olvasmanyos. |
| 05 -- Interjuk dokumentalasa | `05_interjuk_dokumentalasa.md` | **PASS** | Perszóna, journey, workshop -- tartalmilag erős. Callout-ok helyesek. |
| 06 -- UX penzugyei (Fuggelek) | `06_ux_penzugyei.md` | **PASS** | Tartalmazza az Osszefoglalas + Ellenorzo kerdesek szekciot, a fuggelektol is elvarhato minosegben. |

---

## Marado specifikus problemak

### 1. Magázás a tegező szövegben (JAVÍTANDÓ)

**File:** `chapters/02_hasznalhatosagi_teszteles.md`, 115. sor

**Jelenlegi szöveg:**
> `- X dolgot akar csinálni. A Google-ba beírta, hogy X, az ön által most tesztelt honlap jött fel első találati eredményként. Próbálja meg vele megoldani X-et!`

**Probléma:** "az ön által" és "Próbálja meg" magázó forma. A könyv végig tegez. Ez egy tesztfeladat-példa, de az előtte és utána lévő példák is tegeznek (ill. semleges harmadik személyű formát használnak).

**Javaslat:** Átírni semleges formára vagy tegezőre, pl.:
> `- X dolgot akar csinálni. A Google-ba beírta, hogy X, és az általad most tesztelt honlap jött fel első találatként. Próbáld meg vele megoldani X-et!`

---

### 2. Ezres elválasztás hiánya (JAVÍTANDÓ)

**File:** `chapters/01_ux_alapok.md`, 158. sor

**Jelenlegi:** `Nagyjából 9000 teszt alapján`
**Helyesen:** `Nagyjából 9 000 teszt alapján`

A styleguide (C. szekció, 141. sor) előírja: "Ezres elválasztás: Szóköz (nem pont, nem vessző) -- 1 024 válasz, 32 904 felhasználó."

---

**File:** `chapters/03_toborzas.md`, 54. sor

**Jelenlegi:** `3000 Ft-os kupont`
**Helyesen:** `3 000 Ft-os kupont`

---

### 3. Társkönyvre való hivatkozás hiánya (FIGYELEMFELHÍVÁS)

A styleguide (G. szekció) előírja, hogy ahol a kutatási eredmények tervezési döntéssé alakulnak, hivatkozzunk a *Felülettervezési minták* megfelelő fejezetére. Jelenleg az Előszóban (00) van egy általános megjegyzés a társkönyvről, de a többi fejezetben nincs explicit kereszthivatkozás.

Javasolt helyek, ahol egy-egy mondat beilleszthető lenne:
- **Ch01** (Összefoglalás végén): a viselkedési modellekből hogyan lesz tervezési döntés -- utalás a társkönyvre
- **Ch05** (Perszóna szekció): a perszóna szükségleteiből hogyan választunk tervezési mintát -- utalás a társkönyvre
- **Ch06** (Prototípus szekció): a prototípus és a tervezési minták kapcsolata

Ez nem blokkoló hiba, de a kiadói elvárás része.

---

## Ellenőrzőlista -- minden rendben

| Ellenőrzési szempont | Státusz |
|---|---|
| Heading-struktúra: `#` + intro + `## Összefoglalás` + `## Ellenőrző kérdések` | OK (ch01--06 mind tartalmazza; ch00-ban nincs -- helyes) |
| Callout-típusok: csak Tipp: / Megjegyzés: / Figyelem! / A gyakorlatból: | OK -- kizárólag ezek fordulnak elő |
| Tipográfia: `--` (kettős kötőjel) gondolatjelként | OK -- em-dash (—) sehol nem fordul elő |
| Magyar idézőjel: „ " használat | OK -- végig konzisztens |
| Tegező forma végig | OK -- egyetlen kivétel a ch02 115. sora (lásd fent) |
| "Mi"-forma (közös felfedezés) | OK -- minden fejezetben jelen van ("nézzük meg", "arra jutunk", "mi") |
| Terminológia: első előforduláskor zárójelben az angol | OK -- pl. "felhasználókutatás (user research)", "perszóna (persona)", "használhatósági teszt (usability test)" |
| Számformátum: 0--9 betűvel, 10+ számjeggyel | OK -- végig helyes |
| Százalékjel: számjegy + % egybeírva | OK |
| Callout-ok blockquote formátumban (`>`) | OK |

---

## Prioritizált tennivalólista

1. **[P1 -- 2 perc]** Ch02, 115. sor: magázás javítása tegezőre/semlegesre
2. **[P1 -- 1 perc]** Ch01, 158. sor: "9000" -> "9 000"
3. **[P1 -- 1 perc]** Ch03, 54. sor: "3000" -> "3 000"
4. **[P2 -- 15 perc]** 2--3 társkönyv-kereszthivatkozás beillesztése (ch01, ch05, ch06)
5. **[P3 -- opcionális]** Ábraszámozás és ábrahivatkozások bevezetése (jelenleg nincsenek ábrák -- ez a kiadás során kerülhet bele)

---

*A fenti P1-es javítások elvégzése után a könyv 95%+ publikációkész.*
