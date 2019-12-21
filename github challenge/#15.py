# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

s = input()

s2 = s * 2
s3 = s * 3
s4 = s * 4

result = int(s) + int(s2) + int(s3) + int(s4)
print(result)

#DONE