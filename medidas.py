# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt

input_dir = 'C:/Users/adri/PycharmProjects/tarea1_proba/'  # PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename = input_dir + 'energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo)
# se leerá como nan datos = np.genfromtxt(filename, delimiter=';', skip_header=1)
# datos = np.genfromtxt(filename, delimiter=';', skip_header=1, usecols=(5, 5))

datos = np.genfromtxt(filename, delimiter=';', skip_header=1, usecols=(4,))  # ocupamos la 4

# alternativamente, se pueden leer columnas específicas entre el rango [X,Y] de esta forma:
# datos=np.genfromtxt(filename,delimiter=',',skip_header=1, usecols = range(5,5))

print(datos)
# Su código va aquí...

# !!!!!!!!!!! calculo medidas de tendencia !!!!!!!!!!!!
print("------------- medidas de tendencia -------------")

# ------------- promedio -------------
# funcion de numpy: mean
# recibe: array de datos, tipo de dato
# se usa float64 para mas precision
promedio = np.mean(datos, dtype=np.float64)
print(" promedio: " + str(promedio))

# moda
mode_result = st.mode(datos, keepdims=True)
mode = mode_result[0]
print(" moda: " + str(mode))

# ------------- mediana -------------
# funcion de numpy: median
# recibe: array de datos
mediana = np.median(datos)
print(" mediana: " + str(mediana))

# quartiles
print(" quartiles: ")
q1 = np.quantile(datos, 0.25, method="higher")
q2 = mediana
q3 = np.quantile(datos, 0.75, method="higher")
print("     q1: " + str(q1))
print("     q2: " + str(q2))
print("     q3: " + str(q3))

# calculo medidas de dispersion
print("\n------------- medidas de dispersión -------------")

# varianza
var = np.var(datos)
print(" varianza: " + str(var))

# desviacion estandar
std = np.std(datos)
print(" desviacion estandar: " + str(std))

# coeficiente de variacion
coef = std / promedio
print(" coeficiente de variacion: " + str(coef))

