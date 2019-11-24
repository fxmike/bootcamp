def wiecej_niz(string, num):
    ilosc_wystapien = {}
    for l in string:
        ilosc_wystapien[l] = ilosc_wystapien.get(l, 0) + 1

    wybrane = set()
    for litera, wystapienia in ilosc_wystapien.items():
        if wystapienia > num:
            wybrane.add(litera)
    return wybrane

def test_powtorzenia_wiecej_niz_0():
    assert wiecej_niz("ala ma kota a kot ma ale", 0) == {'l', ' ', 'a', 'e', 't', 'o', 'm', 'k'}

def test_brak_powtorzen():
    assert wiecej_niz("abcdefghij", 1) == set()

def test_pusty_string_3():
    assert wiecej_niz("", 0) == set()
    assert wiecej_niz("", 3) == set()

def test_powtorzenia_wiecej_niz_3():
    assert wiecej_niz("ala ma kota a kot ma ale", 3) == {"a", " "}

#test driven development (TDD). Najpierforw piszę test, potem do niego kod tak by test przeszedł. Potem
#tworzę kolejne testy i optymalizuję w razie potrzeby kod

if __name__ = "__main__:"               # to sposób by odpalić kod obok przez przycisk "run", ale nie będzie
    a = input("Podaj tekst:")           # odpalany w innym miejscu (np. pytest). nie ma tu logiki - trzeba umieć na pamięć