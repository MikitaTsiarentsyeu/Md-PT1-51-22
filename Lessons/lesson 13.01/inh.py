class Animal:

    def __init__(self, name):
        print("animal init")
        self.name = name

    def say_hello(self):
        print(f"hello, my name is {self.name}")

    def eat(self, smtng):
        print(f"eating {smtng}")

    def phe(self):
        print("phe...")

class Dog(Animal):

    def __init__(self, name, breed):
        # Animal.__init__(self, name)
        super().__init__(name)
        self.breed = breed

    def hunt(self, smtng):
        print(f"hunting for {smtng}")

    def say_hello(self):
        print(f"hello, I'm {self.name}, the {self.breed}")

d = Dog("Zephyrka", "wss")
d.say_hello()

d.hunt("mouse")

print(type(d))
print(isinstance(d, Dog))
print(isinstance(d, Animal))


class Food:

    def __init__(self, type) -> None:
        self.type = type

class Carnivore(Animal):

    def eat(self, smtng:Food):
        if not isinstance(smtng, Food):
            return
        if smtng.type == "meat":
            Animal.eat(self, smtng)
        else:
            super().phe()

class Herbivore(Animal):

    def eat(self, smtng:Food):
        if not isinstance(smtng, Food):
            return
        if smtng.type == "plant":
            Animal.eat(self, smtng)
        else:
            super().phe()

    def phe(self):
        return super().phe()

class Omnivore(Carnivore, Herbivore):

    def eat(self, smtng: Food):
        if not isinstance(smtng, Food):
            return
        if smtng.type == "plant":
            Herbivore.eat(self, smtng)
        elif smtng.type == "meat":
            Carnivore.eat(self, smtng)
        else:
            super().phe()


human = Omnivore("test name")
meat = Food("meat")
grass = Food("plant")

human.eat(meat)
human.eat(grass)
print(Animal.__mro__)
print(Herbivore.__mro__)
print(Carnivore.__mro__)
print(Omnivore.__mro__)