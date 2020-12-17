import random #imports the random module
#hare and tortoise race simulation

#Next Steps:
#Input validation for very input
#Use the same code for hare and tortoise+tortoise always has a chance of 0


def setRaceLength(): #function that is used to input the race length
    
    length = False   #length variable is set as false for input validation
    while length == False: #loops until the input is valid
        
        try: #try is used as there will be an error if the input is a string
            length = int(input("Enter the length of the race: "))
        except:
            length = False #if there is an error, input is false
    return length

                     
def setValue(animalInfo): #function that lets the user to set the speeds of the animals
    minSpeed = int(input("Enter the minimum speed of "+str(animalInfo[0])+": "))
    maxSpeed = int(input("Enter the maximum speed of "+str(animalInfo[0])+": "))

    animalInfo[1] = minSpeed #animalnfo[1] coressponds to the minspeed
    animalInfo[2] = maxSpeed #and 2 corresponds to the max speed

    return animalInfo 

def runRace(length,animals): #function that performs the 'rounds' of the race
##    rounds = 0 #variable used for testing
    sleepPercentage = 25 # percentage of the hare sleeping

    while animals[0][3] < length and animals[1][3] < length: #loops until neither has finished the race
##        rounds += 1 #used for testing how many rounds

        #for hare:
        if random.randint(1,100) <= sleepPercentage: #random integer between 1 and 100 performs 25%
            animals[0][3] += 0 #hare sleeps, so 0 is added
            sleepPercentage = 25 #the chance is reset back to 25%

        else:
            animals[0][3] += random.randint(animals[0][1],animals[0][2])#random number between min speed and max speed is added
            sleepPercentage += 15 #as it hasnt sleeped, the percentage increases by 15

        
        #for tortoise:
        animals[1][3] += random.randint(animals[1][1], animals[1][2])#adds a random number between minspeed and maxspeed
        

##    print (animals)                           #used for testing
##    print (animals[0][3], animals[1][3])

    if animals[0][3] == animals[1][3]: #checks whether there is a tie
        return "tie"

    #if both have passed the length at the same round, the winner is the one that travels faster
    elif animals[0][3] > animals[1][3]: 
        return animals[0][0] #hare wins if hare's length is larger

    else:
        return animals[1][0]  #tortoise wins


def displayWinner(winner): #function that outputs winner
    if winner == "tie":
        print("There is a tie! Both hare and tortoise are the winners!")
    elif winner == "hare":
        print("The winner is hare!")
    else:
        print("The winner is tortoise!")
        
##    MAIN PROGRAM  ##
        
animals = [["hare",0,0,0],["tortoise",0,0,0]]
#2 dimensional list used to display animals
#every animal's list is in the format: [name,minspeed,maxspeed,distancetravelled]

raceLength = setRaceLength() #race length is set

animals[0] = setValue(animals[0]) #values for tortoise is set

animals[1] = setValue(animals[1]) #values for hare is set

result = runRace(raceLength, animals) #race is run

displayWinner(result) # winner is displayed




