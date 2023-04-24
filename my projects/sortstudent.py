print('--printing the sorted list of students according to first name,marks and finding the contact using the first name --')
l=[]
la=int(input('Enter the maximum number of students you would lyk to input '))
for i in range(0,la):
    x,y,z=input('Enter student name,marks and contact').split()
    l.append((x,y,z))
for i in (l):
    print(i[2],i[1],i[0])