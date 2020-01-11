import przystanki
from pojazdy import kolowe
from pojazdy.szynowe import Tramwaj

def main():
    linie = [Tramwaj(1),
             Tramwaj(2),
             kolowe.Autobus(105),
             kolowe.Autobus(501)]
    print(przystanki.zbuduj_rozklad(linie))

if __name__ == "__main__":
    main()