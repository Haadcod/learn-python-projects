my_list=[1,2,3,4,5,6]
list_=[x**2 for x in my_list]
a=(x**2 for x in my_list)
print(list_)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
next(a)