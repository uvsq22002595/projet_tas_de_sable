#########################################
# groupe MI TD03
# Bertrand Noah 
# Wickramasinghe Adipthya Iduwara
# https://github.com/uvsq-info/l1-python
#########################################

import tkinter as tk

HAUTEUR = 600
LARGEUR = 600

racine = tk.Tk()
racine.title("Tas de sables")
canvas = tk.Canvas(racine,height=HAUTEUR, width=LARGEUR)
canvas.grid(column=1,row=0)


racine.mainloop()
