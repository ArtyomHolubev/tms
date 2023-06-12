import time


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


class Truck(Auto):

    def __init__(self,
                 brand: str,
                 age: int,
                 mark: str,
                 max_load: int,
                 color: str = None,
                 weight: int = None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    @staticmethod
    def load():
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):

    def __init__(self,
                 brand: str,
                 age: int,
                 mark: str,
                 max_speed: int,
                 color: str = None,
                 weight: int = None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


scania = Truck(brand="HZ", age=3, mark="SCANIA", max_load=3000, color="White", weight=35000)

print(scania.brand, scania.age, scania.mark, scania.max_load, scania.color, scania.weight, sep="\n")
scania.move()
scania.load()
scania.birthday()
print(scania.age)
scania.stop()

print("**********************************")

volvo = Truck(brand="HZ", age=5, mark="VOLVO", max_load=3500, color="Black", weight=40000)
print(volvo.brand, volvo.age, volvo.mark, volvo.max_load, volvo.color, volvo.weight, sep="\n")
volvo.move()
volvo.load()
volvo.birthday()
print(volvo.age)
volvo.stop()

print("**********************************")
print("**********************************")

vw = Car(brand="VW", age=30, mark="Golf", max_speed=35, color="Blue", weight=1500)
print(vw.brand, vw.age, vw.mark, vw.max_speed, vw.color, vw.weight, sep="\n")
vw.move()
vw.birthday()
print(vw.age)
vw.stop()

print("**********************************")

bmw = Car(brand="BMW", age=5, mark="X1", max_speed=250, color="Black", weight=3300)
print(bmw.brand, bmw.age, bmw.mark, bmw.max_speed, bmw.color, bmw.weight, sep="\n")
bmw.move()
bmw.birthday()
print(bmw.age)
bmw.stop()
