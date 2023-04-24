a=int(input('Enter the side of triangle:'))
b=int(input('Enter second side of triangle:'))
c=int(input('Enter the third side of the triangle:'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the semi parameter of a triangle is %0.2f'%s)
print('The area of a triangle is %0.2f'%area)