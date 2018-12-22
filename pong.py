from tkinter import *

class Interface:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width = 800, height = 600, bg = 'black')

    def showInterface(self):
        return self.window, self.canvas.grid(), self.window.mainloop()

class Player(Interface):
    def __init__(self, side):
        self.window = Tk()
        self.canvas = Canvas(self.window, width = 800, height = 600, bg = 'black')
        self.side = side

    def addPlayer(self):
        """Fonction permettant d'ajouter un joueur (c'est à dire un rectangle)
        si le side est 0, alors le côté est gauche
        si le side est 1 alors le côté est droit"""

        if self.side == 0:
            x, y, xx, yy = 0, 0, 10, 10
        else:
            datas = '(20, 20), (50, 50)'

        self.canvas.create_rectangle(x, y, xx, yy, fill = 'green')

###############################################################################

# Window creation
pong = Interface()
pong.showInterface()
player1 = Player(0)
player1.addPlayer()