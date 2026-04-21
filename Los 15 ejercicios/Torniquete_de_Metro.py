total_dinero = 0
pasajes_normales = 800
pasaje_estudiantes = 250
normal = 0
estudiantes = 0

while True:
    tipo_pasajero = input("Ingrese que tipo de pasajero es (N/E/CORTE)")
    if tipo_pasajero == "CORTE":
        break
    if tipo_pasajero == "N" :
        total_dinero += pasajes_normales 
        normal += 1
    elif tipo_pasajero == "E" :
        total_dinero += pasaje_estudiantes
        estudiantes += 1
    else:
        print("opcion invalida")

print("Pasajeros Normales:", normal)
print("Pasajeros Estudiantes:", estudiantes)
print("Total de dinero recaudado:", total_dinero)