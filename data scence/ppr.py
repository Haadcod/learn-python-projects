a,b,c=1,20.0,'geekforgeeks'
print(a)
print(b)
print(c)
a,b=2,3
d,c='geekfor','geeks'
print(a+b)
print(d+c)
x=5
def change():
    global x
    x=x+5
    print('the value of x is ',x)
change()
print('the value of x outside of the function',x)
var=123
print('numberic data:',var)
#sequence type
String='welcome to geek for geeks'
print('String with use of single quotes:')
print(String)
#Boolen
print(type(True))
print(type(False))
#creating a set with the use of a string
set1=set('Geekforgeeks')
print('\nSet with the use of string:')
print(set1)
#creating a dictionary with integer keys
dict={1:'Geeks',2:'for',3:'geeks'}
print('\n dictionary with the use of integer keys')
print(dict)
#ptyhon program to show that variable assigned in a class
#is called an instance variable while that assigned in a
#constructor or method is called an instance variable
#class for computer science
class CSSStudent:
    #class variable
    stream='cse'
    #init method or constructor
    def __init__(self,roll):
        #instance variable
        self.roll=roll
#objects of the student class
a=CSSStudent(101)
b=CSSStudent(102)
print(a.stream) #prints cse
print(b.stream) #print cse
print(a.roll)   #prints 101
a=12
b=34
add=a+b
sub=a-b
mult=a*b
div=a/b
div1=a//b
modul=a%b
print(add)
print(sub)
print(mult)
print(div)
print(div1)
print(modul)
#relationl operators
a=13
b=33
print(a>b)
print(a<b)
print(a==b)
print(a !=b)
print(a>=b)
print(a<=b)
print()
#logical operators
a=True
b=False
print(a and b)
print(a or b)
print(not a)
#bitwise operators
a=10
b=4
print(a & b)
print(a | b)
#membership operator
x=24
y=20
list=[10,20,30,40,50]
if (x not in list):
    print('x is Not present in a given list:')
else:
    print('x is present in a given list:')
if (y in list):
    print('y is present in the list:')
else:
    print('y is Not in the list:')
#precedence and associativity operators
# precedence of '+','&','*'
expr=10+20*4
print(expr)
#precedence of 'or','&','and'
name='Alex'
Age=0
if name=='Alex' or name=='John' and Age>=2:
    print('Hello!!!,Welcome')
else:
    print('Good bye!!')
#tenary operator
a,b=10,20
#copy the value of a in min if a<b
min=a if a<b else b
print(min)
#progrma to demstrate tenary operator
a,b=10,20
#use to tuple for selecting an item
#(if_test_false,if_test_true)[test]
#if [a<b] is true it returns 1,so element with index 1 will print
#else if [a<b] is false it returns 0 so element with index 0 will print
print((b,a)[a<b])
#use dictionary for selecting an item
#if [a<b] is true the value of true key will be printed
#elif [a<b] is false the value of the alse keywil be printed
print({True:a,False:b}[a<b])
#lambda is is more effeicient coz we are sure
#that in lambda only one expression will be evaluated unlike in tuple and dictionary
print((lambda: b,lambda: a)[a<b]())
#python program to demostrate tenary operatot
a,b=10,20
if (a!=b):
    if (a<b):
        print('a is less than b')
    else:
        print('a is greater than b')
else:
    print('a is equal to b')
#find the larger number using the tenary operator
a=44
b=55
print(a,'a is greater than b') if (a>b) else print(b,'b is grater')
#python program to demostrate how
#to overload the binary + operator
class A:
    def __init__(self,a):
        self.a=a
    #adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1=A(1)
ob2=A(2)
ob3=A('geeks')
ob4=A('for')
print(ob1+ob2)
print(ob4+ob3)
#pythno prgram adding two complex numbers
class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    #adding two objects
    def __add__(self, other):
        return self.a+other.a, self.b+other.b
ob1=Complex(1,3)
ob2=Complex(4,5)
ob3=ob1+ob2
print(ob3)
#python program to overload a comparison operator
class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self, other):
        if (self.a>other.a):
            return True
        else:
            return False
ob1=A(3)
ob2=A(4)
if (ob1>ob2):
    print('ob1 is greater than ob2')
else:
    print('ob2 is greater than ob1')
#python program to overload equality and less than operator
class A:
    def __init__(self,a):
        self.a=a
    def __It__(self,other):
        if(self.a<other.a):
            return 'ob1 is less than ob2'
        else:
            return 'ob2 is greater than ob1'
    def __eq__(self, other):
        if(self.a==other.a):
            return 'both are equal'
        else:
            return 'Not equal'
ob1=A(2)
ob2=A(3)
#print(ob1 < ob2)
ob3=A(4)
ob4=A(4)
print(ob3==ob4)
#val=input('enter anumber')
#print(val)
#python program to acces elements of a string
String='ewlcome to geek for geeks'
print(String[0])
print(String[-2])
#python program to demostrate slicing
print('Initial string',String)
print('after slicing',String[2:8])
print('after slicing again',String[6:-3])
#python program for formatting of strings
#default formating
String='{},{},{}'.format('geeks','for','life')
print(String)
#positinal formating
String='{1},{0},{2}'.format('geeks','for','life')
print(String)
#keywrd formating
String='{y},{t},{r}'.format(y='geeks',t='for',r='life')
print(String)
#python progrma to demostrate formating using the %
var=15
print('the value ofthe variable is %s'%(var))
#convert variable to integer
var=int(var)
print('value of the variable in int type is %d'%(var))
print('print value off variable as float type %f'%(var))
#demostrate using the f string in strin formating
n1='hello'
n2='geek for geeks'
print(f'{n1}, i am {n2}')
#python program to demostrate creation of lists
list=[]
print(list)
list=['geek','for','geeks']
print(list)
list=[['geek','for','geeks'],'geeks']
print(list)
#addin elements to the list
list.append(1)
list.append(3)
print(list)
list.insert(2,3)
list.insert(5,6)
print(list)
#accesing elements from alist
print(list[2])
print(list[5])
print(list[-1])
#iterate over a list
for i in list:
    print(i)
#iterate through the list with its range
List=[1,2,3,4,5,6,6,3,4,2]
length=len(List)
print(length)
#for i in range(length):
#    print(List[i])
#iterate using a while loop
i=0
#while i<length:
  #  i+=1
 #   print(List[i])
#python function to iterate over a list using ht enumerate function
for i,val in enumerate(List):
    print(i,"," ,val)
#python program to demostrate list compresion in python
#below contains alist of ood numbers from 0-10
odd_squar=[]
for x in range(1,11):
    if x % 2 == 1:
        odd_squar.append(x**2)
print(odd_squar)
odd_square=[]
for x in range(1,20):
    if x % 2 ==1:
        odd_square.append(x)
print(odd_square)
odd_square=[x**2 for x in range(1,20) if x % 2 ==1]
print(odd_square)
#the below list contains power of 2
power_of_2=[2**x for x in range(1,8)]
print(power_of_2)
#below list contains prime and noprime numbers
list1=[]
list2=[]
for i in range(2,8):
    for j in range(i*2,50,i):
       list1.append(j)
#print(list2.append(i))
print(list1)
for x in range(2,50):
    if x not in list1:
        list2.append(x)
print(list2)
#list extracts pnone number
String='This is my phone number: 1234567'
number=[]
for x in String:
    if x.isdigit():
        number.append(x)
print(number)
#program to understand packing and unpacking
#this line packs values
a=('MNNIT alahab',5000,'engineering')
#this demostrates unpacking
(college,student,type_of_colege)=a
print(college)
print(student)
print(type_of_colege)
#unpacking using the *arg operator
x,*y,z=(10,'geeks','for','geeks',50)
print(y)
print(z)
print(x)
print(x,y,z)
#unpackinga tuple using the python function
#function takes normal arguements and multiplies them
def result(x,y):
    return x*y
#function with normal variables
print(result(10,100))
#a tuple is created
z=(10,1000)
#tuplee is packed
#unction is upacked
print(result(*z))
#loops in tuples
tup=('geeks',)
for i in range(5):
    tup=(tup,)
    print(tup)
#python program to demostrate using Cmp(),min(),max()
#python program to demostrate creation of a set
#creating a set
set1=set()
print(set1)
#creating a set of string
set2=set('geekforgeeks')
print(set2)
#creating a set of a list
set3=set(["geek","for","geeks"])
print(set3)
#adding elements to aset
set3.add(1)
set2.add('the')
set1.add('anoyted')
print(set1)
print(set2)
print(set3)
#accessing elements of a set
for i in set3:
    print(i,end="")
#creating a dictionary
dict={}
print(dict)
dict1={1:'name',2:'birth',3:'matrimony'}
print(dict1)
dict3={'name':'nsubuga',1:[1,2,3,4,5]}
print(dict3)
print(dict3[1])
print(dict3['name'])
print(dict1.values())
print(dict1.keys())
#python program to iterate through all the keys in a dictionary
statesAndCapital={
    'kampala':'makindye','mukono':'mubende','sironko':'kyotera','masaka':'mbarara','gulu':'arua','busia':'malaba'}
for state in statesAndCapital:
    print(state)
#iterate over values in a dictionary
for capital in statesAndCapital.values():
    print(capital)
#iterate through all key and value pairs
for states,capital in statesAndCapital.items():
    print(states,":",capital)
#python program to demostrate decision making
#python program to check even numbers and odd numbers
a=5
b=10
#if to check for even number
if (a,b%2==0):
    print('is an even number')
else:
    print('This is an odd number')
#to demostrate nested if statements
a=10
if a%2==0:
    if a%5==0:
        print(a,'is oth divisible by both 2 and 5')
#is elif statement
if a==11:
    print(a,'is 11')
elif a==10:
    print(a,'is 10')
else:
    print('a is not present')
#python program to illustrate while statement
i=0
while (i<3):
    i+=1
    print('hello geeks')
#checks if list still contains any element
a=[1,2,3,4,5,6]
while a:
    print(a.pop())
i=10
while (i<12):
    i+=1
    print(i)
    break
else:#not executed because ther is a break
    print('no break')
#python pregram to illustrate single line statement
count=0
while (count<5): count+=1; print('geekforgeeks')
#python program to illistrate the use of continue statement
#the python program print all values with the exception of e and s
i=0
a='geekforgeeks'
while i<len(a):
    if a[i]=='e' or a[i]=='s':
        i+=1
        continue
    print('Current letter is:',a[i])
    i+=1
#python program to illustrate the use of break
#break as soon as the it finds e or s
i=0
b='geekforgeeks'
while i<len(b):
    if b[i]=='e' or b[i]=='s':
        i+=1
        break
    print('The current value is:',b[i])
    i+=1
#python program to illustrate the use of pass
#an empty loop
while i<len(b):
    i+=1
    pass
print('The value of i is',i)
#python program to elaborate a sentinel value (an input value used to terminate a loop
#generally the sentinel value is a -1
#a= int(input('Enter a number (-1 to quit)'))
#while a!=-1:
 #   a=int(input('Enter a number (-1 to quit '))
#python gotchas examples
numlist=[1,2,3,4]
square=(n**2 for n in numlist)
#python program to elaborate the use of break continue and pass statements
s ='geekforgeeks'
for letter in s:
    if letter=='e' or letter=='s':
        break
    print(letter,end="")
print()
for letter in s:
    if letter=='e' or letter=='s':
        continue
    print(letter,end="")
print()
for letter in s:
    if letter=='e'or letter=='s':
        pass
    print(letter,end="")
print()
#creating functions in python
def ask_user():
    print('hello world')
def my_unction():
    a=0
    for i in range(1,11):
        print(i)
        a=a+i
    return a
print(ask_user())
print(my_unction())
#default function
def my_fun(x,y=50):
    print('x:',x)
    print('y:',y)
my_fun(10)
#variable lenght arguements
#python program to demostrate variable length arguments
def my_funi(*argv):
    for arg in argv:
        print(arg, end=" ")
my_funi('heloo','welcom','to','geek','for','geeks')
def my_name(*art):
    for i in art:
        print(i,end="")
my_name('hi','my','name','is','nsubuga','abdulhaad')
print()
#variable key word args
def myfun(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s"%(key,value))
myfun(first='geeks',mid='for',last='geeks')
#python program to check whether the number passed as an argument is odd
def myfun1(x):
    """Function to check whether the given aurgument is even or odd"""
    if x%2==0:
        print(x,'is even')
    else:
        print(x,'is odd')
print(myfun1.__doc__)
myfun1(11)
#return statement
def square_number(num):
    """The function returns a square of a number """
    return num**2
print(square_number(23))
print(square_number(45))
#parameter passing
#here x is new reference to the same list
def my_fun1(x):
    x[0]=20
#driver code note that lst is modified after function call
lst=[1,2,3,4,5,6]
my_fun1(lst)
print(lst)
#refernce link gets broken if we assign a new value inside the function
def myfun3(x):
    x=[20,30,40]
lst=[1,2,3,4,5,6]
myfun3(lst)
print(lst)
#naother
def myfun4(x):
    x=20
x=10
myfun4(x)
print(x)
#execise
def swap(x,y):
    temp=x
    x=y
    y=temp
x=3
y=4
swap(x,y)
print(x)
print(y)
#anonymous functions created using lambda
def cube(x): return x*x*x
cube1=lambda x: x*x*x
print(cube(34))
print(cube1(34))
#nested or inner functions in python
def my_fun4():
    print('i am fun factory ')
    def my_fun5():
        print('geek for geeks')
    my_fun5()
my_fun4()
#python program to show functions can be treated as objects
def shout(text):
    return text.upper()
print(shout('hello'))
yell=shout
print(yell('hello'))
#python program to illustrate functions can be passed as arguements to other unctions
def shout(text):
    return text.upper()
def whispper(text):
    return text.lower()
def greet(func):
    greeting=func("""hi am created by a function passed as an argument""")
    print(greeting)
greet(shout)
greet(whispper)
#python program to illustrate functons can return another function
def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_15=create_adder(15)
print(add_15(10))
#python program to demostrate use of return statement
def add(a,b):
    return a+b
def is_true(a):
    return bool(a)
res=add(2,3)
print('result of add unction is {}'.format(res))
ress=is_true(2>6)
print('the value of the bool function is {}'.format(ress))
#python program to illustrate the use of return statement to return multiple values form method using a class
class Test:
    def __init__(self):
        self.str='geek for geeks'
        self.x=20
#this function returns an object of test
def fun():
    return Test()
#Driver code to test the above method
t=fun()
print(t.str)
print(t.x)
#proram to return multiple values using a function
class Test:
    def __init__(self):
        self.str='my name is nsubuga abdulhaad'
        self.str1='my other name is amina'
        self.str2='am aged 27 years'
        self.age=27
#This function returns an object of test
def func():
    return Test()
res=func()
print(res.str)
print(res.str1)
print(res.str2)
print(res.age)
#python program to return multiple values from a method using a tuple
def fun():
    str='am by the names nsubuga abdulhaad'
    age=26
    return str,age
str,age=fun()
print(str)
print(age)
#python program to retrn multiple values froom a method using the list
def func():
    str='am by the names nsubuga abdulhaad'
    age=26
    return [str,age]
list=func()
print(list)
#return multiple values from a method using dictionary
#def func():
 #   d=dict();
  #  d['str']='am by thenames nsubuga abdulhaad'
   # d['x']=20
    #return d
#d=func()
#print(d)
#python program to demostrate calling function from some other function
def square(x):
    #computes the square of a given number and returns to the caller function
    return (x*x)
def sumofsquare(Array,n):
    #initialise the sum to zero. it stores the total sum of values of the array
    sum=0
    for i in range(n):
        #square if the array element is stored in the squared value
        squaredvalue=square(Array[i])
        #cumulative sum is stored in sum variable
        sum+=squaredvalue
    return sum
#driver function
Array=[1,2,3,4,5,6,7,8,9]
n=len(Array)
#return value from the function
#sum of squares is stored in total
total=sumofsquare(Array,n)
print('sum of square of a list is :',total)
#print sum of square of numbers
def square(x):
    return (x*x)
def sumofsqaures(Array,n):
    sum=0
    for i in range(n):
        sqauredvalue=square(Array(i))
    sum+=sqauredvalue
    return sum
Array=[178,23,45,56,76,78,956,834]
n=len(Array)
total=sumofsquare(Array,n)
print('The value of the sum of squares is :',total)
#calling a function from within another function of then same class
class Main():
    #constructor of the main class
    def __init__(self):
        self.string1='Hello'
        self.string2='Nsubuga Abdulhaad'
    def function1(self):
        self.function2()
        print(self.string2)
    def function2(self):
        print(self.string1)
obj=Main()
obj.function1()
#calling a function from another function in the same class
class Main():
    def __init__(self):
        self.string1='Aam by the names nsubuga Abdulhaad'
        self.string2='Ileave in makindye division'
        self.string3='A surbub of kampala'
    def function1(self):
        self.function3()
        self.function2()
        print(self.string3)
    def function2(self):
        print(self.string2)
    def function3(self):
        print(self.string1)
obj=Main()
obj.function1()
#pythonprogram for calling parent clas method from child class
class Parent():
    def __init__(self):
        self.string1='Am by the names Abdulhaad Nsubuga'
        self.string='I am an engineer by profession'
        self.string2='I do welding as a side gig'
    def function(self):
        print(self.string2)
class Child(Parent):
    def function1(self):
        print(self.string)
    def function2(self):
        print(self.string1)
        self.function()
        self.function1()
obj=Parent()
obj1=Child()
obj1.function2()
#python program to demostrate the use of the lambda function for anonymous functions
#cube using lambda
cube=lambda x: x*x*x
print(cube(8))
square=lambda x: x*2
print(square(7))
#list compresion using lambda
cube=[(lambda x: x*x*x) (x)for x in range(5)]
print(cube)
square=[(lambda x: x*2) (x) for x in range(20)]
print(square)
#python program of lambda that returns function obeject and memory location
string='geek for geeks'
print(lambda string: string)
#python function to return the string using lambda
x='geek for geeks'
(lambda x: print(x))(x)
r='Am by the names nsubuga abdulhaad'
a=(lambda r:r)(r)
print(r)
#differnce btn the lambda and def function keywords
def cube(y):
    return y*y*y
print(cube(7))
cube1=(lambda y: y*y*y)
print(cube1(7))
#python program to use list compresion and lambda with for loop
table=[lambda x=x: x*10 for x in range(1,11)]
for tables in table:
    print(tables())
#lambda function with if statement
max=lambda a,b: a if(a>b) else b
print(max(1,2))
#python program with multiple statements using lambda
#finging the second max element using lambda
#list=[[2,3,4],[7,4,6],[3,4,5]]
#sort each sub list
#sortList=[lambda x: (sorted(i) for i in x)]
#get second last element
#secondLargest=lambda x, f: [y[len(y)-2] for y in f(x)]
#res=secondLargest(list,sortList)
#print(res)
#python program to filter ou the odd numbersin a given list using the filter functio
#li=[2,4,5,3,6,665,8,6,9,0,5,6,56,78,453,33,35,57,89,13]
#final_list= list(filter(lambda x: (x%2!=0),li))
#print(final_list)
#python programs for classes and object instantiation
class Dog():
    att='mammal'
    attr='dog'
    def fun(self):
        print('i am  a ',self.att)
        print('i am a ',self.attr)
roger=Dog()
print(roger.att)
roger.fun()
#defining instance and class variables in python
class Dog:
    #class variable
    animal='dog'
    def __init__(self,breed,color):
        #instance variables
        self.breed=breed
        self.color=color
    def function(self):
        print(self.breed)
        print(self.color)
#object instantiation
obj=Dog('pud','brown')
obj2=Dog('shepard','white')
obj.animal
obj.function()
#class and instance variables using set and get method
class Dog:
    animal='dog'
    def __init__(self,breed):
        self.breed=breed
    def setcolor(self,color):
        self.color=color
    def getcolor(self):
        return self.color
obj=Dog('pug')
obj.setcolor('brown')
print(obj.getcolor())
#it is clear that self and obj refer to the same object
class Check:
    def __init__(self):
        print('Adress of self is:',id(self))
obj=Check()
print('The address of obj is :',id(obj))
#addressing the default constructor in python
class Geekforgeeks:
    def __init__(self):
        self.geek='I am by the names Nsubuga Abdulhaad'
    def display(self):
        print(self.geek)
obj=Geekforgeeks()
obj.display()
#Demostrating the paramentarised constructor
class Number:
    first_number=0
    second_number=0
    answer=0
    def __init__(self,f,s):
        self.first_number=f
        self.second_number=s
    def printt(self):
        print('The value of first_number is :',self.first_number)
        print('The value of second_number is :',self.second_number)
        print('The value for the answer to the number : ',self.answer)
    def addd(self):
        self.answer=self.first_number+self.second_number
obj=Number(100,300)
obj.addd()
obj.printt()
#demostrate destructorsin python
class Destr:
    def __init__(self):
        print('constructor has beeb created')
    def __del__(self):
        print('destructor for del constructor')
obj=Destr()
del obj
#python inheritance
class Person:
    def __init__(self,name):
        self.name=name
    #To get name
    def getName(self):
        return self.name
    #To check if this person is employee
    def is_Employee(self):
        return False
class Employee(Person):
    #Here we return true
    def is_Employee(self):
        return True
#driver code
emp=Person('geeks')
print(emp.getName(),emp.is_Employee())
emp=Employee('Geeks')
print(emp.getName(),emp.is_Employee())
#python program to demostrate inheritence
class Person:
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def is_Employee(self):
        return False
class Employee(Person):
    def getName(self):
        return self.name
    def is_Employee(self):
        return True
obj=Person('geeks')
print(obj.getName(),obj.is_Employee())
obj=Employee('Geeks')
print(obj.getName(),obj.is_Employee())
#python program to check if one is subclass o the other class
class Base(object):
    pass
class Derived(Base):
    pass
print(issubclass(Derived,Base))
print(issubclass(Base,Derived))
d=Derived()
b=Base()
#b is not an instance of derived
print(isinstance(b,Derived))
#d is an instance of the base class
print(isinstance(d,Base))
#multiple inheritence
#class Base1(object):
#    def __init__(self):
 #       self.str='geeks'
  #      print('base1')
#class Base2(Base1):
 #   def __init__(self):
  #      self.str1='ground'
#class Derived(Base1,Base2):
 #   def __init__(self):
        #calling constructors of the base classes
  #      Base1.__init__()
   #     Base2.__init__()
    #    print('deriveddef')
    #def printt(self):
     #   print(self.str,self.str1)
#ob=Derived()
#ob.printt()
#pythonprogram to ilustrate encapsulation
#creatin a base clase
class Base:
    def __init__(self):
        #protected member
        self._a=2
#creating the derivedbase class
class Derived(Base):
    def __init__(self):
        #calling the base cunstructor class
        Base.__init__(self)
        #printing protected member of the base class
        print('calling the protected member of the base class',self._a)
        #modify the protected variable
        self._a=3
        print('calling the modified variable in the derived class',self._a)
obj1=Base()
obj2=Derived()
#calling protected member
#can be accessed buhshould not be done due to convention
print('accessing the protected member of obj1',obj1._a)
#accessing the protected variable outside
print('Accessing protected member of obj2:',obj2._a)
#python program to demostrate encapsulation using the private variable
class Base:
    def __init__(self):
        self.a='geekforgeeks'
        self.__c='geeksforgeeks'
#creating a derived class
class Derived(Base):
    def __init__(self):
        #calling the constructor ofthe base class
        Base.__init__(self)
        #printing the private member of the base class
        print('calling the private member of the base class')
        print(self.__c)
obj2=Base()
print(obj2.a)
# uncommenting obj1.c will raise an attribute error
#obj1=Derived()#private member cannot be called in the derived classp
#python program to illustrate polymophisim
class A:
    def show(self):
        print('Inside A')
class B:
    def show(self):
        print('inside B')
a=A()
a.show()
b=B()
b.show()
#python program to depict multiple inheritence wen one method is overriden
class Class1:
    def m(self):
        print('Am in class 1')
class Class2(Class1):
    def m(self):
        print('Am in class 2')
class Class3(Class1):
    def m(self):
        print('Am in class 3')
class Class4(Class2,Class3):
    pass
obj=Class4()
obj.m()
#python program to depict multiple inheritence wen methods is overridden in one of the classes
class Class1:
    def show(self):
        print('In class 1')
class Class2(Class1):
    pass
class Class3(Class1):
    def show(self):
        print('In class 3')
class Class4(Class2,Class3):
    pass
obj=Class4()
obj.show()
#python program to depict multiple inheritance wen every class defines the same method
class Class1:
    def m(self):
        print('In class 1')
class Class2(Class1):
    def m(self):
        print('In class 2')
class Class3(Class1):
    def m(self):
        print('In class 3')
class Class4(Class2,Class3):
    def m(self):
        print('Am in class 4')
obj=Class4()
obj.m()
Class3.m(obj)
Class2.m(obj)
Class1.m(obj)
#python program to depict multiple inheritance
#when we try to call method n for class 1
#class2,c;ass 3,class4 from the class4
class Class1:
    def m(self):
        print('In class 1')
class Class2(Class1):
    def m(self):
        print('In class 2')
class Class3(Class1):
    def m(self):
        print('In class 3')
class Class4(Class2,Class3):
    def m(self):
        print('In class4')
        Class3.m(self)
        Class2.m(self)
        Class1.m(self)
obj=Class4()
obj.m()