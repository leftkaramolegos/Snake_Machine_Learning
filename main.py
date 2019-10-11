from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
# import os.path#remove?
from random import randint
from utils.directionUtils import*
from utils.map import*
from utils.userInputConverter import*
from utils.snake import*
from utils.drawEdges import*
from sklearn import model_selection
from sklearn.externals import joblib

class Example(QWidget):
    shouldClose = False
    color = QColor(0, 0, 0)
    color = '#ffffff'
    txt = input("Type y to train: ")
    isTraining = False
    if(txt == 'y'):
        isTraining = True
    direction = 0
				# direction 
				# 0 -> moving right 
				# 1 -> moving down
				# 2 -> moving left
				# 3 -> moving update
    action = -1
				# Action that indicates the way the snake will move based on his current direction
				# 0 -> turn right 
				# 1 -> keep moving in the same direction
				# 2 -> turn left
				# -1 -> no action
    width = 10
    height = 10
    snake = Snake()
    myMap = setMap(width, height)
    myMap.updateMap(snake)
    snake.newFoodPosition(myMap)
    myMap.updateMap(snake)
    lost = False
    s = ''
    loaded_model = joblib.load('snakeModel.sav')


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel('asd',self)
        self.label.resize(self.label.sizeHint())
        self.label.move(10,820)
        self.label.setStyleSheet('color: yellow')
        self.setGeometry(300, 300, 820, 900)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBasic(qp)
        qp.end()

    def keyPressEvent(self, event):
        key = event.key()

        if (self.shouldClose):
            if(key == QtCore.Qt.Key_Y):
                self.saveLogs()
                self.discardTemps()
                self.close()
            else:
                self.discardTemps()
                self.close()

        if(key == QtCore.Qt.Key_Escape): 
            self.shouldClose = True

        logText = self.myMap.printMapDetailed(self.snake) + '\n'
        
        if(self.isTraining):
            self.action = InputConverter.convertUserInput(self.direction, key)
        else:
            count = 0
            a = [float(i) for i in logText.split(',')]
            for i in range(10):
                for j in range(10):
                    x = [[0 for x in range(10)]for y in range(10)]
                    x[i][j] = a[count]
                    count += 1
            strng = ''
            for i in range(10):
                for j in range(10):
                    strng = strng + str(x[i][j])
                strng = strng + '\n'
            print(strng)
            strng = ''
            rotated = zip(*x[::-1])
            for i in range(10):
                for j in range(10):
                    strng = strng + str(rotated[i][j])
                strng = strng + '\n'
            print(strng)
            # print(rotated)
            # predict
            # print(logText)
            xTest = []
            xTest.append(a)
            # print(xTest)
            predicted=self.loaded_model.predict(xTest)
            score = self.loaded_model.predict_proba(xTest)
            print(predicted)
            print(score)
            self.action = predicted #InputConverter.convertUserInput(self.direction, key)

        self.direction = Direction.getDirectionFromAction(self.direction, self.action)

        if(self.action != -1):
            self.lost = self.snake.updateSnake(self.direction, self.myMap)
            fileName = 'tempaAction' + str(self.action) + '.log'
            file = open(fileName, "a")
            file.write(logText)
            file.close()
            self.myMap.updateMap(self.snake)
        if(self.lost):
            self.shouldClose = True
        if(self.snake.getScore() == 97):
            self.shouldClose = True
        self.update()
        # print (self.myMap.printMapDetailed(self.snake))

# save
    @staticmethod
    def saveLogs():
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

    @staticmethod	
    def discardTemps():
        for x in range(3):
            tempFileName = 'tempaAction' + str(x) + '.log'
            f1 = open(tempFileName,"w")
            f1.write('')
            f1.close()
        print ('Temps Discarded')


    def drawBasic(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#000000')
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), col)
        self.setPalette(p)

        # qp.setPen(col)

        brush = QColor(0, 0, 0)
        brush.setNamedColor('#ff0000')
        qp.setBrush(brush)
        qp.drawRect(10, 10, 802, 802)

        brush.setNamedColor(self.color)
        qp.setBrush(brush)
        # temp
        if(self.shouldClose):
            self.label.setText('Press Y for save, or any key for discard')
            self.label.resize(self.label.sizeHint())
            self.label.move(300,400)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet('color: white')
            return

        snakeList = self.snake.getSnake()
        food = self.snake.getFood()

        for j in range(10):
            for i in range(10):
                currentPos = [i, j]
                if(currentPos in snakeList):
                    if(currentPos == snakeList[0]):
                        self.color = '#333333'
                    else:
                        self.color = '#000000'
                elif(food == currentPos):
                    self.color = '#ff0000'
                else:
                    self.color = '#ffffff'
                brush.setNamedColor(self.color)
                qp.setBrush(brush)
                x = i
                y = j
                xx = (x * 80) + 12
                yy = (y * 80) + 12
                qp.drawRect(xx, yy, 78, 78)
        prevCell = [-1,-1]

        EdgeDrawer.drawEdges(snakeList, qp, brush)
        self.label.setText('Score: ' + str(self.snake.getScore()))
        self.label.resize(self.label.sizeHint())

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



