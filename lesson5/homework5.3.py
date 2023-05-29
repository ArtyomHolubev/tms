my_list = [1, 2, 3, 3, 2, 1]


def count(a: list):
    dict_result = {}
    for i in a:
        if i in dict_result:
            dict_result[i] = dict_result[i]+1
        else:
            dict_result[i] = 1
    return dict_result


result = count(my_list)

print(result)
