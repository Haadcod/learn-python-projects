def fibonacci(num):
    x,y=0,1
    for _ in range(num):
        x,y=y,x+y
        yield x
def square(num):
    for i in num:
        yield i**2
print(sum(square(fibonacci(100))))