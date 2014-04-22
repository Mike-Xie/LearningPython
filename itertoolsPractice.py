import itertools

houses = [1,2,3,4,5]
colors = ['red', 'green', 'ivory', 'yellow', 'blue']
people = ['Englishman', 'Spaniard', 'Ukranian', 'Japanese', 'Norwegian']
pets = ['dog', 'snails', 'fox', 'horse', 'zebra']
drink = ['coffee', 'tea', 'milk', 'oj', 'water']
smoke = ['OldGold', 'Kools', 'Chesterfields', 'Luckystrike', 'Parliaments']

def absolute(n):
	return abs(n)

orderings = list(itertools.permutations(houses))

