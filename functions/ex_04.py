def formatuj(*args, **kwargs):
    sbl = "$"
    lst = []
    dic = {}

    for arg in args:                #dzielę zdania na słowa i wrzucam do listy. Tworzą się dwie listy z dzielonymi słowami
        a = arg.split()
        lst.append(a)

    for keys,values in kwargs.items():  #tworzę słownik ze słowami kluczowymi "$" i ich wartościami
        key = sbl + keys
        dic[key] = kwargs[keys]

    flat_lst = []

    for subelem in lst:             # z listy lst wydzielam pojedyncze słowa
        for item in subelem:
            flat_lst.append(item)

    for k, v in dic.items():
        word_idx = flat_lst.index(k)
        print(word_idx)
        for word in flat_lst:
            if word == k:
                print(True)

    print()
    print(flat_lst)
    print()
    print(dic)
    print()

    return
    # return " ".join(flat_lst)


print(formatuj('koszt $cena PLN', 'kwota $koszt brutto', cena=10, koszt=1))


# print(formatuj('Podróż z $miasto1 do $miasto2 zajmuje $czas h', miasto1="Los Angeles", miasto2="Yorktown", czas=5))


# def test_koszt_cena():
#      assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto'
