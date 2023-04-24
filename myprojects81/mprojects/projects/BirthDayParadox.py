import datetime,random
def getBirthDay(numberOfBirthDays):
    """Returns a list of number random date objects for birthdays"""
    birthDay=[]
    for i in range(numberOfBirthDays):
        #The year is not important as long as all birthdays have the same year.
        startOfYear=datetime.date(2001,1,1)

        #Get a random day in the year
        randomNumberOfDays=datetime.timedelta(random.randint(0,364))
        birthday=startOfYear + randomNumberOfDays
        birthDay.append(birthday)
    return birthDay
def getMatch(birthdays):
    """Returns the birthday object of a birthday that occurs more than once in aa birthday list"""
    if len(birthdays)==len(set(birthdays)):
        return None   #All birthdays are unique so return None
    #Compare each birthday to every other birthday
    for a,birthdayA in enumerate(birthdays):
        for b,birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA==birthdayB:
                return birthdayA  #return the matching birthday

#Display the introduction
print("""The birthday paradox: 
          The birthday paradox shows that in a group of N people, The odds that 
          two o them have matching birthdays is suprisingly large.
          This program doesa monte carol simulation (that is repeated random simulations)
          to explore this concept""")
#set a tuple of month names
MONTHS=('jan','feb','mar','april','may','june','july','august','sept','oct','nov','dec')
while True:  #keep asking until a user enters a valid amount
    print('How many birthdays shall i generate (max 100)')
    response=input('>:')
    if response.isdecimal() and (0<int(response)<=100):
        numBdays=int(response)
        break #The user has entered a valid amount

print()

#Generate and display the birthdays
print('Here are ', numBdays,'birthdays')
birthdays=getBirthDay(numBdays)
for i,birthday in enumerate(birthdays):
    if i !=0:
        #Display a coma for each birthday after the first birthday
        print(',',end='')
    monthName=MONTHS[birthday.month -1]
    dateText='{} {}'.format(monthName,birthday.day)
print()
print()
#Determine if there are two birthdays that match
match=getMatch(birthdays)

#Display the results
print('In this simulation',end='')
if match !=None:
    monthName=MONTHS[match.month-1]
    dateText='{} {}'.format(monthName,match.day)
    print('Multiple people have birthdays on ',dateText)
else:
    print('There are no matching birthdays')
print()
#Run through 100,000 simulations
print("Generating",numBdays,'random birthdays 100,000 times')
input('Press enter to beging........')

print('Let\'s run another 100,000 simulations')
simMatch=0  #how many simulations had matching birthdays in them
for i in range(100000):
    #report the progress of every 10,000 simulations
    if i %10000==0:
        print(i,'simulation runs')
    birthdays=getBirthDay(numBdays)
    if getMatch(birthdays) !=None:
        simMatch+=1
print('100,000 simulations run' )

#Display simulation results
probability=round(simMatch/10000*100,2)
print('Out of 100,000 simulations of ',numBdays,'people,there was a')
print('matching birthday in that group',simMatch,'times. This means')
print('that',numBdays,'people have a',probability,'%chance of')
print('having a matching birthday in there group')
print('That\'s probably more than you wud think')


