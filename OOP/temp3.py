class Klient:
    def __init__(self):
        self._zatankowane = 0

    @property
    def rabat(self):
        if self._zatankowane > 1000:
            return 0.1
        else:
            return 0

    @rabat.setter
    def rabat(self, value):
        self._zatankowane = 1001 if value > 0.09 else 0

klient = Klient()
print(klient.rabat)
klient._zatankowane = 1100
print(klient.rabat)
klient.rabat = 0.1
print(klient.rabat)

#settery getteryn