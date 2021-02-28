from tkinter import Tk, Canvas
import random
import time

class Jeu:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("M.Filiforme court vers la sortie")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-tomopost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, \
            highlightthicknes=0)
        self.canvas.pack()
        self.tk.update()
        self.hauteur_canevas = 500
        self.largeur_canevas = 500
        