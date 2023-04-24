def collatz():
    try:
        while True:
            print("Enter a number ")
            number = int(input())
            if number % 2 == 0:
                return number // 2
            else:
                return 3 * number + 1
    except :
        print("invalid value...........")
name=collatz()
print(name)