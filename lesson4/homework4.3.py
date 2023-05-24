my_list = list(range(1, 101))
filter_list = [x for x in my_list if x % 10 == 0]
new_list = [x * 10 if x % 4 != 0 else x * 2 for x in filter_list]
print(filter_list)
print(new_list)
