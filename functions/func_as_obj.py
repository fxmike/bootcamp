def dodaj(a,b):
    return a+b
def odejmij(a,b):
    return a-b

liczba = int(input("liczba 1: "))
liczba2 = int(input("liczba 2: "))
operacja = input("+ czy -? ")

if operacja == "+":
    funkcja = dodaj
else:
    funkcja = odejmij

print(   funkcja(liczba,liczba2)    )