# Przykłady:
# formatuj('Podróż z $miasto1 do $miasto2 zajmuje $czas h', miasto1="Los Angeles", miasto2="Yorktown", czas=5)
# 'Podróż z Los Angeles do Yorktown zajmuje 5 h'
# formatuj('$powitanie', 'Mam $kolor samochód', 'Mam też $kolor rower', 'A nawet mam $kolor dom, bo $kolor to mój
# ulubiony kolor.', powitanie="Hej!", kolor='niebieski')
# 'Hej!\nMam niebieski samochód\nMam też niebieski rower\nA nawet mam niebieski dom, bo niebieski to mój ulubiony kolor.'
# Zaznaczę jeszcze, bo mogło to umknąć w trakcie zajęć: jeśli wewnątrz stringa pojawia się \n, to oznacza to znak nowej
# linii - taki string podany funkcji print wydrukuje się podzielony na linijki. Żeby wydrukować powyższe
# linijki użyłem specjalnie print(repr(formatuj(...))). Znając ten zapis \n i mając zrobioną ściągawkę można
# znaleźć szybki i wygodny sposób łączenia list napisów w jeden napis "wieloninijkowy"

def formatuj(*args, **kwargs):
    sbl = '$'
    new = ""
    for key, value in kwargs.items():
        kword = sbl + key
        value = str(value)
        # print(value)
        # print(kword)
        for arg in args:
            ar = arg.replace(kword,value)
            print(ar)

    return new






print(formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10))

print(formatuj('Podróż z $miasto1 do $miasto2 zajmuje $czas h', miasto1="Los Angeles", miasto2="Yorktown", czas=5))


def test_koszt_cena():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto'