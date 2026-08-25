import pandas as pd
import numpy as np

#Primero se crea el diccionario de listas que convertiremos en un dataframe

ventas = {
    "ID":[1001,1002,1003,1004,1005],
    "Producto":["Laptop","Mouse","Escritorio","Teclado","Silla"],
    "Categoria":["Tecnologia","Tecnologia","Hogar","Tecnologia","Hogar"],
    "Precio":[3500000,85000,620000,180000,450000],
    "Cantidad":[1,2,1,1,2],
     "Ciudad":["Bogota","Medellin","Cali","Ibague","Bogota"]   
}

#Aqui se convierte el diccionario ventas en un dataframe
ventas_df = pd.DataFrame(ventas)

#Aqui agregamos una nueva columna al dataframe
ventas_df["Total"]=ventas_df["Precio"]*ventas_df["Cantidad"]


#Aqui ya empezamos a hacer las primeras cuestiones de analisis

#¿Cual fue el ingreso total de las ventas? = Se resuelve con la sumatoria de toda la columna "total"
print("Ingreso total:",ventas_df["Total"].sum())

#¿Cual fue la venta mas alta? = Se resuelve con el valor mas alto de toda la columna "total"
print("Venta mas alta:",ventas_df["Total"].max())

#¿Cual fue el promedio de las ventas? = Se resuelve con el promedio toda la columna "total"
print("Promedio de las ventas:",ventas_df["Total"].mean())
