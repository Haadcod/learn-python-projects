import Numpy as geek
list=[1,2,4,6,7,8,9,0]
for i in list:
    print(i)
lists=[2,5,7,8,9,3,7]
lenght=len(lists)
print(lenght)
for i in range(lenght):
    print(lists[i])
lis=[1,2,3,4,5,6,7]
length=len(lis)
i=0
while i<lenght:
    print(lis[i])
    i+=1
pen=[1,3,4,6,7,8,9,7]
[print(i) for i in pen]
pens=[2,3,4,5,6,4,3,6,2,5]
for i ,val in enumerate(pens):
    print(i,':',val)
#creating an array using arrange method
a=geek.arange(9)
#shape arraywith 3 rows and 4 columns
a=a.reshape(3,3)
#iterating an array
for x in geek.nditer(a):
    print(x)