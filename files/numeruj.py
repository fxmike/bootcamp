#!/usr/bin/env python
import sys


def main():

    if len(sys.argv) < 2:
        print("użycie: numeruj.py PLIK")

    try:
        with open(sys.argv[1], encoding='utf-8') as f:

            for index, line in enumerate(f):
                print(f'{index + 1}: {line.strip()}')

    except FileNotFoundError:
        print("Podano nieistniejący plik")

if __name__ == "__main__":
    main()