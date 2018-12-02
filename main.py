import curses
import os.path
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

key = -1
width = 12
height = 12
snake = Snake()
myMap = setMap(width, height)
myMap.updateMap(snake)
snake.newFoodPosition(myMap)
myMap.updateMap(snake)
lost = False
s = ''
map = [[0 for x in range(width)] for y in range(height)]
while key != 27:
	key = win.getch()
	win.addstr(0, 0, s)
	action = InputConverter.convertUserInput(direction, key)
	direction = Direction.getDirectionFromAction(direction, action)

	if(action != -1):
		lost = snake.updateSnake(direction, myMap)
		logText = myMap.printMapDetailed(snake) + '\n'
		fileName = 'tempaAction' + str(action) + '.log'
		file = open(fileName, "a")
		file.write(logText)
		file.close()
		myMap.updateMap(snake)
	if(lost):
		break
	if(snake.getScore() == 97):
		break
	#log map on action file

	#draw 
	l = []
	#Draw map!
	l.append('Map: \n' + myMap.drawMap() + '\n')
	# l.append('Snake: ' + str(snake.getSnake()) + '\n')
	l.append('Score: ' + str(snake.getScore()) + '\n')
	l.append('Direction: ' + str(direction) + '\n')
	s = ''.join(l)                          

curses.endwin()
shouldSave =''
shouldSave = input("Press y to save logs ")
if(shouldSave == 'y'):
	for x in range(3):
		tempFileName = 'tempaAction' + str(x) + '.log'
		fileName = 'action' + str(x) + '.log'
		f1 = open(tempFileName,"r")
		if f1.mode == 'r':
			contents = f1.read()
			f1.close()
			f2 = open(fileName, "a")
			f2.write(contents)
			f2.close()
			f1 = open(tempFileName,"w")
			f1.write('')
			f1.close()
	print ('Saved')
else:
	for x in range(3):
		tempFileName = 'tempaAction' + str(x) + '.log'
		f1 = open(tempFileName,"w")
		f1.write('')
		f1.close()
	print ('Discarded')




