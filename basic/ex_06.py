pytanie = int(input("Podaj liczbę: "))

# print("Większa od 10: ", pytanie > 10)
# print("Mniejsza równa 15: ", pytanie <= 15)
# print("Podzielna przez 2: ", pytanie % 2 == 0)

print(f"""Większa od 10: {pytanie > 10}
Mniejsza równa 15: {pytanie <= 15}
Podzielna przez 2: {pytanie % 2 == 0}
Jest nieparzysta, podzielna przez 3 i większa od 10 lub jest to liczba 7: {pytanie % 2 != 0 and pytanie % 3 == 0 and 
                                                                           pytanie > 10 or pytanie == 7}""")