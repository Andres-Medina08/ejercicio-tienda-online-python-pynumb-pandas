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
def ingreso_total(nombre_dataframe):
    #Devuelve la suma total de todas las ventas.
    return nombre_dataframe["Total"].sum()

def venta_mas_alta(nombre_dataframe):
    #Devuelve la venta mas alta en valor
    return nombre_dataframe["Total"].max()
    
def promedio_ventas(nombre_dataframe):
    #Devuelve el promedio de todas las ventas
    return nombre_dataframe["Total"].mean()

def ventas_por_categoria(nombre_dataframe):
    #Devuelve cual fue el ingreso por venta de cada categoria
    return nombre_dataframe.groupby("Categoria")["Total"].sum()

def ventas_por_ciudad(nombre_dataframe):
    #Devuelve las ventas totales por ciudad de mayor a menor
    return nombre_dataframe.groupby("Ciudad")["Total"].sum().sort_values(ascending=False)

def producto_top(nombre_dataframe):
    #Devuelve las caracteristicas del producto mas vendido
    return nombre_dataframe.loc[ventas_df["Total"].idxmax()]

#Se utiliza este if para que no se dispare todo el print largo en caso de usar el archivo importado en otro archivo
if __name__ == "__main__":
    print("\nIngreso total:", ingreso_total(ventas_df))
    print("Venta mas alta:", venta_mas_alta(ventas_df))
    print("Promedio de las ventas:", promedio_ventas(ventas_df))

    print("\nVentas por categoria:")
    print(ventas_por_categoria(ventas_df))

    print("\nVentas por ciudad (de mayor a menor):")
    print(ventas_por_ciudad(ventas_df))

    print("\nProducto con la venta mas alta:")
    print(producto_top(ventas_df))

