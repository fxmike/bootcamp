# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0],
#  [0, 1, 2, 3, 4],
#  [0, 2, 4, 6, 8]]

input_str = input()
dimensions = []

for x in input_str.split(","):          #trzeba input zamienić na listę
    dimensions.append(int(x))

print(dimensions)
print()
rowNum=dimensions[0]
print(rowNum)
colNum=dimensions[1]
print(colNum)

multilist = []

#teraz trzeba zrobić tak, żeby lista była podzielona na 3 mniejsze listy po 5 elementów
for row in range(rowNum):
    multilist.append(list())
    for col in range(colNum):
        multilist[row].append(0)
#WOW!

print()
print(multilist)

#a teraz trzeba zrobić żeby jechało to według wzoru zadania (podmienić 0 na liczby odpowiednie)

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col #każdy element jest mnożony przez każdy element z szyku. Nie do końca to kumam

print()
print(multilist)

#Done z pomocą. Trudne jak dla mnie
