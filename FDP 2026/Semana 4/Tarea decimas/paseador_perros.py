cant_perros_paseados = int(input("Ingrese la cantidad de perros paseados en el día de hoy: "))
total = 0

for i in range(cant_perros_paseados):
    peso_perro = int(input(f"Ingrese el peso (Kg) del perro {i + 1}: "))
    
    if peso_perro < 10:
        total += 2000
    elif peso_perro >= 10 and peso_perro <= 24:
        total += 4000
    else:
        total += 6000

print(f"Resumen del dia: Has paseado {cant_perros_paseados} perros, ganaste en total ${total} pesos")