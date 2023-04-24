print(---we are printing the students marks in descending order--)
Is=[]
n=int(input('Enter the number of students you would like:'))
for i in range(0,n):
    x,y=input('Enter name and marks respectively').split()
    Is.append((x,y))
print('The list of sorted students names is')
Is=sorted(ls,reverse=True)
for i in Is:
    print(i[0],i[1])

    
