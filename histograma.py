
import matplotlib.pyplot as plt
import medidas

'''
------------- histograma -------------
 funcion de matplotlib: hist
 recibe: array de datos, numero de divisiones del histograma, color de barras
 salida: histograma de los datos
'''
num_bins = 10
n, bins, patches = plt.hist(medidas.datos, num_bins, facecolor='blue', alpha=0.5)
plt.xlabel('T1')
plt.ylabel('Cantidad')
plt.title(r'Histograma de T1')
plt.show()