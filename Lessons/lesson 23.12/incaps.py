class Student:

    # __name = ""
    # __speciality = ""
    # __year = ""

    # def init(self, name, spec, year):
    #     self.__name = name
    #     self.__speciality = spec
    #     self.__year = year

    def __init__(self, name, spec, year):
        self.__name = name
        self.__speciality = spec
        self.year = year

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year > 0 and year <= 5:
            self.__year = year

    year = property(get_year, set_year)

    def hello(self):
        print(f"Hello, I'm {self.__name}, a student of {self.__year} {self.__speciality}")

s = Student("Mikita", "math", 3)

# print(s.get_year())
print(s.year)

s.hello()

# s.set_year(4)
s.year = 4
s.hello()