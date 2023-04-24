#python to demostrate bytr array ie it gives a range from 0<=x<256
a=bytearray((12,8,25,2))
print('Creating a byte array:')
print(a)
#accessing elements
print('The element of a byte array:',a[1])
#modiying elements of a byte array
print('\nmodifying elements of a byte array:')
a[1]=3
print('The modified value in tha byte array is :',a[1])
#appending elements to the array
a.append(30)
print('after adding elements to the array',a)
print(a[-1])
#python program to demostrate one of the collection module ie counter
from collections import Counter
#with sequence of items
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
#With a dictionary
count=Counter({'A':3,'B':5,'C':6})
print(count)
count.update(['A',1])
print(count)
#order dict operations
from collections import OrderedDict
print('Before deleting:\n')
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
od['e']=5
od['f']=6
for key,value in od.items():
    print(key,value)
print('After deleting:\n')
od.pop('c')
for key,value in od.items():
    print(key,value)
od['c']=3
for key,value in od.items():
    print(key,value)
#default dict for providing a default value to the dictionary
from collections import defaultdict
d=defaultdict(int)
L=['A','B','B','C','C','D','E','F','H']
#iterate through the list for keeping the count
for i in L:
    #The default value is 0, so there is no need to enter the first key
    d[i]+=1
print(d)
#Chain map encapsulates  dictionaries into a list
from collections import ChainMap
d={'A':2,'B':3}
d1={'D':1,'E':5}
d2={'F':5,'S':2}
#definig a chain map
c=ChainMap(d,d1,d2)
print(c)
#python program for named tuple operations
from collections import namedtuple
#declaring a named tuple
Student=namedtuple('Student',['name','DOB','age'])
#adding values
s=Student('nsubuga',23,23031995)
#accessing using the index noatation
print('Student age using index is:',end='')
print(s[1])
print('Students name is :',end='')
print(s[0])
#access using the name noatation
print('Thestudent name using the keyname is :',end='')
print(s.name)
#deque operations
import collections
#initialising the deque operation
de=collections.deque([1,2,3,4])
#using append to insert element at the right end
de.append(3)
print(de)
#using append left to insert value to the left
de.appendleft(30)
print(de)
#python program to demostrate userlist
from collections import UserList
#creating a list where deletion is not allowed
class Mylist(UserList):
    #function to stop deletion from thelist
    def remove(self, s=None):
        raise RuntimeError('Deletion is not allwed')
    #function to stop pop from the list
    def pop(self, s=None):
        raise RuntimeError('Deletion is not allowd')
#driver code
L=Mylist([2,4,5,6,7,4,4])
print('This is the original list',L)
L.append(5)
print('List after appending  a value:',L)
#L.remove()
#L.pop(5)
#userstring function used to created a string with some added functionality
from collections import UserString
#creating a mutable string
class Mystring(UserString):
    #function to append string
    def append(self,s):
        self.data+=s
    def remove(self,s):
        self.data=self.data.replace(s,'')
#driver code
s1=Mystring('geek')
print('The original string is:',s1.data)
#appending to the string
s1.append('s')
print('The appended string is:',s1.data)
#removing from the string
s1.remove('e')
print('The removed string is :',s1.data)
#defining linked list in python
#node class
class Node:
    #function to initialise a node
    def __init__(self,data):
        #data of the node
        self.data=data
        #initialise our next pointer to null
        self.next=None

#creating a linkd list class for adding a new node
class Linkedlist:
    #we initialose our head to null
    def __init__(self):
        self.head=None
    #method to insert a new node
    def insert(self,new_node):
        #ckeck whether node is empty or not
        if self.head:
            #getting the last node
            last_node=self.head
            while last_node !=None:
                last_node=last_node.next
            #asigning new node to the next pointer of the last node
                last_node.next=new_node
            else:
                #head is empty
                #assigning the node to head
                self.head=new_node
    #function to displaythe linked list
    def display(self):
        #we initialise the variable with head
        temp_node=self.head
        #iterating untill we reach the end of the linked list
        while temp_node !=None:
            #printing node data
            print(temp_node.data, end='->')
            #moving to the next node
            temp_node=temp_node.next
        print('Null')
if __name__=='__main__':
    linked=Linkedlist()
    linked.insert(Node(1))
    linked.insert(Node(2))
    linked.insert(Node(3))
    linked.insert(Node(4))
    linked.insert(Node(5))
    linked.insert(Node(6))
    linked.display()
#simple python program to demostrate linked list
class Node:
    #function to initialise to initialise the node object
    def __init__(self,data):
        self.data=data
        self.next=None #initialise our next as null
#linkedlist class contains node object
class Linkedlist:
    #function to initialise our head
    def __init__(self):
        self.head=None
#code exeution starts here
if __name__=='__main__':
    #start with the empty list
    list=Linkedlist()
    list.head=Node(1)
    second=Node(2)
    third=Node(3)
    forth=Node(4)
    fifth=Node(5)
    sixth=Node(6)
    #link first node with the second node
    list.head.next=second
    second.next=third
    third.next=forth
    fifth.next=sixth
