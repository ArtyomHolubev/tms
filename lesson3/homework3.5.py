import random

random_number = random.randint(0, 10000)
number = int(input(("Угадай число: ")))
#print(random_number)

while random_number != number:
    if random_number > number:
        number = int(input(("Маловато будет: ")))
    else:
        number = int(input(("Перебор: ")))
print('Угадал! Молодец!')
