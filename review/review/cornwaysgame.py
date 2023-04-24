#cornways game of life
import random,copy,time
WIDTH=60
HEIGHT=20

#create a list for th cells
nextCells=[]
for x in range(WIDTH):
    column=[] #create a new column
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#') #add a living cell
        else:
            column.append('') #add a dead cell
    nextCells.append(column)
while True:  #loop main program
    print('\n\n\n\n\n\n') #separate each step with new lines
    currentCells=copy.deepcopy(nextCells)

    #print current cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end="") #print the # or space on the screen
        print() #print new line at the end of the row
    #calculate the next steps cells based on the current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get neighbouring coordinates
            # ' % WIDITH' ensures leftcoord is always between 0 and WIDITH -1
            leftCoord=(x-1) % WIDTH
            rightCoord=(x+1) % WIDTH
            aboveCoord=(y-1) % HEIGHT
            belowCoord=(y+1) %HEIGHT

            #count the number of living neighbours
            numNeighbours=0
            if currentCells[leftCoord][aboveCoord]=='#':
                numNeighbours +=1   #Top-left neghtbour is alive
            if currentCells[x][aboveCoord]=='#':
                numNeighbours +=1  #Top neighbour is alive
            if currentCells[rightCoord][aboveCoord]=='#':
                numNeighbours +=1 #Top_right neighbour is alive
            if currentCells[leftCoord][y]=='#':
                numNeighbours +=1  #Left neighbour is alive
            if currentCells[rightCoord][y]=='#':
                numNeighbours +=1  #right neighbour is alive
            if currentCells[leftCoord][belowCoord]=='#':
                numNeighbours +=1  #Bottom left neighbour is alive
            if currentCells[x][belowCoord]=="#":
                numNeighbours +=1 #bottom neighbour is alive
            if currentCells[rightCoord][belowCoord]=='#':
                numNeighbours +=1  #bottom-right neighbour is alive
            #set cell based on cornways game of life
            if currentCells[x][y]=="#" and (numNeighbours==2 or numNeighbours==3):
                #living cells with 2 or 3 neighbours stay alive
                nextCells[x][y]='#'
            elif currentCells[x][y]=='' and numNeighbours==3:
                #dead cells with 3 neighbours become alive
                nextCells[x][y]='#'
            else:
                #Everthing else dies or stays dead
                nextCells[x][y]=''
    time.sleep(1)  #add a 1-second pause to reduce flickering
