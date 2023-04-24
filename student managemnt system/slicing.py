#demostrate slicing of an array
import array as a
l=[1,2,4,6,7,8,9,6,5,2,4,6,8,9]
b=a.array('i',l)
print('The riginal array is :',end=' ')
for r in (b):
    print(r,end=' ')
print()
#print elements using the slicing operation
Sliced_array=b[3:8]
print('The sliced array in range 3:8 is:',end=' ')
print(Sliced_array)
#print elements from predefined point
arrr=b[5:]
print('The array form a predifined point 5 is:',end=' ')
print(arrr,end=' ')
print()
#printing element of a sliced array till the begining
ggg=b[:]
print('The sliced array is :',end=' ')
print(ggg,end=' ')
print()
c=a.array('i',[1,2,3,4,5,6,7,8,8,9,5,3,24,6])
print('The orinal array is:',end='')
for g in (c):
    print(g,end=' ')
print()
#access the value of the second occurance
print('The value of the second occurance is:',end=' ')
print(c.index(2))
print('The value of the first occurance is:',end='')
print(c.index(1))
print()
c[4]=99
c[7]=100
c[3]=123
#updating array
print('The updated array is :',end=' ')
for j in (c):
    print(j,end=' ')