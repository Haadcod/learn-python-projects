import time,sys
#how many spaces to indent
indent=0
#whether indention is increasing or not
increasingIndent=True
try:
    while True: #The main program loop
        print(' ' * indent, end='')
        print("********")
        time.sleep(0.1) #pause or o.1 secs
        if increasingIndent:
            #increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                increasingIndent = False
            else:
                #decrease the number of spaces
                indent = indent - 1
                if indent == 0:
                    #change direction
                    increasingIndent = True
except KeyboardInterrupt:
    sys.exit()
