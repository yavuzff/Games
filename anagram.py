import random, sys
#Yavuz 2017

#anagram game that shuffles words of different difficulty

#words:
easy = ["down","exit","ball","book","nose","lazy","maze","code","neck","bank","bulb","walk","milk"]
medium = ["radio","pixel","chair","sword","table","pizza","judge","quest","label","logic","image","juice","earth","igloo"]
hard = ["school","monday","bikes","square","flower","bridge","camera","carpet","castle","cinema","coffee","dancer","desert","escort","guitar","injury","jacket"]
replay="y"
score=0
print ("Hello and welcome to my anagram game! \nYou will be given a scrambled 4, 5 or 6 letter word. \nYou will have 3 tries until you find the answer. \nEasy mode awards one point, medium mode awards 2 points and hard mode awards 3 points. \nWrong answer deducts a point! \nGood Luck!")

while replay == "y": #loops while user wants to play
    level = input("Do you want to play the easy, medium or hard mode?")

    if level == "easy":
        word=random.choice(easy) #random word chosen from easy
        anagram = []
        for i in word: #string is changed to a list
            anagram.append(i)

        random.shuffle(anagram) #the list is shuffled randomly
        scrambled = ""
        for i in anagram: #the list is combined back into a string
            scrambled = scrambled+i
            
        tries = 3 #the user gets 3 tries to guess the word
        while tries > 0: 
            answer = input(scrambled)
            
            if answer == word: #if the user guesses the word correctly
                print ("Good job!")
                score = score+1
                print ("Score:",score)
                break
            else: #else tries is reduced
                tries = tries - 1
                
                if tries > 0: 
                    print ("Try again",tries,"tries left,")
                    
                if tries == 0: #if the user is out of tries score is reduced
                    print ("Wrong guess!")
                    score=score-1
                    print ("Score:",score)
                    
               
    elif level == "medium":
        #medium level
        word=random.choice(medium)
        anagram = []
        
        for i in word:
            anagram.append(i)
        random.shuffle(anagram)
        scrambled = ""
        for i in anagram:
            scrambled = scrambled+i
            
        print ("Good Luck:",scrambled)
        tries = 3
        while tries > 0:
            answer = input(scrambled)
            if answer == word:
                print ("Good job!")
                score = score+2 #user gets 2 points if correct
                print ("Score:",score)
                break
            else :
                tries = tries - 1
                if tries > 0:
                    print ("Try again",tries,"tries left,")
                if tries == 0:
                    print ("Wrong guess!")
                    score=score-1
                    print ("Score:",score)
    else:
        #hardest level
        word=random.choice(hard)
        anagram = []
        #word is scrambled
        for i in word:
            anagram.append(i)
        random.shuffle(anagram)
        scrambled = ""
        for i in anagram:
            scrambled = scrambled+i

        #the user has their guesses
        print ("Good Luck:",scrambled)
        tries = 3
        while tries > 0:
            answer = input(scrambled)
            if answer == word:
                print ("Good job!")
                score = score+3
                print ("Score:",score)
                break
            else :
                tries = tries - 1
                if tries > 0:
                    print ("Try again",tries,"tries left,")
                if tries == 0:
                    print ("Wrong guess!")
                    score=score-1
                    print ("Score:",score)
    #after each round, user is prompted to replay
    replay = input("Do you want to play again? y/n")
print ("Total score:",score)
sys.exit()

