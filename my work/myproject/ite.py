num=[1,2,3,4,5,6,7]
def traverse(num):
    it=iter(num)
    while True:
        try:
            items=next(it)
            print(items)
        except StopIteration:
            break
iter=iter(num)
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
class Datastore:
    def __init__(self,data):
        self.index=-1
        self.data=data
    def __iter__(self):
        return self
    def __next__(self):
        if (self.index==len(self.data)):
            raise StopIteration
        self.index +=1
        return self.data[self.index]
ds=Datastore([1,2,3,4])
for i in ds:
    print(i)
#using a sentinel
class Datastore:
    def __init__(self,data):
        self.index=-1
        self.data=data
    def __iter__(self):
        return self
    def __next__(self):
        if (self.index==len(self.data)):
            raise StopIteration
        self.index+=1
        return self.data[self.index]
    __call__=__next__
ds=Datastore([1,2,3,4,5])
itr=iter(ds,4)
for i in itr:
    print(i)
#generator function
def forvalue(x):
    for i in range(x):
        yield i
print(forvalue(6))