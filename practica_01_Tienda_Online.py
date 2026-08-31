import pandas as pd
import numpy as np

#Primero se crea el diccionario de listas que convertiremos en un dataframe

def cargar_datos(n_filas=50): #La funcion tiene como parametro n_filas = 50, asi mas adelante si no se pone parametro al llamarla, hace 50 fialas, si se quiere poner otro numero, solo se pone el numero, "cargar_datos(2000)"
   #Esta funcion va a crear y retornar el dataframe que genere con numeros aleatorios
   
    #Primero determino que todos los numero aleatorios usados, tendran como base 42 para asi poder volver a utilizar esos numeros posteriormente
    np.random.seed(42)

    #Creo una lista de productos
    productos = ["Laptop", "Mouse", "Escritorio", "Teclado", "Silla"]

    #Ahora creo un diccionario determinando cual esa la correcta categoria de cada producto
    categorias_por_producto = {
        "Laptop": "Tecnologia",
        "Mouse": "Tecnologia",
        "Teclado": "Tecnologia",
        "Escritorio": "Hogar",
        "Silla": "Hogar"
    }

    #Creo una lista de ciudades
    ciudades = ["Bogota", "Medellin", "Cali", "Ibague", "Barranquilla"]

    #Los productos aleatorios son escogidos de manera aleatoria de la lista "productos, la cantidad de productos elegidos es igual a la cantidad de filas"
    productos_elegidos = np.random.choice(productos, size=n_filas)

    #Categorias elegidas es buscar en el diccionario de  "categorias por producto" el valor obtenido en la lista "productos_elegidos" y guardarlos en "Categorias elegidas"
    categorias_elegidas = [categorias_por_producto[p] for p in productos_elegidos]

    #Ventas es un diccionario con listas como habiamos visto antes en el que el id, va de un rango desde 1001, sucesivamente hasta el numero de filas,
    #producto es igual a los productos elegidos igual que las categorias que ya irian enlazadas, precio es un numero aleatorio entre 50mil y 4mill cantidad de numero de filas
    #Cantidad del producto es lo mismo que precio pero entre 1 y 5
    #Ciudad es un random choice de la lista ciudades, cantidad el numero de filas
    #Fecha es una fecha random con numero de inicios, cantidad de fechas igual a la cantidad de filas que avanza secuencialmente por dia
    ventas = {
        "ID": range(1001, 1001 + n_filas),
        "Producto": productos_elegidos,
        "Categoria": categorias_elegidas,
        "Precio": np.random.randint(50000, 4000000, size=n_filas),
        "Cantidad": np.random.randint(1, 5, size=n_filas),
        "Ciudad": np.random.choice(ciudades, size=n_filas),
        "Fecha": pd.date_range(start="2024-01-01", periods=n_filas, freq="D")
    }

    #Aqui creamos el dataframe que vamos a retornar
    df = pd.DataFrame(ventas)
    #Creamos la nueva columna correspondiente al total
    df["Total"] = df["Precio"] * df["Cantidad"]
    #retornamos el dataframe
    return df

#--------------------------------------------------AQUI YA EMPEZAMOS CON EL ANALISIS--------------------------------------------------------------

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
    return nombre_dataframe.loc[nombre_dataframe["Total"].idxmax()]

#Se utiliza este if para que no se dispare todo el print largo en caso de usar el archivo importado en otro archivo
if __name__ == "__main__":
    ventas_df = cargar_datos()
    #Esta linea es para exportar el dataframe como csv para crear los graficos en power bi
    ventas_df.to_csv("ventas.csv",index=False)
    
    print("\nIngreso total:", ingreso_total(ventas_df))
    print("Venta mas alta:", venta_mas_alta(ventas_df))
    print("Promedio de las ventas:", promedio_ventas(ventas_df))

    print("\nVentas por categoria:")
    print(ventas_por_categoria(ventas_df))

    print("\nVentas por ciudad (de mayor a menor):")
    print(ventas_por_ciudad(ventas_df))

    print("\nProducto con la venta mas alta:")
    print(producto_top(ventas_df))
