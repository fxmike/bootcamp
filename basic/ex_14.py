liczba_min = None          # w pythonie zmienna może być dowolnym typem
liczba_max = None


while True:
    q = input("Podaj liczbę lub napisz 'koniec': ")
    if q.lower() == "koniec":
        print("Dziękuję.")
        break

    if q == "" or not q.replace("-" , "").isdigit():   #trzeba dać metodę .replace() bo
        print("Nie podałeś liczby")                    #.isdigit() nie kuma liczb ujemnych
        continue

    #user podał liczbę
    liczba = int(q)
    if liczba_min == None or liczba < liczba_min:
        liczba_min = liczba
    if liczba_max == None or liczba > liczba_max:
        liczba_max = liczba


if liczba_min != None:
    print(f"Max to {liczba_max} i min to {liczba_min}")
else:
    print("Nie podałeś liczb")







