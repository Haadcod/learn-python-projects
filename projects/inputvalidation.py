#input validation
while True:
    print("Enter your age:")
    age=input()
    try:
        age=int(age)
    except:
        print("please use numerical digits!")
    if age<1:
        print("Enter positive digits!")
        continue
    break