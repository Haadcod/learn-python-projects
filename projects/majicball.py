import random
messages=['I am nsubuga',
          'a son to yahya mabira',
          "and mothered by nalumu rehma",
          "i grew up in makindye a kampala suburb",
          "presided over by mayor mulyanyama ali",
          "the division has good people"]
name=messages[random.randint(0,len(messages)-1)]
print(name)
names=random.choice(messages)
print(names)
def eggs(someParameter):
    someParameter.append("Heloo")
spam=["nsubuga abdulhaad","hope you are ok "]
eggs(spam)
print(spam)