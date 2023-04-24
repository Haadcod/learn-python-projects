print('---program for printing student name with marks using a list---')
#create an empty dictionary
d={}
n=int(input('how many student many student record you want to store??'))
#create an empty list
#add student information to the empty list
l=[]
for i in range(0,n):
    #take the combined name and percentage and then split them using the split function
    x,y=input('Enter student name and percentage').split()
    #add name and marks stored in x and y respectively using the tuple list
    l.append((x,y))
l=sorted(l,reverse=True)
print('list of sorted students and marks in descending order')
for i in l:
    #print the list of sorted student marks and names in second first order
    print(i[1],i[0])
#C:\Users\haad\PycharmProjects\my projects