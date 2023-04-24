import sys,random,time
try:
    import bext
except ImportError:
    print('This program requires the bext module,which you')
    print('can installby following the instructions at ')
    print('http://pypi.org/project/Bext')
    sys.exit()
#Set up the constants
WIDTH,HEIGHT=bext.size()
#We can't print to the last column on windows without it adding a
#new line automatically, so reduce the width by one
WIDTH -=1
NumberOfLogos=5   #Try changing this to 1 or 100
pauseAmount=0.2   #Try changing this to 1.0 or 0
COLORS=['red','green','yellow','blue','magenta','cyan','white']
upRight='ur'
upLeft='ul'
downLeft='dl'
downRight='dr'
DIRECTION=(upRight,upLeft,downRight,downLeft)
#key names for logo dictionaries
COLOR='color'
X='x'
Y='y'
DIR='direction'

def main():
    bext.clear()
    #Generate some logos
    logos=[]
    for i in range(NumberOfLogos):
        logos.append({COLORS:random.choice(COLORS)
                      X:random.randint(1,WIDTH-4)
                      Y:random.randint(1,HEIGHT-4)
                      DIR:random.choice(DIRECTION)})

