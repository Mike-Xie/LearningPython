"""
Version 1.0 with ugliest validWords function

Reads in a list of legal words, a .txt with 
one word per line and 
and a set of 7 letters (rack) and returns all 
possible words that can be constructed 
from that set and the
base scores for those words

Mike Xie

ex: python ScrabbleSolver.py 

"""
import collections
#from sys import argv # need to put arguments somewhere
#script, filename, rack  = argv




#dictionaryFile = open(filename, 'r')
# Scores
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

 

 
if __name__ == '__main__':	
     
    # 99% sure that this works for .txt inputs with 1 word per line
    # returns a list of the words               
	def dictToList(aDictionary):
		wordList = []
		for word in aDictionary:
			word = word.rstrip('\n').upper()
			wordList.append(word)
		return wordList

		
	def validPlays(aWordList, aRack):
		validPlayList = []
		for word in aWordList:
			if validWordCheck(aRack, word):
				validPlayList.append(word)
		return validPlayList		
	# returns True if the word can be made with the rack
	def validWordCheck(aRack, aWord): # returns a boolean for if the rack can make the word     
	        tempRack = list(aRack) # temp variable
	        valid = True
	        for letter in aWord:
	                if letter not in tempRack:
	                        valid = False
	                else:
	                        tempRack.remove(letter) # we take the letter out and continue comparing
	        return valid           
                        
	testDict = ['why', 'this', 'are', 'bagels'] # a phrase 1 of my dota players used to 
	testW = ['A', 'R', 'E']
	testW2 = ['Z','X','Q']
	testW3 = ['B', 'B','A','G','E','L']
	testR = "BAGELSR"

	print ("I'm here")
	assert validWordCheck(testR, testW) == True
	assert validWordCheck(testR, testW2) == False
	assert validWordCheck(testR, testW3) == False
        
