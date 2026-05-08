dinero_total = 0
pasajeros_normales = 0
estudiantes = 0
tipo = 0

while True:
    tipo = input("¿Tipo de pasajero (N: normal, E: Estudiante, CORTE para salir: ")   
    
    if tipo == "CORTE"or tipo == "corte":
        break
    
    if tipo == "N" or tipo == "n":
        dinero_total = dinero_total + 800
        pasajeros_normales = pasajeros_normales + 1
        print("cobrado $800")

    elif tipo == "E" or tipo == "e":
        dinero_total = dinero_total + 250
        estudiantes = estudiantes + 1
        print("cobrado $250")
        
print(f"Pasajeros normales: {pasajeros_normales}")
print(f"Pasajeros estudiantes: {estudiantes}")
print(f"total de la caja:{dinero_total}")

#ayuda de dia pero igual entiendo un poco mas