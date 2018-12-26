from tkinter import *


class BallProperties:
    """Classe définissant les propriétés et mouvements de la balle"""

    def __init__(self):
        global app, canvas, ball, racket_left, racket_right
        self.speed_movement_ball_x = 5
        self.speed_movement_ball_y = 5

    def move_ball(self):
        """Méthode permettant de réaliser le mouvement de la balle et les rebonds
        sur les raquettes"""

        if canvas.coords(ball)[0] < 0 or canvas.coords(ball)[2] > 900:
            print('Game Over')
        if canvas.coords(ball)[1] < 0 or canvas.coords(ball)[3] > 600:
            self.speed_movement_ball_y *= -1

        if len(canvas.find_overlapping(canvas.coords(player_left)[0], canvas.coords(player_left)[1], canvas.coords(player_left)[2], canvas.coords(player_left)[3])) > 1:
            self.speed_movement_ball_x *= -1
        if len(canvas.find_overlapping(canvas.coords(player_right)[0], canvas.coords(player_right)[1], canvas.coords(player_right)[2], canvas.coords(player_right)[3])) > 1:
            self.speed_movement_ball_x *= -1

        canvas.move(ball, self.speed_movement_ball_x, self.speed_movement_ball_y)
        app.after(20, self.move_ball)


class PlayerProperties:
    """Classe définissant les propriétés et mouvements des joueurs"""

    def __init__(self, side):
        global player_left, player_right
        self.side = side
        self.speed_movement_racket_top = -20
        self.speed_movement_racket_down = 20

        if self.side == 0:
            app.bind('z', self.move_racket)
            app.bind('s', self.move_racket)
        else:
            app.bind('<Up>', self.move_racket)
            app.bind('<Down>', self.move_racket)

    def move_racket(self, event):
        """Méthode permettant de réaliser le mouvement de la raquette"""

        # Gestion des mouvements sur l'axe Y
        if repr(event.char) == "'z'":
            canvas.move(player_left, 0, self.speed_movement_racket_top)
        if repr(event.char) == "'s'":
            canvas.move(player_left, 0, self.speed_movement_racket_down)
        if repr(event.char) == "'\\uf700'":
            canvas.move(player_right, 0, self.speed_movement_racket_top)
        if repr(event.char) == "'\\uf701'":
            canvas.move(player_right, 0, self.speed_movement_racket_down)

        # Gestion des mouvement dans la fenêtre (bords)
        


###############################################################################
######################      PRROGRAM EXECUTION      ###########################
###############################################################################

# Création de la fenêtre
app = Tk()
app.title('Project Pong — Thomas Le Naour')
width = 900
height = 600
canvas = Canvas(app, width=width, height=height, bg='black')
line = canvas.create_line(450, 0, 450,  600, fill='white', dash=6)

# Création des deux raquettes et leurs mouvements
player_left = canvas.create_rectangle(10, 240, 20, 360, fill='white')
player_right = canvas.create_rectangle(880, 240, 890, 360, fill='white')
player_left_properties = PlayerProperties(0)
player_right_properties = PlayerProperties(1)

# Création de la balle et de ses mouvements
ball = canvas.create_oval(435, 285, 460, 310, fill='yellow')
ball_properties = BallProperties()
ball_properties.move_ball()

# Affichage du canvas
canvas.grid()

# Fermeture de la fenêtre
app.mainloop()