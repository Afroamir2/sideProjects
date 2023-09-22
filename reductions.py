# -*- coding: utf-8 -*-
"""
Functions about word reductions

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Amirou Sanoussy 
"""
__version__ = 1

def loadWords():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds each word into a list.  It returns
    the list containing all words in the file.
    '''
    with open('words_alpha.txt') as wordFile:
        wordList = []
        
        for line in wordFile:
            wordList.append(line.rstrip('\n'))

    return wordList

def reduceOne(firstString, secondString, wordList):
    # Here is where you will write your function to determine
    # if the second string can be reduced from the first string
    # The code below checks the string in whether they exist in the worldList. 
    #It checkjs them independent of each other
   
    string1 = False
    string2 = False 
    
    for word in wordList:
        if word == firstString:
            string1 = True
            break
    for word in wordList:
        if word == secondString:
            string2 = True
            break
        


    # The Code below will check whether the first string can be reduced into the
    # the second string. 
    if string1 == string2:
        for i in range(len(firstString)):
            finalString = firstString[:i]+firstString[i+1:]
            if finalString == secondString:
                return True 
        
    return False
    
    pass


def reduceAll(word, wordList):
    # Here is where you will write your function to determine
    # all word reductions that can be obtained from the input word
    # after removing one letter
    #Below is a nested for loop function which at first removes a single character at a time
    #At each index then it checks if it is a real word. If it is, then the word is appended
    #To the new list. 
    augmentedWords = []
    if type(word) is type([]):
        for i in range(len(word)):
            for i in range(len(word[i])):
                newString = word[:i] + word[i+1:]
                for trueWord in wordList:
                    if newString == trueWord:
                        augmentedWords.append(trueWord)
                        newString = ''
    else:
        for i in range(len(word)):
            newString = word[:i] + word[i+1:]
            for trueWord in wordList:
                if newString == trueWord:
                    augmentedWords.append(trueWord)
        
        
    return augmentedWords
    
    pass
        
def reduceTwoAll(word, wordList):
    # Here is where you will write your function to determine
    # all word reductions that can be obtained from the input word
    # after removing two letters
    #This function creates an empty list, and a list of already reduced one character words. 
    #The function then proceeds to remove another letter and see if that newWord is valid within 
    #the wordList. If so, the word is added to the emptylist. 
    augmentedWords =[]
    
    list1 = []
    for i in range(len(word)):
        string = word[:i] + word[i+1:]
        list1.append(string)
    for i in list1:
        reduceList = reduceAll(i, wordList)
        augmentedWords = augmentedWords + reduceList
        reduceList = []
    
    return augmentedWords
    

    
    pass

def validateReduction(reduction, wordList):
    # Here is where you will write your function to determine
    # whether or not the provided sequence is a valid one-letter
    # reduction, checking for both the character removal and the
    # validity of each word
    Boolean = True 
    for i in range(len(reduction)):
        if Boolean == True and i < len(reduction) -1:
            if reduceOne(reduction[i], reduction[i+1], wordList) == True:
                    Boolean = True 
            else:
                return False
    return Boolean     
pass


def main():
    # Here is where you will call your test cases
    wordList = loadWords()
    
    test1(wordList)
    test2(wordList)
    test3(wordList)
    test4(wordList)
    test5(wordList)
    test6(wordList)
    test7(wordList)
    test8(wordList)
    test9(wordList)
    test10(wordList)
    test11(wordList)
    test12(wordList)
    test13(wordList)
    test14(wordList)
    test15(wordList)
    test16(wordList)
    
    
    pass



###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for reduce()
def test1(wordList):
    # This comment explains what test1() is testing for, and is followed by code
    #test a condition 
    
    print(reduceOne('cheese', 'leaves', wordList))
    pass

def test2(wordList):
    # This comment explains what test2() is testing for, and is followed by code
    print(reduceOne("Boats", "Boat", wordList))
    pass

# Below are the tests for reduce2()
def test3(wordList):
    # This comment explains what testN() is testing for, and is followed by code
    print(reduceOne("reads", "read", wordList))
    pass
 
def test4(wordList): 
    print(reduceOne("Boa", "Bpast", wordList))
    pass

def test5(wordList):
    print(reduceAll("boats", wordList))
    pass

def test6(wordList):
    print(reduceAll("cheese", wordList))
    pass

def test7(wordList):
    print(reduceAll("errie", wordList))
    pass

def test8(wordList):
    print(reduceAll("turnable", wordList))
    pass

def test9(wordList):
    print(reduceTwoAll("boats", wordList))
    pass

def test10(wordList):
    print(reduceTwoAll("funeral", wordList))
    pass

def test11(wordList):
    print(reduceTwoAll("beleive", wordList))
    pass

def test12(wordList):
    print(reduceTwoAll("chart", wordList))
    pass

def test13(wordList):
    print(validateReduction(["boats", "boat", "boa"], wordList))
    pass

def test14(wordList):
    print(validateReduction(["chart", "fart", "kart"], wordList))

    pass

def test15(wordList):
    print(validateReduction(["startling", "starting", "staring", "string", "sting", "sing"], wordList))
    pass

def test16(wordList):
    print(validateReduction(["mailbags", "mailbag"], wordList))
    pass 
  


    
###############################################################    
    
if __name__ == "__main__":
    main()    