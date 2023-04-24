# A short game on who reaches 100 first winshave been depicted in the code below
# Each player is allowed a dice of 1-10 numbers ie at each 1-10 can be attained
import random
sum=0
sum1=0
count=0
while(1):
    # Generate random number at each turn 1-10
    r1=random.randrange(1,10)
    r2=random.randrange(1,10)
    # Adding to account of players
    sum=sum+1
    sum1=sum1+1
    count=count+1
    print('Total score of player 1 after %d is : %d' %(count,sum))
    # Break when player 1 reaches 100
    if(sum>100):
        flag=1
        break
    print('Total score of player 2 ater %d is: %d'%(count,sum1))
    if(sum>100):
        flag=2
        break
if(flag==1):
    print('/n Player one wins the game')
else:
    print('/n Player two wins the game')
