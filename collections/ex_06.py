lst = [3, 6, 7, 4, 0, 2, 12, 54, 10, 11]
print(lst)
maxi = None
mini = None
index_max = 0
index_min = 0

#lista[n]
for n in lst:
    if mini == None or n < mini:
        mini = n
        index_min += 1
    if maxi == None or n > maxi:
        maxi = n
        index_max += 1
#
# maxx = lst.index(maxi)
# minn = lst.index(mini)
print(index_min)
print(index_max)
lst[index_max] = mini
lst[index_min] = maxi
print(lst)
# maxi = max(lst)
# mini = min(lst)
# maxi_spot = lst.index(maxi)
# mini_spot = lst.index(mini)
#
# lst[maxi_spot] = mini
# lst[mini_spot] = maxi
# print(lst)                      #drugi sposób