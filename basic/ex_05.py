miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
dystans_ab = float((input(f"Dystans {miasto_a}-{miasto_b}: ")))
cena_paliwa = float((input("Cena paliwa: ")))
spalanie = float((input("Spalanie na 100km: ")))
spalanie_100 = dystans_ab / 100 * cena_paliwa * spalanie

print(f"""Miasto A: {miasto_a}
Miasto B: {miasto_b}
Dystans {miasto_a}-{miasto_b}
Cena paliwa: {cena_paliwa}
Spalanie na 100km: {spalanie}""")

print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {int(spalanie_100)} PLN")