print('---program for student inormation---')
D=dict()
n=int(input('How many student record do you want to store??'))
for i in range(0,n):
    x,y=input('Enter complete name (First and last)of each of the students:').split()
    z=input('Enter contact number:')
    m=input('Enter student marks:')
    D[x,y]=(z,m)
#difine unction for sorting names basing on first name
def sort():
    Is=list()
    #fetch key and value using the item keyword
    for sname,details in D.items():
        #store key parts as a tuple
        tup=(sname[0],sname[1])
        Is.append(tup)
        #sort the last list of tuples
    Is=sorted(Is)
    for i in Is:
         print(i[0],i[1])
    #define a function for getting min marks in sorted data
def minmarks():
    Is=list()
    #fetch key and value using the fetch key word
    for sname,details in D.items():
        #add details second element  (marks) to the list
        Is.append(details[1])
    #sort the list
    Is=sorted(Is)
    print('minimum marks:',min(Is))
    return
def searchitem(fname):
    Is=list()
    for sname,details in D.items():
        tup=(sname,details)
        Is.append(tup)
    for i in Is:
        if i[0][0]==fname:
            print(i[1][0])
    return
def option():
    choice=int(input('Enter oeration detail: \n \
    1:Sorting using firstname: \n \
    2:Finding minimum marks: \n \
    3:Search contact number: \n \
    4:Exit: \n \
    Option:  '))
first=input('Enter first name')
searchitem(first)
minmarks()

sort()