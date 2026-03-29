# Függelék: A UX üzleti megtérülése

Ez a függelék azoknak szól, akiknek meg kell indokolniuk a főnöküknek, a megrendelőjüknek vagy a befektetőjüknek, hogy miért érdemes pénzt költeni felhasználókutatásra. Szép dolog a bűvszámokkal dolgozni, de a nap végén abból kapunk fizetést, amit pénzzé tudunk fordítani. Nézzük tehát végig, hogyan lehet a megtérülés (ROI) nyelvén beszélni a UX-ről -- mind a felhasználó szervezete, mind a megrendelő szemszögéből.

## A használhatóság megtérülése a felhasználó szervezetében

Ennek a történetnek alapvetően két oldala van: az egyik a felhasználó szervezete, a másik a megrendelőé. Kezdjük a felhasználó oldalával.

### Időfaktor

A legkönnyebben számszerűsíthető megtérülés az idő. Munkaszoftverek esetén -- és mi rengeteg munkaszoftvert tervezünk -- a képlet egyszerű: a kiesett idő szorozva a felhasználó munkabérével.

Gondolj bele: ha a felhasználó eltölt tíz percet egy feladattal, és az órabére mondjuk hatezer forint, az a tíz perc ezer forintba kerül. Ha ezren csinálják ugyanezt, az máris egymillió forint. Egy rosszul tervezett felületen elpazarolt napi tíz perc céges szinten óriási összegeket jelent.

> **A gyakorlatból:** A MÁV-nál például a vonatokra 10--15 perccel indulás előtt esnek be az emberek. A pénztári rendszer hatékonysága közvetlenül meghatározta, hány pénztárost kell alkalmazniuk. A kérdés az volt: a vasárnapi csúcsban az átlag négy pénztárosról le tudunk-e menni háromra, mert annyival gyorsabban tudják feldolgozni a jegyeket. Ha igen -- az egy teljes fizetés megtakarítása.

Fogyasztói (consumer) szoftvereknél is érvényes az időfaktor, csak másképp. Ott az számít, hogy a felhasználó csinálhatott volna valami értelmesebbet, valami olyat, amitől jobban érzi magát vagy amivel pénzt kereshetett volna.

### Hasznosság és hibázás költsége

Nem csak az idő számít. Érdemes megnézni, mennyibe kerül, ha valami nem sikerül:

- **Kritikus rendszereknél** -- például egy atomerőmű vezérlőpultjánál -- a hiba ára iszonyatosan magas.
- **Webshopnál** a kiesett bevétel a tét: aki otthagyja a kosarat, mert nem boldogul a felülettel, az elveszett vásárló.
- **A support költsége** -- ha valaki felhívja az ügyfélszolgálatot, mert nem tudja használni a számlázó programot, az bizony pénzbe kerül. Minél több supportos kolléga kell, annál inkább.

> **Megjegyzés:** Van egy jelenség, amit kupaktanács-hatásnak hívunk. Tegyük fel, hogy van három pénztárad. Azt gondolnád, ha az egyikben hiba van, a másik kettő szépen megy tovább. De nem. Ha az egyiknél valaki nem boldogul a szoftverrel, a másik két pénztárból is odagyülekeznek az emberek, és a teljes sor áll. Tehát nem egy pénztár esik ki, hanem az egész rendszer leáll.

### Kiváltási faktor és csatornamix

Érdekes kérdés az is, hogy egy önkiszolgáló csatorna -- mondjuk egy vasútautomata vagy egy mobilalkalmazás (mobile app) -- a forgalom hány százalékát tudja kiváltani.

A bankoknál ez volt az ATM és az internetbank nagy vívmánya: rájöttek, hogy az ügyfelek jelentős része csak azért megy be a bankfiókba, hogy pénzt vegyen fel. Ha ezt meg tudnák tenni egy automatánál, azzal nem terhelnék a diplomás banki alkalmazottakat. Sőt, ha az egyenlegüket is meg tudnák nézni és a betéteiket is le tudnák kötni -- az még jobb.

Az önkiszolgáló csatornák üzemeltetési költsége jellemzően olcsóbb, mint az emberek „üzemeltetése". Ide tartozik a munkafolyamati arány kérdése is: az adott termék a teljes munkafolyamatnak hány százalékát fedi le? Hány másik rendszert kell még használni mellette? Sikerül-e az előző rendszert teljesen kiváltani, vagy párhuzamosan kell két rendszert üzemeltetni?

### Tanulhatóság

A tanulhatósággal is lehet számolni. Kell-e tréning? Milyen szintű emberek kellenek hozzá? Kell-e mondjuk két évig pénztárost képezni -- mert az két évnyi fizetés, mielőtt produktív lenne. Vagy a program segíti a betanulást, és elég egy félnapos oktatás?

> **A gyakorlatból:** Az Uber tulajdonképpen azt hozta a taxizásba, hogy nem kell megtanulni a város térképét kívülről, hiszen a GPS szépen elnavigál. Ezzel drámaian csökkentette a belépési küszöböt.

A tanulási görbének van egy haranggörbéje: átlagosan az emberek közepesen lesznek hatékonyak, van aki nehézkesen kezel egy rendszert, van aki „ropja". Nem mindegy, hogy ez a görbe mennyire keskeny vagy széles -- az is tervezési kérdés.

## A UX haszna a megrendelőnek

Az esetek 90 százalékában őszintén majdnem mindegy, milyen jelenséget okoz a UX a felhasználó szervezetében -- mert nem a felhasználó fizet, hanem a megrendelő. A legtöbb UX-es nem azzal a szerencsés helyzettel találkozik, hogy a felhasználó szervezete kér fel, hanem a megrendelővel vitatkozik, aki nem a felhasználója a terméknek.

Nézzük tehát, mit jelent a UX pénzben a megrendelő számára.

### A Boehm-görbe: a változtatás ára

Van egy fogalom, amit Boehm-görbének hívunk. Ez azt mondja, hogy minél később vagyunk egy szoftverfejlesztési projektben, annál drágább bármit is változtatni. Amíg nem látta senki a szoftvert, viszonylag olcsó változtatni. A fejlesztés végén már rendkívül drága. Kiadás után pedig hirtelen lökést kap a költség.

> **Figyelem!** Kiadott szoftveren rendkívül nehéz változtatni -- még ha az Agile tagadja is ennek a létezését. A fejlesztő nem akar változtatni, mert egyszer már megírta. A felhasználók hozzászoktak, és ha megváltoztatod, akiket megszoktál, azokat elveszítheted. Újra kell tanulniuk -- ott keletkezik egy csomó költség.

Erre a legtöbb cég rájött, ezért használnak úgynevezett határobjektumot (boundary object). A határobjektum egy olyan objektum, ami közösen értelmezett minden érintett számára, viszont mindenki máshogyan értelmezi.

A drótváz (wireframe) tipikus határobjektum: a fejlesztő azt nézi, hogyan fogja lekódolni; a marketinges azt nézi, hogyan lesz ebből eladás és lojalitás (loyalty); a designer azt nézi, milyen színvilágot és elrendezést használ. Ez a három ember nem beszéli egymás nyelvét, de ezen az objektumon keresztül értelmesen tud beszélgetni.

> **Megjegyzés:** Az esetek 98 százalékában a UX cégeket arra kérik fel, hogy csináljanak egy ilyen határobjektumot -- hogy meg tudjuk beszélni, miről lesz szó. De ez önmagában még nem UX, hanem inkább ügyfélélmény (customer experience). A felhasználó ugyanis hiányzik az egyenletből.

### A 30 százalékos megtakarítás a fejlesztésen

Amikor a fejlesztő cégnek ajánlatot kell adnia, a bizonytalanság óriási. Mennyibe kerül egy mobilalkalmazás? Hát 20 és 100 millió forint között bármi lehet. Ha egy üres semmire ad ajánlatot, akár négyszeres is lehet az eltérés.

Azzal, hogy részletes UX specifikációt készítünk -- nem csak drótvázat, hanem teljes logikai rendszertervet a végleges vizuálokkal --, nagyon kis bizonytalanság mellett meg lehet mondani, mennyibe fog kerülni a szoftver. Az ügyfeleink azt mondják, hogy ezzel önmagában nagyjából 30 százalékot spórolnak a fejlesztésen.

> **Tipp:** Ha a megrendelőnek el kell adnod a UX kutatás költségét, ez az az érv, amit a legtöbb fejlesztő cég ért: a részletes specifikáció csökkenti a fejlesztési költségeket, mert kevesebb az újratervezés és a félreértés.

### A valódi érték: megtalálni, mit kell fejleszteni

De a mi ügyfeleink nem ezért használnak minket. A legnagyobb érték nem a specifikáció, hanem annak feltérképezése, hogy egyáltalán mit is kell csinálni.

Képzeld el, hogy van 100 millió forintod, amit el tudsz költeni. Elindulsz egy irányba, de nem igazán találtad el. Ahogy haladsz előre a projektben, beszűkülnek a lehetőségeid -- már nem nagyon tudsz változtatni. Fokozatosan beszorulsz egy szituációba, ami nem az ideális termék. A különbséget aközött, amit valójában kellett volna csinálnod, és aközött, amit ténylegesen csináltál, valahogy bebukod: vagy a felhasználó idejében, vagy felhasználókat veszítesz, vagy konkrétan valaki megcsinálja rendesen, és elveszíted az egész piacot.

A felhasználókutatóknak szerintem ez az egyik leglényegesebb tulajdonsága: meg tudják mondani, hogy mit is kell csinálni. Interjúkkal feltérképezik a piacot, használhatósági tesztekkel pedig ellenőrzik, hogy jó-e, amit fejlesztünk.

## A felhasználókutatás haszna az iteratív fejlesztésben

Az eddigiekben úgy beszéltünk a termékről, mintha az egyben megszülető dolog lenne: kitaláljuk, mit akarunk, megépítjük, kiadjuk, és miénk a piac. Természetesen ez nem így működik -- soha nem így működött.

### Az Apple iPod tanulsága

Mindenki azt gondolja az Apple-ről, hogy „csak úgy" szüli a zseniális termékeket. Nem erről van szó. Nézzük az iPod példáját.

Az iPod egy MP3 lejátszó volt, 2001-ben jelent meg, amikor mindenkinek volt már MP3 lejátszója. Ennek az volt a különlegessége, hogy merevlemezes volt, tehát viszonylag nagy tárhelyet tudott kezelni, ráadásul volt egy fehér fülhallgatója -- ha a metrón láttad, tudtad, hogy a másiknak iPodja van.

De önmagában ez nem adta el a terméket. A második generáció is csak a főbb hiányosságait javította. A harmadik generáció új gombsort és mechanikát kapott -- csak nem kellett senkinek. Közben az Apple rájött, hogy ökoszisztémában kell gondolkodni: megcsinálták az iTunes zeneboltot, PC-re is kihozták. És utána, amikor a negyedik generáció megérkezett -- színes képernyővel, egyszerűsített kezelőfelülettel --, hirtelen mindenki akarta. Karácsonyi slágertermék lett, kifogyott, megdobta az Apple részvényárfolyamát.

> **A gyakorlatból:** Ez nem egy „egyik napról a másikra" siker volt. Négy generációig kellett eljutni, rengeteg terméket legyártani, amelyeket vagy megvettek vagy nem. A piaci tanulásnak iszonyatos kockázatai vannak -- ha a teljes marketinget ráereszted az első verzióra és beégsz, mindenki megjegyzi, hogy „az iPod szar". Rengeteg termék van, ami nem tud kimászni abból, hogy 5--10 évvel ezelőtt rossz volt.

### Az agilis build-measure-learn ciklus korlátai

Az agilis fejlesztés (Agile development) build-measure-learn ciklusa arról szól, hogy van egy ötletünk, megépítjük, megmérjük a piaci reakciót, tanulunk belőle, és kezdjük elölről. A probléma az, hogy megépíteni egy terméket -- még ha csak egy verziót is -- rendkívül drága. Magyarországon a fejlesztések nagyságrendileg a tízmilliós sávban vannak, de vannak százmilliós és milliárdos projektek is.

Ráadásul a fejlesztés közben már bekorlátoz a folyamat: nem tudsz mindent megváltoztatni. Amikor kiadtad, akkor meg végképp nehéz. A legtöbb magyar cégnek nincsenek olyan likviditási tartalékai, mint az Apple-nek, ezért látunk mai napig cégeket, amelyek a '91-ben kiadott DOS-os szoftverükön kapaszkodnak.

### A UX stratégiai ciklus: learn-design-test

Mi egy másik ciklust követünk: learn-design-test. Nem tervezünk első körben semmit -- felhasználói interjúkra megyünk ki. Ebből hipotéziseket építünk, erre tervezünk rendszert, csinálunk belőle prototípust, a prototípust visszük tesztre. Megnézzük az eltéréseket, tanulunk, és a ciklus újra megy. Egészen addig, amíg nincsenek nagy eltérések aközött, ahogy mi gondoljuk, és ahogy a felhasználó szeretné élni az életét.

Ekkor visszük ki építésre, és ekkor már tudjuk, hogy nem nagyon kell módosítani sem a fejlesztés során, sem kiadás után.

### A prototípus mint határobjektum

A prototípus azért hatékony, mert határobjektumot képez a cég és a felhasználó között. A piac csak akkor tudja elmondani a véleményét, ha legalább a marketing anyagait -- de általában az igazi terméket vagy a prototípusát -- megfogta. A trükk az, hogy mi nem csak simán drótvázat építünk, hanem komplett prototípust, amit három-négy-öt fővel tesztelünk.

A prototípus előnyei a késztermékhez képest:

- **A felhasználó el tudja képzelni a terméket** -- mégis „csak egy zöld dobozt lökdösünk".
- **Olcsó módosítani** -- mi szándékosan nem dokumentáljuk agyon, mert ha módosítunk, nem kell a dokumentációt is átírni.
- **Mindenképpen olcsóbb a fejlesztett programnál.**
- **Kevesen látják** -- nem égünk be a piac előtt, tehát tudjuk iterálni.
- **Határobjektumot képez** -- a felhasználó el tudja mondani, mikor van megoldva az ő problémája.

> **Figyelem!** A prototípusnak vannak hátrányai is az agilis módszertanhoz képest. Nincs számszerű piaci visszajelzés -- néhány felhasználóval tesztelünk, nem ezrekkel. Nehezen köthető közvetlenül pénzhez. Nem teljesen modellezi a valóságot -- ha teljesen modellezné, az már programozás lenne, és drága. Ismeretlen technológiánál előfordulhat, hogy a fejlesztők később jönnek rá: amit szerettünk volna, az úgy nem megvalósítható.

Az agilis ciklushoz képest a nagy különbség, hogy mi nem építjük meg a terméket és nem költünk erre pénzt. Cserébe nem tudunk mérni, csak feltételezéseket tudunk tenni egy kisebb mintás módszertannal. De ezek a ciklusok segítenek megépíteni a terméket úgy, hogy a költségvetésben benne maradjunk.

> **Tipp:** Ahhoz, hogy piacot megértsünk, legtöbbször még prototípus sem kell -- elég a felhasználói interjú. A prototípus a használhatósági teszteléshez kell. A piaci igények feltárását interjúkkal is el tudjuk végezni.

## Összefoglalás

A UX kutatás megtérülése több szinten jelentkezik: a felhasználó szervezetében időt és pénzt takarít meg, csökkenti a support és a hibázás költségeit, illetve lehetővé teszi az önkiszolgáló csatornák bevezetését. A megrendelő szervezetében csökkenti a fejlesztési költségeket a részletes specifikációval, és -- ami a legfontosabb -- segít megtalálni, hogy egyáltalán mit is kell fejleszteni. A prototípus-alapú iteratív fejlesztés (iterative development) pedig lehetővé teszi, hogy a piaci igényeket olcsón és gyorsan feltérképezzük, mielőtt a drága fejlesztésbe belevágnánk.

## Ellenőrző kérdések

1. Hogyan tudod kiszámítani egy munkaszoftver használhatóságának javításából származó megtérülést a felhasználó szervezetében?
2. Mit jelent a Boehm-görbe, és miért fontos ezt figyelembe venni, amikor a UX kutatás költségét indokolod a megrendelőnek?
3. Mi a különbség az agilis build-measure-learn ciklus és a UX stratégiai learn-design-test ciklus között, és mikor melyiket érdemes alkalmazni?
4. Milyen érveket használnál, ha meg kellene győznöd egy szkeptikus vezetőt arról, hogy a felhasználókutatás nem „felesleges költség", hanem befektetés?
