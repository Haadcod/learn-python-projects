import random
import datetime
# Global declaration
name=[]
phno=[]
add=[]
day=[]
checkin=[]
checkout=[]
room=[]
roomno=[]
custid=[]
price=[]
rc=[]
p=[]

# Global value declaration
i=0

# Home function
def home():
    print('\t\t\t\t\t WELCOME TO HOTEL ANCASA\n')
    print('\t\t\t 1 Booking\n')
    print('\t\t\t 2 Rooms Info\n')
    print('\t\t\t 3 Room Service Menu\n')
    print('\t\t\t 4 Payment\n')
    print('\t\t\t 5 Record\n')
    print('\t\t\t 0 Exit\n')
    ch=int(input('->'))
    if ch==1:
        print('')
        booking()
# Function used in booking
def date(c):
    if c[2]>=2019 and c[2]<=2020:
        if c[1]!=0 and c[1]<=12:
            if c[1]==2 and c[0]!=0 and c[0]<=31:
                if c[2]%4 ==0 and c[0]<=29:
                    pass
                elif c[0]>29:
                    pass
                else:
                    print('Invalid date\n')

            # If month is odd and less than equal to 7th month
            elif c[1]<=7 and c[1]%2!=0 and c[0]<=31:
                pass
            # If month is even and less than equal to 7th month and not 2nd month
            elif c[1]<=7 and c[1]%2==0 and c[0]<=31 and c[1]!=2:
                pass
            # If month is odd and less than equal to 8th month
            elif c[1]<=8 and c[1]%2!=0 and c[0]<=30:
                pass
            else:
                print('Invalid date\n')

        else:
            print('Invalid date\n')
    else:
        print('Invalid date\n')
# Booking function
def booking():
    # Use global key word to use global variable
    global i
    print('BOOKING ROOMS')
    print('')
    while 1:
        n=str(input('Name:'))
        p1=str(input('PhoneNumber'))
        a=str(input('Address'))
        # Check if any of the fields is empty
        if n!='' and p1!='' and a!='':
            name.append(n)
            add.append(a)
            break
        else:
            print('\tName,PhoneNumber,Address cannot be empty...!')
    cii=str(input('CheckIn:'))
    checkin.append(cii)
    cii=cii.split('/')
    ci=cii
    ci[0]=int(ci[0])
    ci[1]=int(ci[1])
    ci[2]=int(ci[2])
    date(ci)

    coo=str(input('CheckOut:'))
    checkout.append(coo)
    co=coo
    co[0]=int(co[0])
    co[1]=int(co[1])
    co[2]=int(co[2])

    # Check if checkout date falls after checkin date
    if co[1]<ci[1] and co[2]<ci[2]:
        print('\n\tErr..!!\n\tCheckout date must fall after checkin')
        name.pop(i)
        add.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        booking()
    else:
        pass
    date(co)
    d1=datetime.datetime(ci[2],ci[1],ci[0])
    d2=datetime.datetime(co[2],co[1],co[1])
    d=(d2-d1).days
    day.append(d)

    print('--SELECT ROOM TYPE--')
    print('1.Standard No AC')
    print('2.Standard AC')
    print('3.3-Bed No AC')
    print('4.3-Bed AC')
    print(('\t\tPress 0 for room prices '))
    ch=int(input('->'))

    # If condition to display alloted room type and price
    if ch==0:
        print('1. Standard Non AC-Ugx. 120000')
        print('2. Standard AC-Ugx. 150000')
        print('3.3-Bed Non AC-Ugx. 200000')
        print('4.3-Bed AC-Ugx.300000')
    elif ch==1:
        room.append('Standard Non AC')
        print('Room Type- Standard Non-AC')
        price.append(120000)
        print('Price-120000')
    elif ch==2:
        room.append('Standard AC')
        print('Room Type-Standard AC')
        price.append(150000)
        print('Price-150000')
    elif ch==3:
        room.append('3-Bed room AC')
        print('Room Type-3 Bed AC')
        price.append(200000)
        print('Price-200000')
    elif ch==4:
        room.append('3-Bed Non AC')
        print('Room Type -3-Bed Non AC')
        price.append(300000)
        print('Price-300000')
    else:
        print('Wrong Choice')
    # Randomly generating room no. and customer id for the customer
    rn=random.randrange(40)+300
    cid=random.randrange(60)+10
    # Check if alloted room number and customer id are not alloted
    while rn in roomno or cid in custid:
        rn=random.randrange(40)+300
        cid=random.randrange(60)+10
    rc.append(0)
    p.append(0)
    if p1 not in phno:
        phno.append(p1)
    elif p1 in phno:
        for n in range(0,i):
            if p1==phno[n]:
                if p[n]==0:
                    print('\tPhone number already exists and payment yet not done..')
                    name.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    booking.pop(i)
        print('')
        print('\t\t\t***ROOM BOOKED SUCCESSFULLY"***\n')
        print('Room No. -',rn)
        print('Customer Id -',cid)
        roomno.append(rn)
        custid.append(cid)
        i=i+1
        n=int(input('0-BACK\n->'))
        if n==0:
            home()
        else:
            exit()
#ROOM INFO
def rooms_info():
    print('........ROOMS INFORMATION.........')
    print('')
    print('STANDARD NON AC')
    print('--------------------------------------------------------------')
    print('Room amenities include: 1 Double bed, Televison,Telephone')
    print('Double door cupboard, 1 coffee table with 2 sofa,balcony and')
    print('an attached washroomwith hot/cold water.\n')
    print('STANDARD NON-AC')
    print('..................................................................')
    print('Room amenities include: 1 Double bed,Television,Telephone')
    print('Double door cupbord, 1 coffee table with 2 sofa, balcony and')
    print('an attached washroom with hot/cold water + windows/Spit AC.\n')
    print('3 Bed NON-AC')
    print('---------------------------------------------------------------')
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print()
    n=int(input('0-BACK->'))
    if n==0:
        home()
    else:
        exit()
#RESTAURANT FUNCTON
def restaurant():
    ph=int(input('Customer Id:'))
    global i
    f=0
    r=0
    for n in range(0,i):
        if custid[n]==ph and p[n]==0:
            f=1
            print('-------------------------------------------------------------------')
            print('                          HOTEL NSUBUGA')
            print('-------------------------------------------------------------------')
            print('                           MENU CARD  ')
            print('...................................................................')
            print("\n BEVARAGES                              26 Dal Fry................ 140.00")
            print("----------------------------------      27 Dal Makhani............ 150.00")
            print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00")
            print(" 2  Masala Tea.............. 25.00")
            print(" 3  Coffee.................. 25.00      ROTI")
            print(" 4  Cold Drink.............. 25.00     ----------------------------------")
            print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00")
            print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00")
            print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00")
            print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00")
            print(" 9  Cheese Toast Sandwich... 70.00")
            print(" 10 Grilled Sandwich........ 70.00      RICE")
            print("                                       ----------------------------------")
            print(" SOUPS                                  33 Plain Rice.............. 90.00")
            print("----------------------------------      34 Jeera Rice.............. 90.00")
            print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00")
            print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00")
            print(" 13 Veg. Noodle Soup....... 110.00")
            print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN")
            print(" 15 Veg. Munchow........... 110.00     ----------------------------------")
            print("                                        37 Plain Dosa............. 100.00")
            print(" MAIN COURSE                            38 Onion Dosa............. 110.00")
            print("----------------------------------      39 Masala Dosa............ 130.00")
            print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00")
            print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00")
            print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00")
            print(" 19 Palak Paneer........... 120.00")
            print(" 20 Chilli Paneer.......... 140.00      ICE CREAM")
            print(" 21 Matar Mushroom......... 140.00     ----------------------------------")
            print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00")
            print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00")
            print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00")
            print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")
            print('Press 0 to End')


