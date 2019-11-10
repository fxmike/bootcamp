x = int(input("Podaj pozycję x: "))
y = int(input("Podaj pozycję y: "))

# if 0 <= x <= 10 and 0 <= y <= 10:
#     print("Gracz znajduje się w lewym dolnym rogu")
# elif 0 <= x <= 10 and  10 < y < 90 :                     # można dawać porównania jak z matmy, że 10 < x < 90 i to
#     print("Gracz znajduje się przy lewej krawędzi")      # rozpatruje jak na matmie
# elif 0 <= x <= 10 and 100 >= y >= 90:
#     print("Gracz znajduje się w lewym górnym rogu")
# elif 10 < x < 90 and 0 <= y <= 10:
#     print("Gracz znajduje się w dolnej krawędzi")
# elif 10 < x < 90 and 10 < y < 90:
#     print("Gracz znajduje się w centrum")
# elif 10 < x < 90 and 100 >= y >= 90:
#     print("Gracz znajduje się w górnej krawędzi")
# elif 100 >= x >= 90 and 0 <= y <= 10:
#     print("Gracz znajduje się w prawym dolnym rogu")
# elif 100 >= x >= 90 and 10 < y < 90:
#     print("Gracz znajduje się przy prawej krawędzi")
# elif 100 >= x >= 90 and 100 >= y >= 90:
#     print("Gracz znajduje się w prawym górnym rogu")
#
# else:
#     print("Gracz poza planszą")

# da się to zrobić tak, żeby przyjąć pierwsze porównanie ( 0 <= x <= 10) i do tego zagnieżdżać kolejne warunki
# oparte na porówaniu "y"
if x < 0 or x > 100 or y < 0 or y > 100:
    print("Poza planszą")

elif x <= 10:
    if y <= 10:
        print("Lewy dolny róg")
    elif y >= 90:
        print("Lewy górny róg")
    else:
        print("Lewa krawędź")

elif x >= 90:
    if y <= 10:
        print("Prawy dolny róg")
    elif y >= 90:
        print("Prawy górny róg")
    else:
        print("Prawa krawędź")

elif 10 < x < 90:
    if y <= 10:
        print("Dolna krawędź")
    elif 10 < y < 90:
        print("Centrum")
    elif y >= 0:
        print("Górna krawędź")