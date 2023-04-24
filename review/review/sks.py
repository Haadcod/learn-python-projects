"""program takes the function with parameters width and height
to make a litte picture  a box"""
def printBox(symbol,width,hieght):
    if len(symbol) !=1:
        raise Exception('Symbol must be a single character:')
    if width<=2:
        raise Exception('Width must be greater than 2: ')
    if hieght <=2:
        raise Exception('Height must be greater than 2:')
    print(symbol * width)
    for i in range(hieght-2):
        print(symbol +(''*(width -2)) + symbol)
    print(symbol * width)
for sym,w,h in (('*',4,4),('0',4,4),('z',3,3)):
    try:
        printBox(sym,w,h)
    except Exception as err:
        print('An exception happened:' +str(err))
