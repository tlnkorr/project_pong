#############################################################
####  PROJECT 2 — PONG GAME                    ##############
####  Thomas Le Naour — Ynov Informatique B1A  ##############
#############################################################

from tkinter import *
import time


class Game:
    """Classe représentant tous les écrans et paramètres de jeu"""
    
    def __init__(self):
        """Constructeur principal du jeu qui affiche le menu au lancement"""
        global app

        # Définition des variables paramétrables
        self.bg_color = 'black'
        self.ball_color = 'yellow'
        self.racket_color = 'white'
        self.speed_movement_ball_x = 5
        self.speed_movement_ball_y = 5
        self.winning_points = 1
        self.list_colors = ['black', 'white', 'yellow', 'green', 'red', 'purple', 'orange', 'blue', 'pink']

        # Définition des variables des scores de chaque joueur
        self.score_left = 0
        self.score_right = 0

        # Affichage du menu au lancement
        self.show_menu()

    def show_menu(self):
        """Méthode permettant d'afficher l'écran de menu"""

        # Création des éléments du menu
        self.menu = Frame(app, width=900, height=600, bg=self.bg_color)
        self.game_name = Label(self.menu, text="YNOV: PROJECT PONG — Thomas Le Naour")
        self.button_play = Button(self.menu, text="PLAY", width=10, height=2, command=self.switch_menu_to_game)
        self.button_parameters = Button(self.menu, text="PARAMETERS", width=10, height=2, command=self.switch_menu_to_parameters)
        self.button_quit = Button(self.menu, text="Quit", command=app.quit)

        # Affichage du menu
        self.game_name.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.button_play.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.button_parameters.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.button_quit.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.menu.grid()

    def show_parameters(self):
        """Méthode permettant d'afficher l'écran de paramétrage"""

        # Création des élements de l'écran de paramétrage
        self.parameters = Frame(app, width=900, height=600, bg=self.bg_color)
        self.parameters.grid_propagate(0)
        self.button_return = Button(self.parameters, text="Back", width=5, command=self.switch_parameters_to_menu)
        self.label_parameters = Label(self.parameters, text="PARAMETERS")
        self.label_color_racket = Label(self.parameters, text="Racket color", bg='blue')
        self.label_color_ball = Label(self.parameters, text="Ball color", bg='blue')
        self.label_color_bg = Label(self.parameters, text="Background color", bg='blue')
        self.label_speed_ball = Label(self.parameters, text="Speed ball", bg='blue')
        self.label_winning_points = Label(self.parameters, text="Number of winning points", bg='blue')
        self.label_text_info = Label(self.parameters, text="Press Back to save parameters")

        # Element couleur des raquettes
        self.list_color_racket = Listbox(self.parameters, width=5)
        for item in self.list_colors:
            self.list_color_racket.insert(END, item)
        self.list_color_racket.bind('<ButtonRelease-1>', self.change_color_racket)

        # Element couleur de la balle
        self.list_color_ball = Listbox(self.parameters, width=5)
        for item in self.list_colors:
            self.list_color_ball.insert(END, item)
        self.list_color_ball.bind('<ButtonRelease-1>', self.change_color_ball)

        # Element couleur du background
        self.list_color_bg = Listbox(self.parameters, width=5)
        for item in self.list_colors:
            self.list_color_bg.insert(END, item)
        self.list_color_bg.bind('<ButtonRelease-1>', self.change_color_bg)

        # Element vitesse de la balle
        self.scale = Scale(self.parameters, orient=HORIZONTAL, from_=1, to=10, resolution=1, command=self.change_speed_ball)
        self.scale.set(self.speed_movement_ball_x)

        # Element nombre de points gagnants
        self.scale_points = Scale(self.parameters, orient=HORIZONTAL, from_=1, to=10, resolution=1, command=self.change_winning_points)
        self.scale_points.set(self.winning_points)

        # Affichage de l'écran de paramétrage
        self.button_return.grid(padx=3, pady=3)
        self.label_parameters.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.label_color_racket.place(rely=0.2)
        self.list_color_racket.place(rely=0.3)

        self.label_color_ball.place(relx=0.2, rely= 0.2)
        self.list_color_ball.place(relx= 0.2, rely=0.3)

        self.label_color_bg.place(relx=0.4, rely= 0.2)
        self.list_color_bg.place(relx= 0.4, rely=0.3)

        self.label_speed_ball.place(relx=0.6, rely=0.2)
        self.scale.place(relx=0.6, rely=0.3)

        self.label_winning_points.place(relx=0.8, rely=0.2)
        self.scale_points.place(relx=0.8, rely=0.3)

        self.label_text_info.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.parameters.grid()

    def show_game(self):
        """Méthode permettant d'afficher l'écran de jeu"""
            
        # Création des éléments graphiques
        self.canvas = Canvas(app, width=900, height=600, bg=self.bg_color)
        self.line = self.canvas.create_line(450, 0, 450,  600, fill='white', dash=6)
        self.ball = self.canvas.create_oval(435, 285, 465, 315, fill=self.ball_color)
        self.player_left = self.canvas.create_rectangle(10, 240, 20, 360, fill=self.racket_color)
        self.player_right = self.canvas.create_rectangle(880, 240, 890, 360, fill=self.racket_color)

        # Variable de gestions des mouvements des raquettes
        self.speed_movement_racket = 30
        self.block_racket_left_top = False
        self.block_racket_right_top = False
        self.block_racket_left_bottom = False
        self.block_racket_right_bottom = False

        # Initiliasation des mouvements de la raquette lors de l'appui sur les touches
        app.bind('z', self.move_racket)
        app.bind('s', self.move_racket)
        app.bind('<Up>', self.move_racket)
        app.bind('<Down>', self.move_racket)

        # Initialisation du mouvement de la balle
        self.move_ball()

        # Affichage du jeu
        self.canvas.grid()

    def show_victory(self, side):
        """Méthode permettant d'afficher la page de victoire à la fin de la
        partie en fonction du côté gagnant :
        - 0 pour le joueur gauche 
        - 1 pour le joueur droite"""

        self.now = round(time.time() - self.now_start, 2)

        if side == 0:
            self.winner = 'RIGHT'
        else:
            self.winner = 'LEFT'

        # Création des éléments graphiques
        self.victory = Frame(app, width=900, height=600, bg=self.bg_color)
        self.label_victory = Label(self.victory, text=f"PLAYER {self.winner} WIN in {self.now} seconds", bg='red')
        self.scores = Label(self.victory, text=f'{self.score_left} - {self.score_right}')
        self.button_menu = Button(self.victory, text="Menu", command=self.switch_victory_to_menu)
        self.button_replay = Button(self.victory, text="Replay", command=self.switch_victory_to_game)

        # Affichage de la page de victoire
        self.label_victory.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.scores.place(relx=0.5, rely= 0.5, anchor=CENTER)
        self.button_menu.place(relx=0.4, rely= 0.7, anchor=CENTER)
        self.button_replay.place(relx=0.6, rely= 0.7, anchor=CENTER)
        self.victory.grid()

    def switch_parameters_to_menu(self):
        """Méthode permettant de switcher entre l'écran de paramètres et l'écran de menu"""

        self.parameters.destroy()
        self.show_menu()

    def switch_menu_to_game(self):
        """Méthode permettant de switcher entre l'écran de menu et l'écran de jeu"""

        self.menu.destroy()
        self.show_game()
        self.now_start = time.time()

    def switch_menu_to_parameters(self):
        """Méthode permettant de switcher entre l'écran de menu et l'écran de paramètres"""

        self.menu.destroy()
        self.show_parameters()

    def switch_victory_to_menu(self):
        """Méthode permettant de switcher entre l'écran de menu et l'écran de paramètres"""

        self.victory.destroy()
        self.score_left = 0
        self.score_right = 0
        self.now_start = 0
        self.show_menu()

    def switch_victory_to_game(self):
        """Méthode permettant de switcher entre l'écran de menu et l'écran de paramètres"""

        self.victory.destroy()
        self.score_left = 0
        self.score_right = 0
        self.now_start = time.time()
        self.now = 0
        self.show_game()

    def move_ball(self):
        """Méthode permettant de réaliser le mouvement de la balle, les rebonds
        sur les raquettes et les bords et le système de point"""

        # Paramétrage des rebonds de la balle par rapport au canvas
        if self.canvas.coords(self.ball)[1] < 0 or self.canvas.coords(self.ball)[3] > 600:
            self.speed_movement_ball_y *= -1

        # Paramétrage des rebonds de la balle par rapport aux raquettes
        if len(self.canvas.find_overlapping(self.canvas.coords(self.player_left)[0], \
        self.canvas.coords(self.player_left)[1], self.canvas.coords(self.player_left)[2], \
        self.canvas.coords(self.player_left)[3])) > 1:
            self.speed_movement_ball_x *= -1
        if len(self.canvas.find_overlapping(self.canvas.coords(self.player_right)[0], \
        self.canvas.coords(self.player_right)[1], self.canvas.coords(self.player_right)[2], \
        self.canvas.coords(self.player_right)[3])) > 1:
            self.speed_movement_ball_x *= -1

        # Paramétrage du système de points
        if self.canvas.coords(self.ball)[0] < 0:
            self.score_right += 1
            self.canvas.destroy()

            if self.score_right == self.winning_points:
                self.show_victory(0)
            else:
                return self.show_game()

        if self.canvas.coords(self.ball)[2] > 900:
            self.score_left += 1
            self.canvas.destroy()

            if self.score_left == self.winning_points:
                self.show_victory(1)
            else:
                return self.show_game()

        # Mouvement perpetuel de la balle
        self.canvas.move(self.ball, self.speed_movement_ball_x, self.speed_movement_ball_y)
        app.after(20, self.move_ball)
    
    def move_racket(self, event):
        """Méthode permettant de réaliser le mouvement de la raquette"""

        # Paramétrage de la raquette par rapport aux bords du canvas
        if len(self.canvas.find_overlapping(0, 0, 100, 0)) == 1:
            self.block_racket_left_top = True
        else:
            self.block_racket_left_top = False
        if len(self.canvas.find_overlapping(900, 0, 800, 0)) == 1:
            self.block_racket_right_top = True
        else:
            self.block_racket_right_top = False

        if len(self.canvas.find_overlapping(0, 600, 100, 600)) == 1:
            self.block_racket_left_bottom = True
        else:
            self.block_racket_left_bottom = False
        if len(self.canvas.find_overlapping(900, 600, 800, 600)) == 1:
            self.block_racket_right_bottom = True
        else:
            self.block_racket_right_bottom = False

        # Mouvement des raquettes lors de l'appui sur les touches
        if self.block_racket_left_top == False:
            if repr(event.char) == "'z'":
                self.canvas.move(self.player_left, 0, -self.speed_movement_racket)
        if self.block_racket_right_top == False:
            if repr(event.char) == "'\\uf700'":
                self.canvas.move(self.player_right, 0, -self.speed_movement_racket)
        if self.block_racket_left_bottom == False:
            if repr(event.char) == "'s'":
                self.canvas.move(self.player_left, 0, self.speed_movement_racket)
        if self.block_racket_right_bottom == False:
            if repr(event.char) == "'\\uf701'":
                self.canvas.move(self.player_right, 0, self.speed_movement_racket)

    def change_color_racket(self, event):
        """Méthode permettant de changer la couleur de la raquette"""

        self.index = self.list_color_racket.curselection()
        self.racket_color = self.list_color_racket.get(self.index)

    def change_color_ball(self, event):
        """Méthode permettant de changer la couleur de la balle"""

        self.index = self.list_color_ball.curselection()
        self.ball_color = self.list_color_ball.get(self.index)

    def change_color_bg(self, event):
        """Méthode permettant de changer la couleur du background"""
        
        self.index = self.list_color_bg.curselection()
        self.bg_color = self.list_color_bg.get(self.index)

    def change_speed_ball(self, event):
        """Méthode permettant de changer la vitesse de la balle"""

        self.speed_movement_ball_x = int(event)
        self.speed_movement_ball_y = int(event)

    def change_winning_points(self, event):
        """Méthode permettant de changer le nombre de points gagnants"""

        self.winning_points = int(event)


#############################################################
####  PROGRAM EXECUTION  ####################################
#############################################################

if __name__ == "__main__":
    app = Tk()
    app.geometry('900x600')
    game = Game()
    app.mainloop()