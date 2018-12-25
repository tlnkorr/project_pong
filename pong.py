from tkinter import *


class Ball:
    """Classe définissant la balle et ses mouvements"""
    def __init__(self):
        global app, canvas
        self.ball = canvas.create_oval(435, 285, 460, 310, fill='yellow')
        self.speed_movement_ball_x = 5
        self.speed_movement_ball_y = 5
        self.move_ball()

    def move_ball(self):
        """Méthode permettant de réaliser le mouvement de la balle"""

        if canvas.coords(self.ball)[0] < 0 or canvas.coords(self.ball)[2] > 900:
            self.speed_movement_ball_x *= -1
        if canvas.coords(self.ball)[1] < 0 or canvas.coords(self.ball)[3] > 600:
            self.speed_movement_ball_y *= -1

        canvas.move(self.ball, self.speed_movement_ball_x, self.speed_movement_ball_y)
        app.after(40, self.move_ball)

class Racket:
    def __init__(self, side):
        global app, canvas
        self.side = side
        self.speed_movement_racket_top = 4
        self.speed_movement_racket_down = -4

        if self.side == 0:
            self.racket_left = canvas.create_rectangle(10, 240, 20, 360, fill='white')
        else:
            self.racket_right = canvas.create_rectangle(880, 240, 890, 360, fill='white')

    def move_racket(self, event):
        """Méthode permettant de réaliser le mouvement de la raquette"""

        pass


###############################################################################
###############################################################################
###############################################################################

# Création de la fenêtre
app = Tk()
app.title('Project Pong — Thomas Le Naour')
width = 900
height = 600
canvas = Canvas(app, width=width, height=height, bg='black')
line = canvas.create_line(450, 0, 450,  600, fill='white', dash=6)

# Création de la balle et de ses mouvements
ball = Ball()

# Création des deux raquettes et leurs mouvements
racket_left = Racket(0)
racket_right = Racket(1)

# Affichage du canvas
canvas.grid()

# Fermeture de la fenêtre
app.mainloop()