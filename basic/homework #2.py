lst = []

while len(lst) < 10:
    try:
        q = float(input("Podaj liczby (maksymalnie 10): "))
        lst.append(q)
        print(f"Lista ma już {len(lst)} elementów")
    except:
        print("Ops! Podałeś coś innego niż cyfra")
        # print(float(input("Podaj liczby (maksymalnie 10): ")))

print(f"Średnia liczb z listy wynosi: {sum(lst)/len(lst)}")