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
#print("Ingreso total:",ventas_df["Total"].sum())

#¿Cual fue la venta mas alta? = Se resuelve con el valor mas alto de toda la columna "total"
#print("Venta mas alta:",ventas_df["Total"].max())

#¿Cual fue el promedio de las ventas? = Se resuelve con el promedio toda la columna "total"
#print("Promedio de las ventas:",ventas_df["Total"].mean())
print("________________________________________________________________________________________")
#Dinero generado por categoria = se usa group by para categorizar y se suma el total de las ventas
ventas_por_categoria = ventas_df.groupby("Categoria")["Total"].sum()
print("VENTAS POR CATEGORIA:")
print(ventas_por_categoria)

#Ventas totales por ciudad, de mayor a menor
print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")
ventas_por_ciudad = ventas_df.groupby("Ciudad")["Total"].sum().sort_values(ascending=False)
print("VENTAS POR CIUDAD DE MAYOR A MENOR")
print(ventas_por_ciudad)

#Producto que mas ingresos genero
producto_top_ventas = ventas_df.loc[ventas_df["Total"].idxmax()]
print("PRODUCTO MAS VENDIDO")
print(producto_top_ventas)