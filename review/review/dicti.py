birthdays={'nsubuga':'april 1','mariam':'june 3','warid':'july 12','nalumu':'august 23'}
while True:
    print("Enter the name : (blankto quit!")
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name] + 'is the birthday of'+name)
    else:
        print("i dont have that birthday information for "+name)
        print("what is your birthday:")
        bday=input()
        birthdays[name]=bday
        print("Birthday database is updated")