import math
class Circle:
    def __init__(self,radius):
        self.__radius=radius
    def set_raduis(self,radius):
        self.__radius=radius
    def get_radius(self):
        return self.__radius
    def area(self):
        return math.pi *self.__radius**2
    def __add__(self,another_circle):
        return Circle(self.__radius + another_circle.__raduis)
c1=Circle(4)
c1.get_radius()
c2=Circle(6)
print(c2.get_radius())