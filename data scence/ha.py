import numpy as np
import pandas as pd
arr=np.array([1,2,3,4,5],ndmin=5)
print(arr)
#minimum dimensions
a=np.array([1,2,3,4],ndmin=2)
print(a)
#dtype
n=np.array([1,2,3,4,5],dtype=complex)
print(n)
n=pd.array(['a','b','c','d','e','f'])
s=pd.Series(n)
print(s)
data={'Name':['Tom','Jack','Steve','Abdul'],'Age':[23,45,24,25]}
s=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(s)
