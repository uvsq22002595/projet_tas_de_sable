#########################################
# groupe MI TD03
# Bertrand Noah 
# Wickramasinghe Adipthya Iduwara
# https://github.com/uvsq-info/l1-python
#########################################

from tkinter import *

racine = Tk()
racine.title("Tas de sables")

#################################
#Variables
HAUTEUR = 600
LARGEUR = 600


def tableau():
    liste = []
    for i in range (0, 10):
        for j in range (0, 10):
            liste.append(j, i)
    print(liste)

#######################################
# ajout du compteur
label_counter = Label(racine, text="5", font=("Courrier", 30), bg="#dee5dc")
label_counter.grid()

#print("\t",Liste_des_valeur[0],  "\n","\t", Liste_des_valeur[1],"\n","\t", Liste_des_valeur[2])

button1 = Button(racine, text="test")


button1.grid()


canvas = Canvas(racine,height=HAUTEUR, width=LARGEUR)
canvas.grid(column=1,row=0)

racine.mainloop()
