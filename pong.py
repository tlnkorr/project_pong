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
        self.movement_x = 5
        self.movement_y = 5

    def show_game(self):
        """Méthode permettant d'afficher l'interface du jeu"""
        return self.window, self.canvas.grid(), self.window.mainloop()

    def move_ball(self):
        """Méthode permettant de réaliser le mouvement de la balle"""

        if self.canvas.coords(self.ball)[0] < 0 or self.canvas.coords(self.ball)[2] > 900:
            self.movement_x *= -1
        if self.canvas.coords(self.ball)[1] < 0 or self.canvas.coords(self.ball)[3] > 600:
            self.movement_y *= -1

        self.canvas.move(self.ball, self.movement_x, self.movement_y)
        self.window.after(40, self.move_ball)

class Player(Interface):
    """Classe définissant un joueur suivant différentes variables :
    - une raquette
    - des touches différentes pour chaque joueur"""
    
    def __init__(self, side):
        self.side = side


# Création de l'interface de jeu
pong = Interface()

# Initialisation du mouvement de la balle
pong.move_ball()

# Création des 2 joueurs
player1 = Player(0)
player2 = Player(1)

# Affichage de menu
pong.show_game()