print("my name is")
for i in range(5):
    print("jimmy five times ("+ str(i)+")")
#python program to add up numbers from 0-100
total=0
for num in range(100):
    total=total+num
print(total)
print("my name is:")
i=0
while i<5:
    print("jimyy ive times ("+str(i)+")")
    i+=1
#print 5 random numbers in the range of 1 to 10
import random
for i in range(5):
    print(random.randint(1,10))
import  sys
while True:
    print("Type exit to exit")
    response=input()
    if response=='exit':
        sys.exit()
    print("You typed" +response+'.')