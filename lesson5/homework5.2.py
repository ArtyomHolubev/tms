x = int(input('Введите число: '))


def faktorial(a: int):
    j = 1
    for i in range(1, a+1):
        j *= i
    return j


result = faktorial(x)

print(f"Факториал числа {x}: {result}")
