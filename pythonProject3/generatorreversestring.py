def rev_str(my_str):
    lenght=len(my_str)
    for i in range(lenght -1,-1,-1):
        yield my_str[i]
for char in rev_str("abdulhaad"):
    print(char)