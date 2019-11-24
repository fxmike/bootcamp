def pole_trapezu(h, a, b):
    """funkcja licząca pole trapezu"""
    return h * (a + b)/2

def pole_elipsy(promien, rozciagniecie=1):
    return (3.14 * kwadrat(promien)) * rozciagniecie

def kwadrat(n):
    return n ** 2


def test_pole_elipsy_z_rozciagnieciem():
    assert pole_elipsy(1,2) == 3.14 * 2
    assert pole_elipsy(promien=1,rozciagniecie=2) == 3.14 * 2
    assert pole_elipsy(rozciagniecie=2,promien=1) == 3.14 * 2

def test_pole_elipsy_bez_rozciagniecia():
    assert pole_elipsy(1) == pole_elipsy(1,1) == 3.14
    assert pole_elipsy(promien=1) == pole_elipsy(1,1) == 3.14
#   assert pole_elipsy(rozciagniecie=1) - błąd




#testy pole trapezu
def test_argumenty_pozycyjne():
    assert pole_trapezu(10, 3, 6) == 45

def test_argumenty_nazwane():
    assert pole_trapezu(h=10, a=3, b=6) == 45   # nie wolno dawać spacji przy argumentach
                                                # #to nie jest przypisanie do zmiennej to nazwanie argumetów

def test_argumenty_nazwane_nie_w_kolejnosci():
    assert pole_trapezu(a=3, b=6, h=10) == 45

def test_argumenty_nazwane_i_nienazwane():
    assert pole_trapezu(10, a=3, b=6) == 45     # keyword -> klucz=wartość, positional -> argument nienazwany (musi być pierwszy)