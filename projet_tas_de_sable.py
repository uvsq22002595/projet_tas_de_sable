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


#################################
#Fonctions

def creation():
    """Cette fonction permet de créer et d'afficher la grille dans la console"""
    RESULT = [[" "," "," "," "," "] for a in range(0,5)]
    for a in range(0, len(RESULT)):
        for b in range(0,len(RESULT)):
            if ((a == 0 or a == 4) and 0 < b < 4) or ((b == 0 or b == 4) and 0 < a < 4):
                RESULT[a][b] = "#"
            if ((0 < a < 4) and 0 < b < 4):
                RESULT[a][b] = randrange(0,10)
    
    return RESULT

def affichage(CADRE):
    """Cette fonction permet d'afficher correctement la grille dans la console"""
    RESULT=""
    for a in CADRE:
        for b in a:
            RESULT+=str(b)
        RESULT+='\n'
    return RESULT

def valeur(CADRE):
    """Cette fonction permet de récupérer uniquement les valeurs de la grille"""
    #print("le cardre", cadre)
    liste_valeur = [[], [], []]
    for a in range(len(CADRE)): 
        for b in range (len(CADRE)):
            if type(CADRE[a][b]) == int :
                liste_valeur[a-1].append(CADRE[a][b])
    return liste_valeur




#######################################
# appel à fonction

A = creation()
print(affichage(A))
print(valeur(A))
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
