from dataclasses import dataclass


@dataclass(frozen=True)
class MyDataClass:
    a: str
    b: int
    c: list

    @classmethod
    def build(cls, a: str, b: int, c: list):
        cls.a = a
        cls.b = b
        cls.c = c
        if not (isinstance(cls.a, str) and isinstance(cls.b, int) and isinstance(cls.c, list)):
            raise TypeError("invalid parameters")
        return cls.a, cls.b, cls.c


person1 = MyDataClass.build("TEST", 34, [1, 2, 3])  # valid parameters
print(person1)
try:
    person2 = MyDataClass.build(100, 33, [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", "33", [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", 33, (1, 2, 3))  # invalid parameters
except Exception as exc:
    print(exc)





