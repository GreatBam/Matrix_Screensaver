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
