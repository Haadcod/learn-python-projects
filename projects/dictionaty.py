birthdays={"nsubuga":"november","warid":"may","mariam":"jan","wadda":"feb","mahad":"march"}
while True:
    print("Enter your name for date of birth:")
    name=input()
    if name=="":
        break
    if name in birthdays:
        print(name + "Your birthday is " + birthdays[name])
    else:
        print("I dont have birthday information for " +name)
        print("What is your birthday")
        birth=input()
        birthdays[name]=birth
        print("Birthday database is updated")
for v in birthdays.values():
    print(v)
import pprint
#python program to count the number of occurances of a character in a dictionary
message="It was  bright cold day in april, and the clocks wea striking thirteen"
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)
#nested dictionaries to get total brought by all to the picnic
allGuests={'Alice':{'apples':5,'pretzles':4},
           'Bob':{'Ham sandwiches':'2','apples':2},
           'carol':{'cups':3,'Apple pieces':5}}
def totalBrought(guests,item):
    numberBrought=0
    for k,v in guests.items():
        numberBrought=numberBrought + v.get(item)
        return numberBrought
print("Number of things being brought:")
print("-Apples    " + str(totalBrought(allGuests,"apples")))
print("how are you ?")
feelings=input()
if feelings.lower()=='great':
    print("am great too")
else:
    print("i am jhus good")
#manuplating strings
while True:
    print("Enter your age:")
    age=input()
    if age.isdecimal():
        break
    print("Please enter a number for your age:")
while True:
    print("Enter your password:")
    password=input()
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers;")