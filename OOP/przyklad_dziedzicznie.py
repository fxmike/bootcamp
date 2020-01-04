class Pies:
    rasa = 'mieszaniec '

    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"Pies rasy {self.rasa}"

    def biegnij(self):
        self.x += 1
        self.y += 1
        return f"Pies rasy {self.rasa}, x={self.x}, y={self.y}"

    def zjedz_karme(self, karma):
        pass

    def daj_glos(self):
        print("Hau hau")

class Lagotto(Pies):  #to jest ta rasa psów, która znajduje trufle
    rasa = 'Lagotto '

    def znajdz_trufle(self):
        return "Trufla"

class Husky(Pies):
    rasa = 'Husky '

    def daj_glos(self):
        print("Uuuuola!")

class Hart(Pies):
    rasa = 'Hart'

    def biegnij(self):
        super().biegnij()
        super().biegnij()
        super().biegnij()
        return f"Pies rasy {self.rasa}, x={self.x}, y={self.y}"

azor = Pies()
print(azor)
print(azor.biegnij())
azor.daj_glos()


dzuseppe = Lagotto()
print(dzuseppe)
print(dzuseppe.biegnij())


dzuseppe.daj_glos()
print(dzuseppe.znajdz_trufle())

tajga = Husky()
print(tajga)
tajga.daj_glos()

szybki = Hart()
szybki.daj_glos()
print(szybki.biegnij())


