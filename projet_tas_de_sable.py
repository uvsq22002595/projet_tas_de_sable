#########################################
# groupe MI TD03
# Bertrand Noah 
# Wickramasinghe Adipthya Iduwara
# https://github.com/uvsq-info/l1-python
#########################################

#from tkinter import *
from random import *

#racine = Tk()
#racine.title("Tas de sables")

#################################
#Variables
#HAUTEUR = 600
#LARGEUR = 600
a, b, c, d, e, f, g, h, i = 0, 0, 0, 0, 0, 0, 0, 0, 0

#################################
#Fonctions

def cadrillage_aleatoire():
    tableau_valeur = [a, b, c, d, e, f, g, h, i]
    for j in range (0, 9):
        tableau_valeur[j] = randrange(0, 10)
    


    cadre_0 = [
        [" ", "#", "#", "#", " "],
        ["#", a, b, c, "#"],
        ["#", d, e, f, "#"],
        ["#", g, h, i, "#"],
        [" ", "#", "#", "#", " "]
        ]
    return tableau_valeur
    #print(cadre_0)

def create(tableau_valeur):
    result = [[" "," "," "," "," "] for a in range(0,5)]
    for a in range(0, len(result)):
        for b in range(0,len(result)):
            if ((a == 0 or a == 4) and 0 < b < 4) or ((b == 0 or b == 4) and 0 < a < 4):
                result[a][b] = "#"
            if ((0 < a < 4) and 0 < b < 4):
                result[a][b] = randrange(0,10)
    for z in range(0, len(result)):
        print(result[z])
    
    return result

#######################################
# appel à fonction

cadrillage_aleatoire()
create(cadrillage_aleatoire)


#######################################
# ajout du compteur
#label_counter = Label(racine, text="5", font=("Courrier", 30), bg="#dee5dc")
#label_counter.grid()

#print("\t",Liste_des_valeur[0],  "\n","\t", Liste_des_valeur[1],"\n","\t", Liste_des_valeur[2])

#button1 = Button(racine, text="test")
#button1.grid()

#canvas = Canvas(racine,height=HAUTEUR, width=LARGEUR)
#canvas.grid(column=1,row=0)

#racine.mainloop()
