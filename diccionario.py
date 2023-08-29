ProductoTerminado1 = {
    'referencia': 5089,
    'marca':"Americanino",
    'Descripcion':"Chompa",
    'color': "Negro",
    'Precio':100000,
    'Disponibilidad': True,
    'PrecioVenta': 850000,
    'PuntosVentas': ['cc mayorca','terminal norte', 'centro de la moda','centro de la moda'], 
}

ProductoTerminado2 = {
    'referencia': 5085,
    'marca':"Mango",
    'Descripcion':"Camisa",
    'color': "Azul",
    'Precio':200000,
    'Disponibilidad': True,
    'PrecioVenta': 550000,
    'PuntosVentas': ['cc mayorca','terminal norte', 'centro de la moda','centro de la moda'], 
}

#CREANDO LISTA DE DICCIONARIOS

Productos=[ProductoTerminado1,ProductoTerminado2]

#RECORRIENDO LISTA CON CICLO FOR

'''for Contador in range(10):
    print(Contador)'''

#RECORRIENDO LISTA CON FOR EACH

for Producto in Productos:
    for PuntoVenta in Producto["PuntosVentas"]:
        print(PuntoVenta)