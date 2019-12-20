# Question:
# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# q = input("Podaj liczby oddzielone przecinkiem: ")
#
# q = list(q)
# for elem in q:
#     if elem == ",":
#         q.remove(elem)
# print(q)
# q = tuple(q)
# print(q)

# 2 rozwiązanie
values = input()
l = values.split(",")    # funkcja split dzieli wg tego samego znaku i tworzy listę
t = tuple(l)
print(l)
print(t)

#done