import json


def main():

    try:
        with open('employees.json') as f:
            imported_record = json.load(f)
    except json.decoder.JSONDecodeError:
        imported_record = []
    except FileNotFoundError:
        imported_record = []

    q1 = input('Co chcesz zrobić? [d - dodaj, w - wypisz] ')

    if q1 == "d":
        record = {'imie': None, 'nazwisko': None}

        imie = input('imie: ')
        record['imie'] = imie
        nazwisko = input('nazwisko: ')
        record['nazwisko'] = nazwisko

        imported_record.append(record)

        with open('employees.json', 'w') as f:
            json.dump(imported_record, f)

    elif q1 == 'w':
        for numer, dane in enumerate(imported_record):
            print(f'- [{numer + 1}] {dane["imie"]} {dane["nazwisko"]}')
if __name__ == "__main__":
    main()
