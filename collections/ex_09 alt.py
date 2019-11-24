produkty = {'ziemniaki' : 5,'marchew' : 1.24,'jabłka' : 2,'szynka' : 1.45, 'banany' : 0.76}
print("Do kupienia dziś:")
kasa = []
for tow in produkty:
    print(f'- {tow.capitalize()}')

while True:
    q = input("Co chciałbyś kupić?: ").lower()
    try:
        q2 = float(input("Ile kg?: "))
        kasa.append(produkty[q] * q2)

    except:
        print("Podałeś literę/słowo. Jeszcze raz: ")
        continue


    if q in produkty:
        koniec = input("Czy to wszystko (tak/nie): ")
        if koniec.lower() == "tak":
            break
        elif koniec.lower() == "nie":
            pass
    else:
        print(f"Niestety, {q} - brak na stanie!")
        q3 = input("Czy chcesz dodać produkt (tak/nie): ")
        while True:
            if q3.lower() == "tak":
                n_prod = input("Co chcesz dodać?: ")
                n_prod_cena = float(input(f"Cena/KG za {n_prod}: "))
                produkty[n_prod] = n_prod_cena
                print(produkty)
                break

print(f"Do zapłaty {float(sum(kasa))} PLN")


# do zrobienia: zrobić żeby klient mógł kupić więcej niż jedną rzecz
# q3 = input("Czy to wszystko (tak/nie): ")
# if q3.lower() == "tak":
#     break
# elif q3.lower() == "nie":
#     continue
# else:
#     print("Nie napisałeś tak/nie")
# BIBLIOTEKA - COLLECTIONS
