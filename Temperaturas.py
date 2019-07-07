#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:36:19 2019

@author: rodolfopardo
"""

# import
import matplotlib.pyplot as plt
%matplotlib inline

# axis x, axis y
y = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]
x = list(range(len(y)))

# plot
plt.plot(x, y)
plt.axhline(y=70, linewidth=1, color='r')
plt.xlabel('hours')
plt.ylabel('Temperature ºC')
plt.title('Temperatures of our server throughout the day')

# assign a variable to the list of temperatures

# 1. Calculate the minimum of the list and print the value using print()

print("El valor mínimo fue de:", min(y))

# 2. Calculate the maximum of the list and print the value using print()

print("El valor máximo fue de:", max(y))

# 3. Items in the list that are greater than 70ºC and print the result

for valores in y:
    if valores > 70:
        print(valores)
    else:
        print("Valor por debajo de 70º")

# 4. Calculate the mean temperature throughout the day and print the result

promedio = sum(y) / len(y)
print("El promedio de temperaturas fue de:",promedio)

# 5.1 Solve the fault in the sensor by estimating a value

variable03 = y[2]+y[3]/2
y[3] = int(variable03)



# 5.2 Update of the estimated value at 03:00 on the list

print(y)

# Bonus: convert the list of ºC to ºFarenheit Formula: F = 1.8 * C + 32
yFar = []
variable1 = 0

for valores in y: 
    variable1 = 1.8 * valores + 32
    yFar.append(variable1)
    
print("Estas son las temperaturas en F para Estados Unidos:", yFar)

