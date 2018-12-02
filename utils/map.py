from utils.snake import*
# from snake import*

class setMap:
	width = 0
	height = 0
	snakeMap = {}
	snake = None

	def __init__(self, map_width, map_height):
		self.width = map_width
		self.height = map_height
		self.snakeMap = [[0 for x in range(self.width)] for y in range(self.height)]

		# 0 -> empty
		# 1 -> wall
		# 2 -> snake
		# 3 -> food
		# 4 -> head
	def updateMap(self, snake):
		snakeList = snake.getSnake()
		# subSnakeList = [subList[:2] for subList in snakeList]
		for y in range(self.height): 
			for x in range(self.width):
				currentPos = [x, y]
				if(y == 0 or x == 0 or x == self.width - 1 or y == self.height - 1):
					self.snakeMap[x][y] = 1
				elif(currentPos in snakeList):
					if(currentPos == snakeList[0]):
						self.snakeMap[x][y] = 4
					else:
						self.snakeMap[x][y] = 2
				elif(snake.getFood() == currentPos):
					self.snakeMap[x][y] = 3
				else:
					self.snakeMap[x][y] = 0

	def getMap(self):
		return self.snakeMap

	# @classmethod
	def drawMap(self):
		mapString = ''
		for y in range(self.height):
			for x in range(self.width):
				if(self.snakeMap[x][y] == 1 or self.snakeMap[x][y] == 2 or self.snakeMap[x][y] == 4):
					mapString = mapString + ' #'
				elif(self.snakeMap[x][y] == 0):
					mapString = mapString + '  '
				elif(self.snakeMap[x][y] == 3):
					mapString = mapString + ' *'
			mapString = mapString + '\n'
			# mapString = 'as'#str(self.width)
		return mapString 

	@staticmethod
	def printMapDetailed(snake):
		snakeList = snake.getSnake()
		detailedMap = [[0 for x in range(12)] for y in range(12)]
		for y in range(12): 
			for x in range(12):
				currentPos = [x, y]
				if(currentPos in snakeList):
					pos = snakeList.index(currentPos)
					detailedMap[x][y] = 1 - (pos * 0.01)
				elif(snake.getFood() == currentPos):
					detailedMap[x][y] = 3
				else:
					detailedMap[x][y] = 0
		mapString = ''
		for y in range(1, 11):
			for x in range(1, 11):
				mapString = mapString + str(detailedMap[x][y]) + ','
		return mapString[:-1]


	@staticmethod	
	def printMap(mapArray):
		mapString = ''
		for y in range(1, 11):
			for x in range(1, 11):
				mapString = mapString + str(mapArray[x][y])
		return mapString

