#Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
# Sprawdź jak dużo z tych liczb jest liczbami parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu.
#Zamiast programu proszącego użytkownika o wpisanie kolejnych liczb, można napisać funkcję przyjmującą jako argument
# listę liczb - i napisać do niej testy, bo już umiemy

lst = [1, 2, 67, 23, 13, 15, 141, 2, 1, 3 , 5, 14, 66]

s = set(lst)
def lst_count(lst):
    e = []
    for num in lst:
        if num % 2 == 0:
            e.append(num)
    return e


print(f"Liczba unikalnych liczb w zbiorze wynosi: {len(s)}")
print(f'Sposród liczb, które podałeś parzyste to: {lst_count(lst)}')