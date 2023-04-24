class Person:
    "This is a person class"
    age=20
    def greet(self,name):
        self.name=name
        print('hello')
print(Person.age)
haad=Person()
print(haad.greet())
print(Person.__doc__)