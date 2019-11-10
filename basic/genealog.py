pracounter = "pra"
rok = int(input("Podaj rok urodzenia postaci (przed 1960r.): "))
wiek = 2019 - rok
# print("Hej \"YOU\"")                                    #sposób na dodawanie cudzysłowia (backslash)

print(f"Ta osoba urodziła się przed {wiek} laty.")

if wiek <  60:
    print("Osoba zbyt młoda")

else:
    print("To mogła być Twoja", pracounter * (wiek // 30 - 2) +"babka")
