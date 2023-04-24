class Parrot:
    spicies='bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=Parrot('blue','10')
woo=Parrot('woo','90')
print('blu is a {}'.format(blu.__class__.spicies))
print('woo is a {}'.format(woo.__class__.spicies))
print('{} is {} years old'.format(blu.name,blu.age))
print('{} is {} years old'.format(woo.name,woo.age))