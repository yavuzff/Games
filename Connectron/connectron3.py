#copied and re ordered from connectron 2
#in make grid replaced,
#board[column].append([])
#board[column][row-1] = cell
#with:
#board[column].append(cell)


import tkinter #library to create GUI

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
    global board, gridFrame,currentPlayer #global variables used
    currentPlayer = 0 #current player is set to 0, the first player
    displayPlayer() #the player is displayed in the main info label

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


def placeCounter(column): #function used to place counter given a column
    global currentPlayer, board 

    if board[column-1][0]['bg'] != 'skyblue':
        mainInfoLabel['text'] = "That column is full!"
        
    else: 
        for i in range (len(board[0])-1,-1,-1):
        #loops through the bottom of the column to the top
            
            if board[column-1][i]['bg'] == 'skyblue':#if it is empty(blue) 
                board[column-1][i].configure(background=colors[currentPlayer])#color is changed
                currentPlayer = (currentPlayer+1)%players#next players turn
                displayPlayer()#display info of new player
                break
                

def displayPlayer(): #function used to display the current players turn
    mainInfoLabel.config(fg=colors[currentPlayer])#the color is changed to the current player
    mainInfoLabel['text'] = 'Player '+str(currentPlayer+1)+"'s turn. (Click any column or type on the right)"#the text is changed

    
def enterCounter(event):#function called when the user presses enter
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
    cell = event.widget #the cell that was clicked is received
    column = cellColumn(board,cell)+1 #the column its in is identified

    placeCounter(column) #counter is placed in that column

    
def cellColumn(board, cell): #function used to find the column index of a cell in a 2d list
    for i, x in enumerate(board): #loops through the 2d list
        if cell in x:#if the cell is in the column
            return i #column index is returned
    
    
        
window = tkinter.Tk() #window is created
window.title("Connectron") #the title is connectron
window.columnconfigure(0,minsize = 200)#this adds space between the left hand side and the right hand side of the GUI
window.configure(bg='lightyellow') #sets background color to the color gainsboro



colors = ['red','yellow','green','deep pink','dark orange','purple','saddle brown','navy','black','gray35']
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

gridInfoFrame.grid(row = 1,column = 0) #the frame is placed in the second row of the left hand side

gridEntry.bind("<FocusIn> ", clearGridEntry) #when the user presses the entry, it is cleared
gridEntry.bind("<FocusOut> ",checkGrid) #when the user presses out of the entry, an appropiarte message is shown


#start game
startButton = tkinter.Button(master=firstFrame,padx=20,pady=10,highlightbackground='lightyellow',
                            text = "Start Game!", command = startGame, height = 2,width = 15)
startButton.grid(row = 2,column=0)



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
