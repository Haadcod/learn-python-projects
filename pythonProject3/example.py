try:
    x= int(input('Enter a value:'))
    y= int(input('enter a value:'))
    print(x/y)
except(ZeroDivisionError,TypeError) as e:
      print(e)
