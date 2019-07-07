#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:12:34 2019

@author: rodolfopardo
"""
# Un caracol cae en el fondo de un pozo de 125 cm. 
# Cada dia el caracol se eleva 30 cm pero por las noches mientras duerme
# pierde 20 cm porque las paredes están mojadas

#¿Cuántos dias tarda en escapar del fondo? 

#Variables 
pozo = 125
distancia = 0
dias = 0
ganancia = 30
perdida = 20
total = 0

#While

while distancia <= pozo:
    total = ganancia - perdida
    distancia += total
    dias += 1
    #print("Distancia recorrida hasta el momento:", distancia)
    #print("Días recorridos hasta el momento:", dias)
    
#Resultados
print("Al gusano le lleva:", dias, "dias salir del pozo")

#Bonus
#Variables

advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
total = 0
diasrecorridos = 0

#FOR 

for centimetros in advance_cm:
    total += centimetros
    print(total)
    if total <= 125:
         diasrecorridos += 1
        
#Imprimo resultados 
         
print("Le llevo salir del pozo", diasrecorridos, "días")
print("El desplazamiento máximo por día fue de:", max(advance_cm), "centimetros")
print("El desplazamiento mínimo por día fue de:", min(advance_cm), "centimetros")
import statistics 
print("El desplazamiento medio por día fue de:", statistics.mean(advance_cm))
    
print("La desviación standart es de:", statistics.stdev(advance_cm))  
