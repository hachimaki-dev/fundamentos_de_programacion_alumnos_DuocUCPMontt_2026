bandera = True
precio_total = 0
cantidad_total = 0
edad_menor_12 = 0
edad_12_a_64 = 0
edad_65_o_mas = 0

print("Bienvenido al CINE de PYTHON")
print("El precio de las entradas se basara en la edad del espectador")
print("Si tiene menos de 12 años, el precio es de $3000CLP")
print("Si tiene entre 12 a 64 el precio es de $6000CLP")
print("Por último si tiene 65 o más el precio es de $4000CLP")
cantidad_de_entradas = int(input("¿Cuantas personas van a comprar su entrada?"))

while bandera:
    cantidad_total = cantidad_total + 1
    edad = int(input(f"¿Que edad tiene la persona {cantidad_total}?"))
    if edad <= 11:
        edad_menor_12 = edad_menor_12 +  1
        precio_total = precio_total + 3000
        print(f"Perfecto, seria hasta el momento {edad_menor_12} de 12 años o menor")
    elif edad >= 13 and edad < 65:
        edad_12_a_64 = edad_12_a_64 +  1
        precio_total = precio_total + 6000
        print(f"Perfecto, seria hasta el momento {edad_12_a_64} entre 12 a 64 años")
    elif edad >= 65:
        edad_65_o_mas = edad_65_o_mas +  1
        precio_total = precio_total + 4000
        print(f"Perfecto, hasta el momento seria {edad_65_o_mas} entre 65 o más ")
    if cantidad_total == cantidad_de_entradas:
        bandera = False
print(f"Perfecto el precio total seria de ${precio_total}CLP")
print(f"Seria {edad_menor_12} de 12 o menos")
print(f"{edad_12_a_64} de 12 a 64")
print(f"{edad_65_o_mas} de 65 o más")
print("Que tenga una buena funciòn")