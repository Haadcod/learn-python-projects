class Student:
    def __init__(self,name,rollno,m1,m2):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2
    #function to create and append
    def accept(self,Name,Rollno,marks1,marks2):
        ob=Student(Name,Rollno,marks1,marks2)
        ln.append(ob)
    #function to display students information
    def display(self,ob):
        print('Name: ',ob.name)
        print('Age: ',ob.rollno)
        print('Mark1: ',ob.m1)
        print('Mark2: ',ob.m2)
        print('\n')
        #search through
 #   def search(self,rn):
       # for i in range(ln.__len__()):
          #  if(ln[i].rollno==rn):
           #     return i
    #delete function
    #def delete(self,rn):
   # def update(self,rn,No):
#create a list to add students
ln=[]
#an object of student class
obj=Student('',0,0,0)
print('\nOperations used ,')
print('\n1.Accept student Details\n2.Display student Details\n3.Search student details\n4.Delete student details\n5.Update student details\n6.Exit')
#ch=int(input('Enter choice:'))
#if (ch==1):
obj.accept('A',23,100,100)
obj.accept('B',12,78,97)
obj.accept('C',12,69,60)
obj.accept('D',20,30,50)
#elif(ch==2):
print('\n')
print('\nList of students\n')
for i in range(ln.__len__()):
    obj.display(ln[i])
