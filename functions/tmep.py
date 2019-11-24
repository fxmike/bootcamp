# def funkcja(imie ,*args, kupic="nic"):
#     print("funkcja ma imie", imie, "kupić", kupic, "i ma argumenty pozycyjne", args)
#     # if argumenty:
#     #     print("pierwszy argument to", args[0])
#     # for argument in args:
#     #     print(args, end=" ")
#     # print()
#
# funkcja("Burek",2,3,34)
# funkcja("Azor", [1, 5], {1: "a"})
# funkcja("Reksio", kupic ="kot")

# *args = tuple
# *kwargs = dict

def funkcja(*args, **kwargs):
    dzien_mies = kwargs.get('dzien', 1)

    print("Argumenty pozycyjne:")
    for wartosc in args:
        print("- ", wartosc)

    print("Argumenty nazwane (keyword):")
    for klucz, wartosc in kwargs.items():
        print("klucz", klucz, "- wartość", wartosc)
    print()


funkcja()
funkcja("alfa", "omega", dzien=24)
funkcja("beta", dzien=24, miesiac="listopad")