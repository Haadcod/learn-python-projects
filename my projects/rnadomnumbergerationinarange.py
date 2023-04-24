# Python code to demostrate the random range function
import random
print('Random numbers from 0-100')
print(random.randrange(100)+100)
print('Random numbers between 50-500')
print(random.randrange(50,100))
print('Random number between 0,100,5 siping 5')
print(random.randrange(0,100,5))
# Using random to generate numbers from 14.5 to 100
# Raises an exception
print('Random number from 14.5 to 100')
print(random.randrange(14,100))
