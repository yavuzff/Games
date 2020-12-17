#Yavuz 2018 - Dungeon master toolkit
import random, time

def createPlayers(num,names,types):#function that stores the player names and types
    for i in range(0,num):#loops  for every player in game
        player = input("Enter the name of the next player:\n")
        names.append(player)#adds this name to the list of names
        character = input("Enter this player's character type:\n")
        types.append(character)#adds this type to the list of character types

def createStats(num,h,a,d):#function that stores the stats of the players
    choice = input("Do you want to set the same stats for every player? y/n\n")
    if choice == "y" or choice == "Y":
        health = int(input("Enter the health value for all of the players:\n"))
        attack = int(input("Enter the attack value for all of the players:\n"))
        defence = int(input("Enter the defence value for all of the players:\n"))
        for i in range (0,num):
            h.append(health)#adds the stats to the arrays
            a.append(attack)
            d.append(defence)           
    else:
        for i in range(0,num):#loops through every element of the array and asks individually for each stat
            health = int(input("Enter the health value of player " + str(i+1) + "\n"))
            h.append(health)
            attack = int(input("Enter the attack value of player " + str(i+1) + "\n"))
            a.append(attack)
            defence = int(input("Enter the defence value of player " + str(i+1) + "\n"))
            d.append(defence)

def diceRoll(x,y):
    for i in range (0,y):# y is the number of times that the dice will be rolled
        print (random.randint(1,x)) # x is the biggest number i.e the sides of the dice
       
def randomCaverns(n):#function creates random cavern numbers
    caverns = []
    for c in range (1,n+1):
        valid = False
        while valid == False:
            r = random.randint(1,n)
            valid = True
            for i in range (0,len(caverns)):
                if caverns[i] == r:
                    valid = False
        caverns.append(r)
    for i in range (0,len(caverns)):
            print(caverns[i], end = " ")
    return caverns

def changeCharacter(character):#changes player name or player type
    player = int(input("Enter the player number that is being changed:\n"))
    newCharac = input("Enter the new value for this player:\n")
    character[player-1] = newCharac #changes the name or type of a player

def changeStat(stat):#changes stat that is entered (health, attaack, defence)
    player = int(input("Enter the player number that is being changed:\n"))
    if input("Is this player gaining stats? y/n\n") == "y":
        change = int(input("Enter the amount of stats gained:\n"))
        stat[player-1] = stat[player-1] + change # adds the change to health/attack/defence
    else:
        change = int(input("Enter the amount of stat lost:\n"))
        stat[player-1] = stat[player-1] - change # takes away the amount from the attribute
        
        
def removePlayer():
    global playerAmount # changes the global variable inside the function
    player = int(input("Enter the number of the player you want to remove:\n"))
    names.pop(player-1)
    types.pop(player-1)
    playerHealth.pop(player-1)
    playerAttack.pop(player-1)
    playerDefence.pop(player-1) #removes all of the chosen player's attributrd from the lists
    playerAmount = playerAmount - 1

def showBoardstart():# prints the player 1... top part of the table
    print ("         ", end = " ")
    for i in range (0,playerAmount):
        print("Player",i+1,end = " |  ") # end = " " allows to print everything on the same line
    print("\n")#starts a new line for the next output
    
def showBoard(a):#function that prints any attribute to the table
    for i in range (0,playerAmount): # does it for every player
        print("    ",a[i],"    ",end = "|")
    print("\n")



print("WELCOME TO THE DUNGEON MASTER TOOLKIT!\nYou can roll dices, generate random caverns...\nand keep track of any number of player's name, type, health, attack and defence!")

playerAmount = int(input("Enter the amount of players in the game:\n"))
names = []
types = []
playerHealth = []
playerAttack = []
playerDefence = [] # stores different attributes of the players: name type health attack defence 

createPlayers(playerAmount,names,types)
createStats(playerAmount,playerHealth,playerAttack,playerDefence)
choice = 0

while choice < 7:#loops till 7 (exit) or a larger number is chosen
    if playerAmount != 0:
        choice = int(input("\nDo you want to:\n1-Roll a dice\n2-Create random caverns\n3-Change player name or type\n4-Change the stats of a player\n5-Show the attribute of a player\n6-Remove a player\n7-Exit\n"))
        if choice == 1:#choice 1 is rolling a dice
            diceSides = int(input("Enter the amount of sides the dice has:\n"))
            diceTimes = int(input("Enter the amount of times you want to roll the dice:\n"))
            diceRoll(diceSides,diceTimes)
        elif choice == 2:#choice 2 is creating caverns
            cavernAmount = int(input("Enter the amount of caverns you want to create:\n"))
            randomCaverns(cavernAmount) #uses the integer given by the user
        elif choice == 3: #choice 3 is chaning a player name or type
            change = int(input("Do you want to change a player's name or a player's character type? 1/2 \n"))
            if change == 1:
                changeCharacter(names)
            else:
                changeCharacter(types)
        elif choice == 4:#choice 4 is changing a stat (health, attack,defence)
            change = int(input("Do you want to change a player's:\n1-Health\n2-Attack\n3-Defence"))
            if change == 1:
                changeStat(playerHealth)
            elif change == 2:
                changeStat(playerAttack)
            else:
                changeStat(playerDefence)
        elif choice == 5:#choice 5 prints all of the information in a neat way
            showBoardstart()
            print("Health: ", end = "")
            showBoard(playerHealth)#calls the same function but with different attributes
            print("Attack: ", end = "")
            showBoard(playerAttack)
            print("Defence:", end = "")
            showBoard(playerDefence)
            for i in range (0,playerAmount):#prints the name and type of every player
                print("Player",i+1,"is",types[i],names[i])
        elif choice == 6:# removes a player, can be used if a player reaches 0 health etc.
            removePlayer()
        time.sleep(2) # a small delay to let the user read what has been written and to reduce clunkiness
    else:
        print ("No players left! Quitting...")# leaves automatically when every player is gone
        choice = 7 # stops the program infinite looping









