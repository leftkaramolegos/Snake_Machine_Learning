class Direction:

	@staticmethod
	def getDirectionFromAction(direction, action):
		if(action == 0):
			direction = direction + 1
		elif(action == 1):
			direction = direction
		elif(action == 2):
			direction = direction - 1
		if(direction == -1):
			direction = 3
		elif(direction == 4):
			direction = 0
		return direction