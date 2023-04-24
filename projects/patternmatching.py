#pattern matching without using regular expressions for a ugandan phone number
def isphoneNumber(text):
    if len(text) !=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] !='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] !='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
print("075-623-874-8 Is a phone number")
print(isphoneNumber('415-555-4242'))
#finding phone number within a larger string
mesage='Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(mesage)):
    chunk=mesage[i:i+12]
    if isphoneNumber(chunk):
        print("phone number found" +chunk)
print("Done")
#using regx
import re
