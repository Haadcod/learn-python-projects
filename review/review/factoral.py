""""calculating the factorial o a number """
num=int(input("Please enter an integer number"))
factorial=1
if num<0:
    print("The number cant be negative")
elif num==0:
    print("number cant be a negative")
else:
    for i in range(1,num):
        factorial=factorial*i
print('The factorial of' +str(i)+ 'is' +str(factorial))