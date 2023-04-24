def my_gen():
    n=1
    print('This is printed first')
    yield n
    n+=1
    print('This is printed second')
    yield n
    n+=1
    print('This is printed third')
    yield n
for item in my_gen():
    print(item)