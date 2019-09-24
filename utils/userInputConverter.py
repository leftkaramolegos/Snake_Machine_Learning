from PyQt5 import QtCore

class InputConverter:
    # 0 -> turn right
    # 1 -> keep moving in the same direction
    # 2 -> turn left

	@staticmethod
	def convertUserInput(direction, userInput):
		action = -1
		if(direction == 0):
			if(userInput == QtCore.Qt.Key_Down):
				action = 0
			elif(userInput == QtCore.Qt.Key_Up):
				action = 2
			elif(userInput == QtCore.Qt.Key_Right):
				action = 1
			elif(userInput == QtCore.Qt.Key_Left):
				action = -1
		elif(direction == 1):
			if(userInput == QtCore.Qt.Key_Down):
				action = 1
			elif(userInput == QtCore.Qt.Key_Up):
				action = -1
			elif(userInput == QtCore.Qt.Key_Right):
				action = 2
			elif(userInput == QtCore.Qt.Key_Left):
				action = 0
		elif(direction == 2):
			if(userInput == QtCore.Qt.Key_Down):
				action = 2
			elif(userInput == QtCore.Qt.Key_Up):
				action = 0
			elif(userInput == QtCore.Qt.Key_Right):
				action = -1
			elif(userInput == QtCore.Qt.Key_Left):
				action = 1
		elif(direction == 3):
			if(userInput == QtCore.Qt.Key_Down):
				action = -1
			elif(userInput == QtCore.Qt.Key_Up):
				action = 1
			elif(userInput == QtCore.Qt.Key_Right):
				action = 0
			elif(userInput == QtCore.Qt.Key_Left):
				action = 2
		return action
