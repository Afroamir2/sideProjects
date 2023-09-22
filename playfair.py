# -*- coding: utf-8 -*-
"""
Refer to the instructions on Canvas for more information.

"I have neither given nor received unauthorized help on this assignment."
author: Amirou Sanoussy
"""

from string import ascii_lowercase

def createTable(phrase):
    
    '''
    Given an input string, create a lowercase playfair table.  The
    table should include no spaces, no punctuation, no numbers, and 
    no Qs -- just the letters [a-p]+[r-z] in some order.  Note that 
    the input phrase may contain uppercase characters which should 
    be converted to lowercase.
    
    Input:   string:         a passphrase
    Output:  list of lists:  a ciphertable
    '''
    alph = "abcdefghijklmnoprstuvwxyz"
    #Code below alters the string into lower case, and strips away all white spaces and the letter q 
    phrase = phrase.lower()
    phrase = phrase.replace("q", "")
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace("!", "")
    phrase = phrase.replace(".", "")
    phrase = phrase.replace(",", "")
    #Code below creates new string while removing duplicates 
    phraseStrip = ""
    for char in phrase:
        if char in phraseStrip:
            pass
        else: 
            phraseStrip += char
    
    #code below double checks for duplicates and appends the letter by letter 
    for char in alph:
        if char in phraseStrip:
            pass
        else:
            phraseStrip += char
    #The following code sepearates each character into their own list element. 
    #It is subsequently then grouped up in into a 5x5
    stringList = []
    stringList = [char for char in phraseStrip]
    stringList = [stringList[i:i+5] for i in range(0, len(stringList), 5)]
    
    return stringList



def splitString(plaintext):
    '''
    Splits a string into a list of two-character pairs.  If the string
    has an odd length, append an 'x' as the last character.  As with
    the previous function, the bigrams should contain no spaces, no
    punctuation, no numbers, and no Qs.  Return the list of bigrams,
    each of which should be lowercase.
    
    Input:   string:  plaintext to be encrypted
    Output:  list:    collection of plaintext bigrams
    '''

#The code below removes punctuation and adds a charater x if the len of plaintext and separates them into a list of bigrams
    plaintext = plaintext.lower()
    plaintext = plaintext.replace("q", "")
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.replace("!", "")
    plaintext = plaintext.replace(".", "")
    plaintext = plaintext.replace(",", "")
    
    if len(plaintext) % 2 > 0:
        plaintext += "x"
    
    bigramList = [plaintext[i:i+2] for i in range(0, len(plaintext), 2) ]
    #stringList = [stringList[i:i+2] for i in range(0, len(plaintext), 2)]

    return bigramList


# creates a grid for the table
def findInTable(searchLet, table):
    for rowNum,rowList in enumerate(table):
        for colNum, let in enumerate(rowList):
            if let == searchLet:
                return (rowNum, colNum)




            
def playfairRuleOne(pair):
    '''
    If both letters in the pair are the same, replace the second
    letter with 'x' and return; unless the first letter is also
    'x', in which case replace the second letter with 'z'.
    
    You can assume that any input received by this function will 
    be two characters long and already converted to lowercase.
    
    After this function finishes running, no pair should contain two
    of the same character   
    
    Input:   string:  plaintext bigram
    Output:  string:  potentially modified bigram
    '''
    
    


# first rule checks the pair to see if its meets the condition of having the same letters at index 0 and 1 and replaces 
# it with the repective letters
    if pair[0] == "x" and pair[1] == 'x':
        return (pair[0] + 'z')
    elif pair[0] == pair[1]:
        return (pair[0] + 'x')
    else:
        return pair
        
    
    
 

def playfairRuleTwo(pair, table):
    '''
    If the letters in the pair appear in the same row of the table, 
    replace them with the letters to their immediate right respectively
    (wrapping around to the left of a row if a letter in the original
    pair was on the right side of the row).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram
    '''
# The function first gets the position of the letters that we are searching for    

    rowNum, colNum = findInTable(pair[0], table)
    rowNum2, colNum2 = findInTable(pair[1], table)
                       
# the following logic then checks if either letter is at index 4 and switches one column to the right.          
    if rowNum == rowNum2: 
        if colNum == 4:
            return table[rowNum][0] + table[rowNum2][colNum2+1]
        elif colNum2 == 4:
            return table[rowNum][colNum+1] + table[rowNum2][0]
        else:
            return table[rowNum][colNum+1] + table[rowNum2][colNum2+1]
    else:
        return pair
            
        
    
    
    


def playfairRuleThree(pair, table):
    '''
    If the letters in the pair appear in the same column of the table, 
    replace them with the letters immediately below respectively
    (wrapping around to the top of a column if a letter in the original
    pair was at the bottom of the column).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram
    '''
    #the function  first return the transpose the table. 
    #it then uses the funtion from rule two to return the letter that is one row below
    pair = pair 
    # Transpose the table and input the values so to use playfairRuleTwo
    matrixTranspose = [[table[j][i] for j in range(len(table))] for i in range(len(table[0]))]
    modList = playfairRuleTwo(pair, matrixTranspose)
    
     
    
    return modList 
    
    
    
    
    


def playfairRuleFour(pair, table):
    '''
    If the letters are not on the same row and not in the same column, 
    replace them with the letters on the same row respectively but in 
    the other pair of corners of the rectangle defined by the original 
    pair.  The order is important -- the first letter of the ciphertext
    pair is the one that lies on the same row as the first letter of 
    the plaintext pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.  
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram
    '''
    
    #The function first gets the position the letters of the pair
    #the function then checks if the letters are not in the column and row 
    #it then switches their columns repectively to get new value
    pair = pair 
    rowNum, colNum = findInTable(pair[0], table)
    rowNum2, colNum2 = findInTable(pair[1], table)    
    if colNum != colNum2 and rowNum != rowNum2:
        pair = table[rowNum][colNum2] + table[rowNum2][colNum]
        return pair
    else:
        return pair
        
    
    
    
    

def encrypt(pair, table):
    '''
    Given a character pair, run it through all four rules to yield
    the encrypted version!
    
    Input:   string:         plaintext bigram
    Input:   list of lists:  ciphertable
    Output:  string:         ciphertext bigram
    '''
    #the encryoption goes through each line by sending in the pair the first functino and setting the augmented pair.
    #it continues this cycle until the finalEncrypt value
    pair1 = playfairRuleOne(pair)
    pair2 = playfairRuleTwo(pair1, table)
    pair3 = playfairRuleThree(pair2, table)
    finalEncrypt = playfairRuleFour(pair3, table)
    return finalEncrypt




def joinPairs(pairsList):
    '''
    Given a list of many encrypted pairs, join them all into the 
    final ciphertext string (and return that string)
    
    Input:   list:    collection of ciphertext bigrams
    Output:  string:  ciphertext
    '''
    #the function joins the list of charaters into one string
    return ''.join(pairsList)



def main():
    '''
    Example main() function; can be commented out when running your
    tests
    '''
    table = createTable("i am entering a pass phrase")
    splitMessage = splitString("this is a test message")
    pairsList = []
    print(splitMessage)
    print(table) # printed for debugging purposes
    
    for pair in splitMessage:
        # Note: encrypt() should call the four rules
        pairsList.append(encrypt(pair, table))
    cipherText = joinPairs(pairsList)    
    
    print(cipherText) #printed as the encrypted output
    #output will be hjntntirnpginprnpm

    
   
    print(test1(createTable("i am entering a pass phrase")))
    print(test2(createTable("i am entering a pass phrase")))
    print(test3(createTable("i am entering a pass phrase")))
    print(test4(createTable("i am entering a pass phrase")))
    print(test5(createTable("i am entering a pass phrase")))
    print(test6())
    print(test7())
    print(test8())
    print(test9())
    print(test10(table))
    print(test10(table))
    print(test11(table))
    print(test12(table))
    print(test13(table))
    print(test14(table))
    print(test15(table))
    print(test16(table))
    print(test17(table))
    print(test18())
    print(test19())
    print(test20())
    print(test21())
    print(test22())
    print(test23())
    print(test24())
    print(test25())
    print(test26())
    print(test28())
    print(test29())
    print(test30(table))
    print(test31(table))
    print(test32(table))
    
    
###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for createTable()
def test1(table):
    # This comment explains what test1() is testing for, and is followed by code
    assert playfairRuleFour("sb", table) == "rf"
    

def test2(table):
    # This comment explains what test2() is testing for, and is followed by code
    assert playfairRuleFour(playfairRuleOne("va"), table) == "wi"
    pass

# Below are the tests for splitString()
def test3(table):
    # This comment explains what testN() is testing for, and is followed by code
    assert playfairRuleFour("tr", table) == "tr"
    pass

def test4(table):
    assert playfairRuleFour("ir", table) == "at"
    pass
        
def test5(table):
    assert playfairRuleFour("fr", table) == 'bs'
    pass
    assert playfairRuleFour("fr", table) == "bs"
    pass

def test6():
    assert playfairRuleOne("xa") == "xa"
    pass

def test7():
    assert playfairRuleOne("xx" ) == "xz"
    pass

def test8():
    assert playfairRuleOne("as") == "as"
    pass

def test9():
    assert playfairRuleOne("aa") == "ax"
    pass

def test10(table):
    assert playfairRuleThree("th", table) == "hj"
    pass

def test11(table):
    assert playfairRuleThree("ig", table) == "ig"
    pass

def test12(table):
    assert playfairRuleThree("tv", table) == "hi"
    pass

def test13(table):
    assert playfairRuleThree("ax", table) == "ax"
    pass

def test14(table):
    assert playfairRuleTwo("am", table) == "me"
    pass

def test15(table):
    assert playfairRuleTwo("am", table) == "me"
    pass

def test16(table):
    assert playfairRuleTwo("am", table) == "me"
    pass

def test17(table):
    assert playfairRuleTwo("am", table) == "me"
    pass

def test18():
    assert createTable("allah is great boi") == [['a', 'l', 'h', 'i', 's'], ['g', 'r', 'e', 't', 'b'], ['o', 'c', 'd', 'f', 'j'], ['k', 'm', 'n', 'p', 'u'], ['v', 'w', 'x', 'y', 'z']]
    pass


def test19():
    assert createTable("the longest yard") == [['t', 'h', 'e', 'l', 'o'], ['n', 'g', 's', 'y', 'a'], ['r', 'd', 'b', 'c', 'f'], ['i', 'j', 'k', 'm', 'p'], ['u', 'v', 'w', 'x', 'z']]
    pass

def test20():
    assert createTable("ice cream is delicious ! ") == [['i', 'c', 'e', 'r', 'a'], ['m', 's', 'd', 'l', 'o'], ['u', 'b', 'f', 'g', 'h'], ['j', 'k', 'n', 'p', 't'], ['v', 'w', 'x', 'y', 'z']]
    pass

def test21():
    assert createTable("the hangover is a mid movie") == [['t', 'h', 'e', 'a', 'n'], ['g', 'o', 'v', 'r', 'i'], ['s', 'm', 'd', 'b', 'c'], ['f', 'j', 'k', 'l', 'p'], ['u', 'w', 'x', 'y', 'z']]
    pass

def test22():
    assert splitString("the longest yard") == ['th', 'el', 'on', 'ge', 'st', 'ya', 'rd']
    
    pass

def test23():
    assert splitString("the hangover is a mid movie") == ['th', 'eh', 'an', 'go', 've', 'ri', 'sa', 'mi', 'dm', 'ov', 'ie']
    pass


def test24():
    assert splitString("ice cream is delicious ! ") == ['ic', 'ec', 're', 'am', 'is', 'de', 'li', 'ci', 'ou', 'sx']
    pass

def test25():
    assert splitString("allah is great boi") == ['al', 'la', 'hi', 'sg', 're', 'at', 'bo', 'ix']
    pass

def test26():
    assert joinPairs(['th', 'el', 'on', 'ge', 'st', 'ya', 'rd']) == "thelongestyard"
    pass

def test27():
    assert joinPairs(['th', 'eh', 'an', 'go', 've', 'ri', 'sa', 'mi', 'dm', 'ov', 'ie']) == "thehangoverisamidmovie"
    pass

def test28():
    assert joinPairs(['ic', 'ec', 're', 'am', 'is', 'de', 'li', 'ci', 'ou', 'sx']) == "icecreamisdeliciousx"
    pass

def test29():
    assert joinPairs(['al', 'la', 'hi', 'sg', 're', 'at', 'bo', 'ix']) == "allahisgreatboix"
    pass

def test30(table):
    assert encrypt("gg", table) == "cm"
    pass

def test31(table):
    assert encrypt("lm", table) == 'xg'
    pass

def test32(table):
    assert encrypt("tn", table) == 'si'
    pass    
###############################################################    
    
if __name__ == "__main__":
    main()        