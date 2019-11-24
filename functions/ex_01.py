def czy_pierwsza(num):
    if num <= 1:
        return False

    for i in range(2,num):
        if num % i == 0:
            return False

    return True
def test_mniejsza_od_2():
    assert czy_pierwsza(1) == False
def test_nie_pierwsza_nieparzysta():
    assert czy_pierwsza(9) == False
def test_nie_pierwsza_parzysta():
    assert czy_pierwsza(10) == False
def test_pierwsza_2():
    assert czy_pierwsza(2) == True
def test_pierwsza_wieksza_od_2():
    assert czy_pierwsza(17) == True

# assert => komenda do testów!