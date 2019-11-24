def policz_znaki(napis,znacznik1="<",znacznik2=">"):
    counter = 0
    czy_liczymy = False
    for znak in napis:
        if znak == znacznik1:
            czy_liczymy = True
        elif znak == znacznik2:
            czy_liczymy = False
        elif czy_liczymy:
            counter += 1

    return counter




print(policz_znaki('ala ma <kota> a kot <ma> ale'))



def test_pojedyncze_znaczniki_domyslne():
    assert policz_znaki('ala ma <kota> a kot <ma> ale') == 6


#DO DOMU: Jak obsłużyć zagnieżdżenie