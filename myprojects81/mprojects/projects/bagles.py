import random
num_digit=3
max_num=10
def main():
    print("""I am thinking of a three digit number.Try to guess what it is.
    Here are some of the clues.
    When i say            That means
    Pico                  one digit is correct buh in the wrong position
    Fermi                 one digit is correct and  in the right position
    bagles                No digit is correct
    For example, if secret number was 234 and your guess was 843, the clue would fermi pico.""".format(num_digit))
    while True:
        #This stores the secretNumber the player needs to enter
        secretNum=secretNumber()
        print("I have thought up a number")
        print("You have {} guesses to get it".format(max_num))
        num_guesses=1
        while num_guesses<=max_num:
            guess=''
            #keep looping until they enter a valid guess
            while len(guess) !=num_digit or not guess.isdecimal():
                print('Guesses #{}'.format(num_guesses))
                guess=input('>:')
            clues=getClue(guess,secretNum)
            print(clues)
            num_guesses+=1
            if guess==secretNum:
                break
            if num_guesses>max_num:
                print("You ran out of guesses")
                print("The answer was {}.".format(secretNum))
        #Ask player if they want to play again
        print('Do you want to play again? (yes/no')
        if not input('>:').lower().startswith('y'):
            break
    print("Thanks or playing;")


def secretNumber():
    """Returns a string made up of num_digits unique random digits"""
    number=list('0123456789')
    random.shuffle(number)
    #Get the first um_digits in the list for the secretnumber
    secretNum=''
    for i in range(num_digit):
        secretNum=secretNum +str(number[i])
    return secretNum
def getClue(guess,secretNum):
    """This returns a string with pico fermi,bagels clues or a guess and the secrete number pair"""
    if guess==secretNum:
        return 'you got it'
    clues=[]
    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            # A correct digit is in the right place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #A correctdigit is in the incorrect place
            clues.append('Pico')
    if len(guess)==0:
        return 'Bagles'   #Theres no correct value
    else:   #sort the clues in alphabetical order so their original order doesnot give information
        clues.sort()
        #make a single string from the list of strings
        return ''.join(clues)
if __name__=='__main__':
    main()