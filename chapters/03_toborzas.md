# 3. Résztvevők toborzása

Most, hogy megismertük a használhatósági tesztelés alapjait, ideje valódi felhasználókkal beszélnünk. Ahhoz viszont, hogy interjúzni tudjunk, interjúalanyokra van szükségünk -- és ez nem mindig triviális. A toborzás az a folyamat, amellyel megtaláljuk, megszűrjük és behívjuk a számunkra releváns embereket.

## A toborzás menete

A toborzás nagyban hasonlít egy álláshirdetés feladásához. A folyamat lépései a következők:

1. **Hirdetés feladása** -- Készítünk egy hirdetést, amelyet a célközönségünkhöz közel álló felületeken osztunk meg. A gyakorlatban ez Magyarországon szinte mindig Facebook-csoportokban történik, de használhatunk apróhirdetési oldalakat is (Jófogás, Vatera), esetleg álláshirdetési portálokat.
2. **Szűrőkérdőív kitöltése** -- A hirdetés egy kérdőívre viszi az embereket, ahol ki tudjuk szűrni azokat, akik nem felelnek meg a kritériumainknak.
3. **Kiválogatás és meghívó küldése** -- A beérkezett válaszok alapján kiválogatjuk a megfelelő jelölteket, és meghívjuk őket az interjúra. A beválogatástól számított 24 órán belül értesítsük az illetőt -- különben elfelejti, hogy ilyen történt vele, és nem fog reagálni.
4. **Időpont-egyeztetés** -- Felhívjuk telefonon vagy e-mailben egyeztetünk. Az esetek 90%-ában telefonon egyeztetjük le az időpontot -- a gyakorlatban ez vált be. Szoftveresen a Calendly a leggyakrabban használt megoldás.
5. **Visszaigazolás és emlékeztető** -- Küldünk egy visszaigazolást az egyeztetett időpontról, majd az interjú napján -- lehetőleg reggel -- egy emlékeztetőt is, hogy ne felejtse el az alany. Megadjuk a helyszínt is, legyen az akár fizikai, akár egy Zoom- vagy Teams-meghívó.
6. **Interjú lefolytatása** -- Megtörténik az interjú, amelyet általában felveszünk (ennek GDPR-vonzatai vannak, erről később).
7. **Jutalom küldése** -- A sikeres interjú után küldünk egy ajándékot (ösztönzőt).

> **Tipp:** Az interjú napján küldött reggeli emlékeztető drasztikusan csökkenti a lemondások számát. Egy rövid üzenet elég: „Szia! Ne feledd, ma van az interjúnk, itt és itt találkozunk."

## A toborzókérdőív összeállítása

Ha magunk toborzunk, szükségünk van egy szűrőkérdőívre (screener questionnaire). Ezt általában kérdőívszerkesztő eszközzel készítjük -- ilyen a Google Forms, a Microsoft Forms vagy a Typeform.

### A legfontosabb alapelv: ne derüljön ki, kit keresünk

A toborzókérdőív „művészetének" az elsődleges szempontja, hogy **ne derüljön ki, pontosan kit keresünk**. Ennek az az oka, hogy az emberek szeretnek megfelelni -- akkor is, ha semmilyen tétje nincs a dolognak. Ha pedig tétje van, mert ajándékutalványt ajánlunk a végén, akkor még inkább.

Ezért nyílt kérdéseket tegyünk fel, és a válaszlehetőségek között mindig legyen ott az összes eshetőség -- azért, hogy ne lehessen kitalálni, melyik a „helyes" válasz.

### Mit szűrünk ki?

- **Akik hazudnak** -- például azt jelölik be, amit gondolják, hogy hallani akarunk
- **Akik nem célközönség** -- bármilyen okból
- **Akiknél érdekütközés áll fenn** -- például más UX-esek a saját kutatásunkban, vagy a konkurencia munkatársai
- **Akik nem érnek rá** -- rögtön rákérdezünk a számunkra releváns napokra
- **Akik keveset beszélnek** -- nyílt kérdésekkel szűrhetők, de ez telefonon úgyis kiderül

### Példa: BME GTK hallgatókat keresünk

Tegyük fel, hogy budapesti, végzős BME GTK-s hallgatókat keresünk, akik az Ergonómia Tanszéken végzik a szakmai gyakorlatukat és ráérnek szerdán. A kérdőív **nem** úgy néz ki, hogy „A BME GTK-ra jársz? Igen / Nem" -- ez túl egyértelmű lenne. Ehelyett:

1. **Hova jársz egyetemre?** -- BME / ELTE / Corvinus / Egyéb
2. **Melyik karra jársz?** -- Gazdaságtudományi / Természettudományi / Informatikai / Mérnöki / Egyéb (Ha csak BME-seknek osztjuk ki, akkor is felsoroljuk az összes kart -- és hozzáadjuk: „Nem a BME-re járok" / „Már végeztem".)
3. **Hol laksz?** -- Budapest / Agglomeráció / Pest megye / Vidéki nagyváros / Vidéki kisváros / Külföld / Egyéb
4. **Mikor végzel?** -- Ebben a félévben / Következő félévben / Később / Nem tudom / Már végeztem / Nem járok egyetemre
5. **Melyik tanszéken végzed a szakmai gyakorlatodat?** -- (felsorolás vagy szöveges mező)
6. **Mely napokon érsz rá?** -- Hétfő (március 28.) / Kedd (29.) / Szerda (30.) / A héten egyik sem jó

Mindenképpen kérjük be az **e-mail címet** és a **telefonszámot** is.

> **Megjegyzés:** Ha automatikus kiértékelést akarunk, az opciókat listából kell felsorolnunk. Ha manuálisan szűrünk, szöveges válasz is elegendő -- ez kevesebb munka a kérdőív készítésekor, de több munka a kiértékelésnél.

### Kétfajta szűrési megoldás

Az egyik megoldásban a kérdőív automatikusan szűr: a Google Forms szekciókra bontásával (Go to section based on answer) a nem megfelelő válaszok egy „Köszönjük a kitöltést!" oldalra vezetnek, ahol a kitöltő megkapja a kisebb ajándékot (pl. 3000 Ft-os kupont).

A másik megoldásban mi kézzel szűrünk a beérkezett válaszok között, és csak a megfelelő jelölteknek küldünk meghívót a nagyobb értékű interjúra.

> **Tipp:** A Typeform intelligensebb elágazásokat támogat, mint a Google Forms -- nem kell „szekcióépítészetet" csinálnunk. Viszont a Google Forms ingyenes és általánosan elérhető, ezért a legtöbb hazai projektnél ezt használjuk.

### A kérdőív befejezése

A kérdőív végén mindig legyen benne:

- Egy **rövid leírás**, hogy interjúalanyokat keresünk (pl. „Interjúalanyokat keresünk egy egyetemi kutatáshoz")
- Az **incentíva** (ösztönző) összege (pl. „A kutatás díjazása 30 000 Ft/fő")
- A **GDPR adatkezelési nyilatkozat** linkje

Akik a szűrő „jó" ágára futnak, azoktól kérjük be az e-mail címet és telefonszámot is, és ők kapják a nagyobb díjazás ajánlatát.

## Az adatkezelésről röviden

Már azzal, hogy toborzókérdőívet küldünk ki, személyes adatot kezelünk. Az európai adatvédelmet a GDPR szabályozza, Magyarországon pedig a 2011. évi CXII. törvény az irányadó.

> **Figyelem!** Nem adhatok jogi tanácsot -- minden szervezetnek saját adatkezelési szabályzattal kell rendelkeznie. Ha magánvállalkozóként dolgozol, keress egy ügyvédet, aki ír neked egy adatkezelési szabályzatot. Az alábbiak általános irányelvek.

### Általános irányelvek

1. **Ne hazudj.** Ha azt állítod, hogy letörlöd az adatokat, akkor tényleg töröld le őket. A GDPR előírásai alapján az adatkezelés időtartamát előre meg kell határozni, és azt a célhoz szükséges minimumra kell korlátozni -- ezt neked expliciten le kell írnod.
2. **Tisztázd a célt.** Mi az adatkezelés célja? Miért gyűjtjük ezeket az információkat?
3. **A részvétel önkéntes és visszavonható.** Ezt mindig tisztázni kell, és kell egy kontaktot adni, akin keresztül a visszavonás megtörténhet (pl. adatvedelem@cegnev.hu).
4. **Határozd meg a gyűjtött információk körét.** Pontosan milyen adatokat kezelünk?
5. **Határozd meg, kik ismerik meg az információt.** Biztosítsd a résztvevőket, hogy a felvételeket csak az arra jogosult személyek hallgathatják meg, és titoktartás kötelezi őket.
6. **Bizalmasan kezelendő.** Harmadik személynek az adatok nem adhatók ki.
7. **Az adatkezelés helye.** Meg kell adni az adatkezelő szervezet székhelyét vagy telephelyét (magánszemélynél a lakcímet).

### A beleegyező nyilatkozat (consent form)

A beleegyező nyilatkozatban mindezeket le kell írni, és a résztvevőnek külön kell beleegyeznie:

- a kutatás célját megértette
- a részvétel önkéntes és visszavonható
- felvétel készül
- a felvételt bizonyos személyek megismerhetik (és őket titoktartás kötelezi)
- a személyes adatok törlése után mi marad meg (az anonimizált kutatási összefoglalók, amelyekből később a perszónák készülnek)

> **A gyakorlatból:** Ironikus, de a legtöbb személyes adat gyakran pont a beleegyező nyilatkozatban szerepel (születési név, hely, idő, anyja neve), mert az azonosíthatósághoz szükséges -- miközben a kutatáshoz ezekre egyáltalán nem vagyunk kíváncsiak.

### Gyakorlati tippek

- Állíts be Google Naptárban figyelmeztetőt az adattörlés határidejére.
- Három hónapnál tovább úgysem lesz időd visszahallgatni az interjúfelvételeket -- érdemes reálisan kezelni a határidőt.
- Digitális aláíráshoz az AVDH rendszer (Azonosításra Visszavezetett Dokumentumhitelesítés) használható: ha az illetőnek van ügyfélkapuja, alá tudja írni a nyilatkozatot digitálisan, és nem kell külön megadnia a személyes adatait.
- A résztvevőket leginkább az érdekli, hogy ki fogja hallani a felvételeket -- erre mindig adjunk egyértelmű választ.

## Az interjúalanyok jutalmazása

A toborzásban a jutalmat **incentívának** (ösztönzőnek) nevezzük. Kétféle van, két szinten -- összesen tehát négyfajta incentíváról kell beszélnünk.

### Konzumer vs. profi alanyok

Az első kérdés, hogy fogyasztókat (consumer) keresünk, vagy egy adott szakmában dolgozókat. A szakemberek ideje drágább, mert kevesebben vannak és nehezebben elérhetők.

| | Konzumer (fogyasztó) | Profi (szakember) |
|---|---|---|
| **Interjú díjazása** | 6 000 -- 10 000 Ft | 15 000 -- 20 000 Ft (de akár több százezer Ft is) |
| **Toborzás módja** | Facebook-csoport, hirdetés | Ügyfél hálózata, LinkedIn, toborzóplatform |
| **Példa** | Egyetemisták (1 000 -- 3 000 Ft is elég) | Igazgatók, miniszterek (egy félórás interjú akár 300 000 -- 400 000 Ft) |

> **Megjegyzés:** Amerikában egy konzumer interjúalany 20--40 dollárt kap (~5 000--10 000 Ft), egy szakember esetén a toborzóplatform díja 60--80 dollár, plusz az incentíva újabb 60--70 dollár.

### Az interjú vs. a kérdőív jutalma

Fontos, hogy két külön díjazási szintet tartsunk fenn:

- **A kérdőív kitöltéséért** -- kisebb jutalom. Lehet a saját termékünkön belüli kedvezmény (pl. 10%-os kuponkód), 500--1 000 Ft-os utalvány, vagy akár csak egy köszönőüzenet. Lényeg, hogy legalább egy „digitális sörre" hívjuk meg a kitöltőt.
- **Az interjúban való részvételért** -- nagyobb, abszolút értékű jutalom. Ez legyen olyasmi, amit a célközönség ténylegesen fel tud használni: eMAG-, Edigital-, Libri-, Tesco-, Auchan- vagy Lidl-ajándékutalvány. Magyarországon 6 000--30 000 Ft az általános sáv.

> **Figyelem!** Az interjú díját ne próbáld kiváltani a saját terméked ingyenes hozzáférésével -- ez általában nem fog működni. Az interjú az neked (vagy a megbízódnak) fájó dolognak kell hogy legyen pénzügyileg -- ez jelzi, hogy valóban értékes a számodra.

## A hirdetés összeállítása

Ha nem tudjuk másra bízni a toborzást, nekünk kell megcsinálni a hirdetést. Ez ugyanolyan reklám, mint bármelyik másik -- a reklámszabályok érvényesek rá, és érdemes marketinges kollégáktól tanácsot kérnünk.

### Négy lépésben

1. **Célközönség definiálása** -- Ki az, akiről el tudjuk képzelni, hogy az interjúban részt tud venni? Minimum: ország, nyelv, kor. De ki kell rajzolni azt is, hogy ki az, aki biztos nem. Ha például játékkonzolhoz kutatunk, a célcsoport a gémerek (gamer).
2. **A célközönség platformjának megtalálása** -- Hol mozog a célközönségünk online? Konzumer esetben Magyarországon szinte mindig Facebook-csoportok. Kérdezzük meg: mik azok a csoportok, ahová beférünk, és az admin engedélyével posztolhatunk?
3. **A reklámüzenet megírása** -- Erről részletesen alább.
4. **Reklámgrafika készítése** -- A célközönségre rezonáló, figyelemfelhívó grafika, ami nem ízléstelen és nem akar átvágni senkit.

### A reklámüzenet felépítése

A hirdetésben az elemeket erősségi sorrendben érdemes elhelyezni:

1. **Identitás** -- A legerősebb üzenet. „UX designerek, figyelem!" / „Vasútbarátok, figyelem!" / „Színházba járók, figyelem!" Az ember magára ismer, és elkezdi olvasni.
2. **Kontextus (élethelyzet)** -- Eggyel gyengébb, de hatásos. „Utaztál mostanában vonattal?" -- nem feltétlen az identitásod része, de releváns élethelyzet.
3. **Probléma** -- Amit a termékünk megold. „Neked is probléma az autómosás?" / „Vannak problémáid a jegyvásárlással?"
4. **Incentíva** -- Mi a fizetség? „A kérdőívet kitöltőket 3 000 Ft-os kuponnal jutalmazzuk." / „Akit behívunk interjúra, az kap 20 000 Ft-ot."

> **Tipp:** Lehetőleg minél többet és lehetőleg ebben a sorrendben próbáljuk az elemeket berakni a hirdetésbe. Az identitás az, ami a scrollozást megállítja -- ez kell az elejére.

### Hol hirdessünk?

Magyarországon a gyakorlatban az esetek túlnyomó többségében **Facebook-csoportokban** hirdetünk, admin engedéllyel. Emellett opciók:

- Apróhirdetési oldalak (Jófogás, Vatera)
- Álláshirdetési portálok (gyorsmunkák)
- LinkedIn (professzionális célközönség eléréséhez)
- Facebook fizetett hirdetés (ritkábban, de lehetőség)

> **A gyakorlatból:** A legtöbb UX-cég úgynevezett „házikosztot" üzemeltet toborzásra -- azaz saját maga csinálja, mert a magyar piacon egyelőre nem nagyon van olyan partner, aki értelmes áron csak a toborzást oldaná meg. Aki megcsinálja, az általában az egész kutatást átvállalja.

## A toborzottak nyomon követése

Amikor beérkeznek a válaszok a toborzókérdőívre, szükségünk van egy rendszerre, amivel nyomon követjük az egyes jelöltek státuszát. A legegyszerűbb megoldás egy **táblázat** (Google Sheets vagy Excel).

### Státuszok

A Google Forms-ból érdemes rögtön táblázatot generálni (Create Spreadsheet), és bekapcsolni az e-mail értesítéseket az új válaszokról. Adjunk hozzá egy **státusz** oszlopot a következő értékekkel:

| Státusz | Jelentés | Szín |
|---|---|---|
| Kiesett toborzáson | Nem felelt meg a szűrőkritériumoknak | Szürke |
| Elbírálás alatt | Még nem döntöttünk róla | Sárga |
| Tartalék | Jó jelölt, de most teli vagyunk | Sárga |
| Nem választottuk ki | Elbírálás után elutasítva | Szürke |
| Meghívó kiment | Küldtünk meghívót | -- |
| Ismételt meghívó | Nem reagált, újra küldtünk | -- |
| Időpont leegyeztetve | Van lefoglalt időpont | Zöld |
| Interjú megvolt | Sikeresen lezajlott | Zöld |
| Nem jelent meg | Az interjúnapon nem jelent meg | Piros |

Érdemes feltételes formázást használni: a szürke jelöltekkel nem foglalkozunk tovább, a sárga az aktív teendő, a pirosnál az adott napon kell emlékeztetőt küldeni.

### Hasznos extra oszlopok

- **Név** -- Kérdezzük meg a kérdőívben! Ez hasznos infó.
- **Időpont** -- Az egyeztetett interjú dátuma és ideje (érdemes külön dátum- és időmezőbe tenni).
- **Zoom link** -- Vagy egyéb találkozóhely.
- **Moderátor/felelős** -- Ki interjúztat?
- **Megjegyzés** -- Bármi egyéb.

> **Tipp:** Állíts be feltételes formázást úgy, hogy ha az interjú dátuma a mai nap, a sor piros legyen. Így rögtön látod, kinek kell aznap emlékeztetőt küldeni.

### Levelezés a jelöltekkel

A folyamat során többféle e-mailt küldünk:

- **Meghívó** -- „Szia! Jelentkeztél a kutatásunkra. Szeretnénk meghívni egy interjúra. Itt tudod lefoglalni az időpontodat: [Calendly link]."
- **Visszaigazolás** -- „Köszi! Az interjú időpontja: X, a helyszín/link: Y. Kérjük, hozd magaddal a laptopod [ha szükséges]."
- **Emlékeztető** -- „Szia! Ne felejtsd el, ma interjú van. Csatlakozz hozzánk a következő linken: [link]."
- **Tartalék értesítés** -- „Szia! Köszönjük, hogy jelentkeztél. Most teli vagyunk, de ha lemondás van, szólunk."

### CRM-rendszerek

Ha komolyabb rendszerre van szükségünk a táblázatnál, több lehetőség is adódik:

- **Airtable** -- Rugalmas, vizuális adatbázis, státuszkezeléssel.
- **Zoho CRM** -- Automatikus levelezés beállítható.
- **Odoo** -- Nyílt forráskódú CRM, automatizálással.
- **MiniCRM** -- Magyar fejlesztésű, fizetős rendszer, gyönyörűen beállíthatók benne az automatizációk.

A toborzóplatformoknál (pl. User Interviews, PingPong) ezek a funkciók be vannak építve: csatlakoztatjuk a Zoom- és Calendly-fiókunkat, és az összes többi megy magától.

## Toborzóplatformok használata

Ha nem akarjuk (vagy nem tudjuk) magunk csinálni a toborzást, léteznek erre specializálódott platformok.

### User Interviews (userinterviews.com)

Az amerikai piacon az egyik legnépszerűbb platform, különösen interjúalapú kutatásokhoz. A lényeg:

- Konzumer alany: ~40 dollár/fő
- Szakember (professional) alany: ~80 dollár/fő + az incentíva (~60--70 dollár)
- Megadhatjuk az országot, kort, végzettséget, érdeklődési kört, sőt a munkaköri címet (job title) is
- A szűrőkérdőívet a platformon belül állíthatjuk össze, accept/reject válaszokkal
- Automatikus időpont-egyeztetés (Calendly-integráció)

### PingPong

Magyar fejlesztésű toborzóplatform. Hasonló felépítés: beállítjuk a projekt nevét, leírását, a szűrőfeltételeket (ország, kor, iparág, munkakör), és a platform intézi a toborzást, az időpont-foglalást és az emlékeztetőket.

### Facebook fizetett hirdetés

Bár ritkábban használjuk, elvileg Facebook-hirdetéssel is toborozhatunk: beállítjuk az országot, kort, nemet és az érdeklődési köröket (detailed targeting), majd a hirdetés a kérdőívünkre linkkel. A gyakorlatban azonban az organikus posztolás Facebook-csoportokba (admin engedéllyel) hatékonyabb és olcsóbb.

> **A gyakorlatból:** Mi a legtöbb amerikai projektnél a User Interviews-t vagy a PingPongot használjuk, magyar projekteknél pedig Facebook-csoportokban hirdetünk admin engedéllyel. Nem nagyon szoktunk Facebook fizetett reklámot tolni toborzásra -- a csoportokból jobb minőségű jelöltek jönnek.

## Összefoglalás

A toborzás egy strukturált folyamat: hirdetést adunk fel, szűrőkérdőívvel válogatunk, meghívót küldünk, időpontot egyeztetünk, emlékeztetünk, majd lefolytatjuk az interjút és jutalmazzuk az alanyt. A kérdőív összeállításánál a legfontosabb, hogy ne lehessen kitalálni, kit keresünk -- az emberek hajlamosak „jó" válaszokat adni. Az incentívát mindig a célközönséghez igazítsuk: a kérdőív kitöltéséért kisebb, az interjúért nagyobb, abszolút értékű jutalmat adjunk. A GDPR-megfelelőségre pedig már a toborzás első pillanatától figyelnünk kell, hiszen a kérdőív kitöltése is személyesadat-kezelésnek minősül.

## Ellenőrző kérdések

1. Miért fontos, hogy a toborzókérdőívből ne derüljön ki, pontosan milyen válaszokat keresünk? Milyen technikákat alkalmazhatunk ennek elkerülésére?
2. Milyen különbség van a kérdőív kitöltéséért és az interjúban való részvételért adott jutalom között, és miért lényeges ez a megkülönböztetés?
3. Sorold fel a toborzási hirdetés négy kulcselemét erősségi sorrendben! Melyik a leghatásosabb, és miért?
4. Milyen státuszokat érdemes nyomon követni a toborzási táblázatban, és hogyan segíti ez a munkafolyamatot?
