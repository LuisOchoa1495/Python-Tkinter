import matplotlib.pyplot as plt
years = [2020,2021, 2022, 2023]
sales_millions = [14, 18, 23, 32]
plt.title("GRAFICO DE LINEA")
plt.plot(years, sales_millions, color='blue', linewidth=3, label='línea')
plt.legend()
plt.show()