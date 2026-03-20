# 1. IMPORTAR LIBRERÍAS


# Pandas se usa para manipulación y análisis de datos
import pandas as pd

# cargar dataset de arriendos
#arriendos = pd.read_csv("C:/Users/leen/OneDrive - SENA/Documentos/proyectos universisdad/DATAXPERIENCE/arriendos_colombia.csv.csv")
import os
print("Archivos en la carpeta del proyecto:")
print(os.listdir())
# cargar dataset de inflación
inflacion = pd.read_csv(r"C:\Users\leen\Downloads\DATAXPERIENCE\arriendos_colombia.csv")


datos = pd.read_csv(r"C:\Users\leen\Downloads\DATAXPERIENCE\inflacion_colombia.csv")

print(datos.head())



# Matplotlib se usa para visualización de datos
import matplotlib.pyplot as plt




# 2. CARGAR LOS DATASETS


# Cargar dataset de arriendos
arriendos = pd.read_csv("arriendos_colombia.csv")

# Cargar dataset de inflación
inflacion = pd.read_csv("inflacion_colombia.csv")

print("Datasets cargados correctamente")



# 3. EXPLORACIÓN INICIAL DE LOS DATOS


# Mostrar primeras filas del dataset
print("\nPrimeras filas del dataset de arriendos:")
print(arriendos.head())

# Mostrar información general del dataset
print("\nInformación del dataset:")
print(arriendos.info())

# Mostrar estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(arriendos.describe())




# 4. IDENTIFICAR PROBLEMAS EN LOS DATOS


# Contar valores nulos
print("\nValores nulos por columna:")
print(arriendos.isnull().sum())

# Verificar duplicados
print("\nCantidad de registros duplicados:")
print(arriendos.duplicated().sum())




# 5. LIMPIEZA DE DATOS


# Eliminar registros duplicados
arriendos = arriendos.drop_duplicates()

print("\nDuplicados eliminados")

# Rellenar valores nulos en área con la mediana
arriendos["area_m2"] = arriendos["area_m2"].fillna(arriendos["area_m2"].median())

# Eliminar precios irreales (muy bajos)
arriendos = arriendos[arriendos["precio_arriendo_cop"] > 200000]

print("Limpieza de datos completada")




# 6. TRANSFORMACIÓN DE VARIABLES


# Crear variable precio por metro cuadrado
arriendos["precio_m2"] = arriendos["precio_arriendo_cop"] / arriendos["area_m2"]

print("\nNueva variable creada: precio_m2")




# 7. ANÁLISIS ESTADÍSTICO


# Precio promedio por ciudad
precio_ciudad = arriendos.groupby("ciudad")["precio_arriendo_cop"].mean()

print("\nPrecio promedio de arriendo por ciudad:")
print(precio_ciudad)

# Precio promedio por número de habitaciones
precio_habitaciones = arriendos.groupby("habitaciones")["precio_arriendo_cop"].mean()

print("\nPrecio promedio según número de habitaciones:")
print(precio_habitaciones)




# 8. VISUALIZACIÓN DE DATOS


# Gráfico 1: Distribución de precios de arriendo
plt.figure()

plt.hist(arriendos["precio_arriendo_cop"], bins=30)

plt.title("Distribución de precios de arriendo en Colombia")
plt.xlabel("Precio de arriendo")
plt.ylabel("Frecuencia")

plt.show()





# Gráfico 2: Precio promedio por ciudad
plt.figure()

precio_ciudad.plot(kind="bar")

plt.title("Precio promedio de arriendo por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Precio promedio")

plt.show()





# Gráfico 3: Relación entre área y precio
plt.figure()

plt.scatter(arriendos["area_m2"], arriendos["precio_arriendo_cop"])

plt.title("Relación entre tamaño de vivienda y precio de arriendo")
plt.xlabel("Área (m2)")
plt.ylabel("Precio")

plt.show()




# 9. RESULTADOS FINALES


print("\nResumen final del dataset limpio:")
print(arriendos.head())

print("\nCantidad final de registros:")
print(len(arriendos))
