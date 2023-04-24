#simple python program to count the number o characters
messages="It was a bright cold day in April, and the cloocks were striking thirteen"
count ={}
for character in messages:
    count.setdefault(character,0)
    count[character]=count[character]+1
print(count)
#program to calculate the total of items brought by people at the picnic
allGuests={"Alice":{"apples":5,"pretzels":2},
           "Bob":{"ham sandwitches":3,"apples":3},
           "carol":{"cups":2,"apple pies":4}}
def totalBrought(guests,item):
    numberBrought=0
    for k,v in guests.items():
        numberBrought=numberBrought + v.get(item,0)
    return numberBrought
print("Number of things being brought")
print(" _Apples     " + str(totalBrought(allGuests,'apples')))
