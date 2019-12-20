# Question:
# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

s = input()
result = []
for num in s:
    if num.isdigit() and int(num) % 2 == 1:
        result.append(num)

print(",".join(result))

#DONE
