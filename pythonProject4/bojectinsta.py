class Dog:
    attr1='mammal'
    attr2='dog'
    def fun(self):
        print('This is ',self.attr1)
        print('This is ',self.attr2)
rodger=Dog()
print(rodger.attr1)
rodger.fun()