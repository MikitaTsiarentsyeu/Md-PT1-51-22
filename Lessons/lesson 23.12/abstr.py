class Car:

    def __init__(self, make, model, number, vin):
        self.__make = make
        self.__model = model
        self.__number = number
        self.__vin = vin

    def register(self):
        print(f"The number {self.number} was registered")


class Car:

    def __init__(self, make, model, color, body, year):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__body = body
        self.__year = year

    def get_info(self):
        print(f"{self.__color} {self.__body} {self.__make} {self.__model}")