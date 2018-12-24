from tkinter import *

class Interface:
    """Classe définissant l'interface de base du jeu à savoir :
    - la fenêtre
    - la balle et ses mouvements"""

    def __init__(self):
        self.width = 900
        self.height = 600
        self.window = Tk()
        self.canvas = Canvas(self.window, width=self.width, height=self.height, bg='black')
        self.x0, self.y0 = 435, 285
        self.ball = self.canvas.create_oval(self.x0, self.y0, self.x0 + 25, self.y0 + 25, fill='white')
        self.movement_x = 10
        self.movement_y = 10

    def showInterface(self):
        """Méthode permettant d'afficher l'interface du jeu"""
        return self.window, self.canvas.grid(), self.window.mainloop()

    def moveBall(self):
        """Méthode permettant de réaliser le mouvement de la balle"""

        if self.canvas.coords(self.ball)[0] < 0 or self.canvas.coords(self.ball)[2] > 900:
            self.movement_x *= -1
        if self.canvas.coords(self.ball)[1] < 0 or self.canvas.coords(self.ball)[3] > 600:
            self.movement_y *= -1

        self.canvas.move(self.ball, self.movement_x, self.movement_y)
        self.window.after(40, self.moveBall)

class Player(Interface):
    pass

# Création de l'interface de jeu
pong = Interface()

# Initialisation du mouvement de la balle
pong.moveBall()

# Affichage de l'interface de jeu
pong.showInterface()