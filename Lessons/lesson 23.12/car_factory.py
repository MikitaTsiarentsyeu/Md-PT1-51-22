class Engine:

    def __init__(self, power, volume):
        self.power = power
        self.volume = volume


class SerialCar:

    def __init__(self, make:str, model:str, engine:Engine):
        self.__make = make
        self.__model = model
        self.engine = engine

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model


engine = Engine(150, 3)
vw = SerialCar("VW", "POLO", engine)

vw.engine = Engine(330, 6)



class SuperCar:

    def __init__(self, make:str, model:str, power:int, volume:int):
        self.__make = make
        self.__model = model
        self.__engine = Engine(power, volume)

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_power(self):
        return self.__engine.power

    def get_volume(self):
        return self.__engine.volume

f = SuperCar("ferarri", "la ferarri", 550, 8)