class IncorrectUserAction(Exception):  #dobra praktyka - tworzenie własnej klasy do obsługi błędów
    pass

def obsluga_kantoru():
    operacja = input('chcesz kupić czy sprzedać?: [k/s]')

    if operacja.lower() == "k":
        ...
    elif operacja.lower() == 's':
        ...
    else:
        raise IncorrectUserAction('Podana niepoprawna operacja')

    ...
    return 100

print("Początek programu")
try:
    kwota = obsluga_kantoru()
    print("kolejna linijka")
except IncorrectUserAction as e:
    print(e)

finally: # tu się wrzuca instrukcje "sprzątające" przed ukończeniem skryptu

print("Koniec programu")