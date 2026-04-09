print("Paseador de perros")


cantidad = int(input("¿Cuántos perros paseaste hoy?"))
total = 0
#usar el for para repetir lo que se pide
for i in range (cantidad):

    peso = int(input("Ingresa el peso del perro"))
    if peso < 10:
        precio = 2000
        print("Perro pequeño $2000")
        
    elif peso < 25:
        precio = 4000
        print("Perro mediano $4000")

    else :
        precio = 6000
        print("Perro grande $6000")
    total += precio

print(f"Hoy paseaste {cantidad}  de perros y recaudaste un total de {total} pesos")
    