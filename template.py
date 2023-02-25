# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np

input_dir = 'C:/Users/adri/PycharmProjects/tarea1_proba/'  # PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename = input_dir + 'energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo)
# se leerá como nan datos = np.genfromtxt(filename, delimiter=';', skip_header=1)
# datos = np.genfromtxt(filename, delimiter=';', skip_header=1, usecols=(5, 5))

datos = np.genfromtxt(filename, delimiter=';', skip_header=1, usecols=(4,))  # ocupamos la 4

# alternativamente, se pueden leer columnas específicas entre el rango [X,Y] de esta forma:
# datos=np.genfromtxt(filename,delimiter=',',skip_header=1, usecols = range(5,5))

'''
labels = np.genfromtxt('data.txt', delimiter=',', usecols=0, dtype=str)
raw_data = np.genfromtxt('data.txt', delimiter=',')[:,1:]
data = {label: row for label, row in zip(labels, raw_data)}
'''

print(datos)
# Su código va aquí...
