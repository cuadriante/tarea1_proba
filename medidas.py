
"""
Tecnológico de Costa Rica
Probabilidad y Estadística
Tarea #1

Adriana Calderón Barboza
Anthony Chaves Achoy
Kenichi Hayakawa Bolaños

"""

import numpy as np
from scipy import stats as st


input_dir = 'C:/Users/adri/PycharmProjects/tarea1_proba/'  # PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename = input_dir + 'energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo)
# se leerá como nan datos = np.genfromtxt(filename, delimiter=';', skip_header=1)
# datos = np.genfromtxt(filename, delimiter=';', skip_header=1, usecols=(5, 5))

datos = np.genfromtxt(filename, delimiter=';', skip_header=1, usecols=(4,))  # usecols = se usa la columna 4



'''
 !!!!!!!!!!! calculo medidas de tendencia !!!!!!!!!!!!
'''

print("------------- medidas de tendencia -------------")

'''
------------- promedio -------------
 funcion de numpy: mean
 recibe: array de datos, tipo de dato
 salida: float64 para resultado del promedio
 nota: se usa float64 para mas precision
'''
promedio = np.mean(datos, dtype=np.float64)
print(" promedio: " + str(promedio))

'''
------------- moda -------------
 funcion de scipy: mode
 recibe: array de datos, keepdims en valor True se usa pra mantener el axis con 
         valor 1 y poder mostrar el resultado correcto
 salida: ndarray con el resultado de las modas (en este caso, solo hay una)
'''
mode_result = st.mode(datos, keepdims=True)
mode = mode_result[0]
print(" moda: " + str(mode))

'''
------------- mediana -------------
 funcion de numpy: median
 recibe: array de datos
 salida:float64 con el resultado de la mediana
'''
mediana = np.median(datos)
print(" mediana: " + str(mediana))

'''
 ------------- quartiles -------------
 funcion de numpy: quantile
 recibe: array de datos, posicion entre 0 y 1 para la partición de los datos, método para
         elegir el dato en caso de que la partición no sea un dato exacto (higher elige el número más alto)
 salida: float64 con el resultado del cuartil segun la particion seleccionada
'''
print(" quartiles: ")
q1 = np.quantile(datos, 0.25, method="higher")
q2 = mediana
q3 = np.quantile(datos, 0.75, method="higher")
print("     q1: " + str(q1))
print("     q2: " + str(q2))
print("     q3: " + str(q3))

''' 
!!!!!!!!!!! calculo medidas de dispersion !!!!!!!!!!!!
'''
print("\n------------- medidas de dispersión -------------")

'''
------------- varianza -------------
 funcion de numpy: var
 recibe: array de datos
 salida: float64 para resultado de la varianza
'''
var = np.var(datos)
print(" varianza: " + str(var))

'''
------------- desviación estándar -------------
 funcion de numpy: std
 recibe: array de datos
 salida: float64 para resultado de la desviación estándar
'''
std = np.std(datos)
print(" desviacion estandar: " + str(std))

'''
------------- coeficiente de variación -------------
 formula: ( desviación estándar / promedio ) * 100
'''
coef = (std / promedio ) * 100
print(" coeficiente de variacion: " + str(coef))

