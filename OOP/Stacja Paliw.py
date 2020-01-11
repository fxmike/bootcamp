class StacjaPaliw:

    def __init__(self, nazwa, adres, typy_paliw):
        self.nazwa = nazwa
        self.adres = adres
        self.typy_paliw = typy_paliw
        self.tablica_ceny = {}
        self.tablica_litry = {}

    def __str__(self):
        return f'Witaj na stacji {self.nazwa} ({self.adres})'

    def uzupelnij_paliwo(self,typ_paliwa, litry):
        if typ_paliwa in self.typy_paliw:
            if typ_paliwa in self.tablica_litry:
                self.tablica_litry[typ_paliwa] += litry
            else:
                self.tablica_litry[typ_paliwa] = litry
        else:
            return 'Typ paliwa nie wprowadzony do systemu'

    def ustal_cene(self, typ_paliwa, cena):
            for paliwo in self.typy_paliw:
                if paliwo == typ_paliwa or paliwo in self.tablica_ceny:
                    self.tablica_ceny[typ_paliwa] = cena
                else:
                    self.tablica_ceny[paliwo] = 'NIEDOSTĘPNE'
            return self.tablica_ceny

    def zatankuj(self, typ_paliwa, litry):
        litraz = self.tablica_litry[typ_paliwa]
        cena = self.tablica_ceny[typ_paliwa]
        if litraz >= litry:
            litraz -= litry
            return litry * cena
        else:
            return 0

    def generuj_tablice_cen(self):
        if self.tablica_ceny == {}:
            s = ""
            for paliwo in self.typy_paliw:
                s += "- " + paliwo + ' - NIEDOSTĘPNE' + "\n"
            return f'{s}'
        else:
            print('Nasze paliwa:')
            for keys, values in self.tablica_ceny.items():
                print('-',keys, "-", values)

            return ""


if __name__ == "__main__":
    moja_stacja = StacjaPaliw(
        nazwa='Super Paliwo',
        adres='ul. Marszałkowska 1, Warszawa',
        typy_paliw=['PB95', 'PB98', 'ON', 'WERO'],
    )
    # moja_stacja.uzupelnij_paliwo(typ_paliwa='PB95', litry=100)
    # moja_stacja.ustal_cene(typ_paliwa='PB95', cena=4.5)
    # print(moja_stacja.zatankuj(typ_paliwa='PB95', litry=110))
    # print(moja_stacja.generuj_tablice_cen())
    # q_nazwa = input('Podaj nazwę firmy: ')
    # q_adres = input('Podaj adres firmy: ')
    # q_typy_paliw = input('Podaj typy paliw dostępne na stacji: ')
    # moja_stacja = StacjaPaliw(nazwa=q_nazwa, adres=q_adres, typy_paliw=q_typy_paliw)
    print(moja_stacja)
    while True:
        q = input('Co chcesz zrobić? uzupełnij paliwo(u), ustal cenę(c), wypisz paliwa(w), zatankuj(t): ')
        if q.lower() == "u":
            rodzaj_paliw = input("Podaj typ paliwa? ").upper()
            ile_litrow = float(input("Ile litrów? "))
            moja_stacja.uzupelnij_paliwo(typ_paliwa=rodzaj_paliw, litry=ile_litrow)
        elif q.lower() == "c":
            rodzaj_paliw_cena = input("Podaj typ paliwa? ").upper()
            jaka_cena = float(input("Jaka cena? "))
            moja_stacja.ustal_cene(typ_paliwa=rodzaj_paliw_cena,cena=jaka_cena)
        elif q.lower() == 'w':
            print(moja_stacja.generuj_tablice_cen())
        elif q.lower() == 't':
            rodzaj_paliw_tankowanie = input('Podaj typ paliwa? ').upper()
            ile_litrow_tankowanie = float(input('Ile litrów? '))
            print(f'Do zapłacenia {moja_stacja.zatankuj(rodzaj_paliw_tankowanie,ile_litrow_tankowanie)} PLN')
        else:
            print("Nie podałeś właściwej komendy.")
            continue
        # q_ending = input('Czy kończymy [t/n]? ')
        # if q_ending.lower() == 't':
        #     print("Dziękuję")
        #     break
        # elif q_ending.lower() == 'n':
        #     continue

