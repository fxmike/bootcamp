from mathematica.geometry import figures

def test_suqare_area():
    assert figures.square_area(2) == 4

def test_triangle_area():
    assert figures.triangle_area(6,3) == 9