from tkinter import Tk, Canvas, PhotoImage
import random
import time
import copy

class Jeu:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("M.Filiforme court vers la sortie")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, \
            highlightthicknes=0)
        self.canvas.pack()
        self.tk.update()
        self.hauteur_canevas = 500
        self.largeur_canevas = 500
        self.ap = PhotoImage(file='Filiforme/arriere-plan.gif')
        larg = self.ap.width()
        haut = self.ap.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * larg, y * haut, \
                    image=self.ap, anchor='nw')
        self.lutins = []
        self.enfonction = True

    def boucle_principale(self):
        while 1:
            if self.enfonction == True:
                for lutin in self.lutins:
                    lutin.deplacer()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)
class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def dans_x(self, co1, co2):
        if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
                or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
                or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
                or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
            return True
        else:
            return False 
    def dans_y(self, co1, co2):
        if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
                or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
                or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
                or (co2.y2 > co1.y1 and co2.y2 < co1.y1):
            return True
        else:
            return False
        
    def collision_gauche(self, co1, co2):
        if self.dans_y(co1, co2):
            if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
                return True
        return False
    
    def collision_haut(self, co1, co2):
        if self.dans_x(co1, co2):
            if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
                return True
        return False
    
    def collision_bas(self, y, co1, co2):
        if self.dans_x(co1, co2):
            y_calc = co1.y2 + y
            if y_calc >= co2.y1 and y_calc <=co2.y2:
                return True
        return False
class Lutin:
    def __init__(self, jeu):
        self.jeu = jeu
        self.finjeu = False
        self.coordonees = None
    def deplacer(self):
        pass
    def coords(self):
        return self.coordonees
class LutinPlateForme(Lutin):
    def __init__(self, jeu, image_photo, x, y, largeur, hauteur):
        Lutin.__init__(self, jeu)
        self.image_photo = image_photo
        self.image = jeu.canvas.create_image(x, y, \
            image=self.image_photo, anchor='nw')
        self.coordonees = Coords(x, y, x + largeur, y + hauteur)

jeu = Jeu()
plateforme1 = LutinPlateForme(jeu, PhotoImage(\
    file="/home/vincent/Filiforme/Plateformes/Sans titre3.gif"), 0, 480, 100, 10)
plateforme2 = LutinPlateForme\
    (jeu, PhotoImage(file="/home/vincent/Filiforme/Plateformes/Sans titre3.gif"), 150, 440, 100, 10)
plateforme3 = LutinPlateForme(jeu, PhotoImage(\
    file="/home/vincent/Filiforme/Plateformes/Sans titre3.gif"), 300, 400, 100, 10)
plateforme4 = LutinPlateForme(jeu, PhotoImage(\
    file="/home/vincent/Filiforme/Plateformes/Sans titre3.gif"), 300, 160, 100, 10)
plateforme5 = LutinPlateForme(jeu, PhotoImage(\
    file="/home/vincent/Filiforme/Plateformes/Sans titre3.gif"), 300, 160, 100, 10)
jeu.lutins.append(plateforme1)
jeu.lutins.append(plateforme2)
jeu.lutins.append(plateforme3)
jeu.lutins.append(plateforme4)
jeu.boucle_principale()
