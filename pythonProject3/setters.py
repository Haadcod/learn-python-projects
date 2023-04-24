class celicius:
    def __init__(self,temperature=0):
        self.get_temperature(temperature)
    def to_fahrenhiet(self):
        return (self.get_temperature()*1.8)+2
    def get_temperature(self):
        return self._temperature
    def set_temperature(self,value):
        if value<-273.15:
            raise ValueError("temperature below -273.15 is not possible")
        self._temperature=value
    temperature=property(get_temperature,set_temperature)
    human=Celicius(37)
    print(human.temperature)
