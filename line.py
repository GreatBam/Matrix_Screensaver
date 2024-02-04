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

    def getRandomX(self):
        return random.randint(0, self.width - 1)
    
    def getRandomChar(self):
        return random.choice(self.char)
    
    def draw(self):
        self.bext.fg(self.fg)
        self.bext.bg(self.bg)
        self.bext.goto(self.x, self.y)
        print(self.getRandomChar(), end='')
        if(self.y == self.height - 1):
            self.y = 0
            self.x = self.getRandomX()
        else:
            self.y += 1
        sleep(0.5)