def forvalue(x):
    for i in range(x):
        yield i
ds=forvalue(6)
while True:
    try:
        print("Recieved on the next :", next(ds))
    except StopIteration:
        break
for i in ds:
    print(i)