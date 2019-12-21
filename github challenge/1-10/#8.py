# Question:
# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

str_input = input()

lst = str_input.split(",")

a = sorted(lst)

print(",".join(a))

#DONE