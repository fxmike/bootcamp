# Zaimplementuj funkcję spłaszczającą podaną listę.
# Przykład użycia:

# [1, 2, 3, 4, 5, 6, 7]

new = []

def splaszcz(num):

    for x in num:
        if isinstance(x, list):
            splaszcz(x)
        else:
            new.append(x)

    return(new)

print(splaszcz([1, 2, 3, [4, 5, [6]], 7]))

