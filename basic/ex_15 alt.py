from random import randrange

gracz_x = randrange(0,10)
gracz_y = randrange(0,10)

skarb_x = randrange(0,10)
skarb_y = randrange(0,10)

krok = 0

odleglosc_poczatkowa = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

while True:
    odleglosc_przed_ruchem = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    kierunek = input("Podaj kierunek: w/a/s/d: ").lower()

    if kierunek == "w":
        gracz_y += 1
    elif kierunek == "s":
        gracz_y -= 1
    elif kierunek == "a":
        gracz_x -= 1
    elif kierunek == "d":
        gracz_x += 1
    else:
        print("Obsługiwane są tylko kierunki w/a/s/d")
        continue

    oleglosc_po_ruchu = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    krok += 1
    #ciepło / zimno

    if (gracz_x == skarb_x) and (gracz_y == skarb_y):
        print(f"Znalazłeś skarb w {krok} krokach. Minimalna ilość kroków do skarbu to: {odleglosc_poczatkowa}")
        #ile kroków
        break

    if randrange(0,5) == 0:                      #z prawdopodobieństwem 1/5 nie dawaj podpowiedzi
        print("nie dostajesz podpowiedzi")
    elif odleglosc_przed_ruchem > oleglosc_po_ruchu:
        print("ciepło!")
    else:
        print("zimno!")

    # print("Gracz: ",gracz_x, gracz_y)