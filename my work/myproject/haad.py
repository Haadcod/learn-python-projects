from math import pi
#python program to print a string in a specific format
print('Twinkle, twinkle, little star, \n\tHow i wonder what you are ! \n\t\tabove the world is soo high \n\t\tLike a diamond in the sky. \nTwinkle Twinkle little star,\n\thow i wonder what you are! ')
#a program that accepts the input of a radius by a user and calculates the area
#x=float(input('Please enter the radius of the circle:'))
#print('The area of a circle is:', str(pi * x ** 2))
#python progrma to display current date and time
import datetime
now=datetime.datetime.now()
#print('The current date and time is :')
#print(now)
#python program that accepts the radius of a circle and computes area
import math
#X=float(input('Please enter the radius of a circle for which you want to compute the area:'))
#print('The computed area of a circle is:',pi * X **2)
#ptyhon program to print the first and last anme in reverse
#fname=input('Enter the first name:')
#lname=input('Enter the last name')
#print('Hello'  +lname+ '' +fname)
#python program that accepts a coma separated list of numbers
#values=input('Enter a coma separated list of numbers:')
#list=values.split(",")
#print(list)
#tuple=tuple(list)
#print(tuple)
#python program that accepts filename and prints the extension of that file
#filename=input('Please enter file name:')
#f_extns=filename.split('.')
#print('Te file name is :' +repr(f_extns[-1]))
#pythonprogrma to display the first and last colors in a list
list=['blue','green','marron','craion','white','red']
print('The first and last colors in alist are:',list[0],list[5])
#python program to extract examination date
exam_st_date=(11,23,2014)
print('The examination will start on the %i / %i / %i:' %exam_st_date)
#python program that accepts an interger n and computes for the out come
X=int(input("Enter the interger number for compputation"))
n1=int("%s" %X)
print(n1)
n2=int("%s%s" %(X,X))
print(n2)
n3=int("%s%s%s" %(X,X,X))
print(n3)
print((n1+n2+n3))
#python program to print out the calendar of a given month
import calendar
y=int(input("Enter a year"))
m=int(input("Enter a month"))
x=calendar.month(y,m)
print(x)

