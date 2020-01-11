#import dzialania.b #import wykonuje wszystko co jest w importowanym pliku
from dzialania import b

def powitanie():
    print('cześć')


x = input('podaj x: ')
y = input('podaj y: ')
dzialanie = input('podaj dzialanie: ')

if x == "pi":
    x = b.pi
else:
    float(x)
if y == 'pi':
    y = b.pi
else:
    float(y)

if dzialanie == "+":
    wynik = b.dodawanie(float(x), float(y))
elif dzialanie == "-":
    wynik = b.odejmowanie(float(x), float(y))


print(wynik)

# uważać na nazwy plików, które się importuje. na przykład, żeby się to nie nazywało
# jak biblioteki pythona