# Question:
# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
lines = []

while True:
    line = input()

    if line:                    #świetne wykorzystanie TRUE/FALSE. Jeśli line = False to wyłamuje się z pętli
        lines.append(line)      #a wiadome, że jeśli string jest pusty to wtedy jest FALSE. GENIALNE!!!@#!@#!!!
    else:
        break

text = '\n'.join(lines).upper()
print(text)

#done z pomocą - nie wiedziałem, jak zrobić wielolinijkowy input. GENIALNA jest ta metoda powyżej!
