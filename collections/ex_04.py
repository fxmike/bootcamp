counter = 0
new_lst = []
print("Liczby podzielne przez 3 lub 5: ")

for n in range(101):
    if n % 3 == 0 or n % 5 == 0:
        print(n)
        counter += 1
        new_lst.append(n)

print(f"Ilość liczb podzielnych przez 3 lub 5: {counter}, a liczby te to: \n{new_lst}")
