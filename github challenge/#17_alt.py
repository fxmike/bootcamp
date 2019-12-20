# Question:
# Write a program that computes the net amount of a bank account based a transaction
# log from console input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
account = 0

while True:

    q = input()
    lst = q.split(" ")

    if lst[0].upper() == "D":
        account += int(lst[1])

    elif lst[0].upper() == "W":
        account -= int(lst[1])

    if q == "":
        break

print(account)

#DONE