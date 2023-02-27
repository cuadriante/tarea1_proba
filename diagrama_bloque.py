import matplotlib.pyplot as plt  
import numpy as np  
import medidas

figure = plt.figure(figsize =(10, 8))  

plt.boxplot(medidas.datos)  
plt.title("Diagrama de bloques para T1")
plt.show()  