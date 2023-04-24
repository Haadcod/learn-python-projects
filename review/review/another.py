import random

catNames=[]
while True:
    print('Enter cat name' + str(len(catNames)+1))
    name=input()
    if name =='':
        break
    catNames.append(name)
print('Cat list is:')
for name in catNames:
    print(name)
myPets=['cats','goats','cows','donkeys']
print('Enter a per')
pet=input()
if pet not in myPets:
    print("I dont have that pet in my list")
else:
    myPets.append(pet)
for pet in myPets:
    print(pet)
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
print(messages[random.randint(0,len(messages)-1)])
print(random.choice(messages))
def eggs(somparameter):
    somparameter.append('hello')
spam=[1,2,3,4]
eggs(spam)
print(spam)