# Szerkesztői áttekintés -- Felhasználókutatás a gyakorlatban

**Dátum:** 2026. március 29.
**Szerkesztő:** Szerkesztőségi főszerkesztő (editorial review)
**Áttekintett fejezetek:** 00_eloszó -- 05_ux_penzugyei (6 fájl)
**Referencia:** styleguide_hu.md v1.0

---

## 1. Összesített értékelés

**Publikációra való készültség: ~78%**

A kézirat erős alapokon áll. A fejezetek tartalmilag koherensek, a szerzői hang (tegező, közös felfedezés, határozott vélemény) hitelesen és következetesen jelenik meg az összes fejezetben. A callout-rendszer (Tipp, Megjegyzés, Figyelem!, A gyakorlatból) helyes és következetes. A tipográfia (gondolatjel `--`, magyar idézőjel `„"`) korrekt. Az angol szakkifejezések bevezetése a zárójelezési konvenciónak megfelel.

A hiányzó 22% a következő területekből adódik:

- **Kereszthivatkozások teljes hiánya** -- egyetlen fejezet sem hivatkozik a másikra, és a társkönyvre (*Felülettervezési minták*) sincs utalás sehol.
- **Szerkezeti inkonzisztencia** a fejezetek között (ch03 számozott B-szintű címeket használ, a többi nem).
- **Egy szövegromlás** a 00_eloszó végén és **egy szóbeli maradvány** a 02_toborzas GDPR-részében.
- **Egy terminológiai inkonzisztencia** (personákat vs. perszónákat).
- **Egy hiányzó demóinterjú-részlet** a 03-as fejezetben (Bixby-hivatkozás levegőben lóg).

---

## 2. Fejezet-státuszok

### 00_eloszó.md -- MINOR ISSUES

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- nincs fejezetszám, nincs Összefoglalás/Ellenőrző kérdések (elvárt) |
| Callout-ok | OK (Megjegyzés:, Tipp:, A gyakorlatból:) |
| Hang | Tegező, következetes |
| Tipográfia | OK |

**Problémák:**

1. **45. sor:** `Váglak bele!` -- ez nem helyes magyar ige. A „vágni" ige E/1 tárgyas ragozása „váglak", de itt a „Vágjunk bele!" (T/1 alanyi ragozás) vagy „Vágj bele!" (E/2 alanyi felszólítás) lenne a helyes forma a kontextus alapján. A „Váglak bele" úgy hangzik, mintha a szerző az olvasót vágná bele valamibe.
2. **Nincs hivatkozás a társkönyvre** (*Felülettervezési minták*), noha a 27. sor Megjegyzés-calloutja kifejezetten erre a kapcsolatra utal szövegesen. Ez tökéletes hely lenne egy explicit könyvhivatkozásra.

---

### 01_ux_alapok.md -- PASS (apró megjegyzésekkel)

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# 1.` fejezet, bevezető bekezdés, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK -- mind a négy típus megjelenik, formátum helyes |
| Terminológia | OK -- első előfordulásnál zárójelben az angol (pl. „felhasználói élmény (user experience)") |
| Hang | Tegező, következetes |
| Tipográfia | OK -- `--` gondolatjel, `„"` idézőjel |

**Megjegyzések:**

1. **130. sor:** Az RHS (Rendszerhasználhatósági Skála) bevezetése kiváló -- a magyar rövidítés (RHS) és az angol (SUS) is megjelenik. A fejezetben az RHS dominál (8 előfordulás), a SUS csak kétszer jelenik meg, ami helyes.
2. **Relatív** mint határozószó: a 43., 106. és 132. sorban „relatív" jelzőként/határozószóként szerepel (pl. „relatív kényelmetlen", „relatív kevés embert", „relatív jól korrelál"). A helyes írásmód „relatíve" vagy jobb megoldás: „viszonylag". Ez a szerzői előadásmód nyoma. Nem kritikus, de a stilisztikai egységesség érdekében javasolt az egységesítés.
3. **Tartalom:** A fejezet kiválóan lefedi a UX és használhatóság alapjait, a három viselkedési modell bemutatása logikus és jól illusztrált.

---

### 02_toborzas.md -- MINOR ISSUES

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# 2.`, bevezető, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK |
| Terminológia | OK -- toborzó kérdőív (screener questionnaire) bevezetés korrekt |
| Hang | Tegező, következetes |
| Tipográfia | OK |

**Problémák:**

1. **78. sor:** `A GDPR maximális adatkezelési időtartama ha jól emlékszem három év` -- a „ha jól emlékszem" egy szóbeli előadás maradványa. Egy O'Reilly-stílusú szakkönyvben ez nem maradhat. Vagy pontosítsuk a tényt (ellenőrizzük a GDPR-t), vagy hagyjuk ki a feltételes fordulatot. Javasolt javítás: „A GDPR előírásai alapján az adatkezelés időtartamát előre meg kell határozni, és azt a célhoz szükséges minimumra kell korlátozni -- ezt neked expliciten le kell írnod."
2. **Nincs kereszthivatkozás** a 3. fejezetre (interjú-előkészítés), holott a toborzás közvetlenül az interjúra készít elő. A fejezet végi Összefoglalás természetes hely lenne erre.

---

### 03_interju_elokeszites.md -- NEEDS WORK

| Szempont | Értékelés |
|---|---|
| Szerkezet | PROBLÉMA -- számozott B-szintű címek (3.1, 3.2, ...), a többi fejezet nem használ ilyet |
| Callout-ok | OK |
| Terminológia | PROBLÉMA -- 35. sor: „personákat" vs. a könyv többi részében „perszónákat" |
| Hang | Tegező, következetes |
| Tipográfia | OK |

**Problémák:**

1. **B-szintű címek számozása** (5., 39., 113., 155., 183., 205. sorok): A `## 3.1`, `## 3.2` stb. formátum eltér az összes többi fejezettől, amelyek számozás nélküli B-szintű címeket használnak (pl. `## A toborzás menete`). A stílusútmutató E. szekciója sem tartalmaz számozott alcímeket a sablonban. **Javasolt:** Távolítsuk el a számozást, maradjon `## A sztereotípiavizsgálat: honnan indulunk?` stb.

2. **35. sor:** `personákat próbálunk alkotni` -- a könyv mindenhol máshol „perszóna/perszónákat" formát használ (a stílusútmutató D. szekciója is „perszóna (persona)"-t ír elő). Ez egyértelműen terminológiai inkonzisztencia.

3. **111. sor:** A „Bixby-s félretelefonálás" történetére hivatkozó A gyakorlatból callout egy olyan sztorit említ, ami nincs benne a demóinterjú-részletben (39--109. sorok). A demóinterjú szövege a Samsung S9-ről, alkalmazáshasználatról és ébresztőről szól, de a Bixby-s félretelefonálás nem szerepel benne. Vagy az interjúrészlet csonka (és ki kellene egészíteni), vagy a callout hivatkozása rossz.

4. **127. sor:** `hát vagy fogok, vagy nem` -- a „hát" szóbeli töltelékszónak tűnik, bár idézett gondolat kontextusában elfogadható. A 131. sorban a párbeszéd-idézetben természetesen megengedett.

---

### 04_interjuk_dokumentalasa.md -- MINOR ISSUES

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# 4.`, bevezető, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK |
| Terminológia | OK -- perszóna (persona) és user journey bevezetés korrekt |
| Hang | Tegező, következetes |
| Tipográfia | OK |

**Megjegyzések:**

1. **65. sor:** A „Netpincér" írásmód eltér az 1. fejezet 41. sorától, ahol „NetPincér" szerepel. A stílusútmutató C. szekciója a termékneveket változtatás nélkül hagyja -- ellenőrizzük a hivatalos írásmódot és egységesítsünk (a helyes forma valószínűleg „NetPincér").
2. **91. sor:** A Harry Potter és a 22-es csapdája példa a journey-építésnél kreatív és hatásos, de kissé távol esik az UX-kontextustól. Nem szükséges eltávolítani, de mérlegelhető, hogy ne nyúljon el.
3. **Hiányzik a Indi Young könyv pontos hivatkozása** (161. sor: „Indi Young nevű kutató írt róla könyvet"). A stílusútmutató F. szekciója előírja, hogy könyvhivatkozásnál az első előforduláskor cím + szerző + kiadó szükséges. A könyv: *Mental Models* -- Indi Young (Rosenfeld Media).

---

### 05_ux_penzugyei.md -- PASS (apró megjegyzésekkel)

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# Függelék:` cím (fejezetszám helyett, elvárt), bevezető, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK |
| Terminológia | OK |
| Hang | Tegező, következetes |
| Tipográfia | OK |

**Megjegyzések:**

1. **87. sor:** „2002-ben jelent meg" -- az iPod valójában 2001-ben jelent meg. Ellenőrizendő faktum.
2. **„relatív"** határozóként (53., 87. sor) -- ugyanaz a megjegyzés, mint az 1. fejezetnél.
3. **Tartalom:** Kiváló fejezet, amely a UX megtérülését gyakorlatiasan és meggyőzően mutatja be. A Boehm-görbe, a 30%-os megtakarítás és a learn-design-test ciklus jól strukturált.

---

## 3. Konkrét hibák összesítése

| # | Fájl | Sor | Szöveg | Típus | Prioritás |
|---|---|---|---|---|---|
| 1 | 00_eloszó.md | 45 | `Váglak bele!` | Nyelvhelyesség | MAGAS |
| 2 | 02_toborzas.md | 78 | `ha jól emlékszem három év` | Szóbeli maradvány | MAGAS |
| 3 | 03_interju_elokeszites.md | 35 | `personákat próbálunk alkotni` | Terminológiai inkonzisztencia | MAGAS |
| 4 | 03_interju_elokeszites.md | 5, 39, 113, 155, 183, 205 | `## 3.1`, `## 3.2` stb. | Szerkezeti inkonzisztencia | MAGAS |
| 5 | 03_interju_elokeszites.md | 111 | Bixby-s félretelefonálás hivatkozás | Hiányzó tartalomra utalás | KÖZEPES |
| 6 | 04_interjuk_dokumentalasa.md | 65 | `Netpincér` (vs. 01-ben `NetPincér`) | Márkanév-inkonzisztencia | KÖZEPES |
| 7 | 04_interjuk_dokumentalasa.md | 161 | `Indi Young nevű kutató írt róla könyvet` | Hiányzó könyvhivatkozás | KÖZEPES |
| 8 | 05_ux_penzugyei.md | 87 | `2002-ben jelent meg` | Faktuális ellenőrzés szükséges (iPod: 2001) | KÖZEPES |
| 9 | 01, 04, 05 (több sor) | -- | `relatív` határozószóként | Szóbeli stílusmaradvány (6 előfordulás) | ALACSONY |

---

## 4. Kereszthivatkozási javaslatok

A kéziratban jelenleg **nulla** kereszthivatkozás található fejezetek között, és **nulla** hivatkozás a társkönyvre. Ez a legjelentősebb hiányosság a publikációra való készültség szempontjából.

### Fejezetek közötti hivatkozások

| Honnan | Hova | Javaslat |
|---|---|---|
| 00_eloszó, 27. sor (Megjegyzés callout) | -- | Hivatkozás a társkönyvre: „Lásd a *Felülettervezési minták* című könyvet." |
| 01_ux_alapok, 33. sor (perszónák említése) | 04. fejezet | „Lásd a 4. fejezetet a perszónák részletes felépítéséhez." |
| 01_ux_alapok, 35. sor (használhatósági tesztelés) | -- | Jövőbeli fejezet-hivatkozás (ha lesz külön fejezet) vagy a társkönyv |
| 02_toborzas, 3. sor (bevezető) | 01. fejezet | Már tartalmaz implicit utalást -- explicit hivatkozássá alakítandó |
| 02_toborzas, 14. sor (GDPR-vonzatok) | 02. fejezet, GDPR-rész | Önhivatkozás a fejezeten belüli GDPR-szekcióra: „lásd az „Az adatkezelésről röviden" című részt" |
| 03_interju_elokeszites, 35. sor (personákat/perszónákat) | 04. fejezet | „A perszóna felépítéséről részletesen lásd a 4. fejezetet." |
| 03_interju_elokeszites, 3. sor (bevezető) | 02. fejezet | Már tartalmaz implicit utalást -- korrekt |
| 04_interjuk_dokumentalasa, 3. sor (bevezető) | 03. fejezet | Már tartalmaz implicit utalást -- korrekt, de lehetne explicit |
| 04_interjuk_dokumentalasa, 13. sor (user journey) | 01. fejezet | „A felhasználói életút fogalmát az 1. fejezetben vezettük be." |
| 05_ux_penzugyei, 15. sor (MÁV pénztárrendszer) | 01. fejezet, 75. sor | „A MÁV tranzakcióidő-problémáját az 1. fejezetben már bemutattuk (lásd a „Hatékonyság -- az idő pénz" című részt)." |
| 05_ux_penzugyei, 77. sor (interjúkkal feltérképezik) | 03. fejezet | „Az interjútechnikáról lásd a 3. fejezetet." |

### Társkönyv-hivatkozások

| Hely | Javaslat |
|---|---|
| 00_eloszó, 27. sor | „Ez a könyv a *Felülettervezési minták* társa." -- explicit könyvhivatkozás formátumban |
| 01_ux_alapok, 33--35. sor (tervezési minták említése) | „A perszónák alapján választott tervezési mintákról lásd a *Felülettervezési minták* 3--4. fejezetét." |
| 04_interjuk_dokumentalasa, Összefoglalás | „A perszóna szükségleteiből tervezési döntések születnek -- ehhez lásd a *Felülettervezési minták* megfelelő fejezetét." |
| 05_ux_penzugyei, 107. sor (prototípus mint határobjektum) | „A drótváz és a prototípus felépítéséről lásd a *Felülettervezési minták* vonatkozó fejezeteit." |

---

## 5. Terminológiai audit

### Következetesen használt kifejezések (rendben)

- felhasználói élmény (user experience) / UX -- korrekt, zárójelben bevezetve
- használhatóság (usability) -- korrekt
- használhatósági teszt(elés) (usability testing) -- korrekt
- felhasználókutatás (user research) -- korrekt
- perszóna (persona) -- korrekt (1 kivétellel, lásd alább)
- felhasználói út (user journey) -- korrekt
- toborzó kérdőív (screener questionnaire) -- korrekt
- incentíva (ösztönző) -- korrekt
- interjúalany -- korrekt
- interjú-útmutató (interview guide) -- korrekt
- viselkedési kohorsz (behavioral cohort) -- korrekt
- archetípus (archetype) -- korrekt
- RHS (Rendszerhasználhatósági Skála) / SUS -- korrekt
- NPS (Net Promoter Score) -- korrekt
- Boehm-görbe -- korrekt
- GDPR -- korrekt

### Inkonzisztenciák

| Kifejezés | Előfordulás 1 | Előfordulás 2 | Javasolt egységes forma |
|---|---|---|---|
| perszóna / persona | 01, 04, 05: „perszóna" | 03, 35. sor: „personákat" | „perszónákat" |
| NetPincér / Netpincér | 01, 41. sor: „NetPincér" | 04, 65. sor: „Netpincér" | „NetPincér" (hivatalos írásmód) |
| relatív / relatíve / viszonylag | 01 (43, 106, 132), 04 (63), 05 (53, 87): „relatív" határozóként | -- | „viszonylag" vagy „relatíve" |
| sztereotípiavizsgálat / sztereotípia-vizsgálat | 03, 5. sor: „sztereotípiavizsgálat" (egybeírva) | styleguide D.: „sztereotípia-vizsgálat" (kötőjellel) | „sztereotípia-vizsgálat" (kötőjeles forma a stílusútmutatónak megfelelően) |
| interjúkérdéslap / interjú-útmutató | styleguide D.: „interjúkérdéslap (discussion guide)" | 03, 189. sor: „interjú-útmutató (interview guide)" | Mindkettő használható, de egyértelművé kell tenni, hogy különböző dolgok-e |

---

## 6. Priorizált tennivalók

### MAGAS prioritás (publikáció előtt kötelező)

1. **Kereszthivatkozások hozzáadása** -- Minden fejezetbe legalább 1--2 hivatkozás a kapcsolódó fejezetekre és a társkönyvre. Lásd a 4. szekció részletes javaslatait.

2. **00_eloszó.md, 45. sor:** `Váglak bele!` javítása `Vágj bele!`-re vagy `Vágjunk bele!`-re.

3. **02_toborzas.md, 78. sor:** A „ha jól emlékszem" szóbeli maradvány eltávolítása és a GDPR-állítás pontosítása.

4. **03_interju_elokeszites.md:** Számozott alcímek (`## 3.1`, `## 3.2` stb.) átalakítása számozás nélküli formára, a többi fejezettel összhangban.

5. **03_interju_elokeszites.md, 35. sor:** `personákat` javítása `perszónákat`-ra.

### KÖZEPES prioritás (kiadás előtt javasolt)

6. **03_interju_elokeszites.md, 111. sor:** A Bixby-s félretelefonálás történetének vagy hozzáadása a demóinterjú-részlethez, vagy a callout szövegének módosítása, hogy ne hiányzó tartalomra utaljon.

7. **04_interjuk_dokumentalasa.md, 65. sor:** „Netpincér" egységesítése „NetPincér"-re.

8. **04_interjuk_dokumentalasa.md, 161. sor:** Indi Young könyvhivatkozás kiegészítése: „*Mental Models* -- Indi Young (Rosenfeld Media)".

9. **05_ux_penzugyei.md, 87. sor:** iPod megjelenési dátumának ellenőrzése (az első iPod 2001. október 23-án jelent meg, nem 2002-ben).

10. **Terminológiai egységesítés:** „relatív" határozószó javítása „viszonylag"-ra (6 előfordulás, 3 fejezetben). „Sztereotípiavizsgálat" kötőjelezése.

### ALACSONY prioritás (javítja a minőséget)

11. **Ábra- és táblázatszámozás bevezetése** -- A stílusútmutató előírja a `[fejezetszám]-[sorszám]` formátumú számozást (pl. „2-1. táblázat"), de a fejezetek táblázatai jelenleg számozatlanok. Ez a nyomdai előkészítés során is megoldható.

12. **A szerzői hang finomhangolása:** A „hát" néhány nem-idézetes kontextusban előfordulása (03, 127. sor) javítandó. Az „éhes vagy-e vagy csajozni akarsz" (01, 41. sor) erős szóbeli fordulat, ami a stílusútmutató szerint mértékletesen megőrizhető, de a „csajozni" szó esetleg „randizni"-ra cserélhető az inkluzív nyelvhasználat jegyében.

13. **Glosszárium-fejezet** hozzáadása -- A stílusútmutató D. szekciója részletes terminológiai szótárat tartalmaz. Ennek rövidített változata a könyv végén hasznos lenne az olvasónak.

---

## 7. Összesítő táblázat

| Fejezet | Státusz | Nyitott kérdések |
|---|---|---|
| 00_eloszó | MINOR ISSUES | 1 nyelvhelyességi hiba, társkönyv-hivatkozás hiányzik |
| 01_ux_alapok | PASS | „relatív" stílusjavítás, kereszthivatkozások |
| 02_toborzas | MINOR ISSUES | 1 szóbeli maradvány, kereszthivatkozások |
| 03_interju_elokeszites | NEEDS WORK | Szerkezeti inkonzisztencia, terminológiai hiba, hiányzó tartalom |
| 04_interjuk_dokumentalasa | MINOR ISSUES | Márkanév-inkonzisztencia, könyvhivatkozás, kereszthivatkozások |
| 05_ux_penzugyei | PASS | Faktuális ellenőrzés (iPod dátum), „relatív" stílusjavítás |

---

*Ez a szerkesztői áttekintés a styleguide_hu.md v1.0 alapján készült. A javítások elvégzése után újabb áttekintés javasolt a kereszthivatkozások és terminológiai egységesség véglegesítéséhez.*
