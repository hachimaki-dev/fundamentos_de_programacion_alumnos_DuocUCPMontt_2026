print("BIENVENIDO AL CINE") 
cantidad_entradas= int(input("cuantas entradas desea? "))
total_entradas= 0
total= 0
while total_entradas < cantidad_entradas:
    edad= int(input("Ingrese edad "))
    if edad < 12:
        precio= 3000
        total = total + precio
        total_entradas += 1
    elif edad < 64:
        precio= 6000
        total = total + precio
        total_entradas += 1
    elif edad > 65:
        precio= 4000
        total = total + precio
        total_entradas += 1
    else:
        print("edad no valida")

print(f"su total es de {total} por {total_entradas} entradas")
print("=========DISFRUTE SU PELICULA========")