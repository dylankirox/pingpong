from tkinter import Tk, Canvas
import random
import time
import sys

class Balle:
    def __init__(self, canvas, raquette, couleur):
        self.canvas = canvas
        self.raquette = raquette
        self.id = canvas.create_oval(1, 1, 25, 25, fill=couleur)
        self.canvas.move(self.id, 245, 100)
        departs = [-20, -19, -18, -17, -16, -15, -14, -13,-12, -11, -10, -9, -8, -7,\
             -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, \
                15, 16, 17, 18, 19, 20]
        random.shuffle(departs)
        self.x = departs[0]
        self.y = -1
        self.hauteur_canevas = self.canvas.winfo_height()
        self.largeur_canevas = self.canvas.winfo_width()
        self.touche_bas = False
        
    def heurter_raquette(self, pos):
        pos_raquette = self.canvas.coords(self.raquette.id)
        if pos[2] >= pos_raquette[0] and pos[0] <= pos_raquette[2]:
            if pos[3] >= pos_raquette[1] and pos[3] <= pos_raquette[3]:
                return True
            return False


    
    def dessiner(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.hauteur_canevas:
            self.touche_bas = True
        if self.heurter_raquette(pos) == True:
            self.y = -1
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.largeur_canevas:
            self.x = -3

class Raquette:
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 300, fill=couleur)
        self.canvas.move(self.id, 500, 500)
        self.x = 0
        self.y = 0
        self.largeur_canevas = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.vers_gauche)
        self.canvas.bind_all('<KeyPress-Right>', self.vers_droite)
        self.canvas.bind_all('<KeyPress-Down>', self.en_haut)
        self.canvas.bind_all('<KeyPress-Up>', self.en_bas)

    def vers_gauche(self, evt):
        self.x = -5

    def vers_droite(self, evt):
        self.x = 5

    def en_haut(self, evt):
        self.y = 5

    def en_bas(self, evt):
        self.y = -5
    def dessiner(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.largeur_canevas:
            pos[2] = self.largeur_canevas-1
            self.x = 0

tk= Tk()
tk.title("Jeu")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1000, height=900, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

raquette = Raquette(canvas,'blue')
balle = Balle(canvas, raquette, 'red')
while 1:
    if balle.touche_bas == False:
        balle.dessiner()
        raquette.dessiner()
    else:
        canvas.create_text(265,200,text="Perdu !", font=('Courier', 50))
        tk.update_idletasks()
        tk.update()
        time.sleep(3)
        sys.exit()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)