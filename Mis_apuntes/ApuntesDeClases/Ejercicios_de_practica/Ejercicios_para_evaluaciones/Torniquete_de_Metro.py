E = 0
N = 0
Dinero = 0
while True: #EL WHILE TRUE ES PARA GENERAR UN CICLO INFINITO, USAR BREAK PARA CORTAR.
    pasajero = input("Ingrese E si es Estudiante, N para persona corriente.")
    if pasajero == "CORTE":
        break
    if pasajero == "E":
        E += 1
        Dinero = Dinero + 250
    elif pasajero == "N":
        N += 1
        Dinero = Dinero + 800
    else:
        print("Por favor ingrese una opción válida.")
print(Dinero)
print(f"Pasajeros corrientes : {N}.")
print(f"Pasajeros estudiantes : {E}.")
