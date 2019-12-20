def binary_search(list,item):
    counter = 1
    low = 0
    high = len(list) - 1
    print(*list)
    print(len(list))
    print()
    while low <= high:
        mid = (low + high) // 2  #określenie środka
        guess = list[mid]        #określenie "zgadnięcia" jako środek listy
        print("M:",mid, "G:",guess, end="\n")

        if guess == item:
            return(f"Miejsce szukanej liczy w liście: {mid}. Zajęło to {counter} ruchów")

        if guess > item:
            high = mid - 1
            counter += 1
        else:
            low = mid + 1
            counter += 1

    return "Obiekt nie należy do listy"

my_list = range(1,257)

print(binary_search(my_list, 3))

import math
a = math.log2(256)          #obliczenie ile maksymalnie prób potrzeba by zgadnąć liczbę w danym zakresie
print(a)