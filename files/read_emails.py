#!/usr/bin/env python
import sys

def main(args):

    if len(args) < 2:
        print('Podaj nazwy plików')
        return

    emails_all = []
    emails_correct = []
    with open(args[0]) as f:   # otwieram plik wejściowy
        for line in f:
            emails_all.append(line.strip())

    for email in emails_all:
        if  email.count('@') ==  1:
            emails_correct.append(email.lower())

    emails_correct = sorted(set(emails_correct))

    with open(args[1], 'w') as f:  # tworzę plik i wrzucam posortowane i poczyszczone maile
        for email in emails_correct:
            f.write(f'{email} \n')

if __name__ == "__main__":
    main(sys.argv[1:])