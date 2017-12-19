# Jose Hernandez
# 11/21/2017

from random import randint

class Die():
	'''Represents a die that can be rolled.'''
	
	def __init__(self, sides=6):
		'''Initialize the attributes of the die.'''
		self.sides = sides
	
	def rollDie(self, timesRolled=1):
		if timesRolled == 1:
			print("Rolling the " + str(self.sides) + "-sided die " + 
				str(timesRolled) + " time.")
		else:
			print("Rolling the " + str(self.sides) + "-sided die " + 
				str(timesRolled) + " times.")
		x = 0
		while x != timesRolled:
			x += 1
			die = randint(1, self.sides)
			print("Roll " + str(x) + ": " + str(die))


sixSidedDie = Die(6)
sixSidedDie.rollDie(10)

print("")

tenSidedDie = Die(10)
tenSidedDie.rollDie(10)

print("")

twentySidedDie = Die(20)
twentySidedDie.rollDie(10)
