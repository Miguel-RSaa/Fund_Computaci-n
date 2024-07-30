import pandas as pd

# a) Generar un DataFrame con los datos del fichero
# Cargamos el archivo CSV en un DataFrame de pandas
df = pd.read_csv('titanic.csv')

# b) Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene,
# los nombres de sus columnas y filas, los tipos de datos de las columnas,
# las 10 primeras filas y las 10 últimas filas

print("Dimensiones del DataFrame:", df.shape)  # (filas, columnas)
print("Número de datos que contiene:", df.size)  # Total de elementos en el DataFrame
print("Nombres de las columnas:", df.columns.tolist())  # Lista de nombres de columnas
print("Nombres de las filas:", df.index.tolist()[:10])  # Primeros 10 nombres de filas
print("Tipos de datos de las columnas:\n", df.dtypes)  # Tipos de datos de cada columna
print("Primeras 10 filas del DataFrame:\n", df.head(10))  # Muestra las primeras 10 filas
print("Últimas 10 filas del DataFrame:\n", df.tail(10))  # Muestra las últimas 10 filas

# c) Mostrar por pantalla los datos del pasajero con identificador 148
# Seleccionamos la fila con el índice 148
print("Datos del pasajero con identificador 148:\n", df.loc[148])

# d) Mostrar por pantalla las filas pares del DataFrame
# Filtramos las filas con índices pares
print("Filas pares del DataFrame:\n", df.iloc[::2])

# e) Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente
# Filtramos por clase 1 y extraemos la columna 'Name', luego ordenamos alfabéticamente
print("Nombres de las personas en primera clase ordenados alfabéticamente:\n",
      df[df['Pclass'] == 1]['Name'].sort_values())

# f) Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron
# Calculamos el total de pasajeros y el total de sobrevivientes y fallecidos
total_pasajeros = len(df)
total_sobrevivientes = df['Survived'].sum()  # Suponiendo que 'Survived' es 1 para sobrevivientes
total_fallecidos = total_pasajeros - total_sobrevivientes
porcentaje_sobrevivientes = (total_sobrevivientes / total_pasajeros) * 100
porcentaje_fallecidos = (total_fallecidos / total_pasajeros) * 100
print(f"Porcentaje de personas que sobrevivieron: {porcentaje_sobrevivientes:.2f}%")
print(f"Porcentaje de personas que murieron: {porcentaje_fallecidos:.2f}%")

# g) Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase
# Agrupamos por clase y calculamos el porcentaje de sobrevivientes en cada clase
porcentaje_sobrevivientes_por_clase = df.groupby('Pclass')['Survived'].mean() * 100
print("Porcentaje de personas que sobrevivieron en cada clase:\n", porcentaje_sobrevivientes_por_clase)

# h) Eliminar del DataFrame los pasajeros con edad desconocida
# Suponiendo que la edad desconocida está representada por NaN en la columna 'Age'
df = df.dropna(subset=['Age'])

# i) Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase
# Filtramos por género femenino y agrupamos por clase para calcular la edad media
edad_media_mujeres_por_clase = df[df['Sex'] == 'female'].groupby('Pclass')['Age'].mean()
print("Edad media de las mujeres que viajaban en cada clase:\n", edad_media_mujeres_por_clase)

# j) Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no
# Definimos que una edad menor a 18 años es considerada menor de edad
df['Menor_de_edad'] = df['Age'] < 18

# k) Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase
# Agrupamos por clase y por 'Menor_de_edad' para calcular el porcentaje de sobrevivientes
porcentaje_sobrevivientes_por_clase_y_edad = df.groupby(['Pclass', 'Menor_de_edad'])['Survived'].mean() * 100
print("Porcentaje de menores y mayores de edad que sobrevivieron en cada clase:\n",
      porcentaje_sobrevivientes_por_clase_y_edad)
