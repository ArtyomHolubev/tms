from datetime import datetime


def tm(func):
    def wrapped(*args, **kwargs):
        time = datetime.now()
        result = func(*args, **kwargs)
        time_res = datetime.now() - time
        print(f'Время выполнения функции {func}: {time_res}')
        return result
    return wrapped


@tm
def count(a: list):
    dict_result = {}
    for i in a:
        if i in dict_result:
            dict_result[i] = dict_result[i]+1
        else:
            dict_result[i] = 1
    return dict_result

@tm
def faktorial(a: int):
    j = 1
    for i in range(1, a+1):
        j *= i
    return j


result_1 = faktorial(2)
result_2 = count([1, 2, 3, 3, 2, 1])
#
# print(result_1)
# print(result_2)
