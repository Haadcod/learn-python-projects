class Student:
    def __init__(self,name,rollno,m1,m2,m3):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def accept(self,Name,Rollno,mark1,mark2,mark3):
        ob=Student(Name,Rollno,mark1,mark2,mark3)
        Is.append(ob)
    def display(self,ob):
        print('Name:',ob.name)
        print('Rollno:',ob.rollno)
        print('Mark1:',ob.m1)
        print('Mark2:',ob.m2)
        print('Mark3:',ob.m3)
Is=[]
obj=Student('',0,0,0,0)
obj.accept('A',12,34,54,56)
obj.accept('B',23,45,67,89)
obj.accept('C',13,34,44,56)
obj.accept('D',15,23,45,67)
for i in range(Is.__len__()):
    obj.display(Is[i])
