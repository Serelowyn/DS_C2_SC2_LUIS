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

# d. Obtener la cantidad de vacunas aplicadas en todo el mundo. (y por pais)

por_pais = df[["country", "vaccines"]].groupby("country").count()
print(por_pais)
total_mundial = df['total_vaccinations'].sum()
print(total_mundial)

total_vacunas = df["total_vaccinations"].sum(skipna=True)
print(total_vacunas)

num_paises = df["country"].nunique()
promedio_por_pais = total_vacunas / num_paises
print("promedio vacunas aplicadas por pais:", promedio_por_pais)

# f. Determinar la cantidad de vacunas aplicadas el día 29/01/21 en todo el mundo. 

vacunas_dia = df[df["date"] == "2021-01-29"]
total_vacunas_dia = vacunas_dia["daily_vaccinations"].sum(skipna=True)

print("svacunas aplicadas en el mundo el 29/01/2021:", total_vacunas_dia)

#g. Crear un dataframe nuevo denominado conDiferencias que contenga los datos originales y una columna derivada (diferencias) con las diferencias de aplicación entre las columnas daily_vaccionations y daily_vaccionations_raw.

conDiferencias = df.copy()
conDiferencias["diferencias"] = conDiferencias["daily_vaccinations"] - conDiferencias["daily_vaccinations_raw"]

print(conDiferencias)

# h. Obtener el periodo de tiempo entre el registro con fecha más reciente y el registro con fecha más antigua.

fecha_min = df["date"].min()
fecha_max = df["date"].max()
periodo = fecha_max - fecha_min

print("fecha mas antigua:", fecha_min)
print("fecha mas reciente:", fecha_max)
print("tiempo en dias:", periodo)

# i. Crear un dataframe nuevo denominado conCantidad que contenga los datos originales y una columna derivada (canVac) con la cantidad de vacunas utilizadas cada día (usar la columna vaccines y separar por el carácter , ).

df["canVac"] = df["vaccines"].str.split(", ").str.len()
conCantidad = df.copy()
print(conCantidad)

# j. Generar un dataframe denominado antes20 con todos los registros que se hayan realizado antes del 20 de diciembre de 2020.

antes20 = df[df["date"] < "2020-12-20"]
print(antes20.head())
print("registros antes del 20/12/2020:", len(antes20))

# k. Obtener un dataframe denominado pfizer con todos los registros donde se haya utilizado la vacuna Pfizer.

pfizer = df[df["vaccines"].str.contains("Pfizer/BioNTech", na=False)]
print(pfizer)
print("registros con Pfizer/BioNTech:", len(pfizer))

# l. Almacenar los dataframes generados (conDiferencias, conCantidad, antes20 y pfizer) en un archivo de Excel denominado resultadosReto.xlsx, donde cada dataframe ocupe una hoja diferente. Se recomienda ver la documentación de pd.ExcelWriter. 

with pandas.ExcelWriter("C:\\Users\\sasor\\Desktop\\Tec de mty\\2. Procesamiento y manipulacion de datos en python\\2. Panda y Numpy en Python\\reto\\resultadosReto.xlsx", engine="openpyxl") as writer:
    conDiferencias.to_excel(writer, sheet_name="ConDiferencias", index=False)
    conCantidad.to_excel(writer, sheet_name="ConCantidad", index=False)
    antes20.to_excel(writer, sheet_name="Antes20", index=False)
    pfizer.to_excel(writer, sheet_name="Pfizer", index=False)
    
# para el colab
# with pandas.ExcelWriter("/content/drive/MyDrive/Colab Notebooks/resultadosReto.xlsx", engine="openpyxl") as writer:
#     conDiferencias.to_excel(writer, sheet_name="ConDiferencias", index=False)
#     conCantidad.to_excel(writer, sheet_name="ConCantidad", index=False)
#     antes20.to_excel(writer, sheet_name="Antes20", index=False)
#     pfizer.to_excel(writer, sheet_name="Pfizer", index=False)