class Creature:
    def __init__(self, name):
        self.name = name

    def swim(self):
        pass

    def walk(self):
        pass

    def talk(self):
        pass


class Swimmer:
    def __init__(self, name):
        self.name = name

    def swim(self):
        pass


class Walker:
    def __init__(self, name):
        self.name = name

    def walk(self):
        pass


class Human(Swimmer, Walker):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")

    def talk(self):
        print(f"I'm {self.name} and I can talk")


class Fish(Swimmer):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")


class Cat(Swimmer, Walker):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")


human = Human("John Doe")
human.swim()
human.walk()
human.talk()

fish = Fish("Nemo")
fish.swim()

cat = Cat("Mr. Buttons")
cat.walk()
cat.swim()
cat.talk()
