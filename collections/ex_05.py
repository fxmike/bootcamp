# print("ala", end='') ----> to pozwala printować kolejny, poniższy wydruk doklejony do tego
# print(f">{12:5}<") #po dwukropku mówimy ile miejsca ma zająć dany string

# print(f">{12:5}<")
print("   ", end="")
for y in range(10):
    print(f"{y:3}", end="")
print()
print()

for x in range(10):
    print(x, end="  ")
    for y in range(10):
        print(f"{x * y:3}", end="")

    print()                        # najpierw kończy się wewnętrzny for i tworzy się nowa linijka