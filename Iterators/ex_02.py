def vowels(word):
    for x in word:
        if x in "aeiouy":
            yield x

for char in vowels('ala ma kota a kot ma ale'):
    print(char)

print("".join(vowels('ala ma kota a kot ma ale ')))