# 2. Használhatósági tesztelés

Az előző fejezetben áttekintettük a UX és a használhatóság alapjait, megismertük a mérőszámokat és a viselkedési modelleket. Most térjünk rá a legfontosabb gyakorlati módszerre: a használhatósági tesztelésre (usability testing). Ez az a technika, amellyel a leggyorsabban és legkézzelfoghatóbban kideríthetjük, hogy amit terveztünk, azt az emberek valóban tudják-e használni. Nem kell hozzá labor, nem kell hozzá nagy büdzsé -- de kell hozzá módszeresség, és kell hozzá néhány alapszabály, amelyeket ebben a fejezetben járunk végig.

## Mi az a felhasználói teszt?

A felhasználói teszt (usability test) egy kvalitatív vizsgálati módszer, amely a számítógép--ember interakciót vizsgálja szimulált vagy felügyelt kontextusban. Rossz fordításban „felhasználó-tesztelés" -- de ne használjuk ezt a formát, mert nem a felhasználót teszteljük, hanem a szoftvert (erről később bővebben).

Messzebről nézve a felhasználói teszt nem pusztán egy feladat végrehajthatóságát vizsgálja az adott környezetben, hanem azt is, milyen gondolatokat, élményeket vált ki a rendszer használata. Gondolj bele: nem az a kérdés, hogy „működik-e a gomb", hanem hogy mit érez az ember, miközben megpróbálja megnyomni.

## Mi nem a felhasználói teszt?

Először is, a user test **nem véleménykérés**. A teszt rendszerint két „funkcionális" kérdésre keresi a választ:

- Képes-e az ember a szimulált feladat végrehajtására az adott eszközzel?
- Az eszköz az emberi elvárásoknak (expectation) és biológiai adottságainak megfelelően működik-e?

Ezek egy része -- például ha a mobilappban egy fontos gomb hüvelykujjal elérhetetlen -- programozási szempontból nem funkcionális, de UX szempontból annak tekintjük, hiszen a feladat végrehajtási módját befolyásolja.

> **Figyelem!** Hogy kinek mi és mennyire tetszik, azt a felhasználói teszt nem méri jól. Azt se méri jól, mire lenne még szükség, legfeljebb azt, mi hiányzik. Ne keverd össze a tesztet a véleménykutatással -- ez az egyik leggyakoribb hiba, amit kezdő kutatóknál látok.

A user test **nem statisztikai alap**. A kutatási képlet továbbra is:

**kutatás = kvalitatív x kvantitatív**

A kvalitatív mérések felhívják a figyelmet **jelenségekre**, amelyek előfordulását lehet mérni kvantitatív (számszerű) mérésekkel, és amelyek lehetséges magyarázatot adhatnak a már megfigyelt jelenségekre. Így a kvalitatív és kvantitatív vizsgálatok kiegészítik egymást.

Ettől függetlenül, a miértek ismeretében néhány jelenség esetén a gyakorlatban gyakran vonunk következtetéseket kvantitatív ellenőrzés nélkül: ha már a második felhasználó se tudott belépni, mert a login gomb „el van dugva", ennek várhatóan vannak kvantitatív következményei is, egyszerűbb kijavítani, mint mondjuk A/B teszttel lemérni ennek valóságalapját.

## Mi kell a teszthez?

Nézzük meg, mi kell ahhoz, hogy nekiálljunk. Három dolog kell hozzá:

1. **Egy szoftver vagy prototípus** -- amit tesztelünk
2. **Egy tesztalany** -- aki tesztel
3. **Egy megoldandó tesztfeladat** -- amit a tesztalany megpróbál végrehajtani

Ezen kívül jó, ha van nálunk:

- Egy képernyő-felvevő eszköz
- Egy (beszéd)hang felvevő eszköz
- Egy arcfelvevő eszköz
- Papír-ceruza

Az eszközök jó részét biztosítja asztali szoftver esetében egy képernyőfelvevő alkalmazás (például Camtasia), de vannak ingyenes eszközök is. Mobilon iOS esetében reflector típusú szoftvert használunk, de a budapesti UXStudio két webkamerával és egy fakanállal is megoldotta a dolgot -- szóval ne azon akadj fenn, hogy nincs profi felszerelésed.

> **Tipp:** Általánosságban elmondható, hogy ingyenes, beépített szoftverrel és hardverrel is gyönyörűen meg lehet oldani egy tesztelést, de természetesen szakeszközök is tömérdek mennyiségben állnak rendelkezésre. Ilyet ne csináljunk: ne halasszuk a tesztelést azért, mert „még nincs meg a megfelelő eszköz". Egy telefon kamerája és egy csendes sarok is elég az elinduláshoz.

### Beleegyező nyilatkozat

Az európai uniós törvények szerint bármilyen rögzítéshez a tesztalany explicit beleegyezése szükséges. Érdemes kitöltetni egy beleegyező nyilatkozatot.

> **Figyelem!** A magyar adatvédelmi szabályok ennél bonyolultabbak -- adatkezelési nyilatkozat és társai is kellenek. Ha jobb kell, keress egy ügyvédet. Az első tesztünk mindig legyen személyes teszt: a tesztalany, a tesztelendő szoftver és a tesztet vezető moderátor egymás kb. 1 m-es körzetén belül tartózkodjon.

## Kikkel tesztelünk?

Rövid válasz: akit találsz.

Hosszú válasz: a legtöbb hiba nem felhasználó-függő. Bárki, aki **nem ismeri a szoftver működését belülről**, megfelel a célnak.

Ebből rögtön következik az is, hogy **a megrendelő minden esetben alkalmatlan usertesztre tesztalanynak**. Képzeld el: ő ismeri a rendszert, tudja, hol van minden gomb, fejben benne van az egész menüstruktúra. Egyszerűen képtelen nem tudni, amit tud -- olyan, mint nem gondolni a rózsaszín elefántra. Bár szavakban játszhatsz ilyet, a viselkedésed más szinten dől el.

> **Megjegyzés:** A megrendelőt ne engedjük tesztalni, akárhogy is kéri. Nem arról van szó, hogy a véleménye nem számít -- de ő a rendszer belső működéséhez van hozzászokva, és ez megakadályozza, hogy úgy viselkedjen, mint egy valódi felhasználó.

Ritka az a szoftver, amely komoly fogalmi ismereteket feltételez: természetesen érdemes olyannal tesztelni, aki könnyen **bele tudja élni magát a szerepbe**, ha máséba nem, egy **friss gyakornokéba**.

A szerepet elsősorban **a felmerülő probléma határozza meg**: a tesztalany számára a problémának (lesz még róla szó) kell életszerűnek lennie.

> **A gyakorlatból:** A FIBA-n belül vannak olyan részek, amelyet csak szervezőkön tudunk tesztelni (a probléma az ő munkájukban jön csak elő, sportági sajátosság), más dolgokat tetszőleges, a sportok iránt picit is érdeklődő embereken is lehet. Mivel azonban célunk, hogy bárkiből lehessen szervező, aki már látott kosárlabdát, néhány komplex helyzetet kivéve játékosokon, edzőkön, játékvezetőkön és szülőkön is rendszeresen tesztelünk szervezőknek szóló szolgáltatásokat.

### Belső munkatársakkal vigyázzunk

A belső munkatársakkal teszteléssel vigyázzunk: bár rendszerint nincs velük baj, volt, hogy a teszt eredménye -- akaratunk ellenére -- a tesztalany negatív megítélésével járt. Járjunk el körültekintően!

## Hány emberrel tesztelünk?

Rövid válasz: legalább 1.

Hosszú válasz: Nielsen szerint **5 felhasználói tesztből** már a hibák döntő többsége kinyerhető. Ez egy kvalitatív, nem kvantitatív teszt -- nem lesz statisztikai bizonyosságod arról, mennyire jellemző a hiba, amit találtál. A saját minimumszámom a 3, addig nem szeretek nyilatkozni.

> **Megjegyzés:** A Nielsen-féle 5 felhasználós szabály nem azt jelenti, hogy 5 teszt után mindent megtalálsz -- azt jelenti, hogy a legtöbb *súlyos* problémát igen. A ritkább, finomabb hibákhoz több teszt kell, de az 5 felhasználós iteráció meglepően hatékonyan működik a gyakorlatban.

### A RITE-módszer

A Prezi iteratív tesztelésében ha egy hiba előfordul, **akár már egy felhasználói teszt után is változtatnak** a tesztelt prototípuson. Ezt a módszert RITE-módszernek (Rapid Iterative Testing and Evaluation) hívják.

Kérdezheted: egy? Igen, például ha a feladathoz be kéne jelentkezni, de te kompletten lehagytad a bejelentkezés gombot, ez már egy felhasználóval kiderül. Ennél sokkal finomabb okosságokat is meg lehet tudni akár egyetlen felhasználótól, ugyanis beszéltetni fogjuk őket: **arra vagyunk kíváncsiak, milyen gondolatok, érzések játszódnak le egy ember fejében használat közben**, és hasonló jelek kiválthatnak hasonló gondolatokat más emberekben is -- érezni fogod!

> **A gyakorlatból:** A MÁV Start jegyautomatáinak tervezésekor pontosan ezt a RITE-módszert alkalmaztuk a projekt második felében. Minden egyes nap munkába menet előtt egy kávézóban találkoztunk a tesztalannyal, végigvittük a tesztforgatókönyveket, ott helyben elemeztünk, aztán a tervező a munkahelyén megpróbálta úgy módosítani a prototípust, hogy a felmerült problémák a következő alanynál már ne jöjjenek elő. Így tesztelte több mint 30 felhasználó, készült 15 különböző prototípusváltozat, és a végén négy hosszú UX-elemzést írtunk a MÁV-nak. Az iteráció ereje az volt, hogy minden egyes nap kicsit jobb lett az automata -- nem a végén egyszer jöttünk rá, hogy baj van, hanem menet közben, folyamatosan javítottunk.

## Mit tesztelünk?

Első körben mindig **kész szoftvert teszteljünk**: legyen az a saját vagy piaci konkurenciánk szoftvere.

Később akár egy rakás kézi rajz vagy színes cetli felett is tudunk tesztelni (ahogy ezt például Könczöl Eszter a GE-nél tette), sőt, rendszeresen tesztelünk egyetlen vázlatos rajzból álló prototípusokat is.

> **Tipp:** Nem csak szoftvert lehet tesztelni, de elsőre érdemesebb azzal kezdeni. A papírprototípus-tesztelés külön készségeket igényel -- a lényeg, hogy a tesztalany interakcióját szimuláld, ne csak mutogasd a képernyőket.

## Mi az a tesztfeladat?

A „kattintgassa meg" nem user test. Ilyet ne csináljunk.

Egy user testhez mindig tartozik egy vagy több, a szoftver szempontjából **valós életbeli feladat**. A szoftver szempontjából nem valós életbeli az a feladat, amely a szoftver belső működését feltételezi. Gondolj bele: ha a felhasználó nem tud arról, hogy az adott funkció létezik, nem is fogja keresni. A mi dolgunk, hogy olyan helyzetet teremtsünk, amelyben természetesen szüksége lenne rá.

> **Megjegyzés:** Ahogy Laufer László fogalmazott egy UX Breakfast előadáson: „Ha a bejárati ajtó mellett lévő csengőt kéne teszteltetnem, két szót biztos nem ejtenék ki teszt közben: *bejárati ajtó* és *csengő*."

Ez a mondat tökéletesen összefoglalja a lényeget: a tesztfeladatnak a **felhasználó problémáját** kell leírnia, nem a szoftver megoldását. Ez a leggyakoribb hiba, amit tesztfeladat-írásnál látok: a kutató a rendszer nyelvén fogalmaz ahelyett, hogy a felhasználó élethelyzetéből indulna ki.

### Tipikus tesztfeladatok

Nézzünk néhány példát:

- Nagyanyjához utazik péntek munka után Kaposvárra. Vásároljon vonatjegyet (tesztcélpont: MÁV Start jegyvásárló rendszer)
- Lejár a bérlete ötödikén, vásároljon újat (tesztcélpont: BKV jegyautomaták)
- X dolgot akar csinálni. A Google-ba beírta, hogy X, az ön által most tesztelt honlap jött fel első találati eredményként. Próbálja meg vele megoldani X-et! (bármi, ami például 30 napos próbaverziós, X például lehet képernyőfelvevő userteszthez)

A jó tesztfeladat tartalmaz valamennyi **konkrétumot**, de nem túl sokat. Például ha egy e-boltot tesztelünk (GRoby, Tesco Online), nem árt egy bevásárlólistát előállítanunk, vagy legalábbis belőni mondjuk egy elkészítendő ételt. Azt is lehet, hogy ezt az alany hozza magával (például tegnap esti bevásárlás megismétlése online).

> **A gyakorlatból:** A MÁV Start jegyautomatáinak tesztelése előtt bementünk a Keleti pályaudvar pénztárai mögé, és végighallgattunk több mint 200 valós beszélgetést utasok és pénztárosok között. Ezeket mind felírtuk, kategorizáltuk, és ebből állítottuk össze a tesztelési forgatókönyveket: na, ezeknek az élethelyzeteknek az automatán is meg kell felelni ahhoz, hogy azt mondjuk, jó. Nem mi találtuk ki a tesztfeladatokat a fejünkből -- az utasoktól hallottuk, mi az, amire ténylegesen szükségük van. Ha teheted, te is így csináld: előbb figyeld meg a valós használatot, és abból építsd fel a tesztfeladatokat.

### Kerettörténetek

A tesztfeladatokat néha **kerettörténetekbe** szervezzük. A kerettörténetnek van

- egy **főszereplője**, akit a tesztalany játszik el
- egy **célja**, amit meg akar valósítani
- **kontextusa / korlátozó tényezői**, amik a teszt kereteit biztosítják (például ha még nem vagyunk bent a Google-ben az adott feladatra, viszont nem konkurenciatesztet akarunk végezni, játszhatjuk, hogy a mi oldalunk jött be első találatként)

Ez adja a **szimulációt**. Lehetséges, hogy a feladat nagyon is valós, ekkor **felügyelt** környezetnek hívjuk ezt, ahol az elemek megfigyelhetőek. Példa: ha az illetőnek tényleg kell vennie egy BKV bérletet mostazonnal.

### Hány tesztfeladat? Milyen hosszúak legyenek?

Az emberi figyelem korlátai miatt **egy jó teszt felnőttekkel maximum nettó 20 perces**. Egy prototípus-teszt van, hogy 3 perc alatt lezajlik, máshol 4--5 feladat is végrehajtható ennyi idő alatt, de van, hogy egyetlen feladatra is túl korlátozónak tűnik ez a kitétel.

> **Tipp:** Ne felejtsd el, hogy egy jól használható szoftverben a folyamatokat amúgy is érdemes maximum negyed óránként otthagyható részfeladatokra bontani, pont az említett figyelemkorlátok miatt. Ha nem férünk bele, gondolkozzunk, jól van-e ez így!

## Hol tesztelünk?

**Bárhol.** Rendszeresen tesztelünk kosárlabdameccseken állva, vagy épp a Gozsdu udvar környékének kocsmáiban, első tesztre azonban azt javasoljuk, lehetőleg ülve, egy asztal környékén, ne túl zajos környezetben kerüljön sor -- az ugyanis zavarná a felvételt.

Kiválóan megfelel tetszőleges meetingszoba, konyha, kávézó vagy pláza foodcourt asztalsora (csúcsidőn kívül).

> **A gyakorlatból:** A MÁV-automaták tesztelésénél a Kreában tanítottam, és felmerült a kérdés: hol lehetne egy interaktív rendszer tömeges, élő használatát este öt és hét óra között megfigyelni? Hát adott a válasz -- a Nyugati pályaudvaron pont akkor van csúcsidő. Kimentünk a diákokkal és végignéztük, hogyan használják az emberek a jegyautomatákat. A diákok mindenféle következtetéseket vontak le, gondolatban újratervezték a felületet.

## Hogyan tesztelünk? -- A három ökölszabály

Beszéljünk arról, hogyan is zajlik maga a tesztelés. A user tesztelés három ökölszabálya -- ezeket vésd az agyadba:

1. A szoftvert teszteljük, nem a user-t
2. Nincs feedback -- pókerarc
3. Gondolkodtasd hangosan

Térjünk ki egyesével ezekre.

### A szoftvert teszteljük, nem a user-t

A usertesztelés egy zárt ajtós pszichológiai viselkedésteszt, amely a felhasználó--gép interakciót teszteli. Óhatatlanul kiderülnek a felhasználókról is dolgok. De: **egy userteszten minden csak és kizárólag a szoftver hibája lehet**. Mindig gondolj bele: amibe egy felhasználó belebukik, belebukhat másik is!

Ezt minden esetben **mondjuk is el** a tesztalanynak:

> *„Itt minden hiba a szoftver lelkén szárad, ha valami nem megy, az a szoftvert minősíti, semmiképp sem engem vagy téged, itt és most nem tudsz hibázni."*

Sokan mondják, hogy az első feladatok között valami szándékosan lehetetlent (de nem lehetetlennek látszót) kell adni, hogy a tesztalany természetesnek érezze a hibázást.

> **A gyakorlatból:** Olyat is tanácsolnak, hazudjuk azt, hogy a szoftvert nem mi terveztük, sőt, közünk nincs a céghez -- bár ez az amerikaiaknál tényleg fontos lehet, az őszinteség híve vagyok: mondjuk azt, hogy „tudjuk, hogy teli van hibákkal, amit most fogunk cserélni / a fejlesztés már előbbre tart", esetleg „a prototípusra nem volt túl sok idő, ne számíts rá, hogy bármi is működik benne". Az esetek többségében a helyzet valóban ez eleve.

### Nincs feedback -- pókerarc

Valós élethelyzetet szimulálunk: egy valós élethelyzetben nincs senki, aki kijavítaná a felhasználót, segítene neki, vagy a kérdéseire válaszolna.

**Ne válaszoljunk a felhasználó rendszert érintő kérdéseire érdemben!** Ha kérdez, nyugodt hangon figyelmeztessük, hogy a **tényleges felhasználók mögött se fog ülni senki**. Esetleg kérdezzünk vissza: „te mit tennél ebben az esetben?", „szerinted miért van ez így?", „számodra ez hogy lenne logikus?", „te mire számítanál?"

> **Figyelem!** Üljünk úgy, hogy a felhasználó ne lássa a testbeszédünket. A testbeszédünk sok mindent elárulhat arról, hogy mi az, ami nem az elképzeléseink szerint alakul. Ha a fogszívást, felnyögést sikerül is megúsznunk, testünk még ezer módon kommunikálhatja meglepődésünket. **A legjobb, ha a felhasználó mögé ülünk úgy, hogy még lássuk az általa használt felületet, és halljuk, amit mond**, de ő ne lássa a mi arckifejezésünket.

**Ne terelgessük a felhasználót!** Ha a felhasználó nem találja meg magától a dolgokat, az bizony usability hiba. Tudom, hogy nehéz -- ott ülsz mögötte, látod, hogy a megoldás ott van két centire a kurzorától, és az egész tested azt üvölti, hogy „ott van, ott van!" De nem szólhatsz. Ez a szabály.

**Hagyjuk a felhasználót hibázni!** Amíg szó szerint életveszélyes helyzet nem áll elő, a felhasználó igenis bukdácsoljon -- más is fog, pont ezért teszteljük.

**Az is rendben van, ha nem sikerül megoldani a feladatot!** Ez is egy teszteredmény! Ne akarjuk minden áron megoldatni!

> **Tipp:** Persze, ha kevés felhasználóval van csak lehetőségünk tesztelni, és a tesztalany önmagától már semmiképp nem jutna tovább, néha kénytelenek vagyunk súgni. Ekkor az adott **tesztfeladatot könyveljük el bukottnak**, mintha a felhasználó nem tudta volna megoldani, és dolgozzunk a megoldáson a következő iterációban!

A kérdések megválaszolása is olyasmi, amit előre illik közölni a tesztalannyal. Például így:

> *„Ha kérdésed van, kérdezz bármikor bármit nyugodtan, és ha tehetem, válaszolok. Kérlek, vedd figyelembe viszont, hogy a való életben se ül a felhasználók mögött senki, így néhány kérdésedre esetleg nem fogok tudni válaszolni, a kérdésfelvetéseid viszont nagyon is fontosak számunkra."*

### Gondolkodtasd hangosan

A felhasználói élmény azon gondolatok (és érzések) összessége, amit egy felhasználó a használat során átél. Ahhoz, hogy képet kapjunk arról, mi is ez az élmény, ami belül történik, a leginkább célra vezető mód, ha **valós időben, folyamatosan beszéltetjük róla a tesztalanyt**.

Mondjuk el neki a teszt elején:

> *„Szeretnélek megkérni, hogy amennyire csak lehet, a teszt folyamán gondolkozz hangosan: mondd, mire nézel épp, mit keresel, mit próbálsz elérni, mit gondolsz, mit érzel. Ezzel sokat segítesz a problémák megértésében."*

Amennyiben a felhasználó már jó ideje csendben van, esetleg feltehetünk neki kérdéseket:

- Most min gondolkodsz?
- (Váltásnál) Mit látsz most?
- Mit szeretnél elérni?
- Mit keresel?

> **Figyelem!** A kérdések megfogalmazásával csínján kell bánni, **feleslegesen ne zökkentsük ki a felhasználót gondolatmenetéből**. Próbáljuk meg inkább megtalálni a réseket.

Különösen **prototípustesztelésnél** (például papírprototípus) hasznos, ha a felhasználót **megkérdezzük a művelet elvégzése előtt, mire számít**. Ha például azt mondja, ő erre a gombra kattintana, megkérdezhetjük, mi az, amire számít, mi fog történni, majd miután eljátszottuk az interakciót (például lapot cseréltünk), megkérdezhetjük, mi az, amit szerinte lát, és hogy ez mennyire van összhangban azzal, amit gondolt.

## Tesztelés extrém körülmények között

Beszéljünk egy kicsit arról is, hogy a tesztelésnek nem kell mindig a „normál" felhasználói helyzetekre szorítkoznia. Sőt -- az igazán értékes eredmények gyakran éppen a szélsőséges helyzetekben jönnek elő.

> **A gyakorlatból:** A MÁV-automaták tesztelésénél egészen extrém forgatókönyveket is kidolgoztunk. Volt egy „nagyi teszt", ahol 60 év felettiekkel próbáltuk ki az automatát (65 év felett egyébként nem teszteltünk, mert ingyenes a közlekedés, de helyjegyet azért kell venniük). De ennél is tovább mentünk: a harmincéves barátainkat leitattuk -- a harmadik sör és az első rövid után odaadtuk nekik a prototípust, hogy na, most kéne venni egy jegyet. Voltak pszichológiai stressztesztjeink is, ahol az embereket abba a rendkívül idegesítő állapotba hoztuk, hogy „szia, bent áll a vonat, egy perced van jegyet venni!" -- elindítottuk a stoppert, és próbáltuk elérni, hogy tényleg úgy érezze, most indul a vonat és nagyon ideges legyen. Ezt kombináltuk is: részegen, halálidegesen, 60 év felett -- ha így is meg tudod venni a jegyet, akkor az automata valószínűleg működni fog kevésbé terhelő körülmények között is.

## Jutalmazás

Mint minden felhasználókutatási feladatnál, itt is érdemes a tesztalanyt a teszt végével megköszönni. Erre tipikusan pénz, utalvány, céges merch vagy élelmiszer való -- e-commerce körökben megszokott, hogy egyszerűen a teszt során megvásárolt dolgokat ingyen odaadjuk (például kártyafeltöltéssel, vagy 100%-os kuponnal).

> **Megjegyzés:** A felhasználó tesztelés nem nyereményjáték: nem pusztán a „sikeres" tesztfeladat végrehajtást jutalmazzuk, hanem mindenkit, aki megpróbálta! Abból tanulunk a legtöbbet, akiknek kevésbé, sőt, akiknek egyáltalán nem sikerül! Az is információ persze, ha valami elsőre megy...

## Az eredmények tálalása

Az eredmények tálalására első alkalommal a **„ragasztós" módszert** javaslom. Mit csinálsz ilyenkor? A felvétel egy fogyasztásra előkészített (például összevágott, feliratozott, 10 percbe maximalizált) változatát elindítjuk a kivetítőn/monitoron, miközben minden érdekelt felet -- ügyfelet, programozókat -- a helyiségbe terelünk és olyan székbe ültetjük, amiből a kétoldalú ragasztó hatására nem lehet hamar felállni. Mozidélután!

> **Tipp:** Készüljünk fel: **az első nagy felfedezések élőben végignézése előtt mindenkinek jobb dolga lenne**. E-mailben elküldeni felesleges, kilinkelni felesleges -- szinte kizárólag az explicit végignézetés segít. Tapasztalatból mondom: az e-mailben küldött videót senki nem fogja megnézni. A „majd este megnézem" azt jelenti, hogy soha.

A helyzet utána rendszerint azonnal és drámaian változik, főleg, ha több tesztalanyunk is ugyanarra az eredményre jutott. Ezután már el lehet gondolkodni a teszteredmények írásbeli összefoglalásán, a főbb felfedezések, az alanyok szájából elhangzó kulcsmondatok kiemelésén, a „beletekerős" videókivonatok készítésén.

## Hasznos források

- **Steve Krug: Rocket Surgery Made Easy** -- az elsődleges információforrás a témában. Ingyenesen letölthető mellékletei (beleegyező nyilatkozat, tesztforgatókönyv) különösen hasznosak, ezeket Németh Ádám magyarra is lefordította.
- **UXPin: Usability Test Kit** -- egy ingyenesen elérhető angol nyelvű segédanyag-gyűjtemény.
- A Spotify-nál Lin Wang által vezetett guerilla teszt jó példa arra, hogyan lehet informálisan, gyorsan, mégis értékes eredményeket kihozni.
- Az Ubuntu 2010-ben végzett Rhythmbox tesztje ennél hivatalosabb formátumú -- érdemes megnézni összehasonlításként.

> **A gyakorlatból:** A Steve Krug-féle beleegyező nyilatkozatot és tesztforgatókönyvet érdemes kiindulópontként használni. A magyar adatvédelmi szabályok ennél bonyolultabbak -- adatkezelési nyilatkozat és társai is kellenek --, de általában jó lesz. Ha jobb kell, keress egy ügyvédet. Jogi garanciát az interneten senki nem vállal.

## Összefoglalás

A használhatósági tesztelés a felhasználókutatás legközvetlenebb és leggyorsabban megtérülő módszere. Három dolog kell hozzá -- egy szoftver, egy tesztalany és egy életszerű feladat --, és ha betartjuk a három ökölszabályt (a szoftvert teszteljük, nem a user-t; pókerarc; gondolkodtass hangosan), már egyetlen tesztből is rengeteg tanulságot vonhatunk le. A módszer igazi ereje az iterációban rejlik: tesztelj, javíts, tesztelj újra. Nem a tökéletességet keressük, hanem a következő javítandó problémát.

## Ellenőrző kérdések

1. Fogalmazz meg egy tesztfeladatot egy általad választott weboldalhoz vagy alkalmazáshoz úgy, hogy az ne tartalmazza a szoftver belső fogalmait (navigációs elemek, gombok nevei) -- csak a felhasználó élethelyzetét és célját!

2. Egy kollegád a teszt közben segít a tesztalanynak, amikor az elakad, mondván: „nem akarom, hogy frusztrált legyen". Miért probléma ez, és mit mondanál neki?

3. Három tesztalanyod volt, és mindhárman ugyanazon a ponton akadtak el. A fejlesztő azt mondja: „három ember nem statisztika". Hogyan érvelnél amellett, hogy mégis érdemes foglalkozni a problémával?

4. Tervezd meg egy rövid (max. 20 perces) usability teszt vázlatát: válassz szoftvert, határozz meg 2--3 tesztfeladatot kerettörténettel, és írd le, mit mondanál a tesztalanynak a teszt elején!
