#Napisz program zliczajacy liczbe wystapien kazdego znaku w podanym przez uzytkownika napisie. (użyj słownika)

string = "klapaucius"
dic = {}

# opcja 1
# for s in string:
#     if s in dic:
#         dic[s] += 1
#     else:
#         dic[s] = 1
#
# # print(dic)

#opcja 2

for s in string:
    dic[s] = dic.get(s, 0) + 1

for literka, ilosc in dic.items():
    print(f"{literka!r} : {ilosc}")

# opcja 3
# poczytać o defaultdict