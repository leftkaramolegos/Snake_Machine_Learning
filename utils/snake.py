import copy

class Snake:
	snake = []

	def __init__(self):
		self.snake = [[3, 1], [2, 1], [1, 1]]

	def updateSnake(self, direction, food):
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
		if(self.snake[0] == food):
			x = 0
		else:
			self.snake.pop()
		


	def getSnake(self):
		return self.snake