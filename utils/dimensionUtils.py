class setDirection:
	def __init__( self, direction, action ):
		if(action == -1):
			direction = action
	   	elif(action == 0):
			direction = direction - 1
		elif(action == 1):
			direction = direction
		elif(action == 2):
			direction = direction + 1

		if(direction == -1):
			direction = 3
		elif(direction == 4):
			direction = 0
		self.direction =  direction
		self.action = -1