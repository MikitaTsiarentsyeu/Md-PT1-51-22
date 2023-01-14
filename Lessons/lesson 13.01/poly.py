class Animal:

    def hello(self):
        print("hello")

class Dog(Animal): pass

    # def hello(self):
    #     print("bark!")

class Cat(Animal):

    def hello(self):
        print("nya")

a = Animal()
d = Dog()
c = Cat()

for elem in [a, d, c]:
    elem.hello()