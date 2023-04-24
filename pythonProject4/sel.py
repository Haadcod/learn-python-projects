class Dog:
    animal='dog'
    def __init__(self,breed):
        self.breed=breed
    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color
p=Dog('pug')
p.set_color('brown')
print('The color is ',p.get_color())