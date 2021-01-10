#Yavuz first GUI
import random, tkinter
from tkinter.ttk import *

window = tkinter.Tk()

window.title("Hare and Tortoise Race")
window.configure(bg='gainsboro')

def inputGUI():
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
    
hareFrame = tkinter.Frame(window)

imgpath = 'hare.ppm'
hareImg = tkinter.PhotoImage(file=imgpath)
hareImg = hareImg.zoom(1) #with 250, I ended up running out of memory
hareImg = hareImg.subsample(3) #mechanically, here it is adjusted to 32 instead of 320
panelHare = Label(window, image = hareImg)

panelHare.grid(row=3,column=2)

imgpath = 'tortoise.ppm'
img = tkinter.PhotoImage(file=imgpath)
img = img.zoom(1) #with 250, I ended up running out of memory
img = img.subsample(4) #mechanically, here it is adjusted to 32 instead of 320
panelTortoise = Label(window, image = img)

panelTortoise.grid(row=4,column=2)

inputGUI()

window.mainloop()
