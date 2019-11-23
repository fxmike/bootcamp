lst = [3, 6, 7, 4, 0, 2, 12, 54, 10, 11]

maxi = None
mini = None

for n in lst:
    if mini == None or n < mini:
        mini = n
    if maxi == None or n > maxi:
        maxi = n

maxx = lst.index(maxi)
minn = lst.index(mini)

 lst[maxx] = mini
lst[minn] = maxi
print(lst)