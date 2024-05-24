Igrica "2048" je matematicka igrica koja za cilj ima pomeranje plocica sa brojevima i njihovo sabiranje dok se ne dobije
zbir 2048. Sve se odvija na grid-u 4 sa 4.
Igrica zapocinje sa dve inicijalne random plocice sa brojem 2.
Pravila igre nalazu da mogu da se saberu samo jednake plocice (2 sa 2 daje 4, zatim 4 samo sa 4, 16 samo sa 16 i tako do
konacnog zbira).
Plocice pomeramo tasterima na tastaturi u sva cetiri pravca (levo, desno, gore, dole).
Na primer, ukoliko imamo niz od [8, 4, 2, 2] (2 i 2 daju 4, 4 i 4 daju 8, 8 i 8 16),mi ipak necemo klikom ulevo u ovom
slucaju imati zbir 32, jer jednim klikom na taster se sabiraju iskljucivo i samo susedne plocice, te ce nakon prvog klika
na taster za levo, ovaj red izgledati ovako -> [8, 4, 4]. S toga za dalje sabiranje, nastaviti kliktati u tom smeru.
Svakim klikom na jedan od 4 dugmeta i pomeranjem plocica u datom smeru, pojavljuje se nova plocica sa vrednoscu 2 na
jednoj od preostalih praznih random pozicija. Bita stvar u tom slucaju je da, ukoliko vise nemamo poteza klikom na neki
od 4 dugmeta, nova plocica sa vrednoscu 2 se nece pojaviti na ekranu.
Na kraju, postoje dva ishoda igre - ili pomeranjem popunimo sva polja ,ali ne dobijemo broj 2048 i tada za ishod imamo
"Game Over" ili dolazimo do konacnog broja i za ishod imamo "You Win".
Igricu uvek mozemo prekinuti klikom na X.
Ono sto je bitno je da se pamti svaki put samo score koji je maksimalan, sto se i prikazue na vrhu table (trenutni score
i najbolji score do sada).

Uzivajte u igrici!

