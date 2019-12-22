class SwietyMikolaj:
    kolejny_numer = 1

    def __init__(self, imie):
        self.imie = imie   # przez kropkę dostajemy się do funkcji/metod ale także do wartości (w klasach)
        self.wiek = None

    def __str__(self):
        return self.imie

    def przywitaj_sie(self):
        print(f"Hohoho! Jestem {self.imie}")

    def daj_prezent(self, dla_kogo):
        return f"Prezent dla {dla_kogo}"

    @classmethod
    def gdzie_mieszkaja_mikolajowie(cls):
        return "Laponia"

    @classmethod
    def zaloga_4_mikolajow(cls):
        return [cls('Albert'), cls('Baltazar'), cls('Cezary'), cls('Daniel')]

    @classmethod
    def mikolaj_o_kolejnym_imieniu(cls):
        mikolaj = cls(f"Mikolaj{cls.kolejny_numer}")
        cls.kolejny_numer += 1
        return mikolaj

    @staticmethod
    def czy_w_zimie_jest_zimno():
        return True

mikolaj1 = SwietyMikolaj("Mikolajek")
print("Ten Swiety Mikolaj nazywa się", mikolaj1.imie)
print("Ten Swiety Mikolaj ma lat", mikolaj1.wiek)
mikolaj1.przywitaj_sie()
print(mikolaj1.gdzie_mieszkaja_mikolajowie())
inni_mikolajowie = SwietyMikolaj.zaloga_4_mikolajow()

# for mikolaj in inni_mikolajowie:
#     return SwietyMikolaj.przywitaj_sie(), SwietyMikolaj.zaloga_4_mikolajow()

print(SwietyMikolaj.mikolaj_o_kolejnym_imieniu())
print(SwietyMikolaj.mikolaj_o_kolejnym_imieniu())
print(SwietyMikolaj.mikolaj_o_kolejnym_imieniu())

print(SwietyMikolaj.czy_w_zimie_jest_zimno())