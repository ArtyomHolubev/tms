class Auto:

    def __init__(self,
                 brand: str,
                 age: int,
                 mark: str,
                 color: str = None,
                 weight: int = None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    @staticmethod
    def move():
        print("move")

    @staticmethod
    def stop():
        print("stop")

    def birthday(self):
        self.age += 1


# lexus = Auto("Toyota", 3, "Lexus")
# lexus.birthday()
# lexus.stop()
# lexus.move()
# print(lexus.age)
