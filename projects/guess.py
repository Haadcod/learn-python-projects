import random
secretNumber=random.randint(1,10)
print("I am thinking of a number between 1 and 10")
for guessTaken in range(1,7):
    print("Take a guess:")
    guess=int(input())
    if guess<secretNumber:
        print("your guess is too low:")
    elif guess>secretNumber:
        print("your guess is too high:")
    else:
        break
if guess==secretNumber:
   print("Good job , you have guessed the number,",guess,'in',guessTaken,"Times")
else:
    print("The number i was thinking is ",secretNumber)