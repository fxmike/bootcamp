lista = list(range(5))
print(lista)
# list_neg = []
# list_pos = []
# for num in lista:
#     if num < 0:
#         list_neg.append(num)
#     elif num > 0:
#         list_pos.append(num)
ilosc_dod = 0
ilosc_uj = 0

for num in lista:
    if num > 0:
        ilosc_dod += 1
    elif num < 0:
        ilosc_uj += 1


print(f"Jest {ilosc_dod} dodatnich i {ilosc_uj} ujemnych")