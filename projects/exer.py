#python program until you claim to be joe,the program shdnt ask for the password
#and once password is entered it exits
name=""
while name !="joe":
    print("Enter a name :")
    name=input()
print("Enter password:")
password=input()
if password=="haad":
    print("am done with code:")
    #exit()
name=""
while True:
    print("who are you??")
    name=input()
    if name !="joe":
        continue
    print("Hello! ",name,"Please enter your password:")
    password=input()
    if password=="haad":
       print("Am done with code:")
       exit()
