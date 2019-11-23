liczby = []

while len(liczby) < 10:

    dana = input("Wpisz liczbe lub 'koniec': ")
    dana = dana.strip()
    if not dana:                                    #sprawdzenie, jeśli string jest pusty (FALSE)
        print("Nic nie podałeś")
        continue
    if dana.lower() == 'koniec':
        break
    if not dana.replace("-","").isdigit():
        print("Obsługuję tylko liczby całkowite i 'koniec'")
    dana = int(dana)
    liczby.append(dana)

if liczby:                                          #sprawdzenie, czy zmienna są True czy False (bool(liczby))
    print("Średnia to", sum(liczby)/len(liczby))
else:
    print("Nie podałeś żadnej liczby")