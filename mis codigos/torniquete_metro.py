# TERMINADO

normales_pasajeros = 0
estudiantes_pasajeros = 0
dinero_total_caja = 0

while True:
    print("===== BIENVENIDOS AL METRO DE SANTIAGO =====")
    tipo_de_pasajero = input("¿Que tipo de pasajero eres? (N: Normal / E: Estudiante / C:) ")

    if tipo_de_pasajero == "n" or tipo_de_pasajero == "N":
        normales_pasajeros += 1
        dinero_total_caja += 800
        print("PASAJERO NORMAL REGISTRADO ")
    
    elif tipo_de_pasajero == "e" or tipo_de_pasajero == "E":
        estudiantes_pasajeros += 1
        dinero_total_caja += 250
        print("PASAJERO ESTUDIANTE REGISTRADO ")
    
    elif tipo_de_pasajero == "c" or tipo_de_pasajero == "C":
        print("Generando el corte de caja")
        print("Hasta pronto cuidese >:3")
        break
    
    else:
        print("Opcion invalida, intente de nuevo >:C")


print("=================================================")
print(f"Pasajeros normales: {normales_pasajeros}")
print(f"Estudiantes: {estudiantes_pasajeros}")
print(f"Total dinero caja: ${dinero_total_caja}")
print("==================================================")