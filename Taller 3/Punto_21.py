import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv('titanic.csv')

# a) Diagrama de sectores con los fallecidos y supervivientes
# Contamos el número de supervivientes (1) y fallecidos (0) usando value_counts()
conteo_survivientes = df['Survived'].value_counts()

# Creamos un diagrama de sectores para visualizar la proporción de supervivientes y fallecidos
plt.figure(figsize=(8, 6))  # Configuramos el tamaño de la figura
plt.pie(conteo_survivientes, 
        labels=['Fallecidos', 'Sobrevivientes'],  # Etiquetas para las porciones del diagrama
        autopct='%1.1f%%',  # Porcentaje con un decimal en cada porción
        colors=['red', 'green'])  # Colores para cada porción
plt.title('Diagrama de Sectores: Fallecidos vs Supervivientes')  # Título del gráfico
plt.show()  # Mostramos el gráfico

# b) Histograma con las edades
# Creamos un histograma para visualizar la distribución de edades, excluyendo valores NaN
plt.figure(figsize=(8, 6))  # Configuramos el tamaño de la figura
plt.hist(df['Age'].dropna(),  # Eliminamos valores NaN antes de crear el histograma
         bins=30,  # Número de bins o intervalos en el histograma
         color='skyblue',  # Color de las barras
         edgecolor='black')  # Color del borde de las barras
plt.title('Histograma de Edades')  # Título del gráfico
plt.xlabel('Edad')  # Etiqueta del eje X
plt.ylabel('Número de Pasajeros')  # Etiqueta del eje Y
plt.grid(True)  # Activamos la cuadrícula
plt.show()  # Mostramos el gráfico

# c) Diagrama de barras con el número de personas en cada clase
# Contamos el número de personas en cada clase y ordenamos los resultados
conteo_clases = df['Pclass'].value_counts().sort_index()

# Creamos un diagrama de barras para visualizar el número de personas en cada clase
plt.figure(figsize=(8, 6))  # Configuramos el tamaño de la figura
plt.bar(conteo_clases.index,  # Índices de las barras (clases)
        conteo_clases.values,  # Altura de las barras (conteo de personas)
        color='lightcoral',  # Color de las barras
        edgecolor='black')  # Color del borde de las barras
plt.title('Número de Personas en Cada Clase')  # Título del gráfico
plt.xlabel('Clase')  # Etiqueta del eje X
plt.ylabel('Número de Pasajeros')  # Etiqueta del eje Y
plt.xticks([1, 2, 3], ['Primera', 'Segunda', 'Tercera'])  # Etiquetas de las clases en el eje X
plt.grid(True, axis='y')  # Activamos la cuadrícula solo en el eje Y
plt.show()  # Mostramos el gráfico

# d) Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase
# Contamos el número de fallecidos y supervivientes en cada clase
conteo_clases_survival = df.groupby(['Pclass', 'Survived']).size().unstack().fillna(0)

# Creamos un diagrama de barras apiladas para visualizar el número de fallecidos y supervivientes en cada clase
plt.figure(figsize=(8, 6))  # Configuramos el tamaño de la figura
conteo_clases_survival.plot(kind='bar',  # Tipo de gráfico: barras
                            stacked=True,  # Apilamos las barras
                            color=['red', 'green'],  # Colores para cada categoría
                            edgecolor='black')  # Color del borde de las barras
plt.title('Número de Personas Fallecidas y Sobrevivientes en Cada Clase')  # Título del gráfico
plt.xlabel('Clase')  # Etiqueta del eje X
plt.ylabel('Número de Pasajeros')  # Etiqueta del eje Y
plt.xticks([0, 1, 2], ['Primera', 'Segunda', 'Tercera'], rotation=0)  # Etiquetas de las clases en el eje X
plt.legend(['Fallecidos', 'Sobrevivientes'])  # Leyenda para las categorías
plt.grid(True, axis='y')  # Activamos la cuadrícula solo en el eje Y
plt.show()  # Mostramos el gráfico

# e) Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase
# Calculamos los números acumulados de fallecidos y supervivientes en cada clase
conteo_clases_acumulado = conteo_clases_survival.cumsum()

# Creamos un diagrama de barras apiladas para visualizar el número acumulado de fallecidos y supervivientes en cada clase
plt.figure(figsize=(8, 6))  # Configuramos el tamaño de la figura
conteo_clases_acumulado.plot(kind='bar',  # Tipo de gráfico: barras
                            stacked=True,  # Apilamos las barras
                            color=['red', 'green'],  # Colores para cada categoría
                            edgecolor='black')  # Color del borde de las barras
plt.title('Número Acumulado de Personas Fallecidas y Sobrevivientes en Cada Clase')  # Título del gráfico
plt.xlabel('Clase')  # Etiqueta del eje X
plt.ylabel('Número Acumulado de Pasajeros')  # Etiqueta del eje Y
plt.xticks([0, 1, 2], ['Primera', 'Segunda', 'Tercera'], rotation=0)  # Etiquetas de las clases en el eje X
plt.legend(['Fallecidos', 'Sobrevivientes'])  # Leyenda para las categorías
plt.grid(True, axis='y')  # Activamos la cuadrícula solo en el eje Y
plt.show()  # Mostramos el gráfico
