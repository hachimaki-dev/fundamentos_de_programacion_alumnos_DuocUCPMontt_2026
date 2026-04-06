capacidad = 0
edad=0
precio_entrada=0
cantidad_entradas=0
valor_total = 0
respuesta = ""
while capacidad < 25:
    edad=int(input("Por favor ingrese su edad "))
    if edad < 12:
        precio_entrada = 3000
        print(f"El precio de la entrada es de {precio_entrada} pesos" )
        valor_total = valor_total + precio_entrada
        cantidad_entradas +=1
        capacidad += 1
    elif edad >= 12:
        precio_entrada = 6000
        print(f"El precio de la entrada es de {precio_entrada} pesos" )
        valor_total = valor_total + precio_entrada
        cantidad_entradas +=1
        capacidad += 1
    elif edad > 64:
        precio_entrada = 4000
        print(f"El precio de la entrada es de {precio_entrada} pesos" )
        valor_total = valor_total + precio_entrada
        cantidad_entradas +=1
        capacidad += 1
    respuesta=input("Seguir vendiendo? ")
    if respuesta == "si":
        print("Sigues vendiendo")
    else:
        break
print(f"se han cerrado las ventas, he ganado {valor_total} con las entradas y he vendido {cantidad_entradas} entradas")