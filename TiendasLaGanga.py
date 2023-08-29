#MENU OPCIONES
#1.Ingresar Producto bodega
#2.Verificas los productos bodega
#3.Buscar producto en bodega
#4.Editar producto en bodega
#5.Retirar producto en bodega
#6.SALIR

#Producto :nombre,codigo,descripcion,foto,precio,cantidadBodega,fechaEntradaBodega

Opcion=0
print("1.Ingresar Producto bodega")
print("**************************")
print("2.Verificar los productos bodega")
print("3.Buscar producto en bodega")
print("4.Editar producto en bodega")
print("5.Retirar producto en bodega")
print("6.SALIR")
print("**************************")

Productos = []

while(Opcion !=6):

    Producto = {}
    Opcion=int(input("Digita la opcion deseada: "))
    if Opcion==1:
        Producto['Nombre'] = input("Digita el nombre de el producto: ")
        Producto['Codigo'] = int(input("Digita el codigo de el producto: "))
        Producto['Descripcion'] = input("Digita la descripcion de el producto: ")
        Producto['Foto'] = input("Digita la URL de la foto: ")
        Producto['Precio'] = float(input("Digita el precio de el producto: "))
        Producto['Stock'] = int(input("Digita el stock de el producto: "))
        Producto['FechaEntradaBodega'] = input("Digita la fecha de entrada: ")
        Productos.append(Producto)
    elif Opcion==2:
        for ProductoSeleccionado in Productos:
            print(f"Codigo:  = {ProductoSeleccionado['Codigo']}")
            print(f"Nombre:  = {ProductoSeleccionado['Nombre']}")
            print(f"Descripcion:  = {ProductoSeleccionado['Descripcion']}")
            print(f"Foto:  = {ProductoSeleccionado['Foto']}")
            print(f"Stock:  = {ProductoSeleccionado['Stock']}")
            print(f"Fecha de entrada:  = {ProductoSeleccionado['FechaEntradaBodega']}\n")
    elif Opcion ==3:
        pass
    elif Opcion==4:
        pass
    elif Opcion==5:
        pass
    elif Opcion==6:
        pass
    else:
        print("Opcion invalida, Vuelva a inventario")
