#demostrate removal aof an array
import array
arr=array.array('i',[1,2,3,4,5])
#printing the original array
print('The array original array is :',end=' ')
for i in range(0,5):
    print(arr[i],end=' ')
print()
#using pop to remove value in second position
print('The popped element is :',end=' ')
print(arr.pop(3))
#print array after popping out a value
print('The array after popping out the value:',end=' ')
for x in (arr):
    print(x,end=' ')
print()
#using remove to remove the first occurance of the value in the array
arr.remove(1)
print('The array afterremoving the first occurance is :',end=' ')
for r in (arr):
    print(r,end=' ')
print()