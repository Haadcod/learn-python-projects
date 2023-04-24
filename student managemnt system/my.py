class Student:
    def __init__(self,name,rollno,m1,m2,m3):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def accept(self,Name,Rollno,Mark1,Mark2,Mark3):
        ob=Student(Name,Rollno,Mark1,Mark2,Mark3)
        ln.append(ob)
    def dispaly(self,ob):
        print('Name:',ob.name)
        print('Rollno:',ob.rollno)
        print('Mark1:',ob.m1)
        print('Mark2:',ob.m2)
        print('Mark3:',ob.m3)
        print('\n')
ln=[]
obj=Student('',0,0,0,0)
obj.accept('A',23,100,100,23)
obj.accept('B',12,78,97,45)
obj.accept('C',12,69,60,56)
obj.accept('D',20,30,50,67)
print('\n')
print('\n List of students\n')
for i in range(ln.__len__()):
    obj.dispaly(ln[i])
