class Mysuperclass:
    def method(self):
        print('method super method called')
class Mysuperclass2:
    def method2(self):
        print('method super method called')
class Childclass(Mysuperclass,Mysuperclass2)
    def child_method(self):
        print('this is the child ')