messages='It was a bright cold dayin april, and clocks wea ticking thirteen'
count={}
for character in messages:
    count.setdefault(character,0)
    count[character]=count[character]+1
print(count)
#function to readthis data structure and give the total number of gods being brought by people
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests,items):
    numBrought=0
    for k,v in guests.items():
        numBrought=numBrought +v.get(items,0)
    return numBrought
print('-  Apples   ' +str(totalBrought(allGuests,'apples')))

#strings
while True:
    print("Enter your age:")
    age=input()
    if age.isdecimal():
        break
    print("Enter a number for the age:")
while True:
    print("Enter password:")
    password=input()
    if password.isalnum():
        break
    print("Password can only have letters and numbers")
#print tabular data that has correct spacing
def printPicnicData(itemsDict,leftWidth,rightWidth):
    print('picnicItems'.center(leftWidth + rightWidth,'-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.') +str(v).rjust(rightWidth))
picnic={'sandwiches':4,'apples':12,'cups':12,'cookies':3}
printPicnicData(picnic,12,15)

