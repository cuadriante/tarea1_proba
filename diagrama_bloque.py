import matplotlib.pyplot as plt
import medidas

'''
------------- diagrama de bloques -------------
 funcion de matplotlib: figure
 recibe: array de datos, figsize (ancho, largo) para el tamaño del diagrama
 salida: diagrama de bloques de los datos
'''
figure = plt.figure(figsize =(10, 8))
plt.boxplot(medidas.datos)  
plt.title("Diagrama de bloques para T1")
plt.show()  