class setMap:
	width = 0
	height = 0
	snakeMap = {}

	def __init__(self, map_width, map_height):
		self.width = map_width
		self.height = map_height
		self.snakeMap = { (i,j):-2 for i in range(map_width) for j in range(map_height) }

	def updateMap(self, snake, food):
		self.snakeMap = [[0 for x in range(self.width)] for y in range(self.height)]
		for y in range(self.height): 
			for x in range(self.width):
				currentPos = [x, y]
				if(y == 0 or x == 0 or x == self.width - 1 or y == self.height - 1):
					self.snakeMap[x][y] = -2
				elif(currentPos in snake):
					self.snakeMap[x][y] = -1
				elif(food == currentPos):
					self.snakeMap[x][y] = 1
				else:
					self.snakeMap[x][y] = 0


	# @classmethod
	def drawMap(self):
		mapString = ''
		for y in range(self.height):
			for x in range(self.width):
				if(self.snakeMap[x][y] < 0):
					mapString = mapString + ' #'
				elif(self.snakeMap[x][y] == 0):
					mapString = mapString + '  '
				elif(self.snakeMap[x][y] == 1):
					mapString = mapString + ' *'
			mapString = mapString + '\n'
			# mapString = 'as'#str(self.width)
		return mapString 

	@staticmethod
	def printMap(mapArray):
		mapString = ''
		for y in range(12):
			for x in xrange(12):
				mapString = mapString + str(mapArray[x][y])
			mapString = mapString + '\n'
		return mapString