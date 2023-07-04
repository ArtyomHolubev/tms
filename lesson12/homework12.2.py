import random


class RandomValue:
    def __init__(self, limit, *args):
        self._some_list = list(args)
        self._limit = limit
        for element in range(0, self._limit):
            self._some_list.append(random.randint(1, 100))

    def __str__(self):
        return f"MyList object: {self._some_list}"

    def __iter__(self):
        for element in self._some_list:
            yield element
        return print("iterator is stopped")


my_limit = int(input("Введите лимит: "))
my_random = RandomValue(limit=my_limit)

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None


