from tkinter import *


class Game:
    def __init__(self):
        """Constructeur définissant la fenêtre de jeu (dimensions, couleurs) 
        ainsi que les aspects graphiques et techniques"""

        # Création de la fenêtre
        self.window = Tk()
        self.window.title('Project Pong — Thomas Le Naour')
        self.width = 900
        self.height = 600
        self.canvas = Canvas(self.window, width=self.width, height=self.height, bg='black')

        # Création de la balle et de ses mouvements
        self.x0, self.y0 = 435, 285
        self.ball = self.canvas.create_oval(self.x0, self.y0, self.x0 + 25, self.y0 + 25, fill='white')
        self.movement_x = 5
        self.movement_y = 5
        self.move_ball()

        # Affichage du canvas
        self.canvas.grid()

    def mainloop(self):
        """Méthode permettant d'assurer l'ouverture et la fermeture du jeu"""

        return self.window.mainloop()

    def move_ball(self):
        """Méthode permettant de réaliser le mouvement de la balle"""

        if self.canvas.coords(self.ball)[0] < 0 or self.canvas.coords(self.ball)[2] > 900:
            self.movement_x *= -1
        if self.canvas.coords(self.ball)[1] < 0 or self.canvas.coords(self.ball)[3] > 600:
            self.movement_y *= -1

        self.canvas.move(self.ball, self.movement_x, self.movement_y)
        self.window.after(40, self.move_ball)


# Initialisation du jeu
app = Game()

# Fermeture du jeu
app.mainloop()