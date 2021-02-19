"""
Usually the sounds that cause a 'syllable' or 'onji' are 'a e i o u y'
If there are two of these sounds next to each other, it should count as 1 syllable
If there is an 'e' at the end, it shouldnt count as a syllable.
If there are no vowels, then the syllable count should be 1.
"""

import random
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

      #print(words,syllables) #used for testing
      index += 1 #next index

#CHANGED THIS BOTTOM PART SO WORDS STILL CONTAIN '' AND SYLLABLES CONTAIN -10 
      
##    if 0 in syllables: #if the user reached the limit of syllables
##      test = syllables[:]
##      test = list(filter(lambda a: a != 0, test)) #all of the 0s are taken out of the list 
      #words = list(filter(lambda a: a != '', words))#all of the corresponding ''s are taken out of the list
      
    if total > 17: #if the user exceeded the limit
##      words.pop(-1) #the last extra word is removed
##      syllables.pop(-1)
      for i in range(0,5):
        if words[4-i] != '':
          print(words[4-i],"is removed as you have exceeded the syllable limit.")
          words[4-i] = ''
          syllables[4-i] = 0
          break

    syllables = [-10 if x == 0 else x for x in syllables]
    #print(syllables,words)
    
    return [words, syllables] #the words, and their syllables are returned in a 2d list


def read(file):
    my = open(file).readlines()
    new = [[]]

    count = 0
    for i in my:
        if i != '\n':
            new[count].append(i[:-1].lower())
        else:
            count += 1
            new.append([])
    return new


def returnBanned(form):
    if form == "noun:":
      return ["noun:"]
    elif form == ["adjective:"]:
      return ["adjective:","verb:"]
    else:
      return ["adjective:","verb:"]
    


def longWordL2(words,syllables):#line two when there is a word with more than 6 syllables
  index = next(x for x, val in enumerate(syllables) if val >5)

  word = words[index]
  syllable = syllables[index]
  form = forms[index]
  
  words[index] = ''
  syllables[index] = -10

  banned = returnBanned(form)

  #print(word,syllable,form,banned)
  
  if syllable == 7:
    secondLine = word
  
  else:
    secondWord = ''
    for i in range (0,len(syllables)):
      if syllables[i] == 1 and forms[i] not in banned:
        secondWord = words[i]
        secondForm = forms[i]
        words[i] = ''
        syllables[i] = -10
        break

    #print("secondword:",secondWord)
        
    if secondWord == '':
      
      if form == "noun:":
        
        #print("Form is noun and no 1 syllable")
        
        if random.randint(0,1)==1:
          secondLine = word+' '+random.choice(verbs[0])
        else:
          secondLine = random.choice(adjectives[0])+' '+word

          
      elif form == "adjective:":
        #print("form is adjective")
        secondLine = word +' '+random.choice(nouns[0])

      else:
        secondLine = random.choice(nouns[0]) +' '+word
        #print("form is verb")

    else:
      
      if (form == "noun:" and secondForm == "verb:")or form=="adjective:":
        secondLine = word+' '+secondWord
        
      elif (form == "noun:" and secondForm == "adjective:") or form=="verb:":
        secondLine = secondWord+' '+word

  #print(secondLine)
  #print(words,'and',word)
  
  return [secondLine,words,syllables]


def makeSecondLine(words,syllables):
  #second line
  #noun verb, adjective noun
  
  isLine2 = False
  
## Check if long word: 
  if 6 in syllables or 7 in syllables:
    results = longWordL2(words,syllables)
    secondLine = results[0]
    words = results[1]
    syllables = results[2]
    isLine2 = True
#end

  
  #=====There is a single word from user in second line=====
  if isLine2 == False:
    largestSyllable = max(syllables)
    largestIndex = syllables.index(largestSyllable)
    word = words[largestIndex]
    form = forms[largestIndex]
    banned = returnBanned(form)

    syllables[largestIndex] = -10
    words[largestIndex] = ''

    #print(form,word,"syllable:",largestSyllable,"index:",largestIndex)
    
    word2 = ''
    
    for i in range (0,len(words)):
      if forms[i] not in banned and syllables[i] <= 7-largestSyllable and syllables[i] > 0:
        word2 = words[i]
        syllable2 = syllables[i]
        form2 = forms[i]

        syllables[i] = -10
        words[i] = ''

        #print(form2,word2,"syllable:",syllable2,"index:",i)
        
        break
    
    if word2 == '':
      
      wordNum = random.randint(2,3)

      if form =="noun:":
        if wordNum == 2:
          #print("wordNum is 2")
          
          wordType = random.randint(1,2)
          if wordType == 1:
            #print("wordType is 1")
            secondLine = word+' '+random.choice(verbs[6-largestSyllable])
          else:
            #print("wordType is 2")
            secondLine = random.choice(adjectives[6-largestSyllable])+' '+word
            
        else:
          #print("wordNum is 3")
          randAdjSyl = random.randint(0,5-largestSyllable)
          randVerbSyl = 5-largestSyllable-randAdjSyl
          
          #print(randAdjSyl+1,largestSyllable,randVerbSyl+1)
          secondLine = random.choice(adjectives[randAdjSyl])+' '+word+' '+random.choice(verbs[randVerbSyl])

      elif form == "verb:":
        if wordNum == 2:
          secondLine = random.choice(nouns[6-largestSyllable])+' '+word
        else:
          #print("wordNum is 3")
          randAdjSyl = random.randint(0,5-largestSyllable)
          randNounSyl = 5-largestSyllable-randAdjSyl
          
          #print(randAdjSyl+1,randNounSyl+1,largestSyllable)
          secondLine = random.choice(adjectives[randAdjSyl])+' '+random.choice(nouns[randNounSyl])+' '+word
          
      else:
        if wordNum == 2:
          secondLine = word+' '+random.choice(nouns[6-largestSyllable])
        else:
          #print("wordNum is 3")
          randNounSyl = random.randint(0,5-largestSyllable)
          randVerbSyl = 5-largestSyllable-randNounSyl
          
          #print(largestSyllable,randNounSyl+1,randVerbSyl+1)
          secondLine = word+' '+random.choice(nouns[randNounSyl])+' '+random.choice(verbs[randVerbSyl])

      #print(secondLine)
      
    #======END============== There is a single word from user in second line ==================
      
    else:
      if largestSyllable + syllable2 == 7:
        if (form == "noun:" and form2 == "verb:") or (form == "adjective:" and form2 == "noun:"):
          #print("bigger then smaller")
          secondLine = word+' '+word2
        elif (form == "verb:" and form2 == "noun:") or (form == "noun:" and form2 == "adjective:"):
          #print("smaller then bigger")
          secondLine = word2+' '+word
        #print(secondLine,"00000000")
        
      else:
        word3 = ''
        for i in range (0,len(words)):
          
          if forms[i]!=form and forms[i]!=form2 and syllables[i]+largestSyllable+syllable2 == 7 and syllables[i] > 0:
            word3 = words[i]
            syllable3 = syllables[i]
            form3 = forms[i]

            syllables[i] = -10
            words[i] = ''

            #print(form3,word3,"syllable:",syllable3,"index:",i)
            
            break


        if word3 != '':

          if form == "adjective:" and form2=="noun:":
            secondLine = word+' '+word2+' '+word3
          elif form == "adjective:" and form2=="verb:":
            secondLine = word+' '+word3+' '+word2
          elif form == "noun:" and form2=="adjective:":
            secondLine = word2+' '+word+' '+word3
          elif form == "verb:" and form2=="adjective:":
            secondLine = word2+' '+word3+' '+word
          elif form == "noun:" and form2=="verb:":
            secondLine = word3+' '+word+' '+word2
          elif form == "verb:" and form2=="noun:":
            secondLine = word3+' '+word2+' '+word

          #print(secondLine,"111111")
          
        else:
          needed = 6-largestSyllable-syllable2
          if form == "adjective:" and form2=="noun:":
            secondLine = word+' '+word2+' '+random.choice(verbs[needed])
          elif form == "adjective:" and form2=="verb:":
            secondLine = word+' '+random.choice(nouns[needed])+' '+word2
          elif form == "noun:" and form2=="adjective:":
            secondLine = word2+' '+word+' '+random.choice(verbs[needed])
          elif form == "verb:" and form2=="adjective:":
            secondLine = word2+' '+random.choice(nouns[needed])+' '+word
          elif form == "noun:" and form2=="verb:":
            secondLine = random.choice(adjectives[needed])+' '+word+' '+word2
          elif form == "verb:" and form2=="noun:":
            secondLine = random.choice(adjectives[needed])+' '+word2+' '+word

          #print(secondLine,"LAAAAAAST")

  return [secondLine,words,syllables]

def findForSum(syllables,target):
  for i in range (0,len(syllables)):
    if syllables[i]!= -10:
      complementary = target-syllables[i]
      banned = returnBanned(forms[i])
      for j in range (0,len(syllables)):
        if syllables[j] == complementary and forms[j] not in banned:
          return [i,j]
  return None
    
def returnMatchingIndexes(syllables,target):
  

##  for i, number in enumerate(syllables[:-1]): 
##      complementary = target - number
##      if complementary in numbers[i+1:]:  # note 2
##          print("Solution Found: {} and {}".format(number, complementary))
##          break
##  else:  # note 3
##      print("No solutions exist")

  #check if two words add up to total
  
  results = findForSum(syllables,target)

  if results != None:
    return results

  #check if a noun, verb and adjective add up to total
  adjectiveSyl = syllables[4]
  if adjectiveSyl == -10:
    return None
  else:
    newTarget = target - adjectiveSyl
    results = findForSum(syllables[:-1],newTarget)
    if results != None:
      threeIndex = [4,results[0],results[1]]
      return threeIndex
    else:
      return None

def lineSingleInput(index,words,syllables):
  neededSyllable = 4-syllables[index]
  word = words[index]
  words[index] = ''
  syllables[index] = -10
  
  
  if forms[index]=="noun:":
    
    if random.randint(0,1) == 1:
      line = random.choice(adjectives[neededSyllable])+' '+word
    else:
      line = word+' '+random.choice(verbs[neededSyllable])
      
  elif forms[index] == "adjective:":
    line = word+' '+random.choice(nouns[neededSyllable])
  else:
    line = random.choice(nouns[neededSyllable])+' '+word

  return [line,words,syllables]

def fiveSyllableLine(words,syllables):
  if 5 in syllables:
    index = syllables.index(5)
    line = words[index]
    words[index] = ''
    syllables[index] = -10

    return [line,words,syllables]

  else:
    results = returnMatchingIndexes(syllables,5)
    
    if results != None: #if there are valid numbers in the list that add up to 5
      if len(results) == 3: #3 words that add up to 5
        line = words[results[0]] + ' '+words[results[1]]+' '+words[results[2]]
        
        words[results[0]] = ''
        words[results[1]] = ''
        words[results[2]] = ''
        syllables[results[0]] = -10
        syllables[results[1]] = -10
        syllables[results[2]] = -10
        return [line,words,syllables]
      
      else: #two words that add up to 5
        twoForms = [forms[results[0]],forms[results[1]]]
        
        if twoForms[0] == "adjective:" or twoForms[1]=="verb:":
          line = words[results[0]]+' '+words[results[1]]
        else:
          line = words[results[1]]+' '+words[results[0]]
          
        words[results[0]] = ''
        words[results[1]] = ''
        syllables[results[0]] = -10
        syllables[results[1]] = -10

        return [line,words,syllables]

    #none of the numbers in the list add up to 5
    else:
      #if there are no words left
      if all(syllable == -10 for syllable in syllables):
        if random.randint(0,1) == 0:
          syllableFirst = random.randint(1,4)
          line = random.choice(adjectives[syllableFirst-1])+' '+random.choice(nouns[4-syllableFirst])
        else:
          syllableThird = random.randint(1,4)
          line = random.choice(nouns[syllableThird-1])+' '+random.choice(verbs[4-syllableThird])
        return [line,words,syllables]
      
      else: #none of the valid syllables add up to 5 and there is at least 1 word
        onlyValid = syllables[:]    
        wordsAmount = len(list(filter(lambda a: a != -10, onlyValid))) #all of the -10s are taken out of the list 

        if wordsAmount == 1:#if there is 1 word
          index = next(x for x, val in enumerate(syllables) if val != -10 )

          return lineSingleInput(index,words,syllables)


        else:#if there is 2,3,4 words and non add up to 5
          index = next(x for x, val in enumerate(syllables) if val != -10 and val<5) 
          #banned = returnBanned(forms[index])
          wordIndices = None
          
          for i in range (0,len(words)):
            if syllables[i] != -10 and forms[i] != forms[index]:
              total = syllables[i] + syllables[index]
              if total <5:
                wordIndices = [index,i]
                break
              total = 0

          if wordIndices == None:#there are no other suitable words
            return lineSingleInput(index,words,syllables)
              
          else:
            neededSyllables = 4-total

            form = forms[wordIndices[0]]
            form2 = forms[wordIndices[1]]
            word = words[wordIndices[0]]
            word2 = words[wordIndices[1]]

            words[wordIndices[0]] = ''
            words[wordIndices[1]] = ''

            syllables[wordIndices[0]]=-10
            syllables[wordIndices[1]]=-10
            
            #6 combinations
            if form == "adjective:" and form2=="noun:":
              line = word+' '+word2+' '+random.choice(verbs[neededSyllables])
            elif form == "adjective:" and form2=="verb:":
              line = word+' '+random.choice(nouns[neededSyllables])+' '+word2
            elif form == "noun:" and form2=="adjective:":
              line = word2+' '+word+' '+random.choice(verbs[neededSyllables])
            elif form == "verb:" and form2=="adjective:":
              line = word2+' '+random.choice(nouns[neededSyllables])+' '+word
            elif form == "noun:" and form2=="verb:":
              line = random.choice(adjectives[neededSyllables])+' '+word+' '+word2
            elif form == "verb:" and form2=="noun:":
              line = random.choice(adjectives[neededSyllables])+' '+word2+' '+word

            return [line,words,syllables]
                 


      
##        for i in range (0, len(words)):
##          if syllables[i] !
        

  
def makeHaiku(words,syllables):
  results = makeSecondLine(words,syllables)
  secondLine = results[0]
  words = results[1]
  syllables = results[2]

  results2 = fiveSyllableLine(words,syllables)
  firstLine = results2[0]
  words = results2[1]
  syllables = results2[2]

  thirdLine = fiveSyllableLine(words,syllables)[0]

  if random.randint(0,1)==0: 
    temp = firstLine
    firstLine = thirdLine
    thirdLine = temp

  firstLine = firstLine.strip().lower().capitalize()
  secondLine = secondLine.strip().lower().capitalize()
  thirdLine = thirdLine.strip().lower().capitalize()

  haiku = firstLine+'\n'+secondLine+'\n'+thirdLine

  return haiku



#Constants
vowels = ["A","E","I","O","U","Y"] #constant
forms = ["noun:","noun:","verb:","verb:","adjective:"]
adjectives = read("listadjectives.txt")
nouns = read("listnouns.txt")
verbs= read("listverbs.txt")

##results = fiveSyllableLine(["noun1","noun2",'verb1',"verb2","adjective"],[3,-10,4,-10,3])
##print(results[0])
##print(results[1],"AND",results[2])

##results = inputValues()
##words = results[0]
##syllables = results[1]

#print(makeHaiku(words,syllables))

#forms = ["noun:","noun:","verb:","verb:","adjective:"]

for i in range (0,3):
  syble = [2,2,3,4,3]
  words = ["noun"+str(syble[0]),"noun"+str(syble[1]),"verb"+str(syble[2]),"verb"+str(syble[3]),"adjective"+str(syble[4])]
  

  print(makeHaiku(words,syble))
  print("\n")


#print(syllableFirst('Peculiarity'))
