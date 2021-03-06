"""
Features added in V8EXTRA:

-Plural nouns (both english and gibberish) are now converted to singular
-Error Handling uses try except for files if not found
-Greeting message adjusted to be clearer
-import libraries at the top organised
-coding verb conjugation

"""

import random, cmudict, nltk.corpus, inflect, mlconjug3
#I am importing code that finds the amount of syllables in a word, given that it is a proper word

toSingular = inflect.engine() #method that will be used to find the singular of a noun
conjugator = mlconjug3.Conjugator(language='en') 

#this is the function that finds the amount of syllables
dictionary = cmudict.dict()
def syllableFirst(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in dictionary[word.lower()]] 


#if the amount of syllables is found by the function above, I will use my own code to find the amount
#of syllables in the word

def syllableBackUp(word):
    word = word.upper()#all of the words is converted to upper case
    
    results = hardCodedCheck(word) #first some hard coded checks are performed
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

def conjugateVerb(verb): #function that performs checks and conjugates verb to singular
  verb = verb.lower() #sanitsation
  
  
  
  if verb[-2:] in ['ch','ss','sh']:
    return verb+'es' #needs to end with es
  
  elif verb[-1] in ['x','z']:
    return verb+'es'
  
  elif verb[-1] == 's' or verb[-2:] == "ed":#checks if it ends in s or ed
    return verb #no change needed
  
  elif verb[-3:] == "ing": #if it ends with ing,
    verb = verb[:-3] #the ing part is removed
    
    #library is used to automatically conjugate verb
    return conjugator.conjugate(verb).conjug_info['indicative']['indicative present']['3s']
  
  print("Are you sure this verb is singular?(y/n)") 
  choice = input('>')
  
  if choice.strip().lower().startswith('n'):
    
    print("Is this word a model verb like 'play', 'eat' etc.(y/n)")
    choice = input('>')

    if choice.strip().lower().startswith('y'):
      #library can only conjugate model verbs so the user is asked, then it is conjugated 
      return conjugator.conjugate(verb).conjug_info['indicative']['indicative present']['3s']
    else:
      return None #the verb is not valid
    
  else: # the verb is singular, e.g. ate
    return verb

  #conjugator.conjugate("play") conjugator.conjugate("play").iterate() conjugator.conjugate("play",'indicative', 'indicative present', '3s')

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

            try: #try is used as there might be an error when using the library, in which we dont want to change user input
      
              if forms[index] == "a noun:":
                new = toSingular.singular_noun(word) #returns the singular of a noun, or False if its already singular
                #print("word is noun",new)#used for testing
                
                if new != word and new != False:
                  #old = word
                  word = new

            except:
              pass

            if forms[index] == "a verb:":
              word = conjugateVerb(word)
              
            if word == None:
              print("The verb is not singular.")
              
            else:
                    
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
        
    if total > 17: #if the user exceeded the limit
      #removes the last word and syllable from the list
      for i in range(0,5):
        if words[4-i] != '':#finds the last word entered
          print(words[4-i],"is removed as you have exceeded the syllable limit.")
          words[4-i] = ''
          syllables[4-i] = 0
          break #only want the last word to be removed

    syllables = [-10 if x == 0 else x for x in syllables]
    #print(syllables,words)#used for testing
    
    return [words, syllables] #the words, and their syllables are returned in a 2d list


def read(file):#function to read a file

  try:
    my = open(file).readlines() #the whole of the file is opened and read
    new = [[]]#used to put the words in the correct format
    #the index of the list of the word is its syllable count -1

    count = 0
    for i in my:#loops through the lines
        if i != '\n':#if it is empty, a new sublist is created
            new[count].append(i[:-1].lower()) #the word is added to the 
        else:
            count += 1#if there is an empty line
            new.append([])#a new list for a new set of syllables is added
    return new

  except:
    print("Error: File "+file+" not found.")


def returnBanned(form):#banned returns the forms not availabile for a given type of word
    if form == "noun:":
      return ["noun:"]#there cant be 2 nouns in a line
    elif form == ["adjective:"]:
      return ["adjective:","verb:"]#there cant be adjective then a verb/adjective
    else:
      return ["adjective:","verb:"]#there cant be verb then a verb/adjective
    

def longWordL2(words,syllables):#line two when there is a word with more than 6 syllables
  index = next(x for x, val in enumerate(syllables) if val >5)
  #finds the index of the word with more than 5 syllables

  word = words[index]
  syllable = syllables[index]
  form = forms[index]
  
  words[index] = ''#the word is replaced with a placeholder
  syllables[index] = -10#syllable is replaced with a placeholder

  banned = returnBanned(form) #the banned forms are found

  #print(word,syllable,form,banned)#used for testing
  
  if syllable == 7: #if the word is 7 syllables
    secondLine = word #the whole line is the single word
  
  else:
    secondWord = ''
    for i in range (0,len(syllables)):
      if syllables[i] == 1 and forms[i] not in banned: #tries to find a 1 syllables word in the words
        secondWord = words[i]
        secondForm = forms[i]
        words[i] = '' #if found, the word is stored and it is replaced with a placeholder
        syllables[i] = -10
        break#we only need 1 word

    #print("secondword:",secondWord)#used for testing
        
    if secondWord == '':# if ther is no other word, we will need to generate a random word
      
      if form == "noun:": #if word is a noun
        
        #print("Form is noun and no 1 syllable")#used for testing
        
        if random.randint(0,1)==1: #50% chance to perform either, to increase variety of results
          secondLine = word+' '+random.choice(verbs[0]) #either noun and verb
        else:
          secondLine = random.choice(adjectives[0])+' '+word#or adjective and noun

          
      elif form == "adjective:": #if word is an adjective
        #print("form is adjective")#used for testing
        secondLine = word +' '+random.choice(nouns[0]) #word and noun is the only possibility

      else:#if it is a verb
        secondLine = random.choice(nouns[0]) +' '+word#nounn and verb is the only possibility
        #print("form is verb")#used for testing

    else:#if there is a second word
      
      if (form == "noun:" and secondForm == "verb:")or form=="adjective:": 
        secondLine = word+' '+secondWord #noun + verb or adjective + noun
        
      elif (form == "noun:" and secondForm == "adjective:") or form=="verb:":
        secondLine = secondWord+' '+word #the other way around

  #print(secondLine)#used for testing
  #print(words,'and',word)#used for testing
  
  return [secondLine,words,syllables]


def makeSecondLine(words,syllables):#function used to make the second line
  #second line
  #noun verb, adjective noun
  
  isLine2 = False #used to see if there is already a line 2, in case there is a word longer than 6
  
## Check if long word: 
  if 6 in syllables or 7 in syllables: #if there is a long word
    results = longWordL2(words,syllables) #the ling word function is used to create a secondline
    secondLine = results[0] #the values are updated accordingly
    words = results[1]
    syllables = results[2]
    isLine2 = True #there is a line 2
#end

  
  #=====There is a single word from user in second line=====
  if isLine2 == False:
    largestSyllable = max(syllables) #largest syllable (less than 5) is found
    largestIndex = syllables.index(largestSyllable) #the index of this syllable is found
    word = words[largestIndex]
    form = forms[largestIndex]
    banned = returnBanned(form) #banned forms are returned

    syllables[largestIndex] = -10
    words[largestIndex] = ''

    #print(form,word,"syllable:",largestSyllable,"index:",largestIndex)#used for testing
    
    word2 = ''
    
    for i in range (0,len(words)): #checks if there is another word that can be used
      if forms[i] not in banned and syllables[i] <= 7-largestSyllable and syllables[i] > 0:
        #word 2 needs to not be banned and the total has to be less than 7, it has to be more than 0 as -10 is placeholder 
        word2 = words[i]
        syllable2 = syllables[i]
        form2 = forms[i]

        syllables[i] = -10
        words[i] = ''

        #print(form2,word2,"syllable:",syllable2,"index:",i)#used for testing
        
        break #only 1 word is needed
    
    if word2 == '': #if there was no word 2
      
      wordNum = random.randint(2,3) #a random dice is rolled to indicate the line will have 2 or 3 words

      if form =="noun:": #if the word is a noun
        if wordNum == 2: #if there will be 2 words
          #print("wordNum is 2")#used for testing
          
          wordType = random.randint(1,2) #50% to perform either
          if wordType == 1: #if 1
            #print("wordType is 1")
            secondLine = word+' '+random.choice(verbs[6-largestSyllable])#noun and verb
          else:
            #print("wordType is 2")
            secondLine = random.choice(adjectives[6-largestSyllable])+' '+word#adjective and noun
            
        else:#if 3 words
          #print("wordNum is 3")#used for testing
          randAdjSyl = random.randint(0,5-largestSyllable)#a random valid syllable is given for adjective
          #at least 1 syllable is reserved verb
          randVerbSyl = 5-largestSyllable-randAdjSyl #verb syllable is calculated to add to 7 (5 is used for indexing)
          
          #print(randAdjSyl+1,largestSyllable,randVerbSyl+1)#used for testing
          secondLine = random.choice(adjectives[randAdjSyl])+' '+word+' '+random.choice(verbs[randVerbSyl])
          #secondLine is constructed

      elif form == "verb:":#if the word is a verb
        if wordNum == 2: #2 words
          secondLine = random.choice(nouns[6-largestSyllable])+' '+word #noun verb
        else:
          #print("wordNum is 3")#used for testing
          randAdjSyl = random.randint(0,5-largestSyllable)#same process this time with adjective and noun
          randNounSyl = 5-largestSyllable-randAdjSyl
          
          #print(randAdjSyl+1,randNounSyl+1,largestSyllable)#used for testing
          secondLine = random.choice(adjectives[randAdjSyl])+' '+random.choice(nouns[randNounSyl])+' '+word
          
      else:#if word is an adjective
        if wordNum == 2:#2 words
          secondLine = word+' '+random.choice(nouns[6-largestSyllable])#adjective and noun is the only possibility
        else:#3 words
          #print("wordNum is 3")#used for testing
          #adjective noun verb - same process as above
          randNounSyl = random.randint(0,5-largestSyllable)
          randVerbSyl = 5-largestSyllable-randNounSyl
          
          #print(largestSyllable,randNounSyl+1,randVerbSyl+1)#used for testing
          secondLine = word+' '+random.choice(nouns[randNounSyl])+' '+random.choice(verbs[randVerbSyl])

      #print(secondLine)#used for testing
      
    #======END============== Bottom Executed IF There is a single word from user in second line ==================
      
    else:
      if largestSyllable + syllable2 == 7: #checks if the two words add up to 7
        if (form == "noun:" and form2 == "verb:") or (form == "adjective:" and form2 == "noun:"):
          #print("bigger then smaller")#used for testing
          secondLine = word+' '+word2 # constructs secondLine to make grammatical sense
        elif (form == "verb:" and form2 == "noun:") or (form == "noun:" and form2 == "adjective:"):
          #print("smaller then bigger")
          secondLine = word2+' '+word# constructs secondLine to make grammatical sense
       
      else: # if the words' syllables dont add up to 7
        word3 = '' # a 3rd word might be needed
        
        for i in range (0,len(words)):
          
          if forms[i]!=form and forms[i]!=form2 and syllables[i]+largestSyllable+syllable2 == 7 and syllables[i] > 0:
            #checks if the word form is valid, and the total is exactly 7 (if its less, 4 words cant be used)
            #and if the syllables is not -10 which is placeholder for empty
            
            word3 = words[i]
            syllable3 = syllables[i]
            form3 = forms[i]

            syllables[i] = -10 #the corressponding details are removed
            words[i] = ''

            #print(form3,word3,"syllable:",syllable3,"index:",i)#used for testing
            
            break #only 1 word is needed


        if word3 != '': #if there is a 3rd valid word that adds up to 7
          
          #all the options are checked to make a valid sentence
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

      
        #If there isnt a 3rd word in input, we need to generate one 
        else:
          needed = 6-largestSyllable-syllable2 #the amount of syllables needed to make 7

          #all the options are checked to have 7 syllables
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

          

  return [secondLine,words,syllables]

def findForSum(syllables,target): #function used to find a syllable that adds up to a target
  
  for i in range (0,len(syllables)): #loops throught the list 
    if syllables[i]!= -10: #if it isnt empty
      complementary = target-syllables[i] #needed syllables is found
      banned = returnBanned(forms[i]) #banned forms is found
      for j in range (0,len(syllables)): #loops again
        if syllables[j] == complementary and forms[j] not in banned:#if the syllables match and it isnt banned
          return [i,j] #the two indices are returned
  return None #else nothing is returned
    
def returnMatchingIndexes(syllables,target): #used to find matching indexes
  
  #check if two words add up to total
  
  results = findForSum(syllables,target)

  if results != None: #if there are 2 matching indices, they are returned
    return results


  #check if a noun, verb and adjective add up to total/check if 3 words add up
  adjectiveSyl = syllables[4] #there is one adjective
  if adjectiveSyl == -10: #if it is empty, then there is no matching indices
    return None
  
  else:
    newTarget = target - adjectiveSyl #the new target is found
    results = findForSum(syllables[:-1],newTarget) #two words that add up within nouns, and verbs is searched
    if results != None: #if found, the three indices are returned
      threeIndex = [4,results[0],results[1]]
      return threeIndex
    else: #else there are no matchibg indices
      return None

def lineSingleInput(index,words,syllables): #function used to return line with 1 user input
  neededSyllable = 4-syllables[index]#needed syllables are found
  word = words[index]
  words[index] = ''
  syllables[index] = -10 #word info replaced with empty placeholders
  
  
  if forms[index]=="noun:": #if word is noun
    
    if random.randint(0,1) == 1:#50% to create variety
      line = random.choice(adjectives[neededSyllable])+' '+word#adjective noun
    else:
      line = word+' '+random.choice(verbs[neededSyllable])#noun verb
      
  elif forms[index] == "adjective:":#if adjective, adjective noun returned
    line = word+' '+random.choice(nouns[neededSyllable])
  else:#if verb, noun verb returned
    line = random.choice(nouns[neededSyllable])+' '+word

  return [line,words,syllables]

def fiveSyllableLine(words,syllables): #line 1 and 3 are both 5 syllables so one function will be used for both
  if 5 in syllables: #if there is a 5 syllabled word 
    index = syllables.index(5) #the index of it is found
    line = words[index] #the line is just the single word
    words[index] = ''
    syllables[index] = -10 #info is replaced

    return [line,words,syllables]

  else: #else
    results = returnMatchingIndexes(syllables,5)#user input is searched to see if two valid words add up to 5
    
    if results != None: #if there are valid numbers in the list that add up to 5
      if len(results) == 3: #if 3 words that add up to 5
        line = words[results[0]] + ' '+words[results[1]]+' '+words[results[2]]#line is formed
        #the three words will always be in correct order as it is checked as adjective, noun verb in the function
        
        #the used words are removed from the pool of words
        words[results[0]] = ''
        words[results[1]] = ''
        words[results[2]] = ''
        syllables[results[0]] = -10
        syllables[results[1]] = -10
        syllables[results[2]] = -10
        return [line,words,syllables]

      
      else: #if there are two words that add up to 5
        twoForms = [forms[results[0]],forms[results[1]]] # the forms of the words
        
        if twoForms[0] == "adjective:" or twoForms[1]=="verb:":# the words are ordered in the correct format
          line = words[results[0]]+' '+words[results[1]]
        else:
          line = words[results[1]]+' '+words[results[0]]

        #words are removed from the pool of words
        words[results[0]] = ''
        words[results[1]] = ''
        syllables[results[0]] = -10
        syllables[results[1]] = -10

        return [line,words,syllables]

    #none of the numbers in the list add up to 5
    else:
      #if there are no words left in the list of words
      if all(syllable == -10 for syllable in syllables):
        
        if random.randint(0,1) == 0:#50% to create variety
          syllableFirst = random.randint(1,4)#the first syllable is chosen randomly between 1 and 4
          line = random.choice(adjectives[syllableFirst-1])+' '+random.choice(nouns[4-syllableFirst])
          #second syllable is adjusted accordingly to create a line of adjective noun
          
        else:#other 50% is creating line of noun and verb
          syllableThird = random.randint(1,4)
          line = random.choice(nouns[syllableThird-1])+' '+random.choice(verbs[4-syllableThird])
        return [line,words,syllables]
      
      else: #none of the valid syllables add up to 5 and there is at least 1 word
        onlyValid = syllables[:]#new list by value is created to not edit the original one    
        wordsAmount = len(list(filter(lambda a: a != -10, onlyValid))) #all of the -10s are taken out of the list 

        if wordsAmount == 1:#if there is 1 word
          index = next(x for x, val in enumerate(syllables) if val != -10 )#the index of this word is found

          #the line which has only this word as input is returned by calling the function lineSingleInput
          return lineSingleInput(index,words,syllables)


        else:#if there is 2,3,4 words and non add up to 5
          index = next(x for x, val in enumerate(syllables) if val != -10 and val<5)
          #the first word that hasnt been used is found

          wordIndices = None #no other word indices found
          
          for i in range (0,len(words)): #loops through list to find other words that can be used in the line
            if syllables[i] != -10 and forms[i] != forms[index]:
              #checks if word is valid
              
              total = syllables[i] + syllables[index]#the total of the syllables is found
              if total <5:#if total is less than 5, the indices are stored and broken out of the loop
                wordIndices = [index,i]
                break
              total = 0#the total is reset back to 0 

          if wordIndices == None:#there are no other suitable words
            return lineSingleInput(index,words,syllables)#only the single word will be used
              
          else:#there are 2 words that add up to less than 5
            neededSyllables = 4-total #needed syllables is calculated

            #info about words are stored
            form = forms[wordIndices[0]]
            form2 = forms[wordIndices[1]]
            word = words[wordIndices[0]]
            word2 = words[wordIndices[1]]

            #these words are removed from the pool of words
            words[wordIndices[0]] = ''
            words[wordIndices[1]] = ''

            syllables[wordIndices[0]]=-10
            syllables[wordIndices[1]]=-10
            
            #all 6 combinations are tested in order for words to make grammatical sense 
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
                 

  
def makeHaiku(words,syllables): #function to make a 3 line 5-7-5 haiku
  results = makeSecondLine(words,syllables)#firstly the second line is made as the longest word will be used here
  secondLine = results[0]#secondline is stored and words and syllables updated
  words = results[1]
  syllables = results[2]

  #first line with 5 syllables is created and the details are updated
  results2 = fiveSyllableLine(words,syllables)
  firstLine = results2[0]
  words = results2[1]
  syllables = results2[2]

  #third line with 5 syllables is created
  thirdLine = fiveSyllableLine(words,syllables)[0]

  if random.randint(0,1)==0: #50% chance will mean first and third line will swap to increase variety of haiku
    
    temp = firstLine
    firstLine = thirdLine
    thirdLine = temp

  #the lines are sanitised and capitalized
  firstLine = firstLine.strip().lower().capitalize()
  secondLine = secondLine.strip().lower().capitalize()
  thirdLine = thirdLine.strip().lower().capitalize()

  #the haiku is combined to make a single string
  haiku = firstLine+'\n'+secondLine+'\n'+thirdLine+'\n'

  return haiku

def writeFile(haiku):#procedure to write a haiku to a file
  file = "haikus.txt"
  try:#try used to display an error message if file isnt found.
    
    myfile = open(file,'a')#file opened
    myfile.write(haiku+'\n')#haiku is appended and a new line is added to declare a new haiku
    myfile.close()
  except:
    print("Error: File "+file+" not found.")


def outputHaiku():#procedure to output all saved the haikus
  file = "haikus.txt"
  try: #try used to display an error message if file isnt found.\
    
    print("All saved haikus:\n")
    myfile = open(file,'r')
    contents = myfile.read()
    myfile.close()

    print(contents)
    
  except:#error message displayed
    print("Error: File "+file+" not found.")

def choice(words): #function that is used to return a random word from a list of random syllables of nouns/adjectives/verbs
    return random.choice(random.choice(words))

  
def randomHaiku():#function that returns are random haiku
    
  syllableFirst = random.randint(1,4)#first syllable of the first line is randomized
  #(allowing the second word to have at least 1 syllable)
  firstLine = random.choice(adjectives[syllableFirst-1])+' '+random.choice(nouns[4-syllableFirst])

  #for the second line, either adj or noun will have at least 2 syllables
  baseAdj = 1
  baseNoun = 1

  #chosen randomly
  if random.randint(1,2) == 0:
      baseAdj = 2
  else:
      baseNoun = 2
      
  syllableAdj = random.randint(baseAdj,4)#adjective syllables is found
  adjective = random.choice(adjectives[syllableAdj-1]) #adjective is chosen

  #takeaway from 6 as at least one syllable is needed for the last one
  syllableNoun = random.randint(baseNoun,6-syllableAdj)
  noun = random.choice(nouns[syllableNoun-1])# noun is found

  syllableVerb = 7-syllableNoun-syllableAdj #the syllables for verb is chosen to add up to 7
  verb = random.choice(verbs[syllableVerb-1])
  
  secondLine = adjective + ' ' + noun + ' ' + verb #the secondline is formed


  syllableThird = random.randint(1,4)#for the third line, the syllable for the noun is chosen
  #line is generated
  thirdLine = random.choice(nouns[syllableThird-1])+' '+random.choice(verbs[4-syllableThird])

  #the lines are capitalized
  firstLine = firstLine.capitalize()
  secondLine = secondLine.capitalize()
  thirdLine = thirdLine.capitalize()

  #haiku is formed to be a single string
  haiku = firstLine+'\n'+secondLine+'\n'+thirdLine+'\n'

  return haiku


#Some test data:
##results = fiveSyllableLine(["noun1","noun2",'verb1',"verb2","adjective"],[3,-10,4,-10,3])
##print(results[0])
##print(results[1],"AND",results[2])

##results = inputValues()
##words = results[0]
##syllables = results[1]


#Constants
vowels = ['A','E','I','O','U','Y'] 
forms = ["noun:","noun:","verb:","verb:","adjective:"]
verbs= read("listverbs.txt")

abstractAdjectives = read("listadjectives.txt")
abstractNouns = read("listnouns.txt")

natureAdj = read("natureAdj.txt")
natureNoun = read("natureNoun.txt")
#there are no unique verbs for each theme, to make the haiku more unique

print("Welcome to haiku generator.\nYou can choose to generate a random haiku based on nature,\nor one with a more 'abstract' approach.\nFor the best experience, please make sure your nouns and verbs are singular.")


play = True #play is used to continue playing
while play:

  print("\nWould you like your haiku to be nature related (n) or more abstract(a)?")
  haikuTopic = input('>')


  if haikuTopic.lower().strip().startswith('n'):
    #nature adjectives and nouns are assigned
    adjectives = natureAdj
    nouns = natureNoun
  else:
    #abstract nouns and adjectives are assigned
    adjectives = abstractAdjectives
    nouns = abstractNouns

#Some test data
##  syble = [2,2,3,4,3]
##  words = ["noun"+str(syble[0]),"noun"+str(syble[1]),"verb"+str(syble[2]),"verb"+str(syble[3]),"adjective"+str(syble[4])]

  print("\nDo you want to enter some words(w) or generate whole of haiku randomly(r) ?")
  haikuType = input('>')
  
  if haikuType.strip().lower().startswith('w'):#if users chooses to enter words
    results = inputValues() #first values are input, then these are assigned
    words = results[0]
    syllables = results[1]

    #make haiku function is called
    haiku = makeHaiku(words,syllables)

  else:#a random haiku is made with the chosen topic
    haiku = randomHaiku()
    
    
  print("Your haiku:\n")
  print(haiku)

  print("Do you want to save this haiku (s), output all saved haikus (o), exit (e) or continue generating haikus(enter)?")
  choice = input(">")
  
  if choice.lower().startswith('s'): #save haiku
      writeFile(haiku)
  elif choice.lower().startswith('o'): #output all saved haikus
      outputHaiku()
  elif choice.lower().startswith('e'): #exit
      play = False

