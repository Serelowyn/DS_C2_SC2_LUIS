# --------------- Importaciones

import pandas
# from google.colab import drive #se usara solo en la version de googlecolab

# --------------- Fin de las Importaciones

# # a. Extraer la información del archivo.

# drive.mount("/content/drive") para el googlecolab

df = pandas.read_csv(r"C:\\Users\\sasor\\Desktop\\Tec de mty\\2. Procesamiento y manipulacion de datos en python\\2. Panda y Numpy en Python\\reto\\Para entrega en github\\country_vaccinations.csv")

print(df.head())
df.info()

# b. Mostrar la estructura y tipos de datos de cada columna para identificar qué operaciones puedes realizar con cada una de ellas, asegurándote que las columnas con fechas sean del tipo datetime64

print(df.dtypes)
print(df.shape)

df["date"] = pandas.to_datetime(df["date"])
df["date"]

# c. Determinar la cantidad de vacunas aplicadas de cada compañía (con base en cómo lo reporta cada país en la columna vaccines, en otras palabras, agrupe por vaccines y realice la sumatoria). 

df_vacunas = df.assign(vaccine=df["vaccines"].str.split(", ")).explode("vaccine")
conteo_vacunas = df_vacunas["vaccine"].value_counts()

print(conteo_vacunas)