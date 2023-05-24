x = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
y = [(3, 3, 3), (2, 2, 2), (1, 1, 1)]
z = [(2, 2, 2), (3, 3, 3), (4, 4, 4)]
x_list = [i[0] for i in x]
y_list = [i[1] for i in y]
z_list = [i[2] for i in z]

new_list = [a * b * c for a, b, c in zip(x_list, y_list, z_list)]
# print(x_list)
# print(y_list)
# print(z_list)

print(new_list)
