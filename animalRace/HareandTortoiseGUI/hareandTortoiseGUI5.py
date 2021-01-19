import random
import tkinter
import time

window = tkinter.Tk()

window.title("Hare and Tortoise Race")
window.configure(bg='gainsboro')


def startGame():

    #variables
    length =int(lengthEntry.get().strip())
    hareMinSpeed = int(hareMinEntry.get().strip())
    hareMaxSpeed = int(hareMaxEntry.get().strip())
    tortoiseMinSpeed = int(tortoiseMinEntry.get().strip())
    tortoiseMaxSpeed = int(tortoiseMaxEntry.get().strip())

    
    sleepPercentage = 25 # percentage of the hare sleeping
    hareDistance = 0
    tortoiseDistance = 0
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
            hareCurrent = random.randint(hareMinSpeed,hareMaxSpeed)
            hareDistance += hareCurrent#random number between min speed and max speed is added
            sleepPercentage += 0 #as it hasnt sleeped, the percentage increases by 15
            
            
        #print(hareCurrent,'hare',hareDistance)
        
        #for tortoise:
        tortoiseCurrent = random.randint(tortoiseMinSpeed,tortoiseMaxSpeed)
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
    
    hareImage = canvas.create_image(57, 100, image=hareImg)
    tortoiseImage = canvas.create_image(50, 200, image=tortoiseImg)

def resetDetails():
    lengthEntry.delete(0, tkinter.END)
    hareMinEntry.delete(0, tkinter.END)
    hareMaxEntry.delete(0, tkinter.END)
    tortoiseMinEntry.delete(0, tkinter.END)
    tortoiseMaxEntry.delete(0, tkinter.END)
    


window.rowconfigure([0,1,2,3,4,5],minsize = 90)
window.columnconfigure(0,minsize = 250)
##    window.columnconfigure(1,minsize = 300)

#Frames that will be used:
firstFrame = tkinter.Frame(master=window,bg="gainsboro",pady=15)
secondFrame = tkinter.Frame(master = window, bg ="gainsboro",pady=15)


#Widgets that will be used:
testLabel = tkinter.Label(master = firstFrame, text = "Enter Details of the Race:",bg="gainsboro")

lengthLabel = tkinter.Label(master = firstFrame, text = "Race Length:",bg="gainsboro")
lengthEntry = tkinter.Entry(master = firstFrame, width = 20,bg="light yellow")



sleepLabel = tkinter.Label(master = firstFrame, text = "Chance of Hare Sleeping(%):",bg='gainsboro')
sleepEntry = tkinter.Entry(master = firstFrame, width = 20, bg="light yellow")


hareMinLabel = tkinter.Label(master = secondFrame, text = "Minimum Speed of Hare:",bg="gainsboro")
hareMinEntry = tkinter.Entry(master = secondFrame, width = 20,bg="light yellow")

hareMaxLabel = tkinter.Label(master = secondFrame, text = "Maximum Speed of Hare:",bg="gainsboro",pady=10)
hareMaxEntry = tkinter.Entry(master = secondFrame, width = 20,bg="light yellow")

tortoiseMinLabel = tkinter.Label(master = secondFrame, text = "Minimum Speed of Tortoise:",bg="gainsboro",pady=10)
tortoiseMinEntry = tkinter.Entry(master = secondFrame, width = 20,bg="light yellow")

tortoiseMaxLabel = tkinter.Label(master = secondFrame, text = "Maximum Speed of Tortoise:",bg="gainsboro",pady=10)
tortoiseMaxEntry = tkinter.Entry(master = secondFrame, width = 20,bg="light yellow")

#Placement of widgets within the frames

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

#Placement of frames within the window

firstFrame.grid(row=0,column=0)
secondFrame.grid(row=1,column=0)


canvas = tkinter.Canvas(window, width=1160, height=280)

canvas.grid(row=1,column=1) # this makes it visible

hareimgpath = 'hare.ppm'
hareImg = tkinter.PhotoImage(file=hareimgpath)
hareImg = hareImg.zoom(1) 
hareImg = hareImg.subsample(3) 
hareImage = canvas.create_image(57, 100, image=hareImg)

tortoiseimgpath = 'tortoise.ppm'
tortoiseImg = tkinter.PhotoImage(file=tortoiseimgpath)
tortoseImg = tortoiseImg.zoom(1) 
tortoiseImg = tortoiseImg.subsample(4) 
tortoiseImage = canvas.create_image(50, 200, image=tortoiseImg)

buttonFrame = tkinter.Frame(master=window,bg="gainsboro",pady=15)

startButton = tkinter.Button(master=buttonFrame,highlightbackground='lightyellow', text = "Start Race!", command = startGame, height = 2,width = 15)
startButton.grid(row = 0,column = 1)

restartButton = tkinter.Button(master=buttonFrame,highlightbackground='lightyellow', text = "Reset Characters", command = restartPositions, height = 2, width =15)
restartButton.grid(row = 0,column = 2)

resetButton = tkinter.Button(master=buttonFrame,highlightbackground='lightyellow', text = "Reset Details", command = resetDetails, height = 2, width =15)
resetButton.grid(row = 0,column = 3)
buttonFrame.grid(row=0,column=1)

window.mainloop()
