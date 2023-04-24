#numpy progrma to check for the version of numpy
import numpy as np
a=np.__version__
print(a)
print(np.show_config())
#numpy progrma to get help on the add function
print(np.info(np.add))
x=np.arange(9.0).reshape(3,3)
x1=np.arange(3.0)
print(np.add(x,x1))
#numpy program to test whether none of the elements is zero
x=[1,2,3,4,5]
print('original array is :', np.array(x))
print('There is no zero value:',np.all(x))
r=[0,2,0,4,6]
print('The original array is :',np.array(r))
print('there is al  zero value in a the array:',np.all(r))