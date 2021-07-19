#version implementing winning conditions

import tkinter,time #tkinter library to create GUI, time for animations

def createGrid(rows,columns,totalHeight,totalWidth): #function to draw the grid
    global board, gridFrame #because of tkinters event-driven style global variables have to be used
    #total height and width represent the height and width of the screen
    
    board = [] #where every cell on the grid is stored
    gridFrame = tkinter.Frame(master=secondFrame,bg="gainsboro",pady=10)
    #frame that will hold the grid
    

    ratio = columns/rows #the ratio is found to make boxes look like squares


    if 0.9<=ratio<=1.1: #if the ratio is close to 1,
        #there is no need to change the size of the total grid
        
        singleWidth = totalWidth//columns #gives the width of a single cell
        singleHeight = totalHeight//rows #gives the length of a single cell

    else: #if the sizes are greatly different
        totalWidth = totalWidth*ratio
        #the total width that will be used is made to match the ratio

        if totalWidth > 850: #however, if the new size is greater than the width of the screen
            totalWidth = 850 #it is set to the max width (950)

        singleWidth = totalWidth//columns #the width and lengths are assigned
        singleHeight = totalHeight//rows


    if singleWidth<30: #the width is increased if too small
        singleWidth = 30 #the user can now click the columns more easily


    for column in range(0,columns): # for every column
        board.append([])#add a new list to the board

        number1 = tkinter.Label(gridFrame,text = str(column+1),bg = 'gainsboro')
        number1.grid(row = 0,column = column)
        #number1 is the column number that will present at the top of the grid
        #above each column so the user can identify each column to place a counter
        
        for row in range(1,rows+1): #loop starts from 1 as the first row is the number
            #a blue cell is created with black edges and width and length as created above 
            cell = tkinter.Frame(gridFrame, bg='skyblue', highlightbackground="black",
                        highlightcolor="black", highlightthickness=1,
                        width=singleWidth, height=singleHeight,)
            cell.bind("<Button-1>", clickCounter)

            #the cell is placed within the gridframe with the corresponding row and column
            cell.grid(row=row, column=column)
            board[column].append(cell) #the cell is appended to the column

        number2 = tkinter.Label(gridFrame,text = str(column+1),bg = 'gainsboro')
        number2.grid(row = row+1,column = column)
        #number2 is the same as number1 but is added to the bottom of every column
        
    gridFrame.grid(row =1) #the grid is placed in the window (rather in secondFrame)


def startGame(): #function called when the startgame button is pressed 
    global gridFrame,currentPlayer,winCon,end #global board  #global variables used

    end = False
    currentPlayer = 0 #current player is set to 0, the first player
    displayPlayer() #the player is displayed in the main info label
    
    
    winCon = getWinCon()
    
    gridInfo = gridEntry.get() #the grid sizes entered by the user is received
    gridInfo = gridInfo.strip().split() #sanitised
    
    gridFrame.destroy() #the older grid is destroyed

    #if statement checks if the input entered is not valid
    if len(gridInfo)!=2 or not (gridInfo[0].isdigit() and gridInfo[1].isdigit()) or int(gridInfo[0])<1 or int(gridInfo[1])<1:
        #if not valid:
        gridEntry.delete(0,tkinter.END) #the entry is cleared
        gridEntry.config(fg='red') 
        gridEntry.insert(0,'Invalid grid: using 6 7') #the entry is replaced with text to show that 6 7 is being used
        createGrid(6,7,660,660) #the grid is created using original settings
        
    else: #if grid sizes entered is valid
        createGrid(int(gridInfo[0]),int(gridInfo[1]),660,660) #grid is created using user input
            
            
def clearGridEntry(event): #when the grid entry is pressed
    gridEntry.delete(0,tkinter.END) #the placeholder text in the entry is deleted
    gridEntry.config(fg='black') #the color is changed to black

def checkGrid(event): #when keyboard focus is taken away from the gridEntry
    
    info = gridEntry.get() #the info in the grid entry is taken
    info = info.strip().split() #sanitised
    mainInfoLabel.config(fg='red') #the info label color is changed to red
    
    if len(info)!=2 or not (info[0].isdigit() and info[1].isdigit()) or int(info[0])<1 or int(info[1])<1:
        #if invalid: appropiate text is shown
        mainInfoLabel['text'] = "Invalid Grid: Enter 2 positive integers."
    elif int(info[0])>25 or int(info[1])>25:
        #if the grid size is too big, the user is cautioned
        mainInfoLabel['text'] = "Caution, grid size may lead to bad experience."
    else:#valid grid size entered is shown
        mainInfoLabel['text'] = "Valid grid size entered."
        
def updateAnimations(): #function called whenever a radio button is clicked
    global animations #the global value is changed as tkinter is event driven
    
    if choice.get() == 1: #if first button is clicked
        animations = True
    else:
        animations = False
    
def performAnimation(column,index): #function used to show animations
    global drop #the global value is changed as tkinter is event driven

    #drop is used to see if the next player can drop a counter
    drop = False #next player cant drop a counter as this one is being dropped
    
    for i in range(0,index):#loops from the top of the grid to the index that will be filled
        
        board[column][i].configure(background=colors[currentPlayer])
        #color of cell is changed to counter color
        time.sleep(0.1) #wait 0.1 second 
        window.update()#update the GUI window
        
        board[column][i].configure(background='skyblue')#color is changed back

    drop = True #the next player can now drop a counter since the animation is over
        
def placeCounter(column): #function used to place counter given a column
    global currentPlayer, board, animations,end

    
    if not end:
        if board[column-1][0]['bg'] != 'skyblue':
            mainInfoLabel['text'] = "That column is full!"
            
        else:
            for i in range (len(board[0])-1,-1,-1):
            #loops through the bottom of the column to the top
                
                if board[column-1][i]['bg'] == 'skyblue':#if it is empty(blue)

                    if animations == True:
                        performAnimation(column-1,i)

                    board[column-1][i].configure(background=colors[currentPlayer])#color is changed
                    
                    largest = longestLine(column-1,i,[colors[currentPlayer]])
                    #print(largest)
                    
                    if largest>=winCon:
                        mainInfoLabel['text'] = 'Player '+str(currentPlayer+1)+' is the winner!'
                        end = True
                        
                    else:
                        currentPlayer = (currentPlayer+1)%players#next players turn
                        displayPlayer()#display info of new player
                    break
                

                
def displayPlayer(): #function used to display the current players turn
    mainInfoLabel.config(fg=colors[currentPlayer])#the color is changed to the current player
    mainInfoLabel['text'] = 'Player '+str(currentPlayer+1)+"'s turn. (Click any column or type on the right)"#the text is changed

def enterCounter(event):#function called when the user presses enter
    if not end:
        column = columnEntry.get().strip() #text from entry is taken
        columnEntry.delete(0,tkinter.END) #entry is cleared

        #accepts only non-negative integers
        if column.isdigit(): #checks if the string is an integer
            column = int(column) #cast to integer
            if 0<column<=len(board): #checks if it is a valid column
                placeCounter(column)

            else:
                mainInfoLabel['text'] = "Thats not a column!"
            
        else:
            mainInfoLabel['text'] = "Enter a positive integer."


def clickCounter(event): #when a cell is clicked, this function is called
    if drop:
        cell = event.widget #the cell that was clicked is received
        column = cellColumn(board,cell)+1 #the column its in is identified

        placeCounter(column) #counter is placed in that column
    
    
def cellColumn(board, cell): #function used to find the column index of a cell in a 2d list
    for i, x in enumerate(board): #loops through the 2d list
        if cell in x:#if the cell is in the column
            return i #column index is returned
    

def clearWinEntry(event): #clears the entry
    winEntry.delete(0,tkinter.END) #the placeholder text in the entry is deleted
    winEntry.config(fg='black') #the color is changed to black

def checkWinCon(event): #checks if entered data is valid
    info = winEntry.get() 
    info = info.strip() #sanitised

    if info.isdigit() and int(info)>0: #checks if integer: appropriate message shown
        mainInfoLabel['text'] = "Valid win condition entered."
    else:
        mainInfoLabel['text'] = "Invalid Win Condition: Enter an integer."


def getWinCon(): #function used to find the win conditon i.e. how many in a row
    info = winEntry.get()
    info = info.strip() #sanitised

    if info.isdigit() and int(info)>0:
        return int(info) #returns the input if vlaid
    else:
        winEntry.config(fg='red')
        winEntry.delete(0,tkinter.END) #the prewwritten text in the entry is deleted
        winEntry.insert(0,'Invalid win condition: using 4') #the entry is replaced with text to show that 4 is being used
        return 4 #if invalid uses 4


def longestLine(index1,index2,colors):  #function used to find the longest line of a color
    xlength,ylength,new1,new2 = 0,0,index1,index2

    #check total x direction:
    
    while new1<len(board)and board[new1][new2]['bg'] in colors:
    #with every iteration, moves towards the right of the counter
    #until a different color is found or the board limit is reached
        xlength += 1 #the horizontal length is increased
        new1 += 1 #the next index will be checked
        
    new1 = index1 -1   #the index is reset back

    #similarly, checks the left side of the counter
    while new1>=0 and board[new1][new2]['bg'] in colors:
        xlength += 1
        new1 -= 1
    new1 = index1

    #check total y direction:
    #checks above and below the counter to find the total vertical length
    while new2<len(board[0]) and board[new1][new2]['bg'] in colors:
        ylength += 1
        new2 += 1
    new2 = index2-1

    while new2>=0 and board[new1][new2]['bg'] in colors:
        ylength += 1
        new2 -= 1
    new2 = index2

    #checking diagonals:
    diag1,diag2 = 0,0

    #checks both diagonals going a square diagonally each time
    while new1<len(board)and new2<len(board[0]) and board[new1][new2]['bg'] in colors:
        diag1 += 1
        new1 += 1
        new2+= 1
    new1,new2 = index1-1,index2-1

    while new1>=0 and new2>=0 and board[new1][new2]['bg'] in colors:
        diag1 += 1
        new1 -= 1
        new2-= 1

    new1,new2 = index1,index2
    #print('diag1',diag1)

    while new1>=0 and new2<len(board[0]) and board[new1][new2]['bg'] in colors:
        diag2 += 1
        new1 -= 1
        new2+= 1

    new1,new2 = index1+1,index2-1
    
    while new1<len(board) and new2>=0 and board[new1][new2]['bg'] in colors:
        diag2 += 1
        new1 += 1
        new2-= 1
    new1,new2 = index1,index2
    #print('diag2',diag2,'\n')
        
    return max(xlength,ylength,diag1,diag2) #returns the longest line formed



window = tkinter.Tk() #window is created
window.title("Connectron") #the title is connectron
window.columnconfigure(0,minsize = 200)#this adds space between the left hand side and the right hand side of the GUI
window.configure(bg='lightyellow') #sets background color to the color gainsboro

#global variables used to control flow
drop = True
animations = True
end = False
winCon = 4


colors = ['red','yellow','dark green','deep pink','dark orange','purple','saddle brown','navy','light green','gray35']
#the colors of each user will be shown as above

#first frame is left side, second Frame is main grid and third frame is right side of the gui
firstFrame = tkinter.Frame(master=window,bg="gainsboro",pady=10,padx=20)
secondFrame = tkinter.Frame(master = window, bg ="gainsboro",pady=15,padx=15,width = 900, height = 800)
thirdFrame = tkinter.Frame(master=window,bg="gainsboro",pady=10,padx=20)

#this label is just above the grid, showing whose player it is and other information
mainInfoLabel = tkinter.Label(secondFrame,bg='gainsboro',text='Welcome to Connectron!',height=1,fg='red',font=("Calibri",26))
mainInfoLabel.grid(row=0) #the label is packed into the frame

#Game info

players = 2
currentPlayer = 0
createGrid(6,7,660,660) #the starting board is a 6 by 7 grid which is created
window.bind('<Return>',enterCounter)



##left hand side of the grid
#Grid info
gridInfoFrame = tkinter.Frame(master=firstFrame,bg="gainsboro",pady=10) #the frame that contains the grid stuff

gridLabel = tkinter.Label(master = gridInfoFrame, text = "Enter grid size (row,column):",bg="gainsboro")#grid label
gridEntry = tkinter.Entry(master = gridInfoFrame, width = 20,bg="light yellow") #grid entry
gridEntry.insert(0,'example: 6 7') #contains the placerholder to give an idea to user
gridEntry.config(fg='grey')

gridLabel.pack() #the widhgets are packed into the frame
gridEntry.pack()

gridInfoFrame.pack() #the frame is placed 

gridEntry.bind("<FocusIn> ", clearGridEntry) #when the user presses the entry, it is cleared
gridEntry.bind("<FocusOut> ",checkGrid) #when the user presses out of the entry, an appropiarte message is shown


#enter win conditon
winFrame = tkinter.Frame(master=firstFrame,bg="gainsboro",pady=10) #the frame that contains the grid stuff

winLabel = tkinter.Label(master = winFrame, text = "Enter length needed for win:",bg="gainsboro")#grid label
winEntry = tkinter.Entry(master = winFrame, width = 20,bg="light yellow") #grid entry
winEntry.insert(0,'example: 4') #contains the placerholder to give an idea to user
winEntry.config(fg='grey')

winLabel.pack() #the widhgets are packed into the frame
winEntry.pack()

winFrame.pack() #the frame is placed 

winEntry.bind("<FocusIn> ", clearWinEntry) #when the user presses the entry, it is cleared
winEntry.bind("<FocusOut> ",checkWinCon) #when the user presses out of the entry, an appropiarte message is shown



#animation radio buttons
choiceFrame = tkinter.Frame(master=firstFrame,bg="gainsboro",pady=20)

choice = tkinter.IntVar()
choice.set(1)

choiceLabel = tkinter.Label(master = choiceFrame, text = "Counter drop animations:",bg="gainsboro",pady=5)
yesChoice = tkinter.Radiobutton(master = choiceFrame,command = updateAnimations,bg='gainsboro',text = "Yes!",variable=choice,value=1,width = 20)
noChoice = tkinter.Radiobutton(master = choiceFrame,bg='gainsboro',command = updateAnimations, text = "No!",variable=choice,value=2,width = 20)

choiceLabel.pack()
yesChoice.pack()
noChoice.pack()

choiceFrame.pack()


#start game
startButton = tkinter.Button(master=firstFrame,padx=20,pady=10,highlightbackground='lightyellow',
                            text = "Start Game!", command = startGame, height = 2,width = 15)
startButton.pack()



##right hand side:
#entry that will be used to enter a counter - in development
columnFrame = tkinter.Frame(master=thirdFrame,bg="gainsboro") #frame that contains the column entry

columnLabel = tkinter.Label(master=columnFrame,bg="gainsboro",text="Type a column number and press enter:",font=('Calibri',15))
columnEntry = tkinter.Entry(master = columnFrame, width = 20,bg="light yellow")

#column label and entry are packed
columnLabel.pack(pady=5) #pad y so there is some space between them
columnEntry.pack()

columnFrame.grid(row=1,pady=(30,0))



#the main frames are packed
firstFrame.grid(row = 0, column = 0, sticky = "nsew")
secondFrame.grid(row=0, column = 1, sticky = "ns")
thirdFrame.grid(column=2,row=0,sticky = 'nsew')

window.mainloop()
