# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

s = input()
let_ct = 0
num_ct = 0
for letter in s:
    if letter.isalpha():
        let_ct += 1
    elif letter.isdigit():
        num_ct += 1

print("Letters",let_ct)
print("Digits", num_ct)

#DONE