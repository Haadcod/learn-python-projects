x=int(input('Enter a value of x:'))
y=int(input('Enter the value of y:'))
z=int(input('Enter the value of z:'))
if (x>y) and (x>z):
    largest= x
elif (y>x) and (y>z):
    largest=y
else:
    largest=z
print('{0} is the lagest number '.format(largest))