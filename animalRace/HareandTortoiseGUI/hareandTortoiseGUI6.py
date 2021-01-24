import random
import tkinter

 
def startGame(): 

    restartPositions() #at the start of a new game, the animals are moved back to their starting positions
    #variables
    length =int(lengthEntry.get().strip()) #the game length is what was input in the entry asking for it
    hareMinSpeed = int(hareMinEntry.get().strip()) #same for these other variables
    hareMaxSpeed = int(hareMaxEntry.get().strip()) #they are converted to integers for use in random.randint
    tortoiseMinSpeed = int(tortoiseMinEntry.get().strip())# strip() allows the input to have spaces
    tortoiseMaxSpeed = int(tortoiseMaxEntry.get().strip())
    sleepPercentage = int(sleepEntry.get().strip()) # percentage of the hare sleeping

    if length > 0  and hareMaxSpeed >= hareMinSpeed >= 0 and tortoiseMaxSpeed>=tortoiseMinSpeed>=0 and sleepPercentage >=0:
        #line above checks if the inputs are valid, e.g. race length must be bigger than 0
        #variables that will be used:
        hareDistance = 0
        tortoiseDistance = 0
        
        hareCurrent = 0 #current is the number that will be travelled this round
        tortoiseCurrent = 0
        
        while hareDistance < length and tortoiseDistance < length: #loops until neither has finished the race
    ##        rounds += 1 #used for testing how many rounds

            #for hare:
            if random.randint(1,100) <= sleepPercentage: #random integer between 1 and 100 performs 25%
                hareDistance += 0 #hare sleeps, so 0 is added
                hareCurrent = 0

            else:
                hareCurrent = random.randint(hareMinSpeed,hareMaxSpeed)
                hareDistance += hareCurrent #random number between min speed and max speed is added
                
                
            #print(hareCurrent,'hare',hareDistance)
            
            #for tortoise:
            tortoiseCurrent = random.randint(tortoiseMinSpeed,tortoiseMaxSpeed)
            tortoiseDistance += tortoiseCurrent #adds a random number between minspeed and maxspeed

            tortoiseMovement = 1000/length * tortoiseCurrent
            hareMovement = 1000/length * hareCurrent #the amount of 'pixels' between race line and animals is 1000
                                                    #in these lines, the distance that will be travelled is scaled to the length entered
                                                    #if length was 1000, current 5 would be 5 pixels
                                                    #if length is 500, current 5 would be 10 pixels (1000/500)*5
                                                    #so the race always reaches the finish line             
            
            #print(tortoiseCurrent,'tortoise',tortoiseDistance)
        
            #move figures(figure,x direction,y direction):
            canvas.move(hareImage,hareMovement,0) 
            canvas.move(tortoiseImage,tortoiseMovement,0)
            
         
##            time.sleep(0.2)
            window.update() # the window is updated so this single small move will be seen
                            #as there is a while loop, if this line wasnt here, the window would be updated at the end
                            #after the while loop finishes, when the code loops back to window.mainloop()
           
        print(hareDistance,"HareDistance") #used for testing, these are printed in the idle
        print(tortoiseDistance,"TortoiseDistance")

        #Displays the winner in the window, emptyLabel is the label on the top that shows the winner
        if hareDistance == tortoiseDistance:
            emptyLabel['text'] = "There is a tie!"
        elif hareDistance > tortoiseDistance:
            emptyLabel['text'] = "The Hare Wins!"
        else:
            emptyLabel['text'] = "The Tortoise Wins!"


def restartPositions(): #function that resets the positions of the animals
    global hareImage, tortoiseImage, emptyLabel
    
    #print("Deleting...")
    emptyLabel['text'] = '' #the label that shows the winner is set back to nothing
    canvas.delete(hareImage) #the animals are deleted
    canvas.delete(tortoiseImage)
    
    hareImage = canvas.create_image(55, 100, image=hareImg) #the animals are created again at their original positions
    tortoiseImage = canvas.create_image(50, 200, image=tortoiseImg)

def resetAll(): #resets everything - like the program was shut and restarted again

    restartPositions() #firstly all the positions are moved

    #then all the entries are cleared
    sleepEntry.delete(0,tkinter.END)
    lengthEntry.delete(0, tkinter.END)
    hareMinEntry.delete(0, tkinter.END)
    hareMaxEntry.delete(0, tkinter.END)
    tortoiseMinEntry.delete(0, tkinter.END)
    tortoiseMaxEntry.delete(0, tkinter.END)




window = tkinter.Tk() #creating a window

window.title("Hare and Tortoise Race")
window.configure(bg='gainsboro') #sets background color to the color gainsboro

#window.rowconfigure([0,1,2,3,4,5],minsize = 90) 
window.columnconfigure(0,minsize = 250)#this adds space between the left hand side and the right hand side of the GUI

#Frames that will be used on the first column:
    #The main two frames, first one will be in line with the buttons, the second one with the race track 
firstFrame = tkinter.Frame(master=window,bg="gainsboro",pady=15)
secondFrame = tkinter.Frame(master = window, bg ="gainsboro",pady=15)

    #frames that will be next to the buttons on the top, the last 2 contain a label and an entry


#WHAT TO IMPROVE
#resize everything in window when the screen is resized
#After pressing start multiple times then reset, stop the animals from moving

inputFrame = tkinter.Frame(master=firstFrame,bg="gainsboro",pady=15)
lengthFrame = tkinter.Frame(master = firstFrame,bg="gainsboro",pady=10)
sleepFrame = tkinter.Frame(master=firstFrame,bg="gainsboro",pady=10)

    #frames that consist of a label and entry, these will be next to the race track so are in second frame
    #pady is added to separate each frame from others so elements within the frames are closer to each other than other elements
hareMinFrame = tkinter.Frame(master=secondFrame,bg="gainsboro",pady=10)
hareMaxFrame = tkinter.Frame(master=secondFrame,bg="gainsboro",pady=10)
tortoiseMinFrame = tkinter.Frame(master=secondFrame,bg="gainsboro",pady=10)
tortoiseMaxFrame = tkinter.Frame(master=secondFrame,bg="gainsboro",pady=10)


#Widgets that will be used:
#test label just says enter details, doesnt need an entry so is alone in the frame (maybe a frame wasnt needed)
testLabel = tkinter.Label(master = inputFrame, text = "Enter Details of the Race:",bg="gainsboro")

#these two are about the length of the race, they should be closer to each other than other frames
lengthLabel = tkinter.Label(master = lengthFrame, text = "Race Length:",bg="gainsboro")
lengthEntry = tkinter.Entry(master = lengthFrame, width = 20,bg="light yellow")

#chance of the hare sleeping : 1 label to tell the user and 1 entry to recieve input
sleepLabel = tkinter.Label(master = sleepFrame, text = "Chance of Hare Sleeping(%):",bg='gainsboro')
sleepEntry = tkinter.Entry(master = sleepFrame, width = 20, bg="light yellow")

#minimum speed of the hare : same as above
hareMinLabel = tkinter.Label(master = hareMinFrame, text = "Minimum Speed of Hare:",bg="gainsboro")
hareMinEntry = tkinter.Entry(master = hareMinFrame, width = 20,bg="light yellow")

#maximum speed of the hare :
hareMaxLabel = tkinter.Label(master = hareMaxFrame, text = "Maximum Speed of Hare:",bg="gainsboro")
hareMaxEntry = tkinter.Entry(master = hareMaxFrame, width = 20,bg="light yellow")

#same for tortoise
tortoiseMinLabel = tkinter.Label(master = tortoiseMinFrame, text = "Minimum Speed of Tortoise:",bg="gainsboro")
tortoiseMinEntry = tkinter.Entry(master = tortoiseMinFrame, width = 20,bg="light yellow")

tortoiseMaxLabel = tkinter.Label(master = tortoiseMaxFrame, text = "Maximum Speed of Tortoise:",bg="gainsboro")
tortoiseMaxEntry = tkinter.Entry(master = tortoiseMaxFrame, width = 20,bg="light yellow")



#Placement of widgets within their frames

testLabel.pack()

lengthLabel.pack()
lengthEntry.pack()

sleepLabel.pack()
sleepEntry.pack()

hareMinLabel.pack()
hareMinEntry.pack()

hareMaxLabel.pack()
hareMaxEntry.pack()

tortoiseMinLabel.pack()
tortoiseMinEntry.pack()

tortoiseMaxLabel.pack()
tortoiseMaxEntry.pack()

#placement of frames within the main two frames, first three in 1, others in frame 2
inputFrame.pack()
lengthFrame.pack()
sleepFrame.pack()

hareMinFrame.pack()
hareMaxFrame.pack()
tortoiseMinFrame.pack()
tortoiseMaxFrame.pack()

#Placement of main frames within the window

firstFrame.grid(row=0,column=0) #this frame is on the top left, the other is bottom left
secondFrame.grid(row=1,column=0)



#Label and Buttons on the top (left)

topFrame = tkinter.Frame(window,bg='gainsboro',pady=15) #the widgets will be contained in this frame

emptyLabel = tkinter.Label(topFrame,bg='gainsboro',text='',height=2,fg='red',font=("Calibri",30))
#emptyLabel will show who is the winner, it will be empty at the start of the game


#button frame will contain the 3 buttons, pady is used to have space between the label and buttons
buttonFrame = tkinter.Frame(master=topFrame,bg="gainsboro",pady=15)

#first button:, first pad x is used to increase space within the button, the one on the second line to have space between the three buttons, this button calls the function startGame when pressed
startButton = tkinter.Button(master=buttonFrame,padx=20,pady=10,highlightbackground='lightyellow', text = "Start Race!", command = startGame, height = 2,width = 15)
startButton.grid(row = 0,column = 0,padx=40) #it is  placed on the leftmost part of the frame

#second button: same as above
restartButton = tkinter.Button(master=buttonFrame,padx=20,pady=10,highlightbackground='lightyellow', text = "Reset Characters", command = restartPositions, height = 2, width =15)
restartButton.grid(row = 0,column = 1,padx=40)

#third button: same as above
resetButton = tkinter.Button(master=buttonFrame,padx=20,pady=10, highlightbackground='lightyellow', text = "Reset All", command = resetAll, height = 2, width =15)
resetButton.grid(row = 0,column = 2,padx=40)

#both parts of the main topframe is packed on top of each other
emptyLabel.pack()
buttonFrame.pack()

#this frame is placed on the top right of the window
topFrame.grid(row=0,column=1)



#The race track on bottom (left)

canvas = tkinter.Canvas(window, width=1160, height=280,highlightbackground='red') #the canvas is the white race track, the width and height are specified

canvas.grid(row=1,column=1) # it is placed on the bottom right

#the finish line: -this is defined first so when the images overlap, the animals go on top of the finish line
finishlineimgpath = 'finishline.ppm' #needs to be in ppm format when using PhotoImage (I think)
finishlineImg = tkinter.PhotoImage(file=finishlineimgpath) #the image is saved into python by giving the director(just the name as they are in the same folder)
finishlineImg = finishlineImg.zoom(2) #the image is enlarged
finishlineImg = finishlineImg.subsample(4) #not sure what this does :D
finishlineImage = canvas.create_image(1114, 200, image=finishlineImg) #it is placed on the end 
finishlineImage2 = canvas.create_image(1114, 85, image=finishlineImg) #a second one is placed exactly below it to make it seem like a continous line, one single image is too short

#same for the hare image:
hareimgpath = 'hare.ppm'
hareImg = tkinter.PhotoImage(file=hareimgpath)
hareImg = hareImg.subsample(3) 
hareImage = canvas.create_image(55, 100, image=hareImg) 

#same for the tortoise image:
tortoiseimgpath = 'tortoise.ppm'
tortoiseImg = tkinter.PhotoImage(file=tortoiseimgpath)
#tortoiseImg = tortoiseImg.zoom(1) 
tortoiseImg = tortoiseImg.subsample(4) 
tortoiseImage = canvas.create_image(50, 200, image=tortoiseImg)

#the hare is placed 5 units in front of the tortoise as it is then it looks like they are inline


window.mainloop() #the window is infinetly looped to see if there are any events occuring e.g. pressing a button
