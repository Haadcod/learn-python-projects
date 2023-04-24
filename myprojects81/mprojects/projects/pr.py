import random
num_digit=3
numbers=['0123456789']
random.shuffle(numbers)
secretNumber=''
for i in range(num_digit):
    secretNumber+=str(numbers[i])
print(secretNumber)