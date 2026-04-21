cantidad_entradas = int(input("Ingrese la Cantidad de entradas que desea Comprar en Total:  "))
contador_de_entradas = 1
precio_todas_entradas = 0
while contador_de_entradas <= cantidad_entradas:
    edad = int(input("Que edad tiene Usted:  "))
    if edad < 12:
        print("Su entrada Equivale a $3000")
        entrada = 3000
        precio_todas_entradas += entrada
        contador_de_entradas += 1
    elif edad >= 12 and edad <= 64:
        print("Su entrada Equivale a $6000")
        entrada = 6000
        precio_todas_entradas += entrada
        contador_de_entradas += 1
    elif edad >= 65 :
        print("Su entrada equivale a $4000")
        entrada = 4000
        precio_todas_entradas += entrada
        contador_de_entradas += 1
    else:
        print("Ingrese una Opcion Valida")
    

print(f"El total recaudado en esta Transaccion es de un total de :  {precio_todas_entradas}")