# TERMINADO

print("===== Paseador de perros =====")

cantidad_perros_paseados = int(input("Cuantos perros paseaste hoy?:"))

perros_procesados = 0

paseos_acumulados = 0

while perros_procesados < cantidad_perros_paseados:


    print(f"procesando perro {perros_procesados + 1}")
    peso_del_perrito = int(input("cuantos kg pesa el perrito?:"))

    if peso_del_perrito <= 10:
        print(f"perro pequeño, cuesata $2000")
        perros_procesados += 1
        paseos_acumulados += 2000

    elif peso_del_perrito > 10 and peso_del_perrito < 25:
        print("perro mediano, cuesran $4000")
        perros_procesados += 1
        paseos_acumulados += 4000

    elif peso_del_perrito >= 25:
        print("perro grande, cuestan $6000")
        perros_procesados += 1
        paseos_acumulados += 6000

        total_ganado_paseos = paseos_acumulados

print(f"hoy paseaste {perros_procesados} perros, ganando un total de: {paseos_acumulados}")













