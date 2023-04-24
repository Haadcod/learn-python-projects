def smart_divide(func):
    def inner(a,b):
        print('I am going to divide ' ,a, 'and' ,b,)
        if b==0:
            print('whoops! cannot divide by zero')
            return
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    print(a/b)
divide(45,6)
divide(23/0)
