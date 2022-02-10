class Animal:
    # def __init__(self, attrs):
    #     self.attributes = attrs
    size = 1

    def __init__(self, name, age):
        self.attributes = {'name': name, 'age': age}

    def eat(self, amount=0):
        print("Ate some food!")

    @classmethod
    def calculate_weight(cls):
        return cls.size * 2


class Cat(Animal):
    size = 10

    # def __init__(self, size):
    #     self.size = size

    def eat(self, amount=0.1):
        if amount > 0.3:
            print("Can't eat that much!")
        else:
            print("Ate some cat food!")


class Dog(Animal):
    size = 30

    def eat(self, amount=0):
        print("Ate some dog food!")


# pluto = Dog({'name': 'Pluto', 'age': 3})
# goofy = Dog({'name': 'Goofy', 'age': 2})
# buttons = Cat(('Mr. Buttons', 4))
#
# animals = (pluto, goofy, buttons)
#
# for animal in animals:
#     if animal.attributes['age'] > 2:
#         print(animal.attributes['name'])

pluto = Dog('Pluto', 3)
goofy = Dog('Goofy', 2)
buttons = Cat('Mr. Buttons', 4)

animals = (pluto, goofy, buttons)

for animal in animals:
    print(animal.calculate_weight())
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])
