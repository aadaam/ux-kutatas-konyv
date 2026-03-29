# 1. A UX és használhatóság alapjai

Az előszóban már szó esett arról, hogy a felhasználókutatás (user research) nem öncélú tevékenység -- célja, hogy jobban megértsük az embereket, akiknek tervezünk. Ebben a fejezetben tisztázzuk azokat az alapfogalmakat, amelyek nélkül nem tudunk érdemben beszélni sem kutatásról, sem tervezésről. Definiáljuk, mit értünk felhasználói élmény (user experience) és használhatóság (usability) alatt, megismerjük a mérésükhöz használt eszközöket, és áttekintünk három viselkedési modellt, amelyek segítenek értelmezni, amit a kutatások során látunk.

## Mi az a felhasználói élmény?

A felhasználói élmény (UX) fogalmát sokféleképpen lehet meghatározni, de van egy definíció, amelyet különösen hasznosnak tartok, mert nem csak leíró, hanem generatív -- tehát segít újat kitalálni:

> **Megjegyzés:** A felhasználói élmény azon érzések és gondolatok összessége, amely egy emberen keresztül megy egy rendszerrel való kapcsolat során.

Ez a meghatározás azonnal elárul néhány fontos dolgot. Először is: pszichológiai jelenségről beszélünk. Az érzések és gondolatok a pszichológia területéhez tartoznak, nem a technológiáéhoz. Másodszor: beszélhetünk egyszeri UX-ről -- mondjuk most elővettem egy alkalmazást és kapcsolatba léptem vele --, de beszélhetünk hosszú távú UX-ről is. Milyen érzés 10--15 évig Gmail-felhasználónak lenni? Hogyan változnak az érzéseim és gondolataim a Gmail-lel szemben az évek során?

Harmadszor -- és ez nagyon fontos -- az érzések és gondolatok erősen egyén- és szituációfüggők. Lehet, hogy rossz napod van, és ugyanaz a rendszer teljesen más élményt ad, mint amit amúgy kapnál. Nem tudsz figyelni, máshol járnak a gondolataid. Ugyanakkor azt látjuk, hogy nagy számokkal, statisztikailag ezek jól konvergálnak. Ha megcsinálom 100--200 emberrel ugyanazt, és mindannyiukat mondjuk feldühíti egy weboldal, akkor valószínűleg mégiscsak a weboldallal van baj.

> **A gyakorlatból:** A UX igazából az a lenyomat, ami a rendszer használatával keletkezik az ember fejében. Ha elég sok ember fejében hasonló lenyomat keletkezik, az már nem az egyén „hibája" -- az a rendszer tulajdonsága.

## UX kutatás és UX tervezés

Ezzel a lenyomattal alapvetően két dolgot tudunk kezdeni.

Az egyik, hogy **kutatjuk**: mit éreznek és gondolnak az emberek, amikor felmennek egy weboldalra, vagy egyáltalán azzal a tárgykörrel kapcsolatban, amivel a rendszer foglalkozik. Ezt hívjuk UX kutatásnak, felhasználókutatásnak (user research).

A másik, hogy **tervezünk**: megpróbáljuk ezeket az érzéseket és gondolatokat befolyásolni egy létező (vagy majdan létező) szoftvertermékkel. Megpróbáljuk az élményt mássá tenni. Ez a UX tervezés (UX design).

Egyik sem létezik a másik nélkül. Az a kutatás, ami nem befolyásol semmit, az eléggé fióknak készült kutatás. De a tervezés sem működik kutatás nélkül, mert amit megterveztünk, azt utána le kell kutatni -- vajon tényleg jobb lett?

> **Tipp:** A „zöldmezős beruházások" sem igazán zöldmezősek. Mindig van egy alaphelyzet, amiből kiindulunk. Gondolj Henry Ford híres mondására: „Ha megkérdeztem volna az embereket, azt mondták volna, hogy gyorsabb lovakat akarnak." De a kutatás valódi kérdése nem az, hogy „milyen lovat akarsz", hanem az, hogy „mi a problémád a helyváltoztatással". UX kutatni majdnem mindig lehet.

## A két fő módszertani irány

A kutatás két fő módszertanra fókuszál:

1. **Interjú alapú, kontextuális megközelítés** -- terepinterjúkon, etnográfiai megfigyeléseken keresztül perszónákat (persona) és felhasználói utakat (user journey) építünk fel. Ezek megmondják, hogyan gondolkodnak az emberek, milyen szükségleteik, céljaik, problémáik vannak, és azok hogyan változnak az időben. Ez alapján tervezünk valamit.

2. **Használhatósági tesztelés** (usability testing) -- amit megterveztünk, azt megnézzük: mennyire illeszkedik abba a problémakörbe, amit megoldunk? Mennyire tudják használni az emberek?

## UX és használhatóság -- ugyanaz vagy mégsem?

Mi köze van a UX-nek a használhatósághoz? Egyfelől különbözik, másfelől a szempontunkból majdnem ugyanaz. Lássuk, miért.

Vegyünk két mobilalkalmazást: a NetPincért és a Tindert. Melyik használható? A válasz nagyon attól függ, hogy éhes vagy-e vagy csajozni akarsz. Ha enni akarok, a NetPincér segít -- lehet, hogy csúnyább, de előbb tudok rajta ételt rendelni, mint a Tinderen. Ha pedig randizni akarok, a Tinderen jobb esélyeim vannak, mint a NetPincéren -- hiába van rengeteg futárlány.

> **A gyakorlatból:** Egy szobatársam beleszeretett egy pizzafutárlányba, ami miatt mindig arról a helyről rendelt. Egyetlen probléma volt: a helynek több futára is volt, és majdnem három hetet kellett várnia, hogy ugyanaz a lány jöjjön ki, és megkérdezhesse, eljön-e randira. (Sajnos volt barátja.) Használható mindkét app mindkettőre -- csak viszonylag kényelmetlen. Más a felhasználói élmény, ha nem arra van „kipécézve".

A felhasználói élmény tehát nagyon függ attól, hogy mire akarom használni, milyen kontextusban, és mi az én háttértudásom. Az ember mindig adott célra próbálja használni a rendszereket -- soha nem „internetezünk" öncélúan. Még a facebookozás is arról szól, hogy tájékozódom a hírekről, vagy közösségben próbálom érezni magam. Vannak érzelmi célok, információszerzési célok, tranzakciós célok.

Innentől a felhasználói élmény és a használhatóság majdhogynem azonos fogalom.

## A felhasználói élmény rétegei

A felhasználói élmény három-négy szinten állapítható meg:

1. **Funkcionális szint** -- egyáltalán nyújtja-e a rendszer azt, amire szükségem van? Ez az, amit interjúkkal tudunk feltárni.
2. **Megbízhatósági szint** -- megbízhatóan nyújtja-e? Gondoljunk a buszokra: jön-e a busz időben? Ez egy megbízhatósági faktor.
3. **Használhatósági szint** -- kényelmesen, hatékonyan nyújtja-e?

> **Megjegyzés:** A UX-esek (UX designerek) jellemzően a használhatósági réteggel foglalkoznak. A felhasználókutató viszont a funkcionális réteggel is dolgozik -- az ő dolga, hogy azzal foglalkozzon, milyen funkcionalitásra van szükség az adott pillanatban.

## A használhatóság ISO-definíciója

A használhatóságot az ISO 9241-es szabvány definiálja, és három összetevőt különböztet meg:

| Összetevő | Mit mér? | Hogyan mérjük? |
|---|---|---|
| **Hatékonyság** (efficiency) | Mennyi idő alatt végez a felhasználó egy feladattal? | Időméréssel |
| **Hasznosság** (effectiveness) | A felhasználók hány százaléka teljesíti a feladatot? | Sikerráta, hibaszám |
| **Elégedettség** (satisfaction) | Mennyire elégedett a felhasználó? | Kérdőívvel |

### Hatékonyság -- az idő pénz

A hatékonyság alapvetően egy időfogalom. A legtöbb esetben visszavezethető arra, hogy mennyi időt vett el a feladat kezelése -- illetve mennyi *felesleges* időt. Üzleti szoftverek esetén majdnem minden időt feleslegesnek tekintünk, hiszen azt nem más hasznos munkára fordítja a felhasználó.

A hatékonyság legjellemzőbb mérőszáma a **tranzakcióidő** (transaction time): mennyi idő alatt végez a felhasználó egy vásárlással, mennyi idő alatt ad el egy pénztáros egy jegyet?

> **A gyakorlatból:** A MÁV-nál az utasok egyszerre „támadnak" -- nagyjából egy negyedórás blokkban esik be az összes utas, aki mondjuk a 15:15-ös vonattal szeretne menni. 14:59-kor még nincs a pályaudvaron, 15:00-kor robog be az első fecske, és 15:14-kor még valaki megpróbál odafurakodni a pénztárhoz. A tranzakcióidő határozza meg, hány pénztárosra vagy automatára van szükség ahhoz, hogy mindenki jegyhez jusson.

A hatékonyság további mérőszámai:

- **Képernyőnként eltöltött idő** -- például a számlakérés sokkal több időt vehet igénybe, mint a sima fizetés
- **Visszamenetelek száma** -- hányszor kell valamit újrakezdeni? A böngészőben a vissza gomb valójában egy hibajelző gomb: ha vissza kellett menni, az azt jelenti, hogy egyenes flow-ban nem sikerült megépíteni a felületet
- **Ideális abszolút idők** -- navigációs felülettel nagyjából 10 másodperc alatt kell végezni, döntéshozatalra másfél perc, egy feladatblokkra 10--20 perc (maximum fél óra), mert ennyit tudunk egyszerre koncentrálni

### Hasznosság -- hányan jutnak célba?

A hasznosság egy százalékos fogalom. A központi kérdése: az egyes lépéseket a felhasználók hány százaléka teljesítette segítség nélkül?

Gondoljunk egy webshopra, ahol a felhasználó végigmegy a következő lépéseken: főoldal, keresés, termékoldal, kosár, pénztár, fizetés. Minden lépésnél kérdés, hogy hányan jutottak oda, hánynak kellett segítség, és hányszor dobott hibaüzenetet a rendszer.

> **A gyakorlatból:** A webshop tölcsér (funnel) szépen megmutatja a veszteségeket: mondjuk kilenc ember érkezik a főoldalra, a keresőig hat jut el, a termékoldalra négy, kosárba hárman raknak, pénztárba ketten jutnak el, és a végén a kilencből csak egy fizet. A kérdés az, hogy az egyes lépésekben hogyan tartjuk meg a lehető legtöbb embert.

A hasznossághoz kapcsolódó mérőszámok:

- **Sikerráta** (success rate) -- a legfontosabb: jött 100 ember Google-ből, hányan vásároltak?
- **Hibaüzenetek száma** -- hányszor fut hibára a rendszer? Érdemes a fejlesztőket megkérni, hogy naplózzák ezeket
- **Ügyfélszolgálati kérések száma** -- ha annyi kérésünk van, hogy nem elég egy ügyfélszolgálatos, hanem kettő-háromnak kell műszakban lenni, az kétszer-háromszor annyi bér. Ráadásul amíg az ügyfélszolgálatot hívják, addig a vevő nem vásárol
- **Súgóhasználat** -- kiesett idő, amikor a felhasználó böngészi, hogyan működik a rendszer (de ha jó a súgó, annak azért örülünk)

### Áttételes mérőszámok

Két áttételes mérőszám különösen fontos:

**Tanulhatóság** (learnability): ahogy használom a rendszert újra és újra, mennyivel leszek hatékonyabb? Mennyivel hasznosabb számomra? Ez egy áttételes mérték, ami az idővel változó hatékonyságot és hasznosságot mutatja.

**Hibázás kritikussága** (error severity): mit tudok és mennyire elrontani? Itt két dimenziót nézünk: mennyire súlyos a hiba (ha tényleg felrobban egy atomreaktor, ahogy tette ezt többször -- az nagyon para), és hány embert érint?

> **Megjegyzés:** A hibázás priorizálásánál sajnos gyakran közgazdasági döntések születnek. A súlyosságot és az érintettek számát összeszorozzák, és ebből jön ki a prioritás. Ennek következtében az akadálymentességi hibák -- amelyek viszonylag kevés embert érintenek, mondjuk 1--2%-ot -- alacsony prioritást kapnak, pedig az érintettek számára kritikusak lehetnek.

A harmadik áttételes mérőszám a **megjegyezhetőség** (memorability): ha ritkán kell egy funkcióhoz nyúlni -- mondjuk havi jelentés --, mennyire emlékszik az illető, hogyan kell csinálni?

## Az élmény mérése kérdőívekkel

Az objektív mérőszámok -- idő, sikerráta -- jól mérhetők, de maga a felhasználói élmény szubjektív dolog. Hogyan mérjük?

### Az elégedettség egyszerű mérése

A legegyszerűbb megoldás az, amit a Burger Kingben is használnak: három-öt kis figura különböző arckifejezéssel, a nagy mosolytól a szomorú arcig. Elégedettségmérésnek egész jó, de nyilván nem az egyetlen lehetőség.

### Net Promoter Score (NPS)

A klasszikus marketing mérés az NPS: „Mennyire valószínű, hogy ajánlaná ismerőseinek?" Nullától kilencig mérik a skálát -- mindig nullától kilencig, nincs rövidített változat.

A kiértékelés egyszerű: akik 0--5-öt adtak, azok az elégedetlenek (detractor), akik 8--9-et, azok a „reklámozók" (promoter). A reklámozók arányából kivonjuk az elégedetlenek arányát, és megkapjuk az NPS-t. Bármi nulla felett már egész jó -- a lényeg, hogy többen szeressék a terméket, mint ne.

> **Figyelem!** Az NPS klasszikus marketing mérés, nem kifejezetten UX-es mérőszám. Vannak helyzetek, ahol egyszerűen értelmetlen: „Mennyire ajánlaná a Microsoft Windowst ismerőseinek?" Normális emberek nem ajánlgatnak egymásnak operációs rendszert. Bizonyos termékeknél a rendszeres használat sokkal érdekesebb kérdés, mint az ajánlás.

### A NASA Task Load Index (TLX)

A NASA a mentális terhelés mérésére fejlesztett ki kérdőívet, a TLX-et. Ez méri, mennyire volt agyilag fárasztó a feladat, mennyire volt fizikailag fárasztó, érzett-e időnyomást a felhasználó, valamint szubjektív hatékonyságot, hasznosságot és frusztrációs szintet. Atomerőművek vagy űrkompok kezelőfelületeinél teljesen ésszerű a NASA TLX-szel mérni -- mi viszont egy elterjedtebb kérdőívet fogunk használni.

### A Rendszerhasználhatósági Skála -- RHS (System Usability Scale, SUS)

Ez az a kérdőív, amelyről tudományosan több tucat publikáció bizonyítja, hogy nyelvek között stabil, helyzetek között stabil, emberek között stabil -- tehát viszonylag jól korrelál azzal, hogy tényleg milyen a felhasználói élmény.

Az RHS tíz állítást tartalmaz, amelyeket 1-től 5-ig pontozunk (1 = „egyáltalán nem értek egyet", 5 = „teljesen egyetértek"):

1. Szívesen használom ezt az alkalmazást rendszeresen.
2. Az alkalmazást szükségtelenül bonyolultnak találtam.
3. Az alkalmazást könnyen használhatónak éreztem.
4. Úgy gondolom, az alkalmazás használatához technikai személyzetre lenne szükségem.
5. Az alkalmazás funkcióit jól integráltnak találtam.
6. Úgy gondolom, az alkalmazásban túl sok a következetlenség.
7. Szerintem a legtöbb ember nagyon gyorsan megtanulná az alkalmazás használatát.
8. Nehézkesnek találtam az alkalmazás használatát.
9. Magabiztosnak éreztem magam az alkalmazás használatakor.
10. Sok mindent kellett megtanulni az alkalmazás használatának megkezdéséhez.

> **Megjegyzés:** Figyeld meg, hogy a páratlan állítások pozitívak, a párosak negatívak. Ez szándékos: ha valaki lustán végigkattintja 5-5-5-5-5-re, közepes értéket kap, nem kiugróan jót. Ezzel kiszűrjük azokat, akik nem figyelnek oda a kitöltésre. Érdemes minden kérdőívet ilyen ellentétpárokkal összerakni.

**Az RHS kiértékelése:**

1. Pozitív állításoknál (páratlan sorszám): válasz mínusz 1
2. Negatív állításoknál (páros sorszám): 5 mínusz a válasz
3. Az így kapott értékeket összeadjuk (maximum 40 pont)
4. Az összeget beszorozzuk 2,5-del, hogy egy 0--100-as skálát kapjunk

> **Figyelem!** Az RHS-pontszám nem százalék -- hiába mozog 0 és 100 között. Az eloszlása aszimmetrikus, és a szorzó miatt nem feleltethető meg közvetlenül százalékos értéknek.

Nagyjából 9000 teszt alapján az átlagos RHS-pontszám **67--68 pont** körül van -- ez az átlagos felhasználói élmény. Ez az érték meglepően stabil: bár modernizálódunk, az emberek mindig az aktuális mezőnyhöz viszonyítanak.

| RHS-pontszám | Osztályzat | Értelmezés |
|---|---|---|
| 85+ pont | A (ötös) | Kiváló -- a nagyon jó szoftverek szintje |
| 72 pont | B (négyes) | Jó |
| 67 pont | C (hármas) | Átlagos |
| 55 pont | D (kettes) | Gyenge |
| 50 pont alatt | F (egyes) | Többen rosszabbnak ítélték, mint jónak |

> **A gyakorlatból:** Egy tizedesjegyet arrébb csúsztatva a hotelértékelésekre ismerhetünk: a 8,5 pontos hotel az, amibe szívesen szállunk meg, a 6,5 pontos az, amit még talán hajlandóak vagyunk használni -- és ez a hotelek átlagos értékelése. Ami alatta van, az gyakran cserél gazdát.

A 7-es és 10-es kérdésből (tanulásra vonatkozó állítások) külön **tanulhatósági alskálát** is képezhetünk, amely jól korrelál az objektív tanulhatósági mutatókkal.

## Az ember viselkedésének modelljei

A kutatási eredmények értelmezéséhez érdemes ismernünk néhány viselkedési modellt. Nézzünk hármat, amelyeket a leggyakrabban használunk.

### A kognitív-behaviorista modell: cél -- probléma -- kontextus

Ez a modell arról szól, hogy a felhasználónak van egy **célja** -- valami, amit el szeretne érni, amire vágyik. Van egy **kontextus** -- a világ pillanatnyi helyzete, ahol éppen áll. És a kettő között vannak **problémák**, amelyeket le kell küzdenie.

Az informatikai alkalmazás tulajdonképpen egy híd vagy létra a problémák felett: segít átmászni rajtuk. Ezért vesszük igénybe a különböző szolgáltatásokat, alkalmazásokat.

### Az empátiaciklus

Az empátiamodell a felhasználó belső világát írja le. A felhasználónak van egy problémája, és vannak **a priori ismeretei** -- emlékszik dolgokra, használt már mobilalkalmazást, volt már száz webshopban, ezért a százegyedik nem nézhet ki máshogy, mert akkor megkeveredik.

A ciklus így működik: amit a felhasználó **lát** (a felületen) és **hall** (a környezetéből, marketingből), az az emlékeivel együtt befolyásolja, amit **érez** és **gondol**. Az érzései és gondolatai alapján **mond** valamit és **tesz** valamit. Amit tesz, attól megváltozik a világ, újra lát és hall valamit -- és ez adja ki a ciklust.

> **Tipp:** Az empátiaciklus remek eszköz arra, hogy egy használhatósági teszt során megértsd, mi zajlik a felhasználó fejében. Figyeld, mit lát, mit mond, mit tesz -- és próbáld rekonstruálni, mit érezhet és gondolhat.

### A Fogg-féle viselkedésmodell (B=MAT)

A Fogg-modell az ingerküszöb modellje. Három tényezőt vizsgál:

- **Motiváció** (Motivation) -- mennyire fáj az adott probléma, mennyire akarom megoldani?
- **Képesség** (Ability) -- képes vagyok-e rá? Van pénzem, tudásom, időm?
- **Inger/kiváltó ok** (Trigger) -- van-e valami, ami beindítja a cselekvést?

A viselkedés akkor következik be, ha a motiváció és a képesség szorzata elég magas ahhoz, hogy az inger átlépje az ingerküszöböt.

> **A gyakorlatból:** Tegyük fel, hogy van egymillió forintom a bankban és szomjas vagyok. Meglátok egy palack ásványvizet. Ha nagyon szomjas vagyok (magas motiváció), nem kell sok pénz ahhoz, hogy megvegyem -- hamar átugrom az ingerküszöböt. De ha egyáltalán nem vagyok szomjas, akkor lehet, hogy végtelenek a képességeim, mégsem fogok venni. És fordítva: ha annyira le vagyok gyengülve, hogy oda se tudok nyúlni az üvegért, hiába végtelen a motivációm -- nem fog történni semmi.

A képlet: **B = M × A × T** (Behavior = Motivation × Ability × Trigger). Nincs nulla pont: ha bármelyik tényező nulla, a viselkedés nem következik be.

> **Megjegyzés:** Ez a három modell -- a behaviorista cél-probléma-kontextus modell, az empátiaciklus és a Fogg-féle viselkedésmodell -- a leggyakrabban használt keretek arra, hogy elemezzük a felhasználók viselkedését. Együtt használva átfogó képet adnak arról, miért csinálják az emberek azt, amit csinálnak.

## Összefoglalás

A felhasználói élmény (UX) azon érzések és gondolatok összessége, amely egy rendszer használata során keletkezik az emberben -- és ezt a lenyomatot kutathatjuk, illetve tervezéssel befolyásolhatjuk. A használhatóságot az ISO 9241 szerint három pilléren mérjük: hatékonyság (idő), hasznosság (sikerráta) és elégedettség (kérdőív, például RHS/SUS). A viselkedés megértéséhez három modell áll rendelkezésünkre: a cél-probléma-kontextus modell, az empátiaciklus és a Fogg-féle B=MAT képlet. Ezek az alapok adják azt a közös nyelvet, amelyre a könyv további fejezeteiben építünk.

## Ellenőrző kérdések

1. Egy belső vállalati rendszernél (pl. MÁV pénztárrendszer) melyik használhatósági mérőszám a legfontosabb üzleti szempontból: a hatékonyság, a hasznosság vagy az elégedettség? Miért? És egy webshopnál hogyan változik a válasz?

2. Tervezz egy egyszerű mérési tervet egy általad ismert mobilalkalmazáshoz: határozd meg, milyen feladatot mérnél, milyen tranzakcióidőt várnál el, és hogyan állítanád össze az RHS kérdőívet a teszt végére!

3. Gondolj egy helyzetre a saját életedből, ahol valamit nem csináltál meg, annak ellenére, hogy képes lettél volna rá. Hogyan írja le a Fogg-modell, mi történt -- melyik tényező „hiányzott"?
