from tkinter import *

class Interface:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width = 900, height = 600, bg = 'black')
        self.ball = 'e'

    def showInterface(self):
        return self.window, self.canvas.grid(), self.window.mainloop()

###############################################################################

# Window creation
pong = Interface()
pong.showInterface()