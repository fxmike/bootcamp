# Question:
# Write a program which accepts a sequence of comma separated 4 digit
# binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# s = input().split(",")
# lst = []
# for num in s:
#     num = int(num,2)
#     if num % 5 == 0:
#         lst.append(num)
#
# print(lst)

value = []

items=[]
s = input().split(",")
for num in s:
    items.append(num)

for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(value)

#done z pomocą. Rozwiązanie jest z dupy strony a liczba binarna jest traktowana jako string. Miałem dobre rozwiązanie,
#ale nie byłem w stanie przeformatować liczby niebinarnej na poprawną binarną.