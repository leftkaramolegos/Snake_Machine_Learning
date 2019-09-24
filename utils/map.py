from utils.snake import*

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
		for y in range(self.height): 
			for x in range(self.width):
				currentPos = [x, y]
				if(y == -1 or x == -1 or x == self.width or y == self.height):
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
		return mapString 

	@staticmethod
	def printMapDetailed(snake):
		snakeList = snake.getSnake()
		detailedMap = [[0 for x in range(10)] for y in range(10)]
		for x in range(10): 
			for y in range(10):
				currentPos = [x, y]
				if(currentPos in snakeList):
					pos = snakeList.index(currentPos)
					detailedMap[x][y] = format(1 - (pos * 0.01), '.2f')
				elif(snake.getFood() == currentPos):
					detailedMap[x][y] = 3
				else:
					detailedMap[x][y] = 0
		mapString = ''
		for y in range(0, 10):
			for x in range(0, 10):
				mapString = mapString + str(detailedMap[x][y]) + ','
		return mapString[:-1]
