x1 = '200'
x2 = '200'
x3 = '200'
list1 = [1, 2, 3]
list2 = [1, 2, 3]

x1 = list(x1)
x2 = list(x2)
list1 = bool(list1)
list2 = bool(list2)


print(id(x1), id(x2))

print(id(list1), id(list2))


