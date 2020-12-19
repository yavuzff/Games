import random #random library imported to generate random numbers for the dice roll
import time #time library imported to create more tension and be more user friendly at certain times

#the constants
CHARACTER_FORMAT =['','Strength: ','Agility: ','Magic: ','Luck: ','Hitpoints: ']#the constant for the format the data for each character will be stored as
STORY_CHALLENGES=['The party stands before a cavern in the heights of the Mountains of Mourn; the rumoured lair of the Dragon King.\nA foul stench issues from the opening. A sudden rumble from above warns the party of a rock fall. Quickly the party dash forward into the opening.\nThree of the party get in, however, the last one to dash in risks being hit by falling rocks (Agility Challenge rating 10).', 'The cavern slopes down steeply. From above water drips constantly. The way is treacherous.\nOne by one the characters make their way cautiously down the slope; each one wary that the slightest misstep could cause a dangerous fall.\nSuddenly one of the party loses their balance (Agility Challenge rating 12).', 'The slope eventually levels out into a wide cave, its ceiling lost in darkness.\nThe air is foetid and foul. Gnawed upon bones completely cover the floor.\nThe party pick their way carefully across the bone-pile hoping that they don’t step onto anything dangerous (Luck Challenge rating 12).', 'Suddenly there is a terrifying roar.\nA blood-maddened Mountain Troll charges out of a side passage and attacks (Strength Challenge rating 14).', 'As the party continues to walk through the caverns, a hissing sound is heard. It is a snake and it has bitten one of the party members! The bite may be poisonous. (Luck rating ???)', 'A horde of bats start dashing towards you. You have to act fast and destroy them before they reach you. (Magic Rating 14)', "The party make their way through a tunnel into a room. However, they don't realise the flying arrow coming at them from the other side of the door.(Agility rating 18)", 'The room is full of skulls and bones of those who failed to kill or even find the Dragon King. There seems no hope as you approach a stone door that is locked. (Strength rating 16)', "The smell throughout the caverns get even more nasty. Your party can feel that they are close to the Dragon King.\nA tauren, who is too strong to fight with a sword, jumps above you and shouts 'You are just more meat for the king!' (Magic rating 17) ", 'This is it. It is the last dungeon before the Dragon King. A series of boulders start to fall from the ceiling onto the party. (Agility rating 16) ']
STORY_SUCCESS=['At the last second X avoids the falling rocks and enters the cavern.', 'X manages to stay still and continues to follow the party.', 'X steps on a piece of skull, but keeps on going without facing any danger.', 'X destroys the troll by finishing it off by slicing its head.', "The bite wasn't posionous! You continue to walk through the caverns.", 'X uses their wand in the nick of time and all of the bats disappear.', 'X jumps to the side as the arrow goes between their legs, into the door.', 'X lifts the stone up and manages to put a boulder under the opening. The party crawls along the foul ground.', "The tauren attempts to dash towards X, but X's magical powers cause it to dash towards the wall at full speed.", "Amazingly, X bounces from side to side to avoid the pieces of rocks falling down on the party. An opening can be seen which will lead the party to the Dragon King's treasure."]
STORY_DEFEAT=['One of the rocks fall on the leg of X.', 'X slips, leg going out from under and slides down into the darkness bouncing off protruding, jagged rocks.', 'The floor gives way beneath X revealing a spiked pit. X falls in.', 'The troll defeats X in the fight, but then accidentally falls into a spiked trap.', 'X starts seeing hallucinations and loses their balance. The bite was indeed poisonous...', "X was to late to act on their wand and as a result is attacked by the bats. There is now blood on X's face.", 'X jumps to the side, but is too late and the arrow pierces through their right foot. Fortunately, your party manages to get rid of the arrow and prevent blood loss.', 'X bashes their shoulder into the door, which ends up poorly with a half-broken arm. X realizes that there was a lever to the side of the door...', "The tauren dashes into X with its dagger in its hand and manages to stab X's arm right before the spell is said. The tauren still dies due to an unknown power.", "X acts too slowly as a giant boulder drops down from the ceiling. It misses X but a smaller piece smashes into X's stomach. An opening to the Dragon King's layer can be seen..."]
STORY_DIFFICULTY = [[2,10],[2,12],[4,12],[1,14],[4,15],[3,14],[2,18],[1,16],[4,17],[2,16]]
DELAY = 0.005 #the time it takes to output each letter so it looks like typing
#2,10 2,12 4,12 1,14 3,30

def coolOutput(text): #outputs text in a typing-like fashion
    for i in text:
        print(i, end='') #each character is output next to each other (not on a new line)
        time.sleep(DELAY) #program stops for 0.01 seconds between each character
    print()

def diceRoll(sides): #sides of the dice
    return random.randint(1,sides)

def generateAttribute():
    rolls = []              #list used to store the 4 rolls in
    for i in range (1,5):
        rolls.append(diceRoll(6))
        
    #print (rolls) #for testing
    rolls.remove(min(rolls)) #removes the lowest roll

    attribute = rolls[0] + rolls[1] + rolls[2] #adds up the rolls
    return attribute

def sortList(List): #bubble sort algorithm used to sort a list
    changes = True #variable used to make sure loop stops when there are no more changes made in the last pass
    while changes == True:
        changes = False
        for i in range (0,len(List)-1):
            if List[i]<List[i+1]: #checks whether the left number of pair is smaller - then it is swapped as we want a descending order
                temp = List[i] 
                List[i] = List[i+1]
                List[i+1] = temp #temporary variable used to not lose any data
                changes = True
    return List

def assignAttributes(rollData):
    abilities= ['\nStrength (s)','\nAgility (a)','\nMagic (m)','\nLuck (l)']#the abilities' output order
    playerAbilities = ['0']*4 #the player's abilities - starts as 0 each
    allChosen = False #variable to control the while loop 
    attributeNo = 0 #this is increased everytime an attribute is assigned
    
    while allChosen == False:
    
        if attributeNo == 3: #checks if only the last attribute needs assigning
            end = False
            count = 0 #count goes through each assigned attribute to find the last ability
            #print (playerAbilities) #used for testing
            while end == False:
                if abilities[count] != ' ': #the unassigned ability is found by this if statement
                    lastIndex = count #the index of the unassigned ability
                    end = True
                else:
                    count += 1 #goes on to check the next ability
                    
            coolOutput('\nAnd finally, '+str(rollData[3])+' is assigned to '+ abilities[lastIndex].split()[0]+'.\n') 
            playerAbilities[lastIndex] = rollData[attributeNo] #the last attribute is asigned automatically
            abilities[abilityIndex] = ' '
            allChosen = True

        else:
            coolOutput ('\nWhat would you like to assign '+str(rollData[attributeNo] +' to:'+''.join(abilities))) #asks the user
            ability = input('> ')
            try:sanitisedAbility = ability.strip().lower()[0] #the sanitised data is the first letter of the answer so all of Strength strength s S is accepted
            except: sanitisedAbility = 'None' #if the user enters erroneous data, it will be treated as invalid
            
            if sanitisedAbility in (i.lower().replace('\n','')[0] for i in abilities): #checks if a valid attribute is assigned

                abilityIndex = [i.lower().replace('\n','')[0] for i in abilities].index(sanitisedAbility) #the index of this ability is found
                #print(abilities[abilityIndex].split()[0]) #used for testing#

                coolOutput(rollData[attributeNo] +' is assigned to ' + abilities[abilityIndex].split()[0]+'.')
                playerAbilities[abilityIndex] = rollData[attributeNo] #it is assigned to the player's abilities
                abilities[abilityIndex] = ' ' #this ability is replaced with a placeholder so it cant be chosen again
                attributeNo += 1


            else:
                coolOutput('This ability is not availabile.\n')

    return playerAbilities
                                             
def generateCharacter():
    characterData = [''] #the details for the character is stored in a certain format to be extracted afterwards
    
    coolOutput("Enter the name of your character:")
    characterData[0] = input('> ').replace(' ','_')#space is replaced

    while characterData[0].replace(' ','').replace('\t','') == '' or len(characterData[0]) >20 or len(characterData[0])<2:
        coolOutput ('A valid name must be between 2 and 20 characters and must contain letters, numbers or symbols.\nEnter a valid name for your character:')
        characterData[0] = input('> ')
        
    attributes = []                     
    for i in range (1,5): #loops 4 times, one for each attribute
        attributes.append(generateAttribute())
    
    attributes = sortList(attributes) #the attributes are sorted
  
    for i in range (0,len(attributes)): #each value is converted to a string as they will be output further on in the program
        attributes[i] = str(attributes[i])
    
    coolOutput ('Following attributes have been generated: '+str(attributes[0])+' '+str(attributes[1])+' '+str(attributes[2])+' '+str(attributes[3]))
    coolOutput ('\nWould you like to reroll the lowest attribute (y/n)?')
    choice = input('> ')

    if choice.strip().lower().startswith('y'): #the input is sanitised before being checked
        attributes.remove(attributes[3]) #the smallest value is removed (as the list is sorted)
        newAttribute = generateAttribute()
        coolOutput ("The new attribute is "+str(newAttribute))

        attributes.append(newAttribute) #new value is added to list
        for i in range (0,len(attributes)): #each value is converted to a integer as they will be sorted
            attributes[i] = int(attributes[i])
        attributes = sortList(attributes) #the new listof attributes is now sorted

        for i in range (0,len(attributes)): #each value is converted to a string as they will be output further on in the program
            attributes[i] = str(attributes[i])

        coolOutput ('The new set of attributes: '+str(attributes[0])+' '+str(attributes[1])+' '+str(attributes[2])+' '+str(attributes[3]))

    characterData += assignAttributes(attributes) + ['2'] #the attributes for the character is assigned to their data and the 2 is the hitpoints
    #print (attributes) #for testing

    coolOutput('The new character looks like this:')
    for i in range (0,len(characterData)):
        print(CHARACTER_FORMAT[i]+characterData[i])

    return characterData

def displayCharacters(data):
    for i in range (0,len(data)):
        for j in range(0,6):
            print(str(CHARACTER_FORMAT[j]) + str(data[i][j]))
        print('')

def runChallenge(aiRating,playerName,playerRating): #function to perform a single challenge
    aiRoll = diceRoll(20)   #computers roll is generated
    playerRoll = diceRoll(20)   #player's roll is generated
    aiTotal = aiRoll + aiRating
    playerTotal = playerRoll + playerRating #the total for each player is found
    
    coolOutput ('Computer rolls ' + str(aiRoll) + ', which is added to the the challenge rating.\nComputer total is '+str(aiTotal)+'.')
    coolOutput ('\n'+playerName+' rolls ' + str(playerRoll) + ", which is added to "+playerName+"'s ability.\n"+playerName+"'s total is "+str(playerTotal)+'.')

    if aiTotal > playerTotal:   #decides who wins - player wins if they draw
        return 'loss' #the result is returned back to the main program
    else:
        return 'win'

def reduceHealth(playerHealth,name): # function that reduces the health of a player 
    playerHealth = str(int(playerHealth)-1)#it is reduced by 1 first of all
    if int(playerHealth) == 0: #checks if the player is dead
        coolOutput (str(name)+' has died, horribly. You cannot use this character anymore.\n')

        deathList = open('deathList.txt','a') #player is added to the death list
        deathList.write(name+'\n')
        deathList.close()
        return [True,0] #true is returned to have death = true 
    else:
        coolOutput(str(name)+' loses a Hit Point and is fatigued.\n')
        return [False,playerHealth]

def chooseOption(characterData): #function that allows the player to choose which character they will use
    coolOutput ('Who should take on this challenge? Press:')
    for j in range (0,len(characterData)):
        coolOutput (str(j+1)+ ' for '+str(characterData[j][0]))  #this outputs each character and its assigned number for input
    try :character = int(input('> ').strip())-1 #if the input is not an integer, it will give an error --> try is used to stop this
    except:character = None
    acceptedInputs = []
    for i in range (0,len(characterData)): #only  the range of numbers will be accepted
        acceptedInputs.append(i)
    
    while character not in acceptedInputs: #user is asked to enter again until a valid input is entered
        coolOutput ('\nYour input must be one of the following numbers:')
        for k in range (0,len(characterData)):
            coolOutput (str(k+1)+ ' for '+str(characterData[k][0]))
        try: character = int(input('> ').strip()) -1 
        except: None

    return character

def createParty():#function used to create a new party
    partyData = [[],[],[],[]]
    coolOutput('Creating new party...')
    for i in range (0,4):#loops for each character
        partyData[i] = generateCharacter()#character is created for each character
        if i == 0:
            coolOutput ('\nOne character created. 3 more to go.')
        elif i == 1:
            coolOutput ('\n2 characters created. 2 more to go.')
        elif i == 2:
            coolOutput ('\n3 characters created. 1 more to go.')
    return partyData


def writeFile(characters,teamName): #procedure that writes the team into the file
    file = open('teamlist.txt','r')#file is opened
    contents = file.readlines()
    file.close()#the readable file is closed

    if teamName+'\n' not in contents:   #checks if the party is already saved
        if len(characters) != 0:
            file = open('teamlist.txt','a')#appendable file opened
            file.write(teamName+'\n')#the team name is written
            for i in characters:#loops for every character
                file.write(i[0]+' '+i[1]+' '+i[2]+' '+i[3]+' '+ i[4]+' '+i[5]+'\n')#all individual characteristics are written
            file.write('\n')#a new line for the next team is added
            file.close()
        
    else:#the party will be updated
        file = open('teamlist.txt','w') #file opened to overwrite everything
        for i in range (0, len(characters)): #loops through all characters
            #print (characters,characters[i])
            characters[i] = ' '.join(characters[i]) +'\n'#adds a new line in order to write in file
        nameIndex = contents.index(teamName+'\n')#index of the party name
        index = nameIndex
        while contents[index] != '\n':#loops until the end of the party is found
            index += 1 #index represents the end of the party

        #print (contents)
        #print(index)
        if len(characters) != 0:
            contents = contents[:nameIndex+1] + characters + contents[index:]#the party is changed while keeping every other party the same
        else:
            contents = contents[:nameIndex-1] + contents[index:]
        #print(contents)
        for i in contents:#the new contents are written in the file
            file.write(i)
        file.close()
            
    
def readFile(name):
    file = open('teamlist.txt','r') #file is opened
    partyData = [[],[],[],[]]
    contents = file.readlines() #all of the file is read

    #print(contents)#used for testing
    if name+'\n' in contents:#checks if the name is in the file
        nameIndex = contents.index(name+'\n')#the index of the party name is saved
        currentIndex = nameIndex 

        while contents[currentIndex+1] != '\n':#continues until a new party is reached
            currentIndex += 1
            partyData[currentIndex-1-nameIndex]= contents[currentIndex].replace('\n','').split() #the next character is added to the data

        while [] in partyData:
                partyData.remove([]) #removes characters that are empty
                
        return partyData
    else:
        coolOutput('Party not found.')
        return None #returns nothing if the party name is not in file

def checkData(data):
    #print(data,'DATA')
    if len(data) == 4: #no change needed if there are 4 characters
        return data
    else:
        coolOutput('Your party consists of '+str(len(data))+' characters. You need to create '+str(4-len(data))+' more character.\n')
        for i in range (0,(4-len(data))):
            newCharacter = generateCharacter()
            data.append(newCharacter)
    return data

def runStory(characterData): #this function performs the story mode of the game, the whole party data is needed as a parameter
    fatigued = None #these variables are used when a player is fatigued (after first challenge)
    death = False #used to see if there was a death in a round
    end = False #used to stop the for loop after everyone is dead
    win = False #used to show if the player won the final fight
    
    for i in range (0,11): #loops 11 times once for each challenge            
        if len(characterData) == 0 and fatigued == None: # if there is no one alive, the game ends
            end = True
            
        else:

            if len(characterData) == 0 and fatigued != None: #if everyone is dead except a fatigued player:
                coolOutput('Only '+fatigued[0]+' is alive. They will now lose 1 health point at the start of each challenge.\n')
                characterData.append(fatigued) #the fatigued player is made availabile but takes 1 damage every turn
                fatigued = None
                characterData[0][5] = reduceHealth(characterData[0][5],characterData[0][0])[1]
                if characterData[0][5] == 0: #checks if player is dead
                    end = True

            if end != True: #if everyones not dead:
                if i != 10: #the first 10 challenges are run this way as the last challenge combines everyone left
                #if False: #for testing
                    coolOutput (str(STORY_CHALLENGES[i])+'\n')    #outputs the current challenge
                    displayCharacters(characterData)
                    character = chooseOption(characterData)
                    name = characterData[character][0]
                    characterHealth = characterData[character][5]


                    if runChallenge(STORY_DIFFICULTY[i][1],name,int(characterData[character][STORY_DIFFICULTY[i][0]])) == 'win': #if the challenge is won
                        death = False #there will be no deaths this round
                        coolOutput ('\n'+STORY_SUCCESS[i].replace('X',name))#success line is printed
                        if int(characterHealth) > 3: #checks if 4 health (max is 4 )
                            coolOutput (name+' has max(4) health availabile. '+name+' is fatigued.\n')
                        else:
                            coolOutput (name+' gains a Hit Point and is fatigued.\n')
                            characterData[character][5] = str(int(characterHealth)+1)             
                        
                    else:
                        coolOutput (STORY_DEFEAT[i].replace('X',name)+'\n') #if its a loss the loss line is printed
                        result = reduceHealth(characterData[character][5],characterData[character][0]) #health is refuced
                        if result[0] == True:
                            #print(characterData) #used for testing
                            characterData.pop(character) #if there is a death player is removed
                            #print (characterData) #used for testing
                            death = True
                        else:
                            death = False
                            characterData[character][5] = result[1] #if there isnt a death, then the new health is returned

                    if death == False:#if there were no deaths this round ( so someone will be fatigued)
                        if fatigued != None:#if someone was fatigued from last round
                            characterData.append(fatigued) #they are added back to the game
                            fatigued = characterData[character] #and the new character is now fatigued
                            characterData.pop(character)
                        else:   #if no one was fatigued
                            fatigued = characterData[character]  #then this rounds player is fatigued
                            characterData.pop(character)
                            
                    else: #if there was a death this rounf
                        if fatigued != None:
                            characterData.append(fatigued) #the old fatigued is added back
                        fatigued = None #there will be no one fatigued as the player this round died

                else:
                    time.sleep(2)#to create tenstion and let the player read
                    coolOutput('You make it to the final dungeon where the Dragon King is.\nThe only way to finish him is to combine all of your Magic and Luck powers.\n')
                    time.sleep(2)
                    coolOutput('The Dragon King sees you... (Dragon rating 60)\n')
                    

                    if len(characterData)>1:#checks if there is one player left - changes dialogue
                        coolOutput("The Dragon King: You think you mortals can take me on?\n*You look at each other, worriedly*\n")
                    else:
                        coolOutput("The Dragon King: You think you mortal can take me on?\n*You close your eyes and hope for the best.*\n")
                    time.sleep(1)    
                    displayCharacters(characterData)
                    time.sleep(2)
                    coolOutput("For the last time, choose which mortal should take on this challenge:\n1-Mortal!?!?!\n2-Everyone\n3-Can we not fight please?\nAnything else - Let's fight already! ")
                    input('> ')
                    if fatigued != None: #the fatigued player is killed off this round
                        coolOutput(str(fatigued[0])+' looks at the Dragon King, looks at the party, and dies in disbelief.\n')
                        coolOutput(str(fatigued[0]) + ' will not be playable again.')
                        time.sleep(2)
                        #print(characterData)#for testing
                    coolOutput('The Dragon King: MUHAHAHAHAHAHAHA. THIS WILL BE EASY!\nThe Dragon King gets ready for the fight as you plan your feeble tactics.\n')
                    totalMagic = 0
                    totalLuck = 0
                    for i in range (0,len(characterData)):#the values are added together using a for loop to iterate through the whole party
                        totalMagic += int(characterData[i][3])
                        totalLuck += int(characterData[i][4])
                    totalPower = totalMagic +totalLuck #the total power of the player is decided
                    playerRoll = diceRoll(60)
                    aiRoll = diceRoll(60) #the rolls for each is decided
                    
                    coolOutput('Your Magic Power: '+str(totalMagic)+'\nYour Luck Power: '+str(totalLuck)+'\nYour Total Power: '+str(totalPower))
                    time.sleep(0.5)
                    coolOutput('\nThe Final Showdown:\nThe Dragon King(60) v '+partyName+'('+str(totalPower)+')')
                    time.sleep(2)
                    coolOutput('Both sides get their 60 sided-dice out...\nThe Dragon King rolls:')
                    time.sleep(2)
                    coolOutput(str(aiRoll)+' and now has a Power of '+str(aiRoll+60)+'.\n\nThe Dragon King: You fool! I will destroy every single piece of you with this score!\nThere is so little hope left for you as you pick up your dice...')
                    coolOutput('\nPress enter when you are ready to roll your dice:')
                    input('> ')
                    time.sleep(1)
                    coolOutput('You roll:')
                    time.sleep(2)
                    if (aiRoll + 60) <= (totalPower + playerRoll):#checks who won
                        coolOutput(str(playerRoll)+'!\nThe Dragon King:Noooooooooo-\nThe Dragon King perishes before he can roll his dice again.')
                        time.sleep(1)
                        coolOutput('You live happily ever after with all the loot.\n(And best of all, all of your party gains 1 more health)\n')
                        for i in range (0,len(characterData)): #the health of each character is increased by one
                            if characterData[i][5] != '4':
                                characterData[i][5] = str(int(characterData[i][5])+1)
                        win = True#variable to decide if the player won
                    else:
                        error = False
                        coolOutput(str(playerRoll)+'...\nThe Dragon King: I AM THE STRONGEST!\nThe Dragon King throws rocks at you as you crawl away from the cavern.\n(And worst of all, you all lose 1 health)\n')
                        for i in range (0,len(characterData)):#for loop to iterate through everyone to reduce health by 1
                            try:int(characterData[i][5]) - 1
                            except: error = True
                            if error != True:
                                if int(characterData[i][5]) - 1 == 0:
                                    coolOutput(str(characterData[i][0])+' dies. You cannot use this character ever again.')
                                    characterData.pop(i)
                                else:
                                    characterData[i][5] = str(int(characterData[i][5])-1)
                                    win = False
                            
    if end == True:
        deathList = open('deathList.txt','r')        
        no_ofDeaths = len(deathList.read().split())
        deathList.close()
        characterData = []

        coolOutput('The whole party died as the number of people who did not make it out of the cavern increased to '+str(no_ofDeaths)+' poor souls.\nThe Dragon King lives...')
    elif win == True:
        coolOutput('The noble party:')
        displayCharacters(characterData)
    return characterData

#MAIN PROGRAM

##for i in range (0,len(STORY_CHALLENGES)): TESTING
##    print(i, STORY_CHALLENGES[i])
##    print(i, STORY_SUCCESS[i])
##    print(i, STORY_DEFEAT[i])
##                

coolOutput('Welcome to the adventure. Do you wish to create a new party (c) or use a party you have used before (b)?')
partyType = input('> ')

found = False
while found == False:
    #while loop for validation
    while not partyType.strip().lower().startswith('c') and   not partyType.strip().lower().startswith('b'):
        coolOutput('Please enter c for creating a new party or b for a party used before.')
        partyType = input('> ')

    partyData = [[],[],[],[]]

    if partyType.strip().lower().startswith('c'):
        partyData = createParty()
        #print(partyData)#used for testing
        print()
        coolOutput('What is the name of this party:')
        partyName = input('> ')
        found = True
        
    else:
        coolOutput('Enter the name of the party you want to use (case sensitive) (or press enter to create a new party):')
        inputName = input ('> ')
        if inputName != '':
            partyData = readFile(inputName)
            if partyData == None:
                found = False
            else:
                partyName = inputName
                found = True
        else:
            partyType = 'c'

partyData = checkData(partyData) #more characters will be added if the pary doesnt have 4 players      
    
coolOutput('\nYou now have a full party. The adventure begins.\n')

#partyData = [['Hank','16','12','11','8','2'],['Carrie','12','18','11','9','2'],['Magellan','6','13','12','10','2'],['Ambrose','8','10','14','12','2']]#test data
#partyData = [['Hank','0','0','0','0','10'],['Ambrose','8','10','14','12','1']]#test data

coolOutput('This is how your party looks like:')
displayCharacters(partyData)
time.sleep(2)
partyData = runStory(partyData)
if len(partyData) != 0:
    coolOutput('Party saved. You can use this party in another adventure.')
writeFile(partyData,partyName)
time.sleep(1)
coolOutput('Thanks for playing!')
