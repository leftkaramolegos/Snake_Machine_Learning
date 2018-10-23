import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
from utils.directionUtils import*
from utils.map import*
from utils.userInputConverter import*
from utils.snake import*

# Window initialisation
curses.initscr()
win = curses.newwin(30, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(0)
win.timeout(100)  

direction = 0
				# direction 
				# 0 -> moving right 
				# 1 -> moving down
				# 2 -> moving left
				# 3 -> moving up
action = -1
				# Action that indicates the way the snake will move based on his current direction
				# 0 -> turn right 
				# 1 -> keep moving in the same direction
				# 2 -> turn left
				# -1 -> no action

snake = Snake()
food = [5, 5]

key = -1
width = 12
height = 12
myMap = setMap(width, height)
myMap.updateMap(snake, food)
s = ''
map = [[0 for x in range(width)] for y in range(height)]
while key != 27:
	key = win.getch()
	win.addstr(0, 0, s)
	action = InputConverter.convertUserInput(direction, key)
	direction = Direction.getDirectionFromAction(direction, action)
	if(action != -1):
		snake.updateSnake(direction, food)
		myMap.updateMap(snake, food)

	#log map on action file

	#check for food or if looses and recalculate if needed
	#if loose curses.endwin()

	#update snake
	#head = sname[-1]

	#draw 
	l = []
	#Draw map!
	l.append('Map: \n' + myMap.drawMap() + '\n')


	#temp
	text = ''
	for x in snake.getSnake():
		text = text + str(x)

	#Draw info
	l.append('text: ' + text + '\n')
	l.append('Length: ' + str(len(snake.getSnake())) + '\n')
	l.append('Action: ' + str(action) + '\n')
	l.append('Direction: ' + str(direction) + '\n')
	l.append('Key: ' + str(key) + '\n')
	# l.append('Snake: ' + str(snake) + '\n')
	# l.append('Snake: ' + str(snake) + '\n')
	# l.append('Map: \n' + myMap.printMap(myMap.snakeMap) + '\n')
	s = ''.join(l)                          

curses.endwin()
