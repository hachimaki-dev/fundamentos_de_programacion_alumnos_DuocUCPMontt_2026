#Negocio paseador de perros
perro_pequeño = 2000
perro_mediano = 4000
perro_grande = 6000

while True:
    try:
        perros_paseados = int(input("Cuantos perros paseo el dìa de hoy?: "))
        if perros_paseados <0:
            print("Ingrese un nùmero valido.")
        else:
            break
    except ValueError:
        print("Ingresa SOLAMENTE nùmeros.")
    
total_a_cobrar = 0
contador = 0
while contador < perros_paseados:
    try:
        peso = int(input(f"Perro {contador + 1} ¿cuanto pesaba en kg?: "))
        if peso <= 0:
            print("Ingresa un peso valido.")
        elif peso <= 10:
            precio = perro_pequeño
            tamaño = "Pequeño"
        elif peso <= 25:
            precio = perro_mediano
            tamaño = "Mediano"
        else:
            precio = perro_grande
            tamaño = "Grande"
        
        total_a_cobrar += precio
        contador += 1

        print(f"El tamaño es {tamaño} y su precio es de {precio}")
    except ValueError:
        ("ingresa un monto valido.")
print("="*50)
print(f"Has paseado {perros_paseados} perros en total y recibes ${total_a_cobrar}")
print("="*50)