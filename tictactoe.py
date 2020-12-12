import random
#Yavuz 2018

def draw():#function to draw the board after every move
    print (board[0],"|",board[1],"|",board[2])
    print("---------")
    print (board[3],"|",board[4],"|",board[5])
    print("---------")
    print (board[6],"|",board[7],"|",board[8])
    
def checkWin(char):#function that checks if the chosen character has won
    winCombinations = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in winCombinations: #checks every single win combination
        if board[i[0]] == board[i[1]] == board[i[2]] == char: #checks if every element of the win combination is the letter
            return True

def checkTie():#function that checks if all spots are full i.e. a tie
    if len(possibilities) == 0:
        return True

def playRandom():#function that makes random plays 
    computer = random.randint(0,len(possibilities)-1)
    move = possibilities[computer] 
    board[move-1] = "O"
    possibilities.remove(move)
    
def playSmart():#function that doesnt make obvious mistakes
    if board[4] == 5:#checks if the middle is empty
        board[4] = "O"#computer chooses the middle 
        possibilities.remove(5)
        return True #leaves the function
    
    for i in range (0,len(possibilities)): #loops through every possible play      
        board[possibilities[i]-1] = "O" #the possible play is temporarily changed in board
        if checkWin("O") == True:#the change is kept if it is a wining play
            possibilities.remove(possibilities[i])
            return True #leaves the function
        else:
            board[possibilities[i]-1] = possibilities[i]#the change is reversed if it is not a winning play

    for i in range (0,len(possibilities)):#same loop as above       
        board[possibilities[i]-1] = "X"#temporarily changes a possible play to X 
        if checkWin("X") == True:#checks if X will win
            board[possibilities[i]-1] = "O"#if so, O is placed instead of an X
            possibilities.remove(possibilities[i])#removed from possible plays
            return True #exits the function
        else:
            board[possibilities[i]-1] = possibilities[i]#the change is reversed           
    playRandom()#if there is no obvious play, computer plays randomly
    
replay = "y"
while replay == "y":
    board = [1,2,3,4,5,6,7,8,9]
    possibilities = board[:]
    draw()
    continueGame = True #condition to run loop
    while continueGame == True:
        spot = int(input("Enter a spot to put X: "))
        if spot in possibilities: #check if spot is empty
            board[spot-1] = "X" #assign it to X
            possibilities.remove(spot)#number removed from possibile answers
            if checkWin("X") == True:#checks for win for X
                print ("Congratulations, YOU WON!!!")
                continueGame = False
            elif checkTie() == True:#checks for a tie
                print ("It is a tie!")
                continueGame = False
            else:
                playSmart()
                if checkWin("O") == True:#checks for win for O
                    print ("Sorry, Computer Won!")
                    continueGame = False
                elif checkTie() == True:#checks for a tie
                    print("It is a tie!")
                    continueGame = False                  
        else:
            print("That spot is full!")
        draw()
    replay = input("Do you want to play again? y or n? ")

                            
            
        

