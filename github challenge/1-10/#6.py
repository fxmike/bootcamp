# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24


def forumla(D=input(),C=50,H=30):
    res = []
    from math import sqrt
    D = D.split(",")
    for x in D:
        x = int(x)
        result = str(round(sqrt((2 * C * x) / H),))
        res.append(result)

    return ",".join(res)



print(forumla())

#Done ale z pomocą. Trzeba było zamienić result na str i dopiero potem zastosować metodę .join()

