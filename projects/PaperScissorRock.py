#Simple Rock Paper,Scissors game
import sys
import random
print("Rock,Paper,Scissors")
#variables to track number of wins, looses and ties
wins=0
looses=0
ties=0
#main game loop
while True:
    print("%s wins,%s looses, %s ties" %(wins,looses,ties))
    #The player input loop
    while True:
        print("Enter your move: (r)ock,(p)aper,(s)cissors or (q)uit")
        playerMove=input()
        if playerMove=='q':
            sys.exit()
        if playerMove=='r' or playerMove=='p' or playerMove=='s':
            break
        print("Type one of r,p,s or q")
    #display user input
    if playerMove=='r':
        print("Rock versus.......")
    elif playerMove=='p':
        print("Paper versus......")
    elif playerMove=='s':
        print("Scissor versus.....")
    #display wat the computer chose.
    randoNumber=random.randint(1,3)
    if randoNumber==1:
        computerMove='r'
        print("ROCK")
    elif randoNumber==2:
        computerMove="p"
        print("PAPER")
    elif randoNumber==3:
        computerMove='s'
        print("SCISSORS")
    #display and the wins/looses/ties
    if playerMove==computerMove:
        print("Its a tie!")
        ties+=1
    elif playerMove=='r' and computerMove=='s':
        print("You win!")
        wins+=1
    elif playerMove=='p' and computerMove=='r':
        print("You win!")
        wins+=1
    elif playerMove=='s' and computerMove=='p':
        print("You win!")
        wins+=1
    elif playerMove=='r' and computerMove=='p':
        print("You loose!")
        looses+=1
    elif playerMove=='p' and computerMove=='s':
        print("You loose!")
        looses+=1
    elif playerMove=='s' and computerMove=='r':
        print("You loose!")
        looses=+1