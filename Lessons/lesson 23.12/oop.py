class Dog:

    name = ""
    color = ""
    breed = ""

    def Sleep(self):
        print("I'm sleeping, leave me alone...")

    def Bork(self):
        print(f"My name is {self.name}")


print(type(Dog), Dog)
d = Dog()
print(type(d), d)
print(d.name, d.breed, d.color)
d.name = "Zyphirka"
d.color = "white"
d.breed = "wss"
print(d.name, d.breed, d.color)
print(Dog.name, Dog.breed, Dog.color)

Dog.name = "Buddy"
print(d.name)

d.Bork()

# Dog.years = 0
# print(d.years)

d.some_param = "test"
print(d.some_param)