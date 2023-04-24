class Student:

     def __init__(self,name,rollno,m1,m2,m3):
         self.name=name
         self.rollno=rollno
         self.m1=m1
         self.m2=m2
         self.m3=m3
     def accept(self,Name,Rollno,mark1,mark2,mark3):
        ob=Student(Name,Rollno,mark1,mark2,mark3)
        l.append(ob)
     def display(self,ob):
         print('Name:',ob.name)
         print('Rollno:',ob.rollno)
         print('Mark1:',ob.m1)
         print('Mark2:',ob.m2)
         print('Mark3:',ob.m3)
         print()
     def search(self,r):
         for i in range(l.__len__()):
             if(l[i].rollno==r):
                 return i

l=[]
obj=Student('',0,0,0,0)
obj.accept('A',12,23,34,46)
obj.accept('B',32,23,45,65)
obj.accept('C',13,23,34,43)
obj.accept('D',14,12,34,45)
for i in (l):
    obj.display(i)
print('\nstudent found,')
s=obj.search(3)
obj.display(l[s])

