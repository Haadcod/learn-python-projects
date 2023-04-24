def factorial(num):
    if num==1:
        return num
    else:
        return (num*factorial(num-1))
print('the factorial of num is ',factorial(6))