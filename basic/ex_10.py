p1 = int(input("Podaj pierwszą liczbę: "))
p2 = int(input("Podaj drugą liczbę: "))
p3 = input("Podaj rodzaj operacji: ")

if p3 == "+":
    print("Wynik to:", p1 + p2)
elif p3 == "-":
    print("Wynik to:", p1 - p2)
elif p3 == "*":
    print("Wynik to:", p1 * p2)
elif p3 == "/":
    if p2 != 0:
        print("Wynik to:", p1 / p2)
    else:
        print("Nie dzielimy przez 0")
else:
    print("Nieobsługiwany operator")


