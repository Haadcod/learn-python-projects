import numpy as np
a=np.array([1,2,3,4])
print(a)
#more than one dimesion
a=np.array([[1,2],[3,4]])
print(a)
#minimum dimesions
a=np.array([1,2,3,4,5],ndmin=9)
print(a)
#dtype parameter
a=np.array([1,2,3],dtype=complex)
print(a)
#file name can be used to access content of the age column
dt=np.dtype([('age',np.int8)])
a=np.array([(10),(20),(30)],dtype=dt)
print(a)
student=np.dtype([('name','S20'),("age","i1"),("marks","<f4")])
print(student)
#a=np.array([('name','S20'),("age","i1"),("marks","<f4")],dtype=student)
print(a)
a=np.array([[12,3,4],[5,7,8]])
a.shape=[3,2]
print(a)
#this is a one dimesional array
a=np.arange(24)
print(a)
b=a.reshape(2,3,4)
print(b)
#example of an empty array
a=np.empty([3,2],dtype=int)
print(a)
#converting values to an ndarray
x=[1,2,4,4]
a=np.asarray(x)
print(a)