import copy
from random import randint

class Snake:
	snake = []
	food = []
	score = 0

	def __init__(self):
		self.snake = [[2, 0], [1, 0], [0, 0]]


	def updateSnake(self, direction, map):
		# 0 -> moving right 
		# 1 -> moving down
		# 2 -> moving left
		# 3 -> moving up
		head = copy.copy(self.snake[0])
		if(direction == 0):
			head[0] = head[0] + 1
		elif(direction == 1):
			head[1] = head[1] + 1
		elif(direction == 2):
			head[0] = head[0] - 1
		elif(direction == 3):
			head[1] = head[1] - 1
		self.snake.insert(0, head)
		if(head[0] < 0 or head[0] > 9 or head[1] < 0 or head[1] > 9):
			return True

		#food eaten
		headPosition = self.snake[0]
		if(headPosition == self.food):
			self.newFoodPosition(map)
			self.score += 1
		else:
			self.snake.pop()

		if(headPosition in self.snake[1:]):
			return True
		return False

	def newFoodPosition(self, map):
		food = []
		count = 0
		tempMap = map.getMap()
		for tempList in tempMap:
			count += tempList.count(0)
		if(count == 0):
			food = [-1,-1]
			return
		cellPosition = randint(0, count - 1)
		i = -1
		for row in tempMap:
			if(food != []):
				break
			i += 1
			j = -1
			for cell in row:
				j += 1
				if(cell == 0):
					if(cellPosition == 0):
						food = [i, j]
						break
					else:
						cellPosition = cellPosition - 1
		self.food = food

	def getScore(self):
		return self.score

	def getSnake(self):
		return self.snake

	def getFood(self):
		return self.food
