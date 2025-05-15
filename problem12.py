list1 = [3, 5, 7, 4, 8, 8]

list2 = [4, 9, 8, 7, 1, 1, 13]

intersection_list = list(set(list1).intersection(list2))
sum = 0
for item in intersection_list:
    sum += item

print(sum)