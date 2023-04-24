import random
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
print(random.choice(messages))
def eggs(someparameter):
    someparameter.append('hello')
spam=[1,2,3,4]
eggs(spam)
print(spam)
#Regex
def isPhoneNumber(text):
    if len(text) !=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] !='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] !='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return  True
print("415-555-1234 is a phone number")
print(isPhoneNumber('415-555-1234'))
print("Is moshi moshi a phone number")
print(isPhoneNumber("mosh moshi"))



message='call me on 415-555-1011 tomorrow. 414-533-1324'
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found  " + chunk)
print('done')
#input validation
while True:
    print('Enter your name:')
    age=input()
    try:
        age=int(age)
    except:
        print("Please enter a numeric number for the age")
        continue
    if age<1:
        print("The age must be positive")
        continue
    break
#custom functions (python program that sums numbers upto 10
import pyinputplus as np
def addUpToTen(numbers):
    numbersList=list(numbers)
    for i ,digit in enumerate(numbersList):
        numbersList[i] =int(digit)
    if sum(numbersList) !=10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers)
response=np.inputCustom(addUpToTen)



