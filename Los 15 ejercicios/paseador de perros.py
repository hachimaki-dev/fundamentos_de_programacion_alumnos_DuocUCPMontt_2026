perros_paseados = int(input("¿Cuantos perros a paseado e total el dia de hoy:  "))
contador = 1
total_ganado = 0

while contador <= perros_paseados:
    peso_del_perro = float(input(f"Ingrese el peso(en kg) del perro N°{contador}:  "))
    if peso_del_perro < 10:
        print("Perro pequeño: $2000")
        total_ganado += 2000
        contador += 1
    elif peso_del_perro >= 10 and peso_del_perro < 25:
        print("Perro Mediano: $4000")
        total_ganado += 4000
        contador += 1
    elif peso_del_perro >= 25:
        print("Perro Grande: $6000")
        total_ganado += 6000
        contador += 1


print(f"Resumen del dia:\nPerros paseados el dia de hoy: {perros_paseados}\nLo Ganado en total el dia de hoy: {total_ganado}")
