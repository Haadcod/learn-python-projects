# Pick a random number from a list
import random
list=[1,4,5,7,5,2,3,8,9,6,3,6]
print('The random number from a list is:',random.choice(list))
# Creating random numbers with a seeding value
random.seed(5)
print(random.random())
print(random.random())
# Random integers between a given range
#generate radom number btwn a given positive range
r1=random.randint(3,100)
print('Random number between 5,100 is % s'%(r1))
# Generates a random number between 2 give negative numbers
r2=random.randint(-100,-2)
print('Random number -100,-2 is % s'%(r2))
#print(random())
# Using the random seed unction
for i in range(5):
    # Any number can be used in place of 0
    random.seed(8)
    # Generate a random number in the range 1-1000
    print(random.randint(1,1000))
for i in range(4):
     random.seed(3)
     print(random.randint(1,1000))
     # If u want to get the same random number use seed 3
     random.seed(3)
     print(random.randint(1,1000))
# If seed function is not used it gives totally unpredictable response
print(random.randint(1,1000))
# Using the get state function in random number generation
state=random.getstate()
# Print a 10 random numbers in the range of 20
print(random.sample(range(20),k=10))
# Restore state
random.setstate(state)
# Print the first 5 random numbers as above
print(random.sample(range(20),k=5))
list=[2,3,4,5,6,7,4,3,1]
# Get the state
state=random.getstate()
# Print random number from the list
print(random.choice(list))
# Set state
random.setstate(state)
# Print the same random values from the list
print(random.choice(list))