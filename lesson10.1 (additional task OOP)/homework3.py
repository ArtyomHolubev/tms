class Parent1:
    person: str


class Parent2:
    person: str


class Parent3:
    person: str


class MyClass(Parent1, Parent2, Parent3):
    person: str

    def __init__(self, person):
        self.person = person

    def __getitem__(self, item):
        try:
            if 0 <= item < len(self.person):
                return self.person[item]
            else:
                raise IndexError("Неверный индекс")
        except IndexError as err:
            print(err)

    def __setitem__(self, item, value):
        if isinstance(item, int):
            self.person[item] = value
        elif isinstance(item, slice):
            raise ValueError('Cannot interpret slice with multiindexing')
        else:
            for i in item:
                if isinstance(i, slice):
                    raise ValueError('Cannot interpret slice with multiindexing')
                self.person[i] = value


    def get_attribute(self, attribute_name):
        if attribute_name in self.__dict__.keys():
            print(f"Attribute {attribute_name} found in Instance: {self}")
            return self.__dict__[attribute_name]
        # elif attribute_name not in self.__dict__.keys():
