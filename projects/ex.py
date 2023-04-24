spam=0
if spam<5:
    print("hello world")
    spam+=1
print("\n===========================================================")
while spam<5:
    print("hello world")
    spam+=1
name=""
while name !="Your name":
    print("Please type in your name")
    name=input()
print("thank you ",name)
while True:
    print("Please enter your name")
    name=input()
    if name=="nsubuga":
        break
print("Thank you ",name)
while True:
    print("Please identify your self")
    name=input()
    if name !="nsubuga":
        continue
    print("Enter your password:")
    password=input()
    if password=="haad":
        break
print("Welcome to your page !",name)
name=""
while not name:
    print("Enter a name:")
    name=input()
print("How many guests do you want:")
numberOfGuests=int(input())
if numberOfGuests:
    print("Be sure to have enough room for the guests:")
print("Done")

