#function to add multiple arguments
def add(datatype,*args):
    #if the datatype is an int
    #initialise the answer to zero
    if datatype == 'int':
        answer=0
    #if datatype is str
    #initialise answer as ''
    if datatype == 'str':
        answer=''
#traversethrough the aurguments
    for x in args:
        #this will addition if the arguemnts are ints and concatenation if the values are string
        answer=answer+x
    print(answer)
#integer


add('int',3,5)
add('str','hello','nsubuga')