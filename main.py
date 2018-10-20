import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
from utils.dimensionUtils import setDirection
from utils.map import*
from utils.userInputConverter import*

# Window initialisation
curses.initscr()
win = curses.newwin(30, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(0)
win.timeout(500)  

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

snake = [[1, 1], [2, 1], [3, 1]]
head = [3, 1]
food = [5, 5]

key = -1
width = 12
height = 12
myMap = setMap(width, height)
myMap.updateMap(snake, food)
s = ''
count = 0
map = [[0 for x in range(width)] for y in range(height)]
while key != 27:
	count +=1
	key = win.getch()
	win.addstr(0, 0, s)
	action = InputConverter.convertUserInput(direction, key)
	#log map on action file

	#check for food or if looses and recalculate if needed
	#if loose curses.endwin()

	#update snake
	#head = sname[-1]

	#draw 
	l = []
	#Draw map!
	l.append('Map: \n' + myMap.drawMap() + '\n')



	#Draw info
	l.append('Count: ' + str(count) + '\n')
	l.append('Direction: ' + str(direction) + '\n')
	l.append('Action: ' + str(action) + '\n')
	l.append('Key: ' + str(key) + '\n')
	# l.append('Snake: ' + str(snake) + '\n')
	# l.append('Snake: ' + str(snake) + '\n')
	# l.append('Map: \n' + myMap.printMap(myMap.snakeMap) + '\n')
	s = ''.join(l)                          

curses.endwin()



