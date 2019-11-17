from random import randrange

#określenie pozycji gracza
gracz_x = randrange(0,10)
gracz_y = randrange(0,10)
pozycja_gracz = [gracz_x, gracz_y]
print(f"Pozycja gracza: {pozycja_gracz}")

#określenie pozycji skarbu; skarb nie może być w tym samym miejscu co gracz",
skarb_x = randrange(0,10)
skarb_y = randrange(0,10)
pozycja_skarb = [skarb_x, skarb_y]
#print(f"Pozycja skarbu: {pozycja_skarb}")

dystans_gs = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)


counter = 0                     #licznik ruchu
nowa_pozycja = pozycja_gracz    #pozycja po ruchu

#test czy jest na mapie
while  0 <= nowa_pozycja[0] < 10 and 0 <= nowa_pozycja[1] < 10:
    #test czy wygrał:
    if nowa_pozycja != pozycja_skarb:
        #ruch!
        ruch = str(input("Dokąd idziemy? [w,s,a,d]: "))
        # odległość gracza względem skarbu
        diff_x = abs(pozycja_skarb[0]-nowa_pozycja[0])
        diff_y = abs(pozycja_skarb[1]-nowa_pozycja[1])

        #ciepło zimno nie może być w kontekście położenia początkowego tylko w kontekście różnicy obecnej pozycji i
        #pozycji po 1 ruchu

        if ruch == "w":
            nowa_pozycja[1] += 1            #przesunięcie gracza
            print("Góra!", nowa_pozycja)
            counter += 1                    #licznik ruchów
            if diff_x + abs(pozycja_skarb[1] - nowa_pozycja[1]) > diff_x + abs(pozycja_skarb[1] - nowa_pozycja[1]-1):
                print("Ciepło")
            else:
                print("Zimno")
        elif ruch == "s":
            nowa_pozycja[1] -= 1
            print("Dół!",nowa_pozycja)
            counter += 1
            if diff_x + abs(pozycja_skarb[1] - nowa_pozycja[1]) < diff_x + abs(pozycja_skarb[1] - nowa_pozycja[1]-1):
                print("Ciepło")
            else:
                print("Zimno")
        elif ruch == "d":
            nowa_pozycja[0] += 1
            print("Prawo!",nowa_pozycja)
            counter += 1
            if diff_y + abs(pozycja_skarb[0] - nowa_pozycja[0]) > diff_y + abs(pozycja_skarb[0] - nowa_pozycja[0]-1):
                print("Ciepło")
            else:
                print("Zimno")
        elif ruch == "a":
            nowa_pozycja[0] -= 1
            print("Lewo!", nowa_pozycja)
            counter += 1
            if diff_y + abs(pozycja_skarb[0] - nowa_pozycja[0]) < diff_y + abs(pozycja_skarb[0] - nowa_pozycja[0]-1):
                print("Ciepło")
            else:
                print("Zimno")
        else:
            print("Nie wprowadziłeś kierunku! Podaj go jeszcze raz: ", ruch)
    else:
        print(f"Koniec gry. Wykonałeś {counter} ruchów by dotrzeć do skarbu! Minimalna ilość ruchów by do niego \n"
              f"dotrzeć to {dystans_gs}")
        break
else:
    print("Gracz poza mapą! Koniec gry!")
    #koniec gry
    #gamoń jak się cofa to nie wiedzieć czemu pokazuje ciepło

#czy pozycja skarbu jest w tym samym miejscu (na razie zawieszone)
# if pozycja_gracz == pozycja_skarb:
#     print("Gracz i skarb w tym samym miejscu!")
#     pozycja_skarb[0] = randrange(0, 9)
#     pozycja_skarb[1] = randrange(0, 9)
#     print("Pozycja skarbu to:", pozycja_skarb)