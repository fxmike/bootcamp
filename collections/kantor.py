waluty = {"EUR" : 4.27, 'USD' : 3.87, 'CHF' : 3.88}
wymiana = None
portfel = {"EUR" : 0, 'USD' : 0, 'CHF' : 0,'PLN' : 0}
suma_PLN = []
print("Obsługiwane waluty:")
for waluta in waluty:
    print(waluta)


while True:
    q1 = input(str("Czy chcesz dokonać kupna/sprzedaży? [k/s]: "))

    if q1.lower() == 'k':
        q2 = str(input('Jaką walutę chcesz kupić?: ')).upper()

        if q2 in waluty:
            q3 = float(input("Ile chcesz na to przeznaczyć PLN?: "))
            wymiana = round(q3 / waluty[q2],2)
            print(f"Otrzymasz {wymiana} {q2}\n")
            portfel[q2] += wymiana
            suma_PLN.append(q3)
            e1 = input('Czy kończymy? [t/n]: ')
            if e1 == 't':
                break
            elif e1 == 'n':
                continue
            else:
                print('Podaleś błędne dane!')

        else:
            print("Nie podałeś poprawnej nazwy waluty")
            continue

    elif q1.lower() == 's':
        q4 = str(input('Jaką walutę chcesz sprzedać?: ')).upper()

        if q4 in waluty:
            q5 = float(input(f"Ile chcesz na to przeznaczyć {q4}?: "))
            wymiana = round(waluty[q4] * q5, 2)
            print(f"Otrzymasz {wymiana} PLN\n")
            portfel['PLN'] += wymiana
            e2 = input('Czy kończymy? [t/n]: ')
            if e2 == 't':
                break
            elif e2 == 'n':
                continue
            else:
                print('Podaleś błędne dane!')

    elif q1.lower() == "nie":
        break

    else:
        print("Podałeś błędne dane")
        continue

ending = len(f'Dziękujemy za skorzystanie z oferty kantoru. Dokonałeś transakcji '
             f'na łączną sumę {portfel["PLN"] + sum(suma_PLN)} PLN.\n') // 2
print(f'Dziękujemy za skorzystanie z oferty kantoru.\n{ending * "-"} \nDokonałeś transakcji na łączną '
      f'sumę {portfel["PLN"] + sum(suma_PLN)} PLN.')

print(len('  Twój portfel     ') * "-")
print('    Twój portfel   ')
print(len('| Twój portfel    |') * "-")
for curr, kwota in portfel.items():
    print(f"| {curr} : {kwota:9} |")

print(len('| Twój portfel    |') * "-")