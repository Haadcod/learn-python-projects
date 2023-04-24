import random
secretNumber=random.randint(0,10)
print("I am thinking of a number:")
for guessTaken in range(1,6):
    print("Take a guess:")
    guess=int(input())
    if guess<secretNumber:
           print("Your guess is too low")
    elif guess>secretNumber:
        print("Your guess is too high")
    else:
        break
if guess==secretNumber:
    print("Good job the guess is ", guess ,"in " ,str(guessTaken) ,"tyms")
else:
    print("Nop the number i was thinkig is " +str(secretNumber))