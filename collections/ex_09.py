produkty = {'ziemniaki' : 3.45,'marchew' : 1.24,'jabłka' : 2.43,'szynka' : 1.45, 'banany' : 0.76}
print("Do kupienia dziś:")


for tow in produkty:
    print(f'- {tow.capitalize()}')

q = input("Co chciałbyś kupić?: ").lower()
q2 = float(input("Ile kg?: "))

if q in produkty:
    print(f"Do zapłaty {round(q2 * produkty[q],2)}")
else:
    print(f"Niestety, {q} - brak na stanie!")

# do zrobienia: zrobić żeby klient mógł kupić więcej niż jedną rzecz
# q3 = input("Czy to wszystko (tak/nie): ")
# if q3.lower() == "tak":
#     break
# elif q3.lower() == "nie":
#     continue
# else:
#     print("Nie napisałeś tak/nie")
# BIBLIOTEKA - COLLECTIONS
