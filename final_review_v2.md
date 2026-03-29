# Végső lektori áttekintés v2 -- a 02-es fejezet hangvételi átdolgozása után

**Dátum:** 2026. március 29.
**Lektor:** Végső lektori szerkesztés v2 (final review, post-rewrite)
**Fókusz:** A 02_hasznalhatosagi_teszteles.md hangvételi harmonizálásának értékelése
**Referencia:** final_review.md (v1), styleguide_hu.md v1.0

---

## 1. Ch02 hangvételi verdikt: NEEDS MORE WORK

Az átdolgozás **részben sikeres** volt. A v1-es áttekintésben jelzett néhány konkrét hiba javítva lett, de a fő hangvételi problémák és a `pl.` rövidítések változatlanul maradtak.

### Mi javult a v1 óta

| Probléma | Állapot |
|---|---|
| `:)` smiley (régi 123. sor) | JAVÍTVA -- eltávolítva |
| `gondoljunk abba:` (149. sor) | JAVÍTVA -- `gondoljunk bele:` |

### Mi NEM javult

| # | Sor | Probléma | Prioritás |
|---|---|---|---|
| 1 | passim (10 db) | `pl.` rövidítés nem lett kiírva `például`-ra. A ch04 és ch05 **nulla** `pl.`-t tartalmaz, a ch01 egyet. A ch02-ben tíz maradt -- ez továbbra is a legfeltűnőbb stilisztikai eltérés. | MAGAS |
| 2 | 210 | `összázásán` -- elütés, javítandó: `összegzésén` vagy `összefoglalásán` | MAGAS |
| 3 | 61 | `mind a megrendelő alkalmatlan usertesztre tesztalanynak` -- a „mind" nyelvtanilag helytelen ebben a szerkezetben. Javítandó: `a megrendelő is alkalmatlan usertesztre tesztalanynak` vagy `maga a megrendelő is alkalmatlan`. | MAGAS |
| 4 | 32 | `Három dolog szükségeltetik:` -- archaikus, formális regiszter, nem illik a könyv hangjába. A ch01/ch03 hangja: „Három dolog kell hozzá:" | KÖZEPES |
| 5 | 26 | `Ily módon` -- formális fordulat, a többi fejezet nem használ ilyet. Javasolt: „Így" vagy „Ezáltal". | KÖZEPES |
| 6 | 7 | A bevezető mondat (`egy a UX pszichológiai ágából származó kvalitatív vizsgálati módszer`) továbbra is akadémikusabb, mint a többi fejezet indítása. Vö. ch01: „Az előszóban már szó esett arról, hogy..."; ch03: „Most, hogy megismertük...". | KÖZEPES |
| 7 | 214 | Steve Krug könyvhivatkozás formátuma nem felel meg a styleguide F. szekciójának: `*cím* -- szerző (kiadó)`. Jelenleg: `**Steve Krug: Rocket Surgery Made Easy**` (félkövér, fordított sorrend, kiadó hiányzik). Javítandó: `*Rocket Surgery Made Easy* -- Steve Krug (New Riders)` | KÖZEPES |
| 8 | 196 | `katinttana` -- elütés, javítandó: `kattintana` | MAGAS |

### Hangvételi összehasonlítás

A ch02 tegezése rendben van. A "mi"-forma (nézzük, tesztelünk, használjuk) jelen van. A callout-ok típushelyes (Tipp:, Megjegyzés:, Figyelem!, A gyakorlatból:). A tipográfia (`--` gondolatjelek, `„"` idézőjelek) helyes, em-dash nem fordul elő.

A fő maradék probléma **a regiszter**: a ch02 továbbra is formálisabb fordulatokat tartalmaz (`szükségeltetik`, `Ily módon`, `kvalitatív vizsgálati módszer`), mint amilyeneket a ch01 vagy ch03 használna. A ch01 és ch03 társalgósabb, melegebb, anekdotikusabb -- a ch02 inkább tankönyvi.

Az anekdoták terén a FIBA-példa (69. sor), a Gozsdu udvar (133. sor), a BKV bérlet (110., 123. sor) és a „ragasztós módszer" (206. sor) jelen vannak, de **MÁV-anekdota nem került be**, holott az 1. fejezet gazdag MÁV-példákat tartalmaz (pénztáros-tranzakcióidő, 75. sor). A 109. sor MÁV Start-ra hivatkozik, de csak tesztfeladat-példaként, nem narratív anekdotaként.

### Verdikt részletezése

A ch02 jelenleg **75%-ban illeszkedik** a többi fejezet hangvételéhez (a v1-ben 70% volt -- az `:)` eltávolítása és a `gondoljunk bele` javítása minimálisan javított). A teljes illeszkedéshez a következő lépések szükségesek:

1. Mind a 10 `pl.` kiírása `például`-ra (mechanikus feladat, 5 perc)
2. `összázásán` javítása `összegzésén`-re
3. `katinttana` javítása `kattintana`-ra
4. `mind a megrendelő` javítása `a megrendelő is`-re
5. `szükségeltetik` egyszerűsítése `kell`-re
6. `Ily módon` egyszerűsítése
7. A bevezető mondat közvetlenebbé tétele
8. Steve Krug hivatkozás formátumának javítása

---

## 2. Szerkezeti ellenőrzés -- ch02

| Szempont | Eredmény |
|---|---|
| `# 2.` fejezetzím | OK (1. sor) |
| Bevezető bekezdés | OK (3. sor) |
| `## Összefoglalás` | OK (221. sor) |
| `## Ellenőrző kérdések` | OK (225. sor) |
| Callout-típusok | OK -- csak Tipp:, Megjegyzés:, Figyelem!, A gyakorlatból: |
| Tipográfia: `--` gondolatjel | OK -- kizárólag `--`, em-dash (--) nem fordul elő |
| Tipográfia: `„"` idézőjel | OK |

---

## 3. Korábban jelzett problémák állapota (az egész könyvben)

### JAVÍTVA a v1 óta

| Probléma | Állapot |
|---|---|
| `viszonylag` szóközhiány (6 helyen) | JAVÍTVA -- egyetlen előfordulás sincs |
| `:)` smiley a ch02-ben | JAVÍTVA |
| `gondoljunk abba:` a ch02-ben | JAVÍTVA |

### NEM JAVÍTVA

| # | Fájl | Probléma | Prioritás |
|---|---|---|---|
| 1 | 02_hasznalhatosagi_teszteles.md | `pl.` 10x nem kiírva `például`-ra | MAGAS |
| 2 | 02_hasznalhatosagi_teszteles.md | `összázásán` elütés | MAGAS |
| 3 | 02_hasznalhatosagi_teszteles.md | `mind a megrendelő` nyelvtani hiba | MAGAS |
| 4 | 02_hasznalhatosagi_teszteles.md | `katinttana` elütés (196. sor) -- uj | MAGAS |
| 5 | 02_hasznalhatosagi_teszteles.md | Formális fordulatok (`szükségeltetik`, `Ily módon`) | KÖZEPES |
| 6 | 02_hasznalhatosagi_teszteles.md | Bevezető mondat akadémikus regiszterben | KÖZEPES |
| 7 | 02_hasznalhatosagi_teszteles.md | Steve Krug hivatkozás hiányos formátum | KÖZEPES |
| 8 | 04_interju_elokeszites.md | `sztereotípiavizsgálat` egybeírva 6 helyen (kötőjel kéne) | KÖZEPES |
| 9 | 04_interju_elokeszites.md | Bixby-s félretelefonálás hivatkozás hiányzó tartalomra utal (111. sor) | KÖZEPES |
| 10 | Összes fejezet | Kereszthivatkozások teljes hiánya (fejezetek között és társkönyvre) | MAGAS |

---

## 4. Publikációra való készültség

**~84%**

A v1-ben 82% volt. A javulás a `viszonylag` szóközhiányok és a ch02 két konkrét hibájának javításából adódik.

A hiányzó 16% összetétele:

| Terület | Hozzájárulás |
|---|---|
| Kereszthivatkozások teljes hiánya | ~6% |
| Ch02 hangvételi illeszkedés (formális fordulatok, `pl.`) | ~4% |
| Ch02 nyelvi hibák (`összázásán`, `katinttana`, `mind a megrendelő`) | ~3% |
| Ch04 `sztereotípia-vizsgálat` kötőjelezés + Bixby-hivatkozás | ~2% |
| Steve Krug hivatkozás formátum | ~1% |

### Priorizált tennivalók a publikáció előtt

1. **Ch02 `pl.` kiírása `például`-ra** -- 10 előfordulás, mechanikus javítás
2. **Ch02 elütések javítása** -- `összázásán`, `katinttana`
3. **Ch02 `mind a megrendelő` nyelvtani javítás**
4. **Kereszthivatkozások beillesztése** -- legalább a v1-ben javasolt 10 helyen
5. **Ch02 formális fordulatok egyszerűsítése** -- `szükségeltetik`, `Ily módon`, bevezető mondat
6. **Ch04 `sztereotípia-vizsgálat` kötőjelezés** (6 helyen)
7. **Steve Krug hivatkozás formátum** a styleguide szerint

---

*A ch02 tartalmilág kiváló, a szerkezete helyes, és a legfontosabb hangvételi elemek (tegezés, callout-ok, tipográfia) rendben vannak. A maradék munka nagyrészt mechanikus: rövidítések kiírása, elütések javítása, formális fordulatok cseréje. Egy szerkesztői körrel publikálható szintre hozható.*
