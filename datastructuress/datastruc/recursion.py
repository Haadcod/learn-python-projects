num=int(input("please enter the recursive number: "))
def factorial(x):
    """This function returns the factorial of a number input by a user   """
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
print("The factorial of a number ",num,"is",factorial(num))