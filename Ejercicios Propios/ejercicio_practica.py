print("#####"*10)
print("Bienvenido al Cajero Automático de Frutas")
print("#####"*10)

print()


total_compra = 0
total_productos = 0

while True:
    print("Las Frutas Disponibles Para comprar son: \n 1. Manzana : $5 \n 2. Peras : $4\n 3. Platanos : $4\n 4. Sandia : $6 \n 5. Salir  ")
    
    eleccion = input("Que fruta desea Comprar (Seleccione el Numero):    ")

    if eleccion ==  "5" :
        print()
        print(f"Muchas Gracias por su Compra \n El total a pagar es ${total_compra}\nEl Total de Productos que compro son {total_productos}")
        break
    elif eleccion == "1" :
        print()
        print(" A Comprado Una Manzana ")
        total_productos += 1
        total_compra += 5
    elif eleccion == "2" :
        print()
        print("A Comprado una Pera")
        total_productos += 1
        total_compra += 4
    elif eleccion == "3" :
        print()
        print("A Comprado un Platano")
        total_productos += 1
        total_compra += 4
    elif eleccion == "4" :
        print()
        print("A Comprado una Sandia")
        total_productos += 1
        total_compra += 6
    else:
        print()
        print("Producto No Disponible")

