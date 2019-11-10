# mon = float(input("Podaj temperaturę (pon): "))
# tue = float(input("Podaj temperaturę (wt): "))
# wed = float(input("Podaj temperaturę (śr): "))
# thu = float(input("Podaj temperaturę (czw): "))
# fri = float(input("Podaj temperaturę (pt): "))
# sat = float(input("Podaj temperaturę (sob): "))
# sun = float(input("Podaj temperaturę (nd): "))
#
# average = (mon + tue + wed + thu + fri + sat + sun) / 7)
#
# print("Średnia temperatur wynosi",average,"stopni Celsiusza")
#
day_count = 1
sum = 0

while day_count < 8:
    sum += float(input(f"Podaj temp dla dnia {day_count}: "))
    day_count += 1

print(f"średnia wynosi {sum/7:.2f }")       # float dla f-string
print("średnia wynosi", round(sum/7,2))

