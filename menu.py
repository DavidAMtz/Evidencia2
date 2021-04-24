import datetime
import sys
import pandas as pd
import csv
import os

def registroVentas():
    clave=1
    respuesta = 1
    dic_ventas={}
    total=[]
    print("***Registro de Venta***")
    
    while respuesta == 1:
        descArticulo=[]
        cantVendidas=[]
        precioVenta=[]
        tiempoVenta=[]
        
        #Aqui va el numero "clave" de la venta.
        print(f"Venta numero {clave}")
        
        #Aqui va una descripción breve del producto.
        descripcionArticulo = input("¿Cual es la descripción del articulo?: ")
        descArticulo.append(descripcionArticulo)
        
        #Aqui van las piezas compradas por el usuario.
        cantidadPiezasVendidas = int(input("¿Cual es la cantidad de piezas vendidas?: "))
        cantVendidas.append(cantidadPiezasVendidas)
        
        #Aqui va el precio de venta del articulo.
        precioDeVenta = int(input("¿Cual es el precio de venta?: "))
        
        #Aqui se multiplican las piezas vendidas por el precio unitario.
        total.append(precioDeVenta*cantidadPiezasVendidas)
        precioVenta.append(precioDeVenta)
        
        #Aqui se toma el tiempo de la maquina (dia/mes/año).
        time = datetime.datetime.now()
        time_1=time.strftime('%d/%m/%Y')
        tiempoVenta.append(str(time_1))
        
        dic_ventas["Descripcion_Articulo"]=descArticulo
        dic_ventas["Cantidad_Vendida"]=cantVendidas
        dic_ventas["Precio_Venta"]=precioVenta
        dic_ventas["Tiempo"]=tiempoVenta
        dic2=pd.DataFrame(dic_ventas)
        
        #Aqui se crea el archivo de CSV (Valores separados por comas)
        #Para la creacion de la hoja donde se guardan los datos de la venta.
        ruta = "ventas.csv"
        dic2.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
        
        #Aqui se cierra o se abre otra venta, mediante una pregunta al usuario.
        clave = clave + 1  
        respuesta = int(input("¿DESEA REGISTRAR OTRA VENTA?: 1-.SI/2-.NO: "))
        
        #Aqui cuando el usuario haya terminado de registrar sus ventas, se da el total de todos los articulos.
        if respuesta == 2:
            print(f"***TOTAL DE COMPRA***: {sum(total)}")