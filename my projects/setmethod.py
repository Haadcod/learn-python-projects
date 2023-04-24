import random
# Capture the current state
state=random.getstate()
# Print random number of the captured state
num=random.random()
print('A random number of the captured state :' +str(num))
# Print another random number
num=random.random()
print('Another random number is: '+str(num))
# Restore state using the set state
random.setstate(state)
# Print another random number after you have set the state
num=random.random()
print('The random number after the state has been state is:'+str(num))
print('---Another program using a list---')
list=[1,2,4,5,3,2,5,7,8,5,6]
# Get the state
state=random.getstate()
print(random.choice(list))
# Print list of random items  a given lenght
print(random.sample(list,3))
# Restore the state
random.setstate(state)
# print the new state of the list
print(random.sample(list,3))