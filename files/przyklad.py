with open('example.txt') as f:
    for line in f:
        print(line.strip())


with open('example.txt') as f:
    for line in f:
        if line.strip:
            print(line.strip())
