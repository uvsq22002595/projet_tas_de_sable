#########################################
# groupe MI TD03
# Bertrand Noah 
# Wickramasinghe Adipthya Iduwara
# https://github.com/uvsq-info/l1-python
#########################################

import tkinter as tk
from random import *

racine = tk.Tk()
racine.title("Tas de sables")

#################################
#Variables
HAUTEUR = 600
LARGEUR = 600
n = 3

#################################
#Fonctions sans parties graphique

def creation(x, y):
    """Cette fonction permet de créer et d'afficher la grille dans la console"""

    RESULT = [[" " for a in range(x)]for b in range(y)]
    for a in range(y):
        for b in range(x):
            
            if ((a == 0 or a == y-1) and 0 < b < x-1) or ((b == 0 or b == x-1) and 0 < a < y-1):
                RESULT[a][b] = "#"
            if ((0 < a < y-1) and 0 < b < x-1):
                RESULT[a][b] = randrange(0,10)
    
    return RESULT, x, y

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
    LISTE_VALEUR = []
    for a in range (len(CADRE)):
        LISTE_VALEUR.append([])
        for b in range (len(CADRE[a])):
            if type(CADRE[a][b]) == int:
                print(CADRE[a][b])
                LISTE_VALEUR[a].append(CADRE[a][b])
    LISTE_VALEUR.remove(LISTE_VALEUR[0])
    LISTE_VALEUR.remove(LISTE_VALEUR[-1])
    """for a in CADRE: 
        for b in a:
            if type(b) == int :
                LISTE_VALEUR.append(b)"""
    return LISTE_VALEUR

def avalanche(LISTE):
    CADRE = LISTE[0]
    print("init\n" + affichage(CADRE))
    test = True
    result = CADRE
    while test == True:
        for a in range(LISTE[2]):
            for b in range(LISTE[1]):
                if type(CADRE[a][b]) == int and CADRE[a][b]>3:
                    result[a][b] -= 4
                    if CADRE[a-1][b] != "#":
                        result[a-1][b] += 1
                    if CADRE[a+1][b] != "#":
                        result[a+1][b] += 1
                    if CADRE[a][b-1] != "#":
                        result[a][b-1] += 1
                    if CADRE[a][b+1] != "#":
                        result[a][b+1] += 1
        print(affichage(result))
        cadre = result
        n = valeur(CADRE)
        test = False
        for c in range(4,10):
            if c in n:
                test = True
        print(test)
    return result

#######################################
# appel à fonction
#print(creation(5, 5))
#print(affichage(creation(5, 5)[0]))
#print(valeur(creation(5, 5)[0]))
#print(avalanche(creation(5, 5)))
#######################################
# fonctions parties graphique

def grillage(n):
    largeur_case = LARGEUR // n
    hauteur_case = HAUTEUR // n
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 0:
                color = "gray80"
                
                
            else:
                color = "black"
            #TEXT = str(valeur(creation(5, 5)))
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)
            canvas.create_text(75, 75, fill = "red", text = str(valeur(creation(5, 5)[0]))) #il faut ajouter du texte pour chaque case

#print("\t",Liste_des_valeur[0],  "\n","\t", Liste_des_valeur[1],"\n","\t", Liste_des_valeur[2])

bouton = tk.Button(racine, text = "quitter", fg = "black", command = racine.quit, activebackground = "blue", borderwidth=2, bg = "green")
bouton.grid(column = 1, row = 3)

canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR)
canvas.grid(column = 1, row = 1)

bouton_run = tk.Button(racine, text = "Lancer le programme", fg = "black", command = lambda : grillage(n), activebackground = "blue", borderwidth=2, bg = "green")
bouton_run.grid(column = 1, row = 2)
#grillage(3)
#canvas.grid_bbox(column=0, row=0, col2=300, row2=300)


"""canvas2 = tk.Canvas(racine, bg = "blue")
canvas2.grid(column = 1,row = 0)"""

racine.mainloop()