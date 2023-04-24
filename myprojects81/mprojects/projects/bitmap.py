import sys
bitmap="""
...................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""
print("Bitmap message")
print("Enter messaage to display the bitmap :")
message=input(">:")
if message=='':
    sys.exit()
#Loop over each line in a bitmap
for line in bitmap.splitlines():
    #Loop over each character in the line
    for i ,bit in enumerate(line):
        if bit==' ':
            #printanempty space since theres space in the bitmap
            print(' ',end='')
        else:
            #print a character from the message
            print(message[i % len(message)],end='')
    print()

