#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:33:10 2019

@author: rodolfopardo
"""

# Variables

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

# Robin Hood is famous for hitting an arrow with another arrow. Did you get it? 

robin_hood = [x for n, x in enumerate(points) if x in points[:n]]

print("Robin Hood lanzó las siguientes flechas:", robin_hood)

#Calculate how many arrows have fallen in each quadrant. 

print(points[0][0])
q1 = 0
q2 = 0
q3 = 0
q4 = 0    
for x,y in points:
    if x > 0 and y > 0:
        print("Pertenece a caudrante 1")
        q1 += 1
    elif x > 0 and y < 0:
        print("Pertenece a cuadrante 2")
        q2 += 1
    elif x < 0 and y < 0:
        print("Pertenece a cuadrante 3")
        q3 += 1
    else:
        print("Pertecene a cuadrante 4")
        q4 += 1
        
print("Cantidad en cuadrante 1:", q1)
print("Cantidad en cuadrante 2:", q2)
print("Cantidad en cuadrante 3:", q3)   
print("Cantidad en cuadrante 4:", q4)

#Find the point closest to the center. Calculate its distance to the center


from scipy.spatial import distance
print(distance.cdist(points, points, "euclidean"))

centroide = (sum(points[0])/len(points[0]),sum(points[1])/len(points[1]))

# 4. If the target has a radius of 9, calculate the number of arrows that 
# must be picked up in the forest.    
        