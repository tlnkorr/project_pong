from tkinter import *


class Ball:
    """Classe définissant les propriétés et mouvements de la balle"""

    def __init__(self):
        """Constructeur définissant les variables de bases de nos propriétés :
        - la vitesse de mouvement horizontale de la balle
        - la vitesse de mouvement verticale de la balle"""

        global app, canvas, ball, player_left, player_right
        self.speed_movement_ball_x = 5
        self.speed_movement_ball_y = 5

    def move_ball(self):
        """Méthode permettant de réaliser le mouvement de la balle et les rebonds
        sur les raquettes"""

        # Paramétrage des rebonds de la balle par rapport au canvas
        if canvas.coords(ball)[1] < 0 or canvas.coords(ball)[3] > 600:
            self.speed_movement_ball_y *= -1

        # Paramétrage des rebonds de la balle par rapport aux raquettes
        if len(canvas.find_overlapping(canvas.coords(player_left)[0], canvas.coords(player_left)[1], canvas.coords(player_left)[2], canvas.coords(player_left)[3])) > 1:
            self.speed_movement_ball_x *= -1
        if len(canvas.find_overlapping(canvas.coords(player_right)[0], canvas.coords(player_right)[1], canvas.coords(player_right)[2], canvas.coords(player_right)[3])) > 1:
            self.speed_movement_ball_x *= -1

        # Mouvement perpetuel de la balle
        canvas.move(ball, self.speed_movement_ball_x, self.speed_movement_ball_y)
        app.after(20, self.move_ball)


class Player:
    """Classe définissant les propriétés et mouvements des joueurs"""

    def __init__(self, side):
        """Constructeur définissant les variables de bases de nos propriétés :
        - le côté du joueur (0 pour gauche, 1 pour droite)
        - la vitesse de mouvement verticale de la raquette en haut
        - le bloquage de la raquette (False pour ne pas bloquer le mouvement)"""

        global ball, player_left, player_right
        self.side = side
        self.speed_movement_racket = 30
        self.block_top = False
        self.block_bottom = False

        if self.side == 0:
            app.bind('z', self.move_racket)
            app.bind('s', self.move_racket)
        else:
            app.bind('<Up>', self.move_racket)
            app.bind('<Down>', self.move_racket)

        self.victory()

    def move_racket(self, event):
        """Méthode permettant de réaliser le mouvement de la raquette"""

        # Paramétrage de la raquette par rapport aux bords du canvas
        if len(canvas.find_overlapping(0, 0, 900, 0)) == 2:
            self.block_top = True
        else:
            self.block_top = False
        if len(canvas.find_overlapping(0, 600, 900, 600)) == 2:
            self.block_bottom = True
        else:
            self.block_bottom = False

        # Mouvement des raquettes lors de l'appui sur les touches
        if self.block_top == False:
            if repr(event.char) == "'z'":
                canvas.move(player_left, 0, -self.speed_movement_racket)
            if repr(event.char) == "'\\uf700'":
                canvas.move(player_right, 0, -self.speed_movement_racket)
        if self.block_bottom == False:
            if repr(event.char) == "'s'":
                canvas.move(player_left, 0, self.speed_movement_racket)
            if repr(event.char) == "'\\uf701'":
                canvas.move(player_right, 0, self.speed_movement_racket)

    def victory(self):
        if canvas.coords(ball)[0] < 0:
            print('Player Right score 1!')
            app.quit()
        if canvas.coords(ball)[2] > 900:
            print('Player Left score 1!')
            app.quit()


###############################################################################
######################      PRROGRAM EXECUTION      ###########################
##########s#####################################################################

# Création de la fenêtre
app = Tk()
app.title('Project Pong — Thomas Le Naour')
width = 900
height = 600
canvas = Canvas(app, width=width, height=height, bg='black')
line = canvas.create_line(450, 0, 450,  600, fill='white', dash=6)

# Création des éléments graphiques
ball = canvas.create_oval(435, 285, 465, 315, fill='yellow')
player_left = canvas.create_rectangle(10, 240, 20, 360, fill='white')
player_right = canvas.create_rectangle(880, 240, 890, 360, fill='white')

# Initialisation des propriétés
ball_properties = Ball()
ball_properties.move_ball()
player_left_properties = Player(0)
player_right_properties = Player(1)

# Affichage du canvas
canvas.grid()

# Fermeture de la fenêtre
app.mainloop()