import random #random module is imported as we will generate random numbers between max and min speed

def inputValues(fileName):  #function that returns the contents of a file
    
    while True: #the function loops until contents are in a valid format, if valid it is returned within the infinite loop

        myfile = open(fileName,"r") #opens file
        
        contents = [[value for value in line.split()] for line in myfile]   #reads each line of the file, converts each line string
                                                                            #to a list and adds it to a new list to create 2d list
        contents.pop(0) #the first line (instructions in the file) is removed
        #print (contents) #used for testing

        if all(len(animal) == 5 for animal in contents): #checks if each line contains 5 elements (name,minspeed,maxspeed,endurance,wins)
            try: #try is used to catch errors e.g. if a string was entered instead of an integer for the speed
                
                animals = [[(int(x) if i>0 else x) for i,x in enumerate(value)] for value in contents]
                #in the 2d list, all elements of all lists except the first index of each list (the name) is converted to an integer

                if all(0<=animal[1]<=animal[2]<=animal[3] and animal[4] >= 0 and 0 not in [animal[2],animal[3]] for animal in animals):
                #checks if min speed is >= 0 and minspeed <= maxspeed <= endurance, and if max speed and endurance are > 0 and
                # if amount of wins is > 0 for all the animals

                    myfile.close() # file is closed
                    print("File read successfully.")
                    return animals #the animals are returned to the main program
            
            except: #if there is an error the user will need to enter again
                pass

        print ("Please enter the data in the file in the correct format and press enter. ")    
        input(">") #the user is given the chance to change the file contents to match the 

        
def inputRaceLength() : #function used to input length of the race
    valid = False

    while not valid: #loops until answer is valid
        print ("Enter the length of the race: ")
        raceLength = input("> ")
        
        try: #try except used in case user enters non-integer
            
            if int(raceLength) > 0: # integer must be positive
                valid = True
            else:
                print ("Race length must be positive!")
                
        except:
            print ("Enter an integer.") #input must be integer
    
    return int(raceLength)



def animalTurn(minSpeed,maxSpeed,originalEndurance,animalData):
    #animalData is a list in format [distance travelled, current endurance]

    if animalData[1] == 0: #checks if current endurance is 0
        roundDistance= 0 #will move 0 this round / have a rest
        animalData[1] = originalEndurance #endurance will go back up to original endurance

        #print("I moved 0")#used for testing

    elif animalData[1] >= maxSpeed: #checks if animal's endurance is more than their max speed
        roundDistance = random.randint(minSpeed,maxSpeed) #distance will be a random number between the speeds
        #print("high endurance ")#used for testing

    elif animalData[1] <= minSpeed: #checks if current endurance is less than min speed
        roundDistance = animalData[1] # the current distance is endurance left
            
        #print ("very low endurance ")

    else: #endurance is between min speed and max speed
        roundDistance = random.randint(minSpeed,animalData[1]) #the maximum possible movement is amount of endurance

        #print("middle endurance")

    animalData[0] += roundDistance #this rounds distance is added to the total distance
    animalData[1] -= roundDistance #distance travelled this round is taken away from current endurance


    #print(roundDistance,"roundDistance")#used for testing
    #print(animalData,"animal data of animal below")#used for testing
   
    return animalData
            
def runRace(animals, raceLength): 
    currentAnimalData = [[0,animal[3]] for animal in animals] #this list of lists contains each animals current distance and current endurance
    
    #print(animals,"animals")#used for testing
    #print(currentAnimalData) #used for testing

    #loops until any of the animals' distance is greater than the racelength (max finds the maximum distance within the list)
    while max(animal[0] for animal in currentAnimalData) < raceLength:

        
        for i in range (0, len(animals)):#loops for every animal
            currentAnimalData[i] = animalTurn(animals[i][1],animals[i][2],animals[i][3],currentAnimalData[i])
            #the animals data is updated by the animalTurn() function after a round has finished

            
            #print (animals[i][0],'\n') #used for testing

    #print("End")#used for testing
    #print(currentAnimalData)#used for testing

    finalScores = [data[0] for data in currentAnimalData] #the distance of every animal at the end of the race
    #print(finalScores) #used for testing
    
    winningScore = max(finalScores) #the winning score is stored (in case of ties)
    winningIndexes = [i for i, j in enumerate(finalScores) if j == winningScore]
    #line above gives the index of all the characters that got the highest score(if there is a tie) 

    return winningIndexes

def updateData(animals, index):
    for i in index: #loops through the winning indexes
        animals[i][4]+=1 #adds 1 to no of wins of that animal
        
    choice = "" #choice decides if the list is sorted alphabetically or by no of wins
    
    while choice != 'a' and choice != 'w': #loops until choice starts with a or w (alphabetically or wins)
        print ("Do you want to sort the list alphabetically (a) or by number of wins (w): ")
        choice = input('>')
        try:
            choice = choice.strip().lower()[0] #finds the first letter ignoring spaces or capitalisations
        except:
            choice = ''

    if choice == 'a': #if alphabetical
        animals.sort() #2d list is sorted by the first element of every sub list (the name)

    else:
        animals.sort(key=lambda x : x[4] , reverse = True) #2d list is sorted by the 5th element of every sub list,
        #it is in reverse order as we want to see the best at top

    
    return animals


def writeFile(contents,fileName): #function to write the new results into a file
    contents = [[str(x) for i,x in enumerate(value)] for value in contents] #converts all of the elements to strings
    contents = [' '.join(i) for i in contents] #all the sublists are joined to make a list of strings

    contents.insert(0,"Input data in this format: Name, minimum speed, maximum speed, endurance, no of wins")
    #the first line (which is the instructions) is inserted into the list of strings

    contents = "\n".join(contents) # the list of strings is joined together with a new line between every string

    myfile = open(fileName,"w") #file is opened

    myfile.write(contents) #the string is overwritten in the file
    
    myfile.close() #file is closed


replay = True

while replay:
    animals = inputValues("animals.txt")
    raceLength = inputRaceLength()

    winningIndexes = runRace(animals, raceLength)
    print ("The winner is ...")
    for i in winningIndexes:
        print (animals[i][0]+"!")

    animals = updateData(animals, winningIndexes)

    writeFile(animals, "animals.txt")

    print ("\nPress Enter if you want to replay")
    answer = input('>')

    if answer == '':
        replay = True

    else:
        replay = False
