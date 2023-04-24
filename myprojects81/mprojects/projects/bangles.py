"""guess a three digit number based on clues. The guess offers the following hints in response to
your guess. 'PICO' when your guess has a correct digit in the wrong place. 'FERMI' when your guess
has correct digit in the right place, 'BANGLES' when your guess has no correct digit. You also have
10 tries to guess the correct secret number"""
import random
max_guess=10
num_digits=3
def main():
    print("""Bagels a deductive logic game.
    I am thinking of a {}- digit number with no repeated digits.
    Trying to guess the number would be. The following are the clues:
    when i say:             That means:
    PICO                     Digit is correct but in the wrong place
    FERMI                    Digit is correct nad in the right position
    BAGLE                    Digit is not correct
    For example if the secret number was 248 and my guess was 843,the clues would be FERMI,PICO""")
    while True:
        #This stores the secrete number the player needs to guess
        secretNumber=getSecretNum()
        numGuess=1
        while numGuess<=max_guess:
            guess=''
            # keep looping until a valid guess is entered
            while len(guess) != num_digits or not guess.isdecimal():
                print("Guess #{}".format(numGuess))
                guess=input('>')
            clues=getClues(guess,secretNumber)
            print(clues)
            numGuess+=1

            if guess==secretNumber:
                break  # They are correct, so break out of this loop
            if numGuess > max_guess:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secretNumber))
        #Ask player if they want to play again
        print("Do you want to play again ? Yes/No")
        if not input('>').lower().startswith('y'):
            break
    print("Thanks for playing")

def getSecretNum():
    """Returns the string made up of NumDigits unique random digits """
    numbers=list('0123456789') #Create a list of digits 0 to 9
    random.shuffle(numbers)
    #Get the first num_digit in the list for the secret number
    secretNumber=''
    for i in range(num_digits):
        secretNumber+=str(numbers[i])
    return secretNumber
def getClues(guess,secretNum):
    """Returns a string with the pico, fermi, bagle clues for a guess and secretnumber pair."""
    if guess==secretNum:
        return 'You got it'
    clues=[]
    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            #A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #A correct digit is in the incorrect place
            clues.append('pico')
    if len(clues)==0:
        return 'Bagels' #There are no correct digits at all
    else:
        #Sort the clues into alphabetical order so their original order doesnt give information way
        clues.sort()
        #make  a single string from the list of string clues
        return ''.join(clues)

print(main())