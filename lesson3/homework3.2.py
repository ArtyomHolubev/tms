name = input('Имя: ')
age = input("Возраст: ")

if not age.isdigit() or int(age) == 0:
    print('Ошибка, повторите ввод')

elif int(age) in range(1, 10):
    print(f'Привет, шкет {name}')

elif int(age) in range(10, 19):
    print(f'Как жизнь {name}?')

elif int(age) in range(19, 100):
    print(f'Что желаете {name}?')

else:
    print(f'{name}, вы лжете - в наше время столько не живут...')
