import constants


class Plocica:
    def __init__(self):
        pass

    def konverzija_vrednosti_int(self, plocica):
        """
        Metoda koja konvertuje vrednost trenutne plocice iz string tipa u integer
        :param plocica: trenutna plocica koju konvertujemo
        :return: cast-ovana plocica
        """
        if plocica == "":
            plocica = 0
        else:
            plocica = int(plocica)

        return plocica

    def pomeranje_plocice(self, poz_za_pomeraj, vrednost_plocice, matrica, i, j, tabla, vrsta):
        """
        Pomocna metoda koja pomera trenutnu plocicu i vrsi sabiranje ukoliko su u pitanju dve susedne sa istom vrednoscu
        """
        if poz_za_pomeraj > -1:
            if vrednost_plocice > 0:
                if vrsta:
                    matrica[i][poz_za_pomeraj] = str(vrednost_plocice)
                else:
                    matrica[poz_za_pomeraj][j] = str(vrednost_plocice)
                tabla.setScore(tabla.getScore() + vrednost_plocice)
            else:
                if vrsta:
                    matrica[i][poz_za_pomeraj] = matrica[i][j]
                else:
                    matrica[poz_za_pomeraj][j] = matrica[i][j]
            matrica[i][j] = ""

    def pomeri_udesno(self, matrica, tabla):
        """
        Metoda koja pomera plocicu udesno
        """
        for i in range(0, constants.GRID_SIZE):
            i_na_kom_je_mergeano = -1
            for j in range(constants.GRID_SIZE - 2, -1, -1):
                j_za_pomeraj = -1
                vrednost_plocice = 0
                if matrica[i][j] != "":
                    trenutna_plocica = self.konverzija_vrednosti_int(matrica[i][j])
                    for z in range(j + 1, constants.GRID_SIZE):
                        sledeca_plocica = self.konverzija_vrednosti_int(matrica[i][z])
                        if sledeca_plocica == 0:
                            j_za_pomeraj = z
                        elif sledeca_plocica == trenutna_plocica and z != i_na_kom_je_mergeano:
                            j_za_pomeraj = z
                            vrednost_plocice = sledeca_plocica * 2
                            i_na_kom_je_mergeano = z
                            break
                        elif sledeca_plocica != trenutna_plocica:
                            break

                    self.pomeranje_plocice(j_za_pomeraj, vrednost_plocice, matrica, i, j, tabla, True)

    def pomeri_ulevo(self, matrica, tabla):
        """
        Metoda koja pomera plocicu ulevo
        """
        for i in range(0, constants.GRID_SIZE):
            j_na_kom_je_mergeano = -1
            for j in range(1, constants.GRID_SIZE):
                j_za_pomeraj = -1
                vrednost_plocice = 0
                if matrica[i][j] != "":
                    trenutna_plocica = self.konverzija_vrednosti_int(matrica[i][j])
                    for z in range(j - 1, -1, -1):
                        sledeca_plocica = self.konverzija_vrednosti_int(matrica[i][z])
                        if sledeca_plocica == 0:
                            j_za_pomeraj = z
                        elif sledeca_plocica == trenutna_plocica and z != j_na_kom_je_mergeano:
                            j_za_pomeraj = z
                            vrednost_plocice = sledeca_plocica * 2
                            j_na_kom_je_mergeano = z
                            break
                        elif sledeca_plocica != trenutna_plocica:
                            break

                    self.pomeranje_plocice(j_za_pomeraj, vrednost_plocice, matrica, i, j, tabla, True)

    def pomeri_nagore(self, matrica, tabla):
        """
        Metoda koja pomera plocicu na gore
        """
        for j in range(0, constants.GRID_SIZE):
            i_na_kom_je_mergeano = -1
            for i in range(1, constants.GRID_SIZE):
                i_za_pomeraj = -1
                vrednost_plocice = 0
                if matrica[i][j] != "":
                    trenutna_plocica = self.konverzija_vrednosti_int(matrica[i][j])
                    for z in range(i - 1, -1, -1):
                        sledeca_plocica = self.konverzija_vrednosti_int(matrica[z][j])
                        if sledeca_plocica == 0:
                            i_za_pomeraj = z
                        elif sledeca_plocica == trenutna_plocica and z != i_na_kom_je_mergeano:
                            i_za_pomeraj = z
                            vrednost_plocice = sledeca_plocica * 2
                            i_na_kom_je_mergeano = z
                            break
                        elif sledeca_plocica != trenutna_plocica:
                            break

                    self.pomeranje_plocice(i_za_pomeraj, vrednost_plocice, matrica, i, j, tabla, False)

    def pomeri_nadole(self, matrica, tabla):
        """
        Metoda koja pomera plocicu na dole
        """
        for j in range(0, constants.GRID_SIZE):
            i_na_kom_je_mergeano = -1
            for i in range(constants.GRID_SIZE - 2, -1, -1):
                i_za_pomeraj = -1
                vrednost_plocice = 0
                if matrica[i][j] != "":
                    trenutna_plocica = self.konverzija_vrednosti_int(matrica[i][j])
                    for z in range(i + 1, constants.GRID_SIZE):
                        sledeca_plocica = self.konverzija_vrednosti_int(matrica[z][j])
                        if sledeca_plocica == 0:
                            i_za_pomeraj = z
                        elif sledeca_plocica == trenutna_plocica and z != i_na_kom_je_mergeano:
                            i_za_pomeraj = z
                            vrednost_plocice = sledeca_plocica * 2
                            i_na_kom_je_mergeano = z
                            break
                        elif sledeca_plocica != trenutna_plocica:
                            break

                    self.pomeranje_plocice(i_za_pomeraj, vrednost_plocice, matrica, i, j, tabla, False)

    """
    Metode koje proveravaju da li ima vise mogucih poteza u bilo kom od 4 pravca - u slucaju da vise ne mozemo da 
    pomerimo nijednu plocicu u odredjenom smeru, nastavljanjem pritiskanja tog tastera, nece doci do poziva metode za 
    otvaranje nove random plocice
    """

    def provera_poteza(self, trenutna_plocica, sledeca_plocica):
        """
        Metoda koja proverava da li ima vise mogucih poteza u bilo kom od 4 moguca smera
        :param trenutna_plocica: plocica koju trenutno ispitujemo
        :param sledeca_plocica: naredna plocica sa kojom uporedjujemo
        :return: vraca da li postoji mogucih poteza
        """
        return ((trenutna_plocica != 0 and trenutna_plocica == sledeca_plocica) or
                (trenutna_plocica != 0 and sledeca_plocica == 0))

    def ima_li_poteza_udesno(self, matrica):
        for i in range(0, constants.GRID_SIZE):
            for j in range(0, constants.GRID_SIZE):
                if j < constants.GRID_SIZE - 1:
                    trenutna_plocica = self.konverzija_vrednosti_int(matrica[i][j])
                    sledeca_plocica = self.konverzija_vrednosti_int(matrica[i][j + 1])
                    if self.provera_poteza(trenutna_plocica, sledeca_plocica):
                        return True
        return False

    def ima_li_poteza_ulevo(self, matrica):
        for i in range(0, constants.GRID_SIZE):
            for j in range(constants.GRID_SIZE - 1, -1, -1):
                if j > 0:
                    trenutna_plocica = self.konverzija_vrednosti_int(matrica[i][j])
                    sledeca_plocica = self.konverzija_vrednosti_int(matrica[i][j - 1])
                    if self.provera_poteza(trenutna_plocica, sledeca_plocica):
                        return True
        return False

    def ima_li_poteza_nagore(self, matrica):
        for j in range(0, constants.GRID_SIZE):
            for i in range(constants.GRID_SIZE - 1, -1, -1):
                if i > 0:
                    trenutna_plocica = self.konverzija_vrednosti_int(matrica[i][j])
                    sledeca_plocica = self.konverzija_vrednosti_int(matrica[i - 1][j])
                    if self.provera_poteza(trenutna_plocica, sledeca_plocica):
                        return True
        return False

    def ima_li_poteza_nadole(self, matrica):
        for j in range(0, constants.GRID_SIZE):
            for i in range(0, constants.GRID_SIZE):
                if i < constants.GRID_SIZE - 1:
                    trenutna_plocica = self.konverzija_vrednosti_int(matrica[i][j])
                    sledeca_plocica = self.konverzija_vrednosti_int(matrica[i + 1][j])
                    if self.provera_poteza(trenutna_plocica, sledeca_plocica):
                        return True
        return False
