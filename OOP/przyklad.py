class SwietyMikolaj:

    def __init__(self, imie):
        self.imie = imie   # przez kropkę dostajemy się do funkcji/metod ale także do wartości (w klasach)
        self.wiek = None
    def przywitaj_sie(self):
        print(f"Hohoho! Jestem {self.imie}")

    def daj_prezent(self, dla_kogo):
        return f"Prezent dla {dla_kogo}"


mikolaj1 = SwietyMikolaj("Mikolajek")
print("Ten Swiety Mikolaj nazywa się", mikolaj1.imie)
print("Ten Swiety Mikolaj ma lat", mikolaj1.wiek)
mikolaj1.przywitaj_sie()
