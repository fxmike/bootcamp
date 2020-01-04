class Pojazd:
    def podaj_wlasciciela(self):
        return "ZTM"

class Tramwaj(Pojazd):
    def podnies_pantograf(self):
        return "Pantograf podniesiony"

class Autobus(Pojazd):
    def zatrab(self):
        return "Bip! Biiip!"

class Trolejbus(Tramwaj, Autobus):   # kolejność ma znaczenie
    def rozpocznij_prace(self):
        print(self.podnies_pantograf())
        print(self.zatrab())
        print(f"Ku chwale {self.podaj_wlasciciela()}")

t = Trolejbus()
t.rozpocznij_prace()