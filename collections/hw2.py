import string
lst = []
a = list(string.ascii_lowercase)

try:
    while len(lst) < 10:
        q = input("Podaj liczby (maksymalnie 10) lub wpisz 'koniec': ")

        if q.lower() == 'koniec':
            break
        elif q.lower() == "":
            print("Nie podałeś żadnej liczby!")
            continue
        elif q.lower() in a or q.lower()[0] in a:
            print("Podałeś literkę a nie cyferkę ;(")
        else:
            lst.append(float(q))
            print(f"Lista ma już {len(lst)} elementów")
    print(f"Liczby, które podałeś: {lst}")
    result = float(sum(lst)/len(lst))
    print(f"Średnia liczb z listy wynosi: {round(result,2)}")

except ZeroDivisionError:
    print("Ops, szybko kończysz!")

# jeden problem - co zrobić, żeby wracało gościa jak na początku od razu napisze koniec