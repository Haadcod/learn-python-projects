catNames=[]
while True:
    print("Enter catname" +str(len(catNames)+1),"or enter nothing to stop.")
    name=input()
    if name=='':
        break
    catNames.append(name)
print("Catnames is !")
for name in catNames:
    print(name)
myPets=[]
while True:
    print("Please enter your pet name " +str(len(myPets)+1)+ "or enter nothing to stop")
    pet=input()
    if name=='':
        break
    myPets.append(name)
    exit()
print("enter a pet name or check")
pet=input()
if pet not in myPets:
    print("I dont have that pet in my list")
    myPets.append(pet)
else:
    print('The pet '+ pet + 'exists in my list')
    for i in range(len(myPets)):
        print("index" +str(i)+ "is in mypets" +myPets[i])
