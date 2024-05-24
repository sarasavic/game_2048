import random
import constants
import upis_u_fajl


class Tabla:
    def __init__(self):
        self.__matrica = [["" for _ in range(4)] for _ in range(4)]
        # matrica za test
        # self.__matrica = [
        #     ["2", "128", "64", "32"],
        #     ["4", "16", "2", "8"],
        #     ["8", "1024", "1024", "4"],
        #     ["2", "", "64", "8"]
        # ]
        self.__score = 0
        self.__ishod = constants.PLAYING

    def getMatrica(self):
        return self.__matrica

    def getScore(self):
        return self.__score

    def setScore(self, noviScore):
        self.__score = noviScore

    def getIshod(self):
        return self.__ishod

    def prikazi_random_plocicu(self):
        """
        Metoda koja pomerajem ostalih plocica, po pravilu, otvara novu plocicu sa vrednoscu 2 na nekom random mestu
        """
        while True:
            red = random.randrange(constants.GRID_SIZE)
            kolona = random.randrange(constants.GRID_SIZE)
            if self.__matrica[red][kolona] == "":
                self.__matrica[red][kolona] = "2"
                break

    def prokazi_prve_dve_plocice(self):
        """
        Metoda koja, na pocetku igre, ubacuje prve dve random plocice sa vrednoscu 2
        """
        zauzete_pozicije = set()

        while len(zauzete_pozicije) < 2:
            red = random.randrange(constants.GRID_SIZE)
            kolona = random.randrange(constants.GRID_SIZE)
            if (red, kolona) not in zauzete_pozicije:
                self.__matrica[red][kolona] = "2"
                zauzete_pozicije.add((red, kolona))

    def kraj_igre(self, plocica):
        """
        Metoda koja proverava da li je doslo do kraja igre, tj. da li smo dosli do zbira plocica koji iznosi 2048 (Win)
        ili smo popunili sve slobodne plocice, ali bez zbira (Game Over)
        """

        ima_krajnji_zbir = False
        for red in self.__matrica:
            for broj in red:
                if broj == "2048":
                    ima_krajnji_zbir = True

        if ima_krajnji_zbir:
            self.__ishod = constants.WIN
        elif not plocica.ima_li_poteza_udesno(self.__matrica) and not plocica.ima_li_poteza_ulevo(self.__matrica) and \
                    not plocica.ima_li_poteza_nadole(self.__matrica) and not plocica.ima_li_poteza_nagore(self.__matrica):
            self.__ishod = constants.GAME_OVER

    def nova_igra(self):
        """
        Metoda koja klikom na dugme "New Game" ponovo pokrece igricu
        """
        upis_u_fajl.upis_scorea_u_fajl(self.getScore())
        self.__matrica = [["" for _ in range(4)] for _ in range(4)]
        self.__score = 0
        self.__ishod = constants.PLAYING
