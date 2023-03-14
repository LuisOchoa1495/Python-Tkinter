#Libreria
import matplotlib.pyplot as plt

#Definimos los datos
years = [2019,2020, 2021, 2022]
sales_a = [14, 18, 23, 32]
sales_b = [11, 12, 26, 35]

#Configurar las características del gráfico
plt.plot(years, sales_a, color='blue', linewidth=3, label='EMPRESA A')
plt.plot(years, sales_b, color='red', linewidth=3, label='EMPRESA B')

#Definir título y nombres de ejes
plt.title("DIAGRAMA DE LINEA")
plt.ylabel('Sales')
plt.xlabel('Years')
#plt.xticks(years)

#Mostrar leyenda, cuadrícula y figura
plt.legend() # loc='upper left' upper center ,lower center
plt.grid()
plt.show()
