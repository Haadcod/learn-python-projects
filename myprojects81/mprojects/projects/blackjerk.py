import random,sys
#set up constants
HEARTS=chr(9829) #character 9829 is 'hearts'
DIAMONDS=chr(9830) #character 9830 is 'diamonds
SPADES=chr(9824)   #character 9825 is 'spades'
CLUBS=chr(9827)    #character 9827 is 'clubs'
BACKSIDE='backside'

def main():
    print("""BLACK JERK
    RULES:
    Try to get as close to 21 without going over.
    Kings,Queens,jacks are worth 21 points.
    Aces are worth 1 or 11 points
    cards 2 through 10 are worth their face value
    (H)it to take another card
    (S)tand to stop taking cards
    On your first play you can (D)ouble down to increase your bet
    but must first hit exactly one more time before standing.
    Incase of a tie, the bet is returned to the player.
    The dealer stops hiting at 17""")
    money=5000
    while True:
        #Check i player has run out of money:
        if  money <=0:
            print('You are broke!')
            print("Good thing you weren't playing with real money.")
            print("Thanks or playing!")
            sys.exit()
        #Let the player enter their bet for this round
        print("Money:",money)
        bet=getBet(money)
        #Give the dealer and player two cards from each deck each.
        deck=getDeck()
        dealerHand=[deck.pop(),deck.pop]
        playerHand=[deck.pop(),deck.pop()]
        #Handle player actions
        print('BET:',bet)
        while True:  #loop until player stands or busts.
            displayHands(playerHand,dealerHand,False)
            print()

            #Check if player has bust.
            if getHandValue(playerHand)>21:
                break
            #Get the players move, either H,S or D
            move=getMove(playerHand,money-bet)
            #Handle player actions
            if move=='D':
                #Player is doubling down, they can increase their bet.
                additionalBet=getBet(min(bet,(money-bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print("Bet:",bet)
            if move in ('H','D'):
                #Hit/Doublingdown takes another stand
                newCard=deck.pop()
                rank,suit=newCard
                print("You drew a {} of {}.".format(rank,suit))
                playerHand.append(newCard)
                if getHandValue(playerHand)>21:
                    continue #The player has busted

            if move in ('S','D'):
                #Stand/Doubling down stops the players turn
                break
        #Handle the dealers actions
        if getHandValue(playerHand) <=21:
            while getHandValue(dealerHand) < 17:
                #The dealer hits:
                print("DEALER hits......")
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)

                if getHandValue(dealerHand) >21:
                    break  #The dealer has busted
                input('Press Enter to continue.....')
                print('\n\n')
        #show final hands
        displayHands(playerHand,dealerHand,True)

        playerValue=getHandValue(playerHand)
        dealerValue=getHandValue(dealerHand)
        #Handle whether player won,lost,tied
        if dealerValue >21:
            print("Dealer busts! You win ${}!".format(bet))
            money+=bet
        elif playerValue >21 or (playerValue <dealerValue):
            print("Player busts. You lost!")
            money-=bet
        elif playerValue > dealerValue:
            print("You won ${}!".format(bet))
            money+=bet
        elif playerValue==dealerValue:
            print("It's a tie The bet is returned to you. ")
        input("Press Enter to continue........")
        print('\n\n')

def getBet(maxBet):
     """Ask the player how much they want to bet for this round."""
     while True:  #keep asking until the user enters a valid amount
         print("How much do you want to bet?(1-{}, or QUIT)".format(maxBet))
         bet=input('>:').upper().strip()
         if bet=='QUIT':
             print('Thanks for playing!')
             sys.exit()
         if not bet.isdecimal():
             continue   #If player didnot enter a number ask again
         bet=int(bet)
         if 1 <= bet <= maxBet:
             return bet   #player entered a valid bet
def getDeck():
    """Return alist (rank,suit) tuples for all 52 cards"""
    deck=[]
    for suit in (HEARTS,DIAMONDS,SPADES,CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit))  #Add the numbered cards
        for rank in ('J','Q','K','A'):
            deck.append((rank,suit))   #Add the face and ace cards
    random.shuffle(deck)
    return deck
def displayHands(playerHand,dealerHand,showDealerHand):
    """Show players and dealers cards . Hide the dealers first card if showDealerHand is False"""
    print()
    if showDealerHand:
        print('DEALER:',getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        #Hide the dealers first card
        displayCards([BACKSIDE]) + dealerHand[1:]
    #Show the players card
    print("PLAYER:",getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10,aces are worth 11 or 1
     (This function picks the most suitable ace value)."""
    value=0
    numberOfAces=0
    #Add value for non-ace cards
    for card in cards:
        rank=card[0]  #card is a tuple like (rank,suit)
        if rank=='A':
            numberOfAces+=1
        elif rank in ('K','Q','J'):   #Face cards are worth 10 points
            value+=10
        else:
            value+=int(rank)  #numbered values are worth their rank
        #Add value for aces
        value+=numberOfAces   #Add 1 per Ace
        for i in range(numberOfAces):
            #I another 10 can be added without busting,do so
            if value + 10 <= 21:
                value+=10
        return value
def displayCards(cards):
    """Display all the cards in the list"""
    rows=['','','','','']  #The text to display on each row

    for i,card in enumerate(cards):
        rows[0]='___'  #Print the top line of the card
        if card ==BACKSIDE:
            #Print the cards back
            rows[1]+='|##| '
            rows[2]+='|###|'
            rows[3]+='|_##|'
        else:
            #Print the cards front
            rank,suit=card  #The card is a tuple data structure
            rows[1]+='|{} |'.format(rank.ljust(2))
            rows[2]+='| {} |'.format(suit)
            rows[3]+='|_{}|'.format(rank.rjust(2,'_'))
    #Print each row on the screen
    for row in rows:
        print(row)
def getMove(playerHand,money):
    """Asks the player for their move, and returns 'H' for hits, 'S' for stand, and 'D' for double down"""
    while True: #Keep looping until a player enters a correct value
        #Determine what moves the player can make
        moves=['(H)it','(S)tand']
        #The player can double down their first move which we can tell because they'll have exactly two cards
        if len(playerHand)==2 and money>0:
            moves.append('(D)ouble down')
        #Get the players move
        movePrompt=', '.join(moves) + '>'
        move=input(movePrompt).upper()
        if move in ('H','S'):
            return move #Player has entered a correct move
        if move=='D' and '(D)ouble down' in moves:
            return move   #Player has entered a valid move
if __name__=='__main__':
    main()