"""
Usually the sounds that cause a 'syllable' or 'onji' are 'a e i o u y'
If there are two of these sounds next to each other, it should count as 1 syllable
If there is an 'e' at the end, it shouldnt count as a syllable.
If there are no vowels, then the syllable count should be 1.
"""

#I am importing code that finds the amount of syllables in a word, given that it is a proper word
import nltk.corpus
import cmudict

#this is the function that finds the amount of syllables
dictionary = cmudict.dict()
def checkSyllable(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in dictionary[word.lower()]] 

##myfile = open('dictionary.txt','r')
##myDictionary = myfile.read()
##myDictionary = myDictionary.split()
##myfile.close()

#if the amount of syllables is found by the function above, I will use my own code to find the amount
#of syllables in the word

def mySyllable(word):
    word = word.upper()
    
    vowels = ["A","E","I","O","U","Y"]
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

        
    wordLength = len(word)
    
    for letter in range (0,wordLength): #loops through every letter
        if word[letter] in vowels: #checks if its a vowel
            
            try: #error might be given as index is greater than the length of the string

                if word[letter+1] not in vowels: #checks if double vowel present, only counts 1
                    syllables += 1

                elif (letter + 2 == wordLength and word[letter+1] == 'E'):
                    #checks if there is a vowel before the e at the end. This would count as 1 syllable
                    syllables += 1
                    
            except: #reached the last letter
                if word[letter] != 'E': #no syllable added if the last letter is an e
                    syllables += 1
                    
    if syllables == 0: #if the word has no vowels, it is still one syllable
        syllables = 1
        
    return syllables

def checkWord(word):
    global longWord
    global myDictionary

    word = word.upper()

##    firstCheck = mySyllable(word)
##    if firstCheck > 7 or (firstCheck>5 and longWord == True) :
##      print("That word is too long.")
##      return 0
    
##    if word in myDictionary:
      #print("found")
    
    syllables = checkSyllable(word) #finds number of syllables 
    try:
        syllables = int(syllables[0]) #converts it to a single string(from a list)
        found = True
      
    except: #if the number of syllables wasn't found
      #print("error")
      syllables = mySyllable(word)

      if (syllables > 7) or (longWord == True and syllables > 5):
        print("That word is too long.")
        return 0
      
      print("This word wasn't found in the dictionary. Press enter if you still want to use this word:")
      choice = input('>')
      
      if choice != '':
        return 0

    
    if syllables < 6:
        return syllables
    elif 6 <= syllables <= 7 and longWord == False:
        return syllables
    
    else:
        return 0

def inputValues():
    #2 nouns 2 verbs 1 adjective
    global longWord

    words = ['','','','','']
    syllables = [0,0,0,0,0]
    forms = ["a noun:","a noun:","a verb:","a verb:","an adjective:"]
    longWord = False


    for i in range (0,len(forms)):
        
        valid = False
        while not valid:
            print("Enter " + forms[i])
            word = input(">")
            word = word.strip()

            if word.isalpha():
              syllable = checkWord(word)
              if syllable != 0:
                words[i] = word
                syllables[i] = syllable
                valid = True
                print("Word accepted.")

                if 6 <= syllable <= 7:
                  print("You can no longer enter a word with more than 5 syllables.")
                  longWord = True
                
              else:
                  valid = False
                  print("That is not a valid word.")

            else:
                print("Words must contain only letters.")
        

    return [words,syllables]
        
