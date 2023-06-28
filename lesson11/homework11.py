import random


class RandomValue:
    def __init__(self, limit, *args):
        self._list = list(args)
        self._limit = limit

    def __str__(self):
        return f"MyList object: {self._list}"

    def __iter__(self):
        return RandomValueIterator(self._list, self._limit)


class RandomValueIterator:

    def __init__(self, some_list, some_limit):
        self._some_list = some_list
        self._some_limit = some_limit
        self._curr_index = 0
        for element in range(0, self._some_limit):
            self._some_list.append(random.randint(1, 101))

    def __iter__(self):
        return self

    def __next__(self):
        if self._curr_index < self._some_limit:
            result = self._some_list[self._curr_index]
            self._curr_index += 1
            return result
        else:
            raise StopIteration("Iterator is stopped!")

my_limit = int(input("Введите лимит: "))
my_random = RandomValue(limit=my_limit)

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None



# class RandomValue:
#     def __init__(self, limit, *args):
#         self._list = list(args)
#         self.limit = limit
#         for element in range(0, self.limit):
#             self._list.append(random.randint(1, 101))
#
#     def __str__(self):
#         return f"MyList object: {self._list}"
#
#     def __iter__(self):
#         return RandomValueIterator(self._list)
#
#
# class RandomValueIterator:
#
#     def __init__(self, some_list):
#         self._some_list = some_list
#         self._size = len(self._some_list)
#         self._curr_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._curr_index < self._size:
#             result = self._some_list[self._curr_index]
#             self._curr_index += 1
#             return result
#         else:
#             print("Iterator is stopped!")
#             raise StopIteration

