# from PyQt5.QtGui import *

class EdgeDrawer:

    @staticmethod
    def drawEdges(snakeList, qPainter, brush):
        prevCell = [-1,-1]
        for snakeCell in snakeList:
            if(prevCell == [-1,-1]):
                prevCell = snakeCell
                continue
            x = 0
            y = 0
            w = 0
            h = 0
            constX = 0
            constY = 0
            if(prevCell[0] > snakeCell[0]):
                # dexia
                x = prevCell[0]
                y = prevCell[1]
                h = 78
                w = 2
                constX = 10
                constY = 12
            elif(prevCell[0] < snakeCell[0]):
                # aristera
                x = snakeCell[0]
                y = prevCell[1]
                h = 78
                w = 2
                constX = 10
                constY = 12
            elif(prevCell[1] < snakeCell[1]):
                # pano
                x = prevCell[0]
                y = snakeCell[1]
                h = 2
                w = 78
                constX = 12
                constY = 10
            elif(prevCell[1] > snakeCell[1]):
                # kato
                x = prevCell[0]
                y = prevCell[1]
                h = 2
                w = 78
                constX = 12
                constY = 10
            prevCell = snakeCell
            brush.setNamedColor('#000000')
            qPainter.setBrush(brush)
            xx = (x * 80) + constX
            yy = (y * 80) + constY
            qPainter.drawRect(xx, yy, w, h)
            # return true