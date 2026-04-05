pasajeros_normales=0
estudiantes=0
total_dinero_caja=0
precio_pasajeros_normales= 800
precio_estudiantes= 250

while True:
    tipo_pasajero= input("Ingrese tipo de pasajero: ")
    if tipo_pasajero =="CORTE":
        break
    elif tipo_pasajero== "N":
        pasajeros_normales+=1
        total_dinero_caja+= precio_pasajeros_normales
    elif tipo_pasajero== "E":
        estudiantes+=1
        total_dinero_caja+=precio_estudiantes

print(f"Pasajeros normales: {pasajeros_normales} \nEstudiantes: {estudiantes} \nTotal de dinero en caja: {total_dinero_caja}")