"""
Usually the sounds that cause a 'syllable' or 'onji' are 'a e i o u y'
If there are two of these sounds next to each other, it should count as 1 syllable
If there is an 'e' at the end, it shouldnt count as a syllable.
If there are no vowels, then the syllable count should be 1.
"""

vowels = ["A","E","I","O","U","Y"] #constant

#I am importing code that finds the amount of syllables in a word, given that it is a proper word
import nltk.corpus
import cmudict

#this is the function that finds the amount of syllables
dictionary = cmudict.dict()
def syllableFirst(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in dictionary[word.lower()]] 


#if the amount of syllables is found by the function above, I will use my own code to find the amount
#of syllables in the word

def syllableBackUp(word):
    word = word.upper()
    
    results = hardCodedCheck(word)
    word = results[0]
    syllables = results[1]
    
    wordLength = len(word)
    
    for letter in range (0,wordLength): #loops through every letter
        if word[letter] in vowels: #checks if its a vowel
          
              if letter != wordLength - 1: #checks if last letter
                if word[letter+1] == "Y" and word[letter+2] in vowels: # for words like 'kayak'
                  syllables += 1
                  
                elif word[letter+1] not in vowels: #checks if double vowel present, only counts 1
                    syllables += 1
                    
                elif (letter + 2 == wordLength and word[letter+1] == 'E'):
                    #checks if there is a vowel before the e at the end. This would count as 1 syllable
                    #the 'ie' at the end of a word like 'cookie' will not count if this code wasnt added
                  
                    syllables += 1
                    
            #except: #reached the last letter
              else:
                if word[letter] != 'E': #no syllable added if the last letter is an e
                    syllables += 1
                    
    if syllables == 0: #if the word has no vowels, it is still one syllable
        syllables = 1
        
    return syllables

def hardCodedCheck(word):
    syllables = 0

    #hard coding some cases 
    if word[0:2] == "RE": #suffix 're'
        syllables += 1
        word = word[2:] #the first part is removed from the word


    if word[-2:] == 'LE' and word[-3] not in vowels: #ending in 'le'
        syllables += 1
        word = word[:-2]


    if word[-3:] == 'LES' and word[-4] not in vowels: #ending in 'les'
        syllables += 1
        word = word[:-3]

    return [word, syllables]


def checkWord(word):

    word = word.upper() #made all upper case as the data stored in the text file is all upper
    syllables = syllableFirst(word) #finds number of syllables
    
    try: #there will be an error here if the number of syllables wasnt found
        syllables = int(syllables[0]) #converts it to a single string(from a list)
      
    except: #if the number of syllables wasn't found
      
      #print("error")#used for testing
      syllables = syllableBackUp(word) #my own tool will decide the no of syllables 

      if (syllables > 7) or (longWord == True and syllables > 5): #checks if the word is too long
        print("That word is too long.")
        return 0 #0 is returned to show that the input was invalid
      
      print("This word wasn't found in the dictionary. Press enter if you still want to use this word:")
      choice = input('>')
      
      if choice != '': #if the user doesnt want to use the word, the function is ended
        return 0


    return syllables #the amount of syllables is returned


def inputValues():
    #2 nouns 2 verbs 1 adjective
  
    global longWord #This value is a boolean that can only change once in the runtime of the program
    longWord = False
    
    words = ['','','','','']
    syllables = [0,0,0,0,0]
    forms = ["a noun:","a noun:","a verb:","a verb:","an adjective:"]
    

    index = 0 #the current index of the type of word asked
    total = 0 #the total number of syllables entered

    while index < len(forms) and total <= 16: #loops until every input is entered or the limit of syllables is passed

      valid = False 
      
      while not valid: #loops until input is valid
          print("\nEnter " + forms[index]) #user is prompted to enter type of word
          word = input(">")
          word = word.strip() #word is sanitised

          if word.isalpha(): #checks if word is only letters
            syllable = checkWord(word) #finds the syllable count of the word
            
            if syllable != 0: #if a valid count is returned
              
              if total > 17: #checks if the limit is exceeded
                print("You have exceeded the limit of syllables. Your last input will not be used.")
                
              elif 6 <= syllable <= 7 : #checks the syllables of the words, only 1 5-6 syllable word can be used
                print("Word accepted. You can no longer enter a word with more than 5 syllables.")
                longWord = True #there can no longer be a long word
                
              else:
                print("Word accepted.")


              words[index] = word #the word is added to the list of word
              syllables[index] = syllable #the number of syllables it has is added to the list
              
              valid = True #the word is valid
              total= total + syllable #the total is updated
              
          else:
              print("Words must contain only letters.")

      print(words,syllables) #used for testing
      index += 1 #next index
      
    if 0 in syllables: #if the user reached the limit of syllables
      syllables = list(filter(lambda a: a != 0, syllables)) #all of the 0s are taken out of the list
      words = list(filter(lambda a: a != '', words))#all of the corresponding ''s are taken out of the list
        
    if total > 17: #if the user exceeded the limit
      words.pop(-1) #the last extra word is removed
      syllables.pop(-1)

    return [words, syllables] #the words, and their syllables are returned in a 2d list

