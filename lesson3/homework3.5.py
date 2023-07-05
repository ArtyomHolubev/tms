import random

# random_number = random.randint(0, 10000)
# number = int(input(("Угадай число: ")))
# #print(random_number)
#
# while random_number != number:
#     if random_number > number:
#         number = int(input(("Маловато будет: ")))
#     else:
#         number = int(input(("Перебор: ")))
# print(f'Угадал! Молодец! Да, я загадал число {number}')
my_list = []
for i in range(0, 50):
    my_list.append(random.randint(0,50))

print(my_list)
