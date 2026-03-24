# --------------- Importaciones

import pandas
# from google.colab import drive #se usara solo en la version de googlecolab

# --------------- Fin de las Importaciones

# # a. Extraer la información del archivo.

# drive.mount("/content/drive") para el googlecolab

df = pandas.read_csv(r"C:\\Users\\sasor\\Desktop\\Tec de mty\\2. Procesamiento y manipulacion de datos en python\\2. Panda y Numpy en Python\\reto\\Para entrega en github\\country_vaccinations.csv")

print(df.head())
df.info()