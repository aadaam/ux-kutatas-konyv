# Végső lektori áttekintés -- Felhasználókutatás a gyakorlatban

**Dátum:** 2026. március 29.
**Lektor:** Végső lektori szerkesztés (final review)
**Áttekintett fejezetek:** 00_eloszó -- 06_ux_penzugyei (7 fájl)
**Referencia:** styleguide_hu.md v1.0 + editorial_review.md
**Változás az előző áttekintéshez képest:** Új 02-es fejezet (használhatósági tesztelés, PDF-forrásból), fejezetek átszámozása (régi 02--05 -> új 03--06)

---

## 1. Összesített értékelés

**Publikációra való készültség: ~82%**

Az előző szerkesztői áttekintés óta a kézirat érezhetően javult. A korábbi MAGAS prioritású hibák közül az alábbiak megoldódtak:

- **00_eloszó.md:** `Váglak bele!` javítva `Vágjunk bele!`-re -- RENDBEN
- **03_toborzas.md (régi 02):** `ha jól emlékszem három év` szóbeli maradvány eltávolítva, GDPR-megfogalmazás pontosítva -- RENDBEN
- **04_interju_elokeszites.md (régi 03):** `personákat` javítva `perszónákat`-ra -- RENDBEN
- **04_interju_elokeszites.md (régi 03):** Számozott alcímek (`## 3.1`, `## 3.2` stb.) eltávolítva -- RENDBEN
- **06_ux_penzugyei.md (régi 05):** iPod megjelenési dátuma javítva 2001-re -- RENDBEN
- **05_interjuk_dokumentalasa.md (régi 04):** Indi Young könyvhivatkozás kiegészítve (*Mental Models*, Rosenfeld Media) -- RENDBEN
- **05_interjuk_dokumentalasa.md (régi 04):** `Netpincér` egységesítve `NetPincér`-re -- RENDBEN

Az új 02-es fejezet tartalmilag kiváló, de stílusban és hangban eltér a többi fejezettől (részletesen lásd a 4. szekciót).

A hiányzó 18% az alábbi területekből adódik:

- **Kereszthivatkozások továbbra is hiányoznak** -- az előző áttekintés legfontosabb pontja, a fejezetek közötti és társkönyvre mutató hivatkozások nem kerültek be.
- **Az új 02-es fejezet hangvételi illeszkedése** -- a PDF-ből átdolgozott szöveg érezhetően más stílusú, mint az SRT-alapú fejezetek.
- **Szóközhiányok a „viszonylag" szóval** -- az eredeti „relatív" javítása során hat helyen elmaradt a szóköz.
- **Az 00_eloszó.md tartalomjegyzéke nem frissült** -- nem említi az új 2. fejezetet (használhatósági tesztelés) önálló pontként.

---

## 2. Fejezet-státuszok

### 00_eloszó.md -- MINOR ISSUES

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- nincs fejezetszám, nincs Összefoglalás/Ellenőrző kérdések (elvárt) |
| Callout-ok | OK (Megjegyzés:, Tipp:, A gyakorlatból:) |
| Hang | Tegező, következetes |
| Tipográfia | OK -- `--` gondolatjel, `„"` idézőjel |

**Problémák:**

1. **17--27. sor:** A „Mit tanulsz ebből a könyvből?" szekció öt pontot sorol fel, de az új fejezetstruktúra hét fejezetet tartalmaz (00--06). A 2. pont („Használhatósági tesztelés") helyes, de a számozás és a leírások nem tükrözik teljesen az átszámozott fejezetstruktúrát. A jelenlegi öt pont megfelel a tartalomnak, de a 3. pont („Toborzás") és a 4. pont („Interjúzás") között érdemes lenne jelezni, hogy az interjú előkészítése és a dokumentálás külön fejezet.
2. **Kereszthivatkozás a társkönyvre hiányzik** -- a 29. sor Megjegyzés-calloutja említi a tervezési minták könyvét, de nem tartalmaz explicit könyvhivatkozást (*Felülettervezési minták*).
3. **43. sor:** `Mielőtt belevágsz` -- az „Az első fejezet a UX alapjairól szól, a második a használhatósági tesztelésről" szöveg most korrekt az átszámozás után.

---

### 01_ux_alapok.md -- MINOR ISSUES

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# 1.`, bevezető bekezdés, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK |
| Hang | Tegező, következetes |
| Tipográfia | PROBLÉMA -- három helyen hiányzó szóköz |

**Problémák:**

1. **43. sor:** `viszonylagkényelmetlen` -- hiányzó szóköz. Javítandó: `viszonylag kényelmetlen`.
2. **106. sor:** `viszonylagkevés` -- hiányzó szóköz. Javítandó: `viszonylag kevés`.
3. **132. sor:** `viszonylagjól` -- hiányzó szóköz. Javítandó: `viszonylag jól`.
4. **Kereszthivatkozás hiányzik:** A 33. sorban a perszónák említésénél természetes hely lenne a „Lásd az 5. fejezetet a perszónák részletes felépítéséhez" hivatkozás (az átszámozás miatt most 5. fejezet).

---

### 02_hasznalhatosagi_teszteles.md -- NEEDS WORK

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# 2.`, bevezető bekezdés, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK -- Tipp:, Figyelem!, Megjegyzés:, A gyakorlatból: mind jelen vannak |
| Hang | PROBLÉMA -- eltérő hangvétel (lásd 4. szekció) |
| Tipográfia | OK -- `--` gondolatjel, `„"` idézőjel |

**Problémák:**

1. **123. sor:** `mostazonnal :)` -- smiley emoticon nem felel meg a könyv stílusának. Távolítsuk el a `:)`-t. Javítandó: `mostazonnal.`
2. **149. sor:** `gondoljunk abba: amibe` -- nyelvtanilag helytelen. A helyes forma: `gondoljunk bele: amibe`. Az „abba" vonzat nem illik a kontextusba.
3. **210. sor:** `összázásán` -- valószínűleg elütés. Javítandó: `összegzésén` vagy `összefoglalásán`.
4. **61. sor:** `mind a megrendelő alkalmatlan usertesztre tesztalanynak` -- furcsa fogalmazás, a „mind" itt nem értelmes. Javítandó: `a megrendelő is alkalmatlan usertesztre tesztalanynak` vagy `maga a megrendelő is alkalmatlan`.
5. **7. sor:** A fejezet formálisabb, akadémikusabb stílusban indul, mint a többi fejezet. Az „egy a UX pszichológiai ágából származó kvalitatív vizsgálati módszer" mondat tudományos regiszterben van, míg a többi fejezet közvetlenebb hangot üt meg.
6. **Kereszthivatkozás hiányzik:** A fejezet nem hivatkozik sem az 1. fejezetre (ahol a használhatóságot definiáltuk), sem a 3. fejezetre (toborzás -- honnan kerülnek a tesztalanyok).
7. **Steve Krug könyvhivatkozás:** A 214. sorban a *Rocket Surgery Made Easy* csak félformálisan van bevezetve. A stílusútmutató F. szekciója előírja: cím + szerző + kiadó az első előfordulásnál. Javítandó: „*Rocket Surgery Made Easy* -- Steve Krug (New Riders)".
8. **Rövidítések:** A `pl.` rövidítés tízszer fordul elő ebben a fejezetben, míg a többi fejezetben alig (01-ben egyszer). Ez szóbeli/PDF-maradvány -- a többi fejezet kiírja: „például".

---

### 03_toborzas.md -- PASS

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# 3.`, bevezető bekezdés, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK |
| Hang | Tegező, következetes |
| Tipográfia | OK |

**Megjegyzések:**

1. **1. sor:** A fejezetszám helyes (`# 3.`), a fájlnév (`03_toborzas.md`) illeszkedik.
2. **3. sor:** A bevezető bekezdés korrekt: „Most, hogy megismertük a használhatósági tesztelés alapjait" -- ez helyes visszautalás a (most már) 2. fejezetre.
3. **Kereszthivatkozás hiányzik** a 4. fejezetre (interjú-előkészítés) az Összefoglalás végén.

---

### 04_interju_elokeszites.md -- PASS

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# 4.`, bevezető bekezdés, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK |
| Terminológia | OK -- perszóna (korábban javítva) |
| Hang | Tegező, következetes |
| Tipográfia | OK |

**Megjegyzések:**

1. **3. sor:** A bevezető helyesen utal az előző fejezetre.
2. **5. sor:** A `sztereotípiavizsgálat` egybeírva szerepel; a styleguide D. szekciója kötőjeles formát ír elő (`sztereotípia-vizsgálat`). Ez az előző áttekintésben KÖZEPES prioritásúként volt jelölve, és nem lett javítva.
3. **111. sor:** A Bixby-s félretelefonálás hivatkozás továbbra is levegőben lóg -- a demóinterjú-részletben nem szerepel. Ez az előző áttekintésben KÖZEPES prioritásúként volt jelölve.
4. **127. sor:** A „hát vagy fogok, vagy nem" idézett gondolat kontextusban elfogadható.
5. **131. sor:** A „Hát, az egy rossz dolog" és „Hát hogyne" idézett párbeszédben vannak, tehát megengedettek.

---

### 05_interjuk_dokumentalasa.md -- MINOR ISSUES

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# 5.`, bevezető bekezdés, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK |
| Hang | Tegező, következetes |
| Tipográfia | PROBLÉMA -- egy helyen hiányzó szóköz |

**Problémák:**

1. **63. sor:** `viszonylagtriviális` -- hiányzó szóköz. Javítandó: `viszonylag triviális`.
2. **Kereszthivatkozás hiányzik** az 1. fejezetre a user journey fogalom bevezetésénél (13. sor).

---

### 06_ux_penzugyei.md -- MINOR ISSUES

| Szempont | Értékelés |
|---|---|
| Szerkezet | OK -- `# Függelék:` cím (fejezetszám helyett, elvárt), bevezető, `## Összefoglalás`, `## Ellenőrző kérdések` |
| Callout-ok | OK |
| Hang | Tegező, következetes |
| Tipográfia | PROBLÉMA -- két helyen hiányzó szóköz |

**Problémák:**

1. **53. sor:** `viszonylagolcsó` -- hiányzó szóköz. Javítandó: `viszonylag olcsó`.
2. **87. sor:** `viszonylagnagy` -- hiányzó szóköz. Javítandó: `viszonylag nagy`.

---

## 3. Konkrét hibák összesítése

### Új hibák (az előző áttekintés óta keletkezett)

| # | Fájl | Sor | Szöveg | Típus | Prioritás |
|---|---|---|---|---|---|
| 1 | 01_ux_alapok.md | 43, 106, 132 | `viszonylagkényelmetlen`, `viszonylagkevés`, `viszonylagjól` | Hiányzó szóköz (find-replace hiba) | MAGAS |
| 2 | 05_interjuk_dokumentalasa.md | 63 | `viszonylagtriviális` | Hiányzó szóköz | MAGAS |
| 3 | 06_ux_penzugyei.md | 53, 87 | `viszonylagolcsó`, `viszonylagnagy` | Hiányzó szóköz | MAGAS |
| 4 | 02_hasznalhatosagi_teszteles.md | 123 | `:)` smiley | Stílusidegen elem | MAGAS |
| 5 | 02_hasznalhatosagi_teszteles.md | 149 | `gondoljunk abba:` | Nyelvtani hiba (helyes: `gondoljunk bele:`) | MAGAS |
| 6 | 02_hasznalhatosagi_teszteles.md | 210 | `összázásán` | Elütés (javítandó: `összegzésén`) | MAGAS |
| 7 | 02_hasznalhatosagi_teszteles.md | 61 | `mind a megrendelő alkalmatlan` | Nyelvtani hiba | KÖZEPES |
| 8 | 02_hasznalhatosagi_teszteles.md | 7 | akadémikus stílus a bevezető bekezdésben | Hangvételi eltérés | KÖZEPES |
| 9 | 02_hasznalhatosagi_teszteles.md | passim | `pl.` tízszer | Rövidítés-sűrűség (SRT-fejezetek kiírják) | KÖZEPES |
| 10 | 02_hasznalhatosagi_teszteles.md | 214 | Steve Krug könyvhivatkozás hiányos | Stílusútmutató F. szekció szerinti formátum hiánya | KÖZEPES |

### Korábbi hibák, amelyek NEM lettek javítva

| # | Fájl | Sor | Szöveg | Típus | Prioritás |
|---|---|---|---|---|---|
| 11 | 04_interju_elokeszites.md | 5, 11, 37, 189, 229, 233 | `sztereotípiavizsgálat` egybeírva | Kötőjelezés (styleguide: `sztereotípia-vizsgálat`) | KÖZEPES |
| 12 | 04_interju_elokeszites.md | 111 | Bixby-s félretelefonálás hivatkozás | Hiányzó tartalomra utalás | KÖZEPES |
| 13 | Összes fejezet | -- | Fejezetek közötti kereszthivatkozások | Teljes hiány | MAGAS |
| 14 | Összes fejezet | -- | Társkönyv-hivatkozások (*Felülettervezési minták*) | Teljes hiány | MAGAS |

---

## 4. Hangvételi konzisztencia -- a PDF-forrású 02-es fejezet értékelése

### Eltérések a SRT-alapú fejezetekhez képest

A 02_hasznalhatosagi_teszteles.md tartalmilag kiváló és jól strukturált fejezet, amely a használhatósági tesztelés módszertanát gyakorlatiasan és hozzáférhetően mutatja be. Ugyanakkor a hangvétele több ponton eltér a többi fejezettől:

**1. Regiszter és szókincs**

Az SRT-alapú fejezetek közvetlenebb, társalgóbb hangnemet ütnek meg: „Vegyünk két mobilalkalmazást", „Gondolj bele", „Ezért kérdezzük azt, hogy...". A 02-es fejezet gyakrabban használ formálisabb, akadémikusabb fordulatokat: „egy a UX pszichológiai ágából származó kvalitatív vizsgálati módszer" (7. sor), „A kutatási képlet továbbra is" (23. sor), „Ily módon" (26. sor), „szükségeltetik" (32. sor).

**2. Rövidítések**

A 02-es fejezet tízszer használja a `pl.` rövidítést, míg az SRT-alapú fejezetek szinte kivétel nélkül kiírják: „például". Ez apró, de ismétlődő jelzés a stílusváltásra.

**3. „Mi"-forma**

Az SRT-alapú fejezetek erősen használják az első személy többest, a közös felfedezés hangját: „nézzük meg", „arra jutunk", „mi szándékosan". A 02-es fejezet is használja (pl. „tesztelünk", „használjuk"), de kevésbé hangsúlyosan. Ehelyett gyakrabban jelenik meg a semleges, leíró tónus.

**4. Anekdoták és magyar kontextus**

Az SRT-alapú fejezetek jellegzetes erőssége a gazdag, magyar kontextusú anekdota (MÁV pénztáros, NetPincér vs. Tinder, pizzafutárlány). A 02-es fejezet is tartalmaz gyakorlati példákat (FIBA, Gozsdu udvar, BKV bérlet, MÁV Start), de azok rövidebbek és kevésbé személyesek.

**5. Idézett beszédminták**

A 02-es fejezet tartalmaz három szó szerinti „mondandó" részt (153., 177., 185. sor), amelyeket kurzív blockquote-ban ad meg. Ez hasznos és gyakorlatias, és nincs párhuzama a többi fejezetben -- de illik a stílushoz, és értékes hozzáadás.

### Verdikt

A 02-es fejezet **70%-ban illeszkedik** a SRT-alapú fejezetek hangvételéhez. A tegezés, a gyakorlati példák és a határozott álláspontok jelen vannak. A fő eltérések -- a formálisabb regiszter, a `pl.` rövidítések és a kevésbé személyes anekdoták -- egy szerkesztői körben javíthatók. A tartalom értékes és hiánypótló. A javítás nem a tartalom átírását igényli, hanem a következő hangolási lépéseket:

1. A bevezető bekezdés (7. sor) átalakítása közvetlenebb hangra.
2. A `pl.` rövidítések kiírása `például`-ra.
3. Az „Ily módon" (26. sor) és „szükségeltetik" (32. sor) típusú formális fordulatok egyszerűsítése.
4. A `:)` emotikon eltávolítása (123. sor).
5. A nyelvtani hibák javítása (149., 210. sor).

---

## 5. Kereszthivatkozási állapot

A korábbi áttekintés a kereszthivatkozások teljes hiányát jelölte a legjelentősebb hiányosságnak. Ez a helyzet **nem változott**: egyetlen fejezet sem tartalmaz explicit kereszthivatkozást másik fejezetre vagy a társkönyvre.

Az átszámozás után a korábbi javaslatok frissített verziója:

| Honnan | Hova | Javaslat |
|---|---|---|
| 00_eloszó, 29. sor | társkönyv | „Lásd a *Felülettervezési minták* című társkötetet." |
| 01_ux_alapok, 33. sor | 5. fejezet | „A perszónák felépítéséről lásd az 5. fejezetet." |
| 01_ux_alapok, 35. sor | 2. fejezet | „A használhatósági tesztelés módszertanáról lásd a 2. fejezetet." |
| 02_hasznalhatosagi_teszteles, Összefoglalás | 3. fejezet | „A tesztalanyok toborzásáról lásd a 3. fejezetet." |
| 03_toborzas, Összefoglalás | 4. fejezet | „Az interjú előkészítéséről lásd a 4. fejezetet." |
| 04_interju_elokeszites, 35. sor | 5. fejezet | „A perszóna felépítéséről részletesen lásd az 5. fejezetet." |
| 05_interjuk_dokumentalasa, 13. sor | 1. fejezet | „A felhasználói életút fogalmát az 1. fejezetben vezettük be." |
| 06_ux_penzugyei, 15. sor | 1. fejezet | „A MÁV tranzakcióidő-problémáját az 1. fejezetben bemutattuk." |
| 06_ux_penzugyei, 77. sor | 4. fejezet | „Az interjútechnikáról lásd a 4. fejezetet." |
| 06_ux_penzugyei, 107. sor | társkönyv | „A prototípus felépítéséről lásd a *Felülettervezési minták* vonatkozó fejezeteit." |

---

## 6. Terminológiai audit (frissített)

### Korábban jelzett inkonzisztenciák javítási állapota

| Kifejezés | Állapot | Megjegyzés |
|---|---|---|
| perszóna / persona | JAVÍTVA | A `personákat` javítva `perszónákat`-ra a 04-es fejezetben |
| NetPincér / Netpincér | JAVÍTVA | Egységesen `NetPincér` mindenhol |
| relatív -> viszonylag | RÉSZBEN JAVÍTVA | A szó cserélve, de 6 helyen hiányzik a szóköz utána |
| sztereotípiavizsgálat / sztereotípia-vizsgálat | NEM JAVÍTVA | A 04-es fejezetben továbbra is egybeírva |
| 2002-ben -> 2001-ben (iPod) | JAVÍTVA | A 06-os fejezetben helyes dátum |
| Indi Young könyvhivatkozás | JAVÍTVA | *Mental Models*, Rosenfeld Media formátum |

### Új terminológiai kérdések a 02-es fejezetből

| Kifejezés a 02-ben | A többi fejezetben | Megjegyzés |
|---|---|---|
| userteszt, user test | használhatósági teszt | A 02-es fejezetben vegyesen szerepel a `user test`, `userteszt` és `felhasználói teszt`. Az 1. fejezetben és az előszóban konzekvensen `használhatósági teszt(elés)` szerepel. Érdemes egységesíteni. |
| tesztalany | interjúalany | A 02-es fejezetben `tesztalany`, a többi fejezetben `interjúalany`. Ez korrekt, mert más kontextus, de a 02-es fejezetben egyszer `user` (141., 147. sor) is megjelenik -- javasolt egységesen `felhasználó`-nak írni. |

---

## 7. Priorizált tennivalók

### MAGAS prioritás (publikáció előtt kötelező)

1. **Hat helyen hiányzó szóköz javítása** a `viszonylag` szó után -- ez valószínűleg egy find-replace hiba eredménye:
   - 01_ux_alapok.md, 43. sor: `viszonylagkényelmetlen` -> `viszonylag kényelmetlen`
   - 01_ux_alapok.md, 106. sor: `viszonylagkevés` -> `viszonylag kevés`
   - 01_ux_alapok.md, 132. sor: `viszonylagjól` -> `viszonylag jól`
   - 05_interjuk_dokumentalasa.md, 63. sor: `viszonylagtriviális` -> `viszonylag triviális`
   - 06_ux_penzugyei.md, 53. sor: `viszonylagolcsó` -> `viszonylag olcsó`
   - 06_ux_penzugyei.md, 87. sor: `viszonylagnagy` -> `viszonylag nagy`

2. **02_hasznalhatosagi_teszteles.md nyelvi hibák javítása:**
   - 123. sor: `:)` eltávolítása
   - 149. sor: `gondoljunk abba:` -> `gondoljunk bele:`
   - 210. sor: `összázásán` -> `összegzésén`
   - 61. sor: `mind a megrendelő alkalmatlan` -> `a megrendelő is alkalmatlan` (vagy `maga a megrendelő is alkalmatlan`)

3. **Kereszthivatkozások hozzáadása** -- lásd az 5. szekció részletes javaslatait. Minimum: fejezetenként 1 hivatkozás.

### KÖZEPES prioritás (kiadás előtt javasolt)

4. **02-es fejezet hangvételi harmonizálása:** A `pl.` rövidítések kiírása `például`-ra, formális fordulatok egyszerűsítése (lásd 4. szekció).

5. **04_interju_elokeszites.md:** `sztereotípiavizsgálat` kötőjelezése `sztereotípia-vizsgálat`-ra (6 előfordulás).

6. **04_interju_elokeszites.md, 111. sor:** A Bixby-s félretelefonálás hivatkozás továbbra is hiányzó tartalomra utal -- vagy kiegészítendő a demóinterjú, vagy módosítandó a callout.

7. **02-es fejezet terminológiai egységesítése:** A `user test` / `userteszt` formák helyett `használhatósági teszt` vagy `felhasználói teszt` -- összhangban a többi fejezettel.

### ALACSONY prioritás (javítja a minőséget)

8. **00_eloszó.md tartalomjegyzéke:** A „Mit tanulsz ebből a könyvből?" szekció öt pontja helytálló, de a 4. pont (Interjúzás) alatt érdemes jelezni, hogy ez két fejezetet fed le (előkészítés + dokumentálás).

9. **Ábra- és táblázatszámozás** -- továbbra is hiányzik.

10. **Glosszárium-fejezet** -- továbbra is javasolt.

---

## 8. Összesítő táblázat

| Fejezet | Fájlnév | Fejezetszám a szövegben | Státusz | Fő teendők |
|---|---|---|---|---|
| Előszó | 00_eloszó.md | (nincs) | MINOR ISSUES | Társkönyv-hivatkozás, tartalomjegyzék finomítás |
| 1. fejezet | 01_ux_alapok.md | `# 1.` | MINOR ISSUES | 3 hiányzó szóköz, kereszthivatkozások |
| 2. fejezet | 02_hasznalhatosagi_teszteles.md | `# 2.` | NEEDS WORK | Nyelvi hibák, hangvételi harmonizálás, `:)` eltávolítás |
| 3. fejezet | 03_toborzas.md | `# 3.` | PASS | Kereszthivatkozás a 4. fejezetre |
| 4. fejezet | 04_interju_elokeszites.md | `# 4.` | PASS | Sztereotípia-vizsgálat kötőjelezés, Bixby-hivatkozás |
| 5. fejezet | 05_interjuk_dokumentalasa.md | `# 5.` | MINOR ISSUES | 1 hiányzó szóköz, kereszthivatkozások |
| Függelék | 06_ux_penzugyei.md | `# Függelék:` | MINOR ISSUES | 2 hiányzó szóköz |

---

*Ez a végső lektori áttekintés a styleguide_hu.md v1.0 és az editorial_review.md alapján készült. A MAGAS prioritású javítások elvégzése után a kézirat publikálhatóvá válik; a KÖZEPES és ALACSONY prioritású javítások a kiadói korrektúra során is megoldhatók.*
