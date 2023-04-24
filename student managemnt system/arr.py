#python program to demostrate adding value to an array
import array as arr
a= arr.array('i',[1,3,4,5])
print('The original array before insertion is :', end=' ')
for i in range(0,4):
    print(a[i],end=' ')
print()
#insert array using insert function
a.insert(1,4)
#print array after insertion
print('the array after insertion is :',end=' ')
for i in (a):
    print(i,end=' ')
print()
b=arr.array('d',[2.3,4.5,5.7,1.3])
print('The array of float numbers before insertion is :',end=' ')
for x in range(0,4):
    print(b[x],end=' ')
print()
b.append(0.3)
print('The array of a float number after insertion is :',end='')
for l in (b):
    print(l,end=' ')