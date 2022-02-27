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

def creation(n):
    """Cette fonction permet de créer et d'afficher la grille dans la console"""

    RESULT = [[" " for a in range(n+2)]for b in range(n+2)]
    for a in range(n + 2):
        for b in range(n + 2):
            
            if ((a == 0 or a == n+1) and 0 < b < n+1) or ((b == 0 or b == n+1) and 0 < a < n+1):
                RESULT[a][b] = "#"
            if ((0 < a < n+1) and 0 < b < n+1):
                RESULT[a][b] = randrange(0,10)
    
    return RESULT

def affichage(CADRE):
    """Cette fonction permet d'afficher correctement la grille dans la console"""
    RESULT=""
    #CADRE = CADRE[0]
    for a in CADRE:
        for b in a:
            RESULT+=str(b)
        RESULT+='\n'
    return RESULT

def valeur(CADRE):
    """Cette fonction permet de récupérer uniquement les valeurs de la grille"""
    LISTE_VALEUR = []
    #CADRE = CADRE[0]
    for a in range (len(CADRE)):
        LISTE_VALEUR.append([])
        for b in range (len(CADRE[a])):
            #print("valeur de b", b)
            if type(CADRE[a][b]) == int:
                #print(CADRE[a][b])
                LISTE_VALEUR[a].append(CADRE[a][b])
    LISTE_VALEUR.remove(LISTE_VALEUR[0])
    LISTE_VALEUR.remove(LISTE_VALEUR[-1])
    """for a in CADRE: 
        for b in a:
            if type(b) == int :
                LISTE_VALEUR.append(b)"""
    return LISTE_VALEUR

"""def avalanche(LISTE):
    Cette fonction permet de déclancher l'avalanche et donc de faire tourner le programme
    CADRE = LISTE[0]
    print(LISTE)
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
        print( "affichage : ", affichage(result))
        cadre = result
        n = valeur(CADRE)
        test = False
        for c in range(4, 10):
            for d in n:
                for e in d:
                    if e == c:
                        test = True
    return result"""

def avalanche(LISTE):
    """Cette fonction permet de déclancher l'avalanche et donc de faire tourner le programme"""
    CADRE = LISTE
    print("la liste est : ",CADRE)
    print("init\n" + affichage(CADRE))
    test = True
    result = CADRE
    while test == True:
        for a in range(len(CADRE)):
            for b in range(len(CADRE)):
                #print( "cardre_a_B : ",CADRE[a][b])
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
        #print(" result : ", result)
        cadre = result
        n = valeur(CADRE)
        test = False
        for c in range(4, 10):
            for d in n:
                for e in d:
                    if e == c:
                        test = True
    #print("dernier result : ", result)
    return result

#######################################
# appel à fonction
#print(creation(n))
#
#print(affichage(creation(n)))
#print(valeur(creation(n)))
#print(avalanche(creation(n)))
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
            #il faut ajouter du texte pour chaque case

def affichage_valeurs(CADRE, n):
    
    largeur_case = LARGEUR // n
    hauteur_case = HAUTEUR // n
    emplacement_x = largeur_case // 2
    emplacement_y = hauteur_case // 2
    for a in CADRE:
        for b in a:
            canvas.create_text(emplacement_x, emplacement_y, fill = "red", text = str(b))
            emplacement_x += largeur_case 
        emplacement_x = largeur_case // 2
        emplacement_y += hauteur_case 

def avalanche_graphique(CADRE):
    """Cette fonction permet d'effectuer toutes les avalanches """
    New_CADRE = avalanche(CADRE)
    grillage(n)
    affichage_valeurs(valeur(New_CADRE), n)

    

##############################@
#variable partie graphique
CADRE_0 = creation(n)
CADRE = valeur(CADRE_0)

##############################
#code partie graphique

bouton = tk.Button(racine, text = "quitter", fg = "black", command = racine.quit, activebackground = "blue", borderwidth=2, bg = "green")
bouton.grid(column = 1, row = 3)

canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR)
canvas.grid(column = 1, row = 1)

bouton_cadre = tk.Button(racine, text = "Créer le cadre", fg = "black", command = lambda : grillage(n), activebackground = "blue", borderwidth=2, bg = "green")
bouton_cadre.grid(column = 1, row = 2)

bouton_affichage = tk.Button(racine, text = "Affichage des valeurs", fg = "black", command = lambda : affichage_valeurs(CADRE,n), activebackground = "blue", borderwidth=2, bg = "green")
bouton_affichage.grid(column = 0, row = 1)

bouton_avalanche = tk.Button(racine, text = "déclencher une avalenche", fg = "black", command = lambda : avalanche_graphique(CADRE_0), activebackground = "blue", borderwidth=2, bg = "green")
bouton_avalanche.grid(column = 0, row = 2)

racine.mainloop()