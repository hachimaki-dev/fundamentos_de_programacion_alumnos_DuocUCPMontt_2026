# Ejercicio 2 — Stock de una farmacia

print("======================")
print("Farmacia sin negativos")
print("======================")

while True:
    try:
        medicamentos = int(input("Ingrese el número de medicamentos por favor: "))

        if medicamentos >= 0:
            print(f"El número de medicamentos solicitado es de: {medicamentos}")
            break
        
        elif medicamentos < 0:
            print("Error, ¡¿COMO VAN HABER MEDICAMENTOS NEGATIVOS?!")
            print("Dato inválido. Ingresa un entero positivo para el stock.")

    except ValueError:
        print("Error, ingrese un numevo número por favor")