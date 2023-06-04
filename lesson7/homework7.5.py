x = input('Введите число: ')


def check(x: str):
    if x.isdigit():
        y = f'Вы ввели положительное целое число: {x}'
    elif x[0] == '-':
        if x[1:].isdigit():
            y = f'Вы ввели отрицательно целое число: -{x[1:]}'
        elif x[1:].replace(",", "", 1).isdigit() or x[1:].replace(".", "", 1).isdigit():
            y = f'Вы ввели отрицательно дробное число: -{x[1:]}'
        else:
            y = f'Вы ввели некорректное значение: {x}'
    elif x.replace(",", "", 1).isdigit() or x.replace(".", "", 1).isdigit():
        y = f'Вы ввели дробное число: {x}'
    else:
        y = f'Вы ввели некорректное значение: {x}'
    return y


print(check(x))
