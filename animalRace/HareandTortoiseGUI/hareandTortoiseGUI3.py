import random, tkinter
from tkinter.ttk import *
import time

window = tkinter.Tk()

window.title("Hare and Tortoise Race")
window.configure(bg='gainsboro')

def inputGUI():
    window.rowconfigure([0,1,2,3,4,5],minsize = 90)
    window.columnconfigure(0,minsize = 250)
##    window.columnconfigure(1,minsize = 300)

    #Frames that will be used:
    inputFrame = tkinter.Frame(master=window,bg="gainsboro",pady=15)
    lengthFrame = tkinter.Frame(master = window,bg="gainsboro",pady=10)
    hareMinFrame = tkinter.Frame(master=window,bg="gainsboro",pady=10)
    hareMaxFrame = tkinter.Frame(master=window,bg="gainsboro",pady=10)
    tortoiseMinFrame = tkinter.Frame(master=window,bg="gainsboro",pady=10)
    tortoiseMaxFrame = tkinter.Frame(master=window,bg="gainsboro",pady=10)

    #Widgets that will be used:
    testLabel = tkinter.Label(master = inputFrame, text = "Enter Details of the Race:",bg="gainsboro")

    lengthLabel = tkinter.Label(master = lengthFrame, text = "Race Length:",bg="gainsboro")
    lengthEntry = tkinter.Entry(master = lengthFrame, width = 20,bg="light yellow")

    hareMinLabel = tkinter.Label(master = hareMinFrame, text = "Minimum Speed of Hare:",bg="gainsboro")
    hareMinEntry = tkinter.Entry(master = hareMinFrame, width = 20,bg="light yellow")

    hareMaxLabel = tkinter.Label(master = hareMaxFrame, text = "Maximum Speed of Hare:",bg="gainsboro")
    hareMaxEntry = tkinter.Entry(master = hareMaxFrame, width = 20,bg="light yellow")

    tortoiseMinLabel = tkinter.Label(master = tortoiseMinFrame, text = "Minimum Speed of Tortoise:",bg="gainsboro")
    tortoiseMinEntry = tkinter.Entry(master = tortoiseMinFrame, width = 20,bg="light yellow")

    tortoiseMaxLabel = tkinter.Label(master = tortoiseMaxFrame, text = "Maximum Speed of Tortoise:",bg="gainsboro")
    tortoiseMaxEntry = tkinter.Entry(master = tortoiseMaxFrame, width = 20,bg="light yellow")

    #Placement of widgets within the frames

    testLabel.pack()

    lengthLabel.pack()
    lengthEntry.pack()

    hareMinLabel.pack()
    hareMinEntry.pack()

    hareMaxLabel.pack()
    hareMaxEntry.pack()

    tortoiseMinLabel.pack()
    tortoiseMinEntry.pack()

    tortoiseMaxLabel.pack()
    tortoiseMaxEntry.pack()

    #Placement of frames within the window

    inputFrame.grid(row=0,column=0)
    lengthFrame.grid(row=1,column=0)
    hareMinFrame.grid(row=2,column=0)
    hareMaxFrame.grid(row=3,column=0)
    tortoiseMinFrame.grid(row=4,column=0)
    tortoiseMaxFrame.grid(row=5,column=0)
    
def startGame():

    #variables
    sleepPercentage = 25 # percentage of the hare sleeping
    hareDistance = 0
    tortoiseDistance = 0
    length = 1000
    hareCurrent = 0
    tortoiseCurrent = 0
    
    while hareDistance < length and tortoiseDistance < length: #loops until neither has finished the race
##        rounds += 1 #used for testing how many rounds

        #for hare:
        if random.randint(1,100) <= sleepPercentage: #random integer between 1 and 100 performs 25%
            hareDistance += 0 #hare sleeps, so 0 is added
            hareCurrent = 0
            sleepPercentage = 25 #the chance is reset back to 25%

        else:
            hareCurrent = random.randint(12,20)
            hareDistance += hareCurrent#random number between min speed and max speed is added
            sleepPercentage += 0 #as it hasnt sleeped, the percentage increases by 15
            
            
        #print(hareCurrent,'hare',hareDistance)
        
        #for tortoise:
        tortoiseCurrent = random.randint(8,16)
        tortoiseDistance += tortoiseCurrent #adds a random number between minspeed and maxspeed
    
        
        #print(tortoiseCurrent,'tortoise',tortoiseDistance)
        

        #move figures:
        canvas.move(hareImage,hareCurrent,0)
        canvas.move(tortoiseImage,tortoiseCurrent,0)
        
     
        time.sleep(0.05)
        window.update()

        
    print(hareDistance,"HareDistance")
    print(tortoiseDistance,"TortoiseDistance")

def restartPositions():
    global hareImage, tortoiseImage
    print("Deleting...")
    canvas.delete(hareImage)
    canvas.delete(tortoiseImage)
    
    hareImage = canvas.create_image(55, 50, image=hareImg)
    tortoiseImage = canvas.create_image(50, 150, image=tortoiseImg)


inputGUI()


hareFrame = tkinter.Frame(window)

canvas = tkinter.Canvas(window, width=1200, height=200)

canvas.grid(column=1) # this makes it visible

hareimgpath = 'hare.ppm'
hareImg = tkinter.PhotoImage(file=hareimgpath)
hareImg = hareImg.zoom(1) 
hareImg = hareImg.subsample(3) 
hareImage = canvas.create_image(55, 50, image=hareImg)

tortoiseimgpath = 'tortoise.ppm'
tortoiseImg = tkinter.PhotoImage(file=tortoiseimgpath)
tortoseImg = tortoiseImg.zoom(1) 
tortoiseImg = tortoiseImg.subsample(4) 
tortoiseImage = canvas.create_image(50, 150, image=tortoiseImg)

startButton = tkinter.Button(window,highlightbackground='lightyellow', text = "Start Race!", command = startGame, height = 4,width = 15)
startButton.grid(row = 2,column = 1)

restartButton = tkinter.Button(window,highlightbackground='lightyellow', text = "Reset Characters", command = restartPositions, height = 4, width =15)
restartButton.grid(row = 3,column = 1)



window.mainloop()
