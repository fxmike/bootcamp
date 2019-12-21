# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

s = input()
up_ct = 0
low_ct = 0

for letter in s:
    if letter.isupper():
        up_ct += 1
    elif letter.islower():
        low_ct += 1

print("Upper case",up_ct)
print("Lower case", low_ct)

#DONE