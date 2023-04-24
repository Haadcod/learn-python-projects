spam=0
if spam<5:
    spam+=1
   # print(spam)
spam=0
while spam<5:
    spam+=1
    print(spam)
while True:
    print("Enter your name:")
    name=input()
    if name !="joe":
        continue
    print("hello" + name + "Please enter your pssword")
    password=input()
    if password=="haad":
        break
print("Thank you!")
total=0
for num in range(100):
    total+=num
print(total)
import random
for i in range(5):
    print(random.randint(0,10))
import sys
while True:
    print("enter exit to exit ")
    response=input()
    if response=="exit":
        sys.exit()
    print("You have typed exit" +response)
