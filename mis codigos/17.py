tipo_automovil = "camion"

velocidad = 95

print("===== CONTROL DE VELOCIDAD =====")

print ("ANALIZANDO DATOS...")

if tipo_automovil.lower() == "camion" and velocidad > 80:
    print("¡Multa grave camion!")

elif tipo_automovil.lower() == "camion" and velocidad < 80:
    print("¡Velocidad dentro del límite permitido, NO HAY MULTA!")

elif tipo_automovil.lower() == "automovil" and velocidad > 120:
    print("¡Multa gravisima!")    

elif tipo_automovil.lower() == "automovil" and velocidad < 120:
    print("¡Velocidad dentro del límite permitido, NO HAY MULTA!")

else:
    print("Tipo de automóvil no reconocido")