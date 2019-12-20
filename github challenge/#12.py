# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def is_even():
    lst = []
    for num in range(1000,3001):
        if num % 2 == 0:
            lst.append(str(num))

    return ",".join(lst)

print(is_even())

#DONE