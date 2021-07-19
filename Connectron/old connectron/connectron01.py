import tkinter 

def createGrid(rows,columns,totalHeight,totalWidth):
    global cells,gridFrame
    
    cells = []

    gridFrame = tkinter.Frame(master=secondFrame,bg="gainsboro",pady=10)
    
    #columns = 20
    #rows = 16
    #totalHeight = 700
    #totalWidth = 700

    ratio = columns/rows

    if 0.9<=ratio<=1.2:
        #print('square')
        singleWidth = 660//columns
        singleHeight = 660//rows

    else:
        totalWidth = 660*ratio
        if totalWidth > 950:
            totalWidth = 950

        singleWidth = totalWidth//columns
        singleHeight = 660//rows


    for column in range(0,columns):
        cells.append([])

        number1 = tkinter.Label(gridFrame,text = str(column+1),bg = 'gainsboro')
        number1.grid(row = 0,column = column)    
        
        for row in range(1,rows+1):
            cells[column].append([])
            cell = tkinter.Frame(gridFrame, bg='skyblue', highlightbackground="black",
                        highlightcolor="black", highlightthickness=1,
                         #width=singleWidth, height=singleHeight,  padx=3,  pady=3)
                        width=singleWidth, height=singleHeight)
            cell.grid(row=row, column=column)
            cells[column][row-1] = cell
        number = tkinter.Label(gridFrame,text = str(column+1),bg = 'gainsboro')
        number.grid(row = row+1,column = column)
        
    gridFrame.grid(row =1)
    return cells


def placeCounter(event):
    global currentPlayer, cells
    
    column = columnEntry.get().strip()
    columnEntry.delete(0,tkinter.END)
    

    if column.isdigit(): #accepts only non-negative integers
        column = int(column)
        if 0<column<=len(cells):
            for i in range (len(cells[0])-1,-1,-1):
                #print (cells[column-1][i]['bg'])
                if cells[column-1][i]['bg'] == 'skyblue':
                    cells[column-1][i].configure(background=colors[currentPlayer])
                    currentPlayer = (currentPlayer+1)%players
                    displayPlayer()
                    break

        else:
            print("Thats not a column!")
        
    elif column == '':
        print("Is empty.")
    else:
        print("Error, enter a number.")

def startGame():
    global cells, gridFrame, currentPlayer
    currentPlayer = 0
    displayPlayer()

    info = gridEntry.get()
    info = info.strip().split()
    gridFrame.destroy()

    if len(info)!=2 or not (info[0].isdigit() and info[1].isdigit()) or int(info[0])<1 or int(info[1])<1:
        gridEntry.delete(0,tkinter.END)
        gridEntry.config(fg='red')
        gridEntry.insert(0,'Invalid grid: using 6 7')
        cells = createGrid(6,7,660,660)
        
    else:
        cells = createGrid(int(info[0]),int(info[1]),660,660)
            
            
def displayPlayer():
    mainInfoLabel['text'] = 'Player '+str(currentPlayer+1)+"'s turn."
    mainInfoLabel.config(fg=colors[currentPlayer])
  
##def key(event):
##    print ("pressed", repr(event.char))
##
##def callback(event):
##    print ("clicked at", event.x, event.y)

def clear(event):
    gridEntry.delete(0,tkinter.END)
    gridEntry.config(fg='black')

def checkGrid(event):
    info = gridEntry.get()
    info = info.strip().split()
    mainInfoLabel.config(fg='red')
    
    if len(info)!=2 or not (info[0].isdigit() and info[1].isdigit()) or int(info[0])<1 or int(info[1])<1:
        mainInfoLabel['text'] = "Invalid Grid: Enter 2 positive integers."
    elif int(info[0])>25 or int(info[1])>25:
        mainInfoLabel['text'] = "Caution, grid size may lead to bad experience."
    else:
        mainInfoLabel['text'] = "Valid grid size entered."
            
        
window = tkinter.Tk()
window.title("Connectron")
window.columnconfigure(0,minsize = 200)#this adds space between the left hand side and the right hand side of the GUI
#window.columnconfigure(1,minsize = 100)

window.configure(bg='lightyellow') #sets background color to the color gainsboro
#first frame is left side second frame is right side of the gui
firstFrame = tkinter.Frame(master=window,bg="gainsboro",pady=10,padx=20)
secondFrame = tkinter.Frame(master = window, bg ="gainsboro",pady=15,padx=15,width = 1110, height = 800)
thirdFrame = tkinter.Frame(master=window,bg="gainsboro",pady=10,padx=20)

mainInfoLabel = tkinter.Label(secondFrame,bg='gainsboro',text='Welcome to Connectron!',height=1,fg='red',font=("Calibri",26))
mainInfoLabel.grid(row=0)

window.bind('<Return>',placeCounter)

cells = createGrid(6,7,660,660)

colors = ['red','yellow','green','deep pink','dark orange','purple','saddle brown','navy','black','gray35']
players = 10
currentPlayer = 0


#left hand side
gridInfoFrame = tkinter.Frame(master=firstFrame,bg="gainsboro",pady=10)

gridLabel = tkinter.Label(master = gridInfoFrame, text = "Enter grid size (row,column):",bg="gainsboro")
gridEntry = tkinter.Entry(master = gridInfoFrame, width = 20,bg="light yellow")
gridEntry.insert(0,'example: 6 7')
gridEntry.config(fg='grey')

gridLabel.pack()
gridEntry.pack()

gridInfoFrame.grid(row = 1,column = 0)

gridEntry.bind("<FocusIn> ", clear)
gridEntry.bind("<FocusOut> ",checkGrid)

#gridEntry.bind("<Button-1>", callback)


startButton = tkinter.Button(master=firstFrame,padx=20,pady=10,highlightbackground='lightyellow',
                             text = "Start Game!", command = startGame, height = 2,width = 15)
startButton.grid(row = 2,column=0)


##right hand side:
columnEntry = tkinter.Entry(master = thirdFrame, width = 20,bg="light yellow")
columnEntry.pack()

thirdFrame.grid(column=2,row=0,sticky = 'nsew')


#the two main frames are packed
firstFrame.grid(row = 0, column = 0, sticky = "nsew")
secondFrame.grid(row=0, column = 1, sticky = "ns")


window.mainloop()
