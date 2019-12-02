def policz_znaki(napis,znacznik1="<",znacznik2=">"):
    counter = []
    new_lst = []
    czy_liczymy = 0

    for znak in napis:
        print(znak, end=" ")

        if znak == znacznik1:
            czy_liczymy += 1
            # print(czy_liczymy, end="* ")
        elif znak == znacznik2:
            czy_liczymy -= 1
            # print(czy_liczymy, end="* ")

        if czy_liczymy > 0:
            counter.append(znak * czy_liczymy)
            # print(counter)

    for elem in counter:
        new_lst += elem
    # print(new_lst)
    adj = new_lst.count(znacznik1) + new_lst.count(znacznik2)

    return len(new_lst) - adj


print(policz_znaki('<<<alan>>>'))



def test_pojedyncze_znaczniki_domyslne():
    assert policz_znaki('ala ma <kota> a kot <ma> ale') == 6

def test_pojedyncze_znaczniki_zmienione():
    assert policz_znaki('ala ma [kota] a kot [ma] ale', '[',']') == 6

def test_podwojne_znaczniki_zmienione():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[',']') == 18


#DO DOMU: Jak obsłużyć zagnieżdżenie