p1 = int(input("Podaj d2ługość pierwszego podstawy opakowania (cm): "))
p2 = int(input("Podaj długość drugiego boku podstawy opakowania (cm): "))
h = int(input("Podaj wysokość podstawy opakowania (cm): "))
v = p1 * p2 * h

print(f"Objętość opakowania wynosi: {v} cm\u00B3")

if v > 1000:
    print("Za duża objętość! Większa niż 1 L")
    nadmiar = v - 1000
    print("Za dużo o", nadmiar,"cm\u00B3")
else:
    print(f"Czy objętość opakowania jest większa od 1 litra: Nie")

