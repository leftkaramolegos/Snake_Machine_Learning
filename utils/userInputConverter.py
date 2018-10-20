import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

class InputConverter:
	# def __init__():

	@classmethod
	def convertUserInput(self, direction, userInput):
		action = -1
		if(direction == 0):
			if(userInput == curses.KEY_DOWN):
				action = 0
			elif(userInput == curses.KEY_UP):
				action = 2
			elif(userInput == curses.KEY_RIGHT):
				action = 1
			elif(userInput == curses.KEY_LEFT):
				action = -1
		elif(direction == 1):
			if(userInput == curses.KEY_DOWN):
				action = 1
			elif(userInput == curses.KEY_UP):
				action = -1
			elif(userInput == curses.KEY_RIGHT):
				action = 2
			elif(userInput == curses.KEY_LEFT):
				action = 0
		elif(direction == 2):
			if(userInput == curses.KEY_DOWN):
				action = 2
			elif(userInput == curses.KEY_UP):
				action = 0
			elif(userInput == curses.KEY_RIGHT):
				action = -1
			elif(userInput == curses.KEY_LEFT):
				action = 1
		elif(direction == 3):
			if(userInput == curses.KEY_DOWN):
				action = -1
			elif(userInput == curses.KEY_UP):
				action = 1
			elif(userInput == curses.KEY_RIGHT):
				action = 0
			elif(userInput == curses.KEY_LEFT):
				action = 2
		return action