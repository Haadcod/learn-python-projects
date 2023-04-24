catNames=[]
while True:
    print("Enetr name of the cat "  + str(len(catNames)+1) +   " Or enter nothing to stop.")
    name=input()
    if name=="":
        break
    catNames=catNames+[name]
print("The cats are:")
for name in catNames:
    print(" " +name)
for i in range(len(catNames)):
    print(" index" + str(i) + " in catnames is " +catNames[i])
print("Enter cat name to check for its existance:")
names=input()
if names not in catNames:
    print("I dont have that catname in the list")
else:
    print(names+ " is my cat")
#using the enumerate function
for index,item in enumerate(catNames):
    print("index" +str(index) + "in catnames" +item)
