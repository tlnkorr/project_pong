from tkinter import *


class Game:
    """Classe représentant tous les écrans et paramètres de jeu"""
    
    def __init__(self):
        """Constructeur principal du jeu qui affiche le menu au lancement"""
        global app

        # Définition des variables paramétrables
        self.bg_color = 'black'
        self.ball_color = 'yellow'
        self.racket_color = 'white'
        self.list_colors = ['black', 'white', 'yellow', 'green', 'red', 'purple', 'orange', 'blue']

        # Affichage du menu au lancement
        self.show_menu()

    def show_menu(self):
        """Méthode permettant d'afficher l'écran de menu"""

        # Création des éléments du menu
        self.menu = Frame(app, width=900, height=600, bg=self.bg_color)
        self.menu.grid_propagate(0)
        self.game_name = Label(self.menu, text="YNOV: PROJECT PONG — Thomas Le Naour")
        self.button_play = Button(self.menu, text="PLAY", width=10, height=2, command=self.show_game)
        self.button_parameters = Button(self.menu, text="PARAMETERS", width=10, height=2, command=self.show_parameters)

        # Affichage du menu
        self.game_name.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.button_play.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.button_parameters.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.menu.grid()

    def show_parameters(self):
        """Méthode permettant d'afficher l'écran de paramétrage"""

        self.menu.destroy()

        # Création des élements de l'écran de paramétrage
        self.parameters = Frame(app, width=900, height=600, bg=self.bg_color)
        self.parameters.grid_propagate(0)
        self.button_return = Button(self.parameters, text="Retour", width=5, command=self.switch_parameters_to_menu)
        self.label_parameters = Label(self.parameters, text="PARAMETERS")
        self.label_color_racket = Label(self.parameters, text="Racket color", bg='blue')
        self.label_color_ball = Label(self.parameters, text="Ball color", bg='blue')
        self.label_color_bg = Label(self.parameters, text="Background color", bg='blue')

        # Element couleur des raquettes
        self.list_color_racket = Listbox(self.parameters, width=5)
        for item in self.list_colors:
            self.list_color_racket.insert(END, item)
        self.list_color_racket.bind('<ButtonRelease-1>', self.click_on_item_color_racket)

        # Element couleur de la balle
        self.list_color_ball = Listbox(self.parameters, width=5)
        for item in self.list_colors:
            self.list_color_ball.insert(END, item)
        self.list_color_ball.bind('<ButtonRelease-1>', self.click_on_item_color_ball)

        # Element couleur du background
        self.list_color_bg = Listbox(self.parameters, width=5)
        for item in self.list_colors:
            self.list_color_bg.insert(END, item)
        self.list_color_bg.bind('<ButtonRelease-1>', self.click_on_item_color_bg)

        # Affichage de l'écran de paramétrage
        self.button_return.grid(padx=3, pady=3)
        self.label_parameters.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.label_color_racket.place(rely=0.2)
        self.list_color_racket.place(rely=0.3)

        self.label_color_ball.place(relx=0.2, rely= 0.2)
        self.list_color_ball.place(relx= 0.2, rely=0.3)

        self.label_color_bg.place(relx=0.4, rely= 0.2)
        self.list_color_bg.place(relx= 0.4, rely=0.3)

        self.list_color_bg
        self.parameters.grid()

    def show_game(self):
        """Méthode permettant d'afficher l'écran de jeu"""

        self.menu.destroy()

        # Création des éléments graphiques
        self.canvas = Canvas(app, width=900, height=600, bg=self.bg_color)
        self.line = self.canvas.create_line(450, 0, 450,  600, fill='white', dash=6)
        self.ball = self.canvas.create_oval(435, 285, 465, 315, fill=self.ball_color)
        self.player_left = self.canvas.create_rectangle(10, 240, 20, 360, fill=self.racket_color)
        self.player_right = self.canvas.create_rectangle(880, 240, 890, 360, fill=self.racket_color)

        # Variables de gestion de la vitesse de mouvement de la balle
        self.speed_movement_ball_x = 5
        self.speed_movement_ball_y = 5

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

    def switch_parameters_to_menu(self):
        """Méthode permettant de switcher entre l'écran de paramètres et l'écran de menu"""

        self.parameters.destroy()
        self.show_menu()

    def move_ball(self):
        """Méthode permettant de réaliser le mouvement de la balle et les rebonds
        sur les raquettes"""

        # Paramétrage des rebonds de la balle par rapport au canvas
        if self.canvas.coords(self.ball)[1] < 0 or self.canvas.coords(self.ball)[3] > 600:
            self.speed_movement_ball_y *= -1

        # Paramétrage des rebonds de la balle par rapport aux raquettes
        if len(self.canvas.find_overlapping(self.canvas.coords(self.player_left)[0], self.canvas.coords(self.player_left)[1], self.canvas.coords(self.player_left)[2], self.canvas.coords(self.player_left)[3])) > 1:
            self.speed_movement_ball_x *= -1
        if len(self.canvas.find_overlapping(self.canvas.coords(self.player_right)[0], self.canvas.coords(self.player_right)[1], self.canvas.coords(self.player_right)[2], self.canvas.coords(self.player_right)[3])) > 1:
            self.speed_movement_ball_x *= -1

        # Paramétrage du système de points
        if self.canvas.coords(self.ball)[0] < 0:
            self.canvas.destroy()
            self.show_menu()
        if self.canvas.coords(self.ball)[2] > 900:
            self.canvas.destroy()
            self.show_menu()

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

    def click_on_item_color_racket(self, event):
        index = self.list_color_racket.curselection()
        self.racket_color = self.list_color_racket.get(index)

    def click_on_item_color_ball(self, event):
        index = self.list_color_ball.curselection()
        self.ball_color = self.list_color_ball.get(index)

    def click_on_item_color_bg(self, event):
        index = self.list_color_bg.curselection()
        self.bg_color = self.list_color_bg.get(index)


###############################################################################
######################       PROGRAM EXECUTION      ###########################
###############################################################################

app = Tk()
app.geometry('900x600')
game = Game()
app.mainloop()