import random
from time import sleep

class Line:
    def __init__(self, fg, bg, width, height, bext, pending, x, y=0):
        self.fg = fg
        self.bg = bg
        self.width = width
        self.height = height
        self.bext = bext
        self.pending = pending
        self.x = x
        self.y = y
        self.char = ['*', '/', '+', '-']
        self.oldPosition = []

    def getRandomX(self):
        return random.randint(0, self.width - 1)
    
    def getRandomChar(self):
        return random.choice(self.char)
    
    def draw(self):
        self.bext.fg(self.fg)
        self.bext.bg(self.bg)
        self.bext.goto(self.x, self.y)
        self.oldPosition.append((self.x, self.y))
        print(self.getRandomChar(), end='')
        if(self.y == self.height - 1):
            self.y = 0
            self.x = self.getRandomX()
        else:
            self.y += 1
        sleep(0.5)
        
    def removeOldPosition(self):
        self.bext.goto(self.oldPosition[0][0], self.oldPosition[0][1])
        print(' ', end='')
        self.oldPosition.pop(0)
            
    def printLine(self):
        if(self.pending <= 0):
            self.removeOldPosition()
            self.draw()
        else:
            self.pending -= 1
            self.draw()