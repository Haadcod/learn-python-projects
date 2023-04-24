#convert kilometers to miles
kilometers=float(input('Enter a values in kilometers:'))
conv_fac=0.621371
miles=kilometers*conv_fac
print('%0.2f kilometers is equal to %0.2f miles'%(kilometers,miles))
#convert miles to kilometers
miles=float(input('Enter value in miles:'))
kilometers=miles/conv_fac
print('%0.2f  miles is equal to %0.2f kilometers'%(miles,kilometers))