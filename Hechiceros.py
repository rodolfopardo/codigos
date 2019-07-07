#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:46:03 2019

@author: rodolfopardo
"""

#Caso 2: enfrentamiento de hechiceros 

#Poderes de cada hechicero

gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

#Variables de ganancia

win_gandalf = []
win_saruman = []
i = 0

#Comienza la batalla 

for hechizo in gandalf:

    if gandalf[i] > saruman[i]:
        win_gandalf.append(gandalf[i])
        print("Ganó Gandalf")
    elif gandalf[i] < saruman[i]:
        win_saruman.append(saruman[i])
        print("Gano Saruman")
    else:
        print("Esto es un empate")
    i += 1

#Se imprimen la cantidad de victorias por hechicero
        
print("El hechicero Gandalf tuvo:", len(win_gandalf), "victorias")
print("El hechicero Saruman tuvo:", len(win_saruman), "victorias")

if len(win_gandalf) > len(win_saruman):
    print("Resultado final: ganador Gandalf")
elif len(win_gandalf) < len(win_saruman):
    print("Resultado final: ganador Saruman")
else:
    print("Fue un justo empate")

#Bonus 
    
power = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalfpw = [50, 40, 40,10, 50, 10, 40, 50, 10, 50] 
           
sarumanpw = [45, 45, 25, 50, 25, 40, 10, 45, 10, 10]
vecesgandal = 0
vecessaruman = 0
i = 0

#while vecesgandal <3 | vecessaruman < 3:
     for hechizo in gandalfpw:
        if gandalfpw[i] > sarumanpw[i]:
            vecesgandal += 1
            print("Gano Gandalf")
        elif gandalfpw[i] < sarumanpw[i]:
            vecessaruman += 1
            print("Gano Saruman")
        else:
            print("Esto es un empate")
        i += 1
        



