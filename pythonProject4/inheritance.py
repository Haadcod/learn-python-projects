class Vehicle:
    def __init__(self,name,color):
        self.__color=color
        self.__name=name
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color=color
    def get_name(self):
        return self.__name
class Car(Vehicle):
    def __init__(self,name,color,model):
        super().__init__(name,color)
        self.__model=model
    def getDiscription(self):
        return self.get_name() + self.__model + "in" + self.get_color() + "color"
c=Car('mastung','red','GT03')
print(c.getDiscription())
print(c.get_name())