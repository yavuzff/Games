import random

class Animal(): #animal class for each contestant

    #contains name, speed values,endurance and wins
    def __init__(self,name,minSpeed,maxSpeed,endurance,wins):
        self.name = name
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
        self.endurance = endurance
        self.wins = wins
        self.currentEndurance = endurance
        self.distance = 0


    def turn(self):
        if  self.currentEndurance == 0: #checks if current endurance is 0
            roundDistance = 0 #will move 0 this round / have a rest
            self.currentEndurance = self.endurance #endurance will go back up to original endurance

            #print("I moved 0")#used for testing

        elif self.currentEndurance >= self.maxSpeed: #checks if animal's endurance is more than their max speed
            roundDistance = random.randint(self.minSpeed,self.maxSpeed) #distance will be a random number between the speeds
            #print("high endurance ")#used for testing

        elif self.currentEndurance <= self.minSpeed: #checks if current endurance is less than min speed
            roundDistance = self.currentEndurance # the current distance is endurance left
                
            #print ("very low endurance ")

        else: #endurance is between min speed and max speed
            roundDistance = random.randint(self.minSpeed,self.currentEndurance) #the maximum possible movement is amount of endurance

            #print("middle endurance")

        self.distance += roundDistance #this rounds distance is added to the total distance
        self.currentEndurance -= roundDistance #distance travelled this round is taken away
            
class Race():
    def __init__(self,length,contestants): #race has a length and contestants
        self.length = length
        self.contestants = contestants

    def start(self):
        #loops while no one has reached the race length
        while max(contestant.distance for contestant in self.contestants) < self.length:

            for contestant in self.contestants: #turn for each contestant
                contestant.turn()

        #everyones distances are stored
        finalScores = [contestant.distance for contestant in self.contestants]
        winningScore = max(finalScores)
        winningIndexes = [i for i, j in enumerate(finalScores) if j == winningScore]
        #winners are stored (there can be more than 1 winner)
        
        return winningIndexes

class FileHandling():
    def __init__(self,fileName):
        self.fileName = fileName
    

    def readFile(self):
        while True: #the function loops until contents are in a valid format, if valid it is returned within the infinite loop

            myfile = open(self.fileName,"r") #opens file
            
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


    def writeFile(self,data):
        contents = [[str(x) for i,x in enumerate(value)] for value in data] #converts all of the elements to strings
        contents = [' '.join(i) for i in contents] #all the sublists are joined to make a list of strings

        contents.insert(0,"Input data in this format: Name, minimum speed, maximum speed, endurance, no of wins")
        #the first line (which is the instructions) is inserted into the list of strings

        contents = "\n".join(contents) # the list of strings is joined together with a new line between every string

        myfile = open(self.fileName,"w") #file is opened

        myfile.write(contents) #the string is overwritten in the file
        
        myfile.close() #file is closed


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

def updateData(animals, index):
    for i in index: #loops through the winning indexes
        animals[i].wins +=1 #adds 1 to no of wins of that animal

    animals = [[animal.name,animal.minSpeed,animal.maxSpeed,animal.endurance,animal.wins] for animal in animals]

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

def main():   
    replay = True

    while replay:

        fileHandler = FileHandling("animals.txt")
        animalData = fileHandler.readFile()

        animals = []
        for animal in animalData:
            animals.append(Animal(animal[0],animal[1],animal[2],animal[3],animal[4]))


        raceLength = inputRaceLength()

        animalRace = Race(raceLength,animals)
        winningIndexes = animalRace.start()

        print ("The winner is ...")
        for i in winningIndexes:
            print (animals[i].name +"!")

        animalList = updateData(animals,winningIndexes)

        fileHandler.writeFile(animalList)


        print ("\nPress Enter if you want to replay")
        answer = input('>')

        if answer == '':
            replay = True

        else:
            replay = False

if __name__ == '__main__':
    main()



    
