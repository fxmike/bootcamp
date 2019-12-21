# Zaimplementuj funkcję spłaszczającą podaną listę.
# Przykład użycia:
# [1, 2, 3, 4, 5, 6, 7]



def splaszcz(num):
    new = []

    for x in num:
        if isinstance(x, list):
            for subelement in splaszcz(x):
                new.append(subelement)
        else:
            new.append(x)

    return(new)

print(splaszcz([1, 2, 3, [4, 5, [6]], 7]))

def test_flat_list():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

def test_one_embedded_list():
    assert splaszcz([1,[2, 3]]) == [1, 2, 3]

def test_flat_list_2():
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]
