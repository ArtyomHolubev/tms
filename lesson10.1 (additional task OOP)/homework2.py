import datetime


class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def year_of_birth(self):
        today = datetime.datetime.today().year
        return today - self.age

    @year_of_birth.setter
    def year_of_birth(self, value):
        self.year_of_birth = value

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name.lower() == other.name.lower() and self.age == other.age

    # def __ne__(self, other):
    #     if not isinstance(other, Person):
    #         return NotImplemented
    #     return self.name.lower() != other.name.lower() and self.age != other.age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

    def __le__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age <= other.age

    def __gt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age > other.age

    def __ge__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age >= other.age


person1 = Person('Alex', 34)
# ==
assert person1 == Person('Alex', 34)
assert person1 == Person('alex', 34)
assert person1 == Person('ALEX', 34)
# !=
assert person1 != Person('Alex!', 34)
assert person1 != Person('Alex', 35)
# >
assert person1 > Person('Alex', 33)
assert person1 > Person('Ann', 33)
# <
assert person1 < Person('Alex', 35)
assert person1 < Person('Ann', 35)
# >=
assert person1 >= Person('Alex', 34)
assert person1 >= Person('Alex', 33)
assert person1 >= Person('Ann', 34)
assert person1 >= Person('Ann', 33)
# <=
assert person1 <= Person('Alex', 34)
assert person1 <= Person('Alex', 35)
assert person1 <= Person('Ann', 34)
assert person1 <= Person('Ann', 35)
