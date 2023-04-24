#cresting an array
import array as arr
a=arr.array('i',[1,2,3])
#printing the original array
print('The new created array is:',end=' ')
for i in range(0,3):
    print(a[i],end=' ')
print()
b=arr.array('d',[2.3,4.6,5.7])
#printing the oringinal array
print('The new created array is :',end=' ')
for x in range(0,3):
    print(b[x],end=' ')
print()

