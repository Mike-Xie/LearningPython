def break_words(stuff):
	"""This function will break up words for us."""
	return stuff.split()
	#more efficient not to have temp variable

def sort_words(words):
	"""This function will return the words sorted. """
	return sorted(words)

def print_first_word(words):
	"""This function returns the first word."""
	#thought tempvar wasn't necessary at first but it is
	#pop removes and returns an element from the list
	#so we have to create a temp copy to not mess with 
	#the original
	wordCopy = words.pop(0)
	return wordCopy


def print_last_word(words):
	"""This function returns the last word. """
	#same deal here
	wordCopy = words.pop(-1)
	return wordCopy

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	sortedS = sort_sentence(sentence)
	print_first_word(sortedS)
	print_last_word(sortedS)




