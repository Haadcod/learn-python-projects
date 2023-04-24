class Close():
    def __init__(self):
        self.someover=42
d=Close()
print(d.someover)
class Forbar():
    def __init__(self,value=43):
        self.somvar=value
f=Forbar("i am nsubuga abdulhaad")
print(f.somvar)
class Bird():
    def __init__(self):
        self.hungry=True
    def  eat(self):
        if self.hungry:
            print('Aaaaaaaaa....')
            self.hungry=False
        else:
            print("No, thanks")
T=Bird()
print(T.eat())
print(T.eat())
class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound='Sqwak'
    def sing(self):
        print(self.sound)
R=SongBird()
print(R.sing())
print(R.eat())
print(R.eat())
class Rectangle():
    def __init__(self):
        self.width=0
        self.length=0
    def set_size(self,size):
        self.width=size
        self.length=size
    def get_size(self):
        return self.width,self.length
E=Rectangle()
E.width=10
E.length=20
print(E.get_size())
E.set_size((39,58))
print(E.get_size())
nested=[[1,2],[3,4],[6,8]]
def flattened(nested):
    for sublist in nested:
        for element in sublist:
            yield element
print(flattened())