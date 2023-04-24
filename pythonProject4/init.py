class Person:
    def __init__(self,name):
        self.name=name
    def say(self):
        print('hello,hi this is ',self.name)
dog=Person('nsubuga')
dog.say()