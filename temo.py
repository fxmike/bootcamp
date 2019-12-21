# def liczby():
#     for i in range(11):
#         yield i * 2
#
# for parzysta in liczby():
#     print(parzysta)

# for i in range(11):
#     print(i * 2)

def wznowienia():
    print("wstrzymuje dzialanie")
    yield 1
    print("wznawiam dzialanie")

    print("wstrzymuje dzialanie")
    yield 2
    print("wznawiam dzialanie")

for i in wznowienia():
    print("Zwrocono wartosc: " + str(i))