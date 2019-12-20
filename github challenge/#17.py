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

    q = input("D or W: ")
    q2 = input("How much: ")

    if q.lower() == "d" and q2.isdigit():
        account += int(q2)
    elif q.lower() == "w" and q2.isdigit():
        account -= int(q2)
    elif q == "" and q2 == "":
        break
    else:
        print("Nie podałeś właściwej danej")
        continue

print(account)

#DONE!