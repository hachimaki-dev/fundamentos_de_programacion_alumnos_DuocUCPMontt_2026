contador_de_intentos = 0

clave = "12345"

while True:
    clave_ingresada = int(input("Ingrese clave"))
    if clave_ingresada != clave:
        contador_de_intentos = contador_de_intentos + 1
    if contador_de_intentos == 3:
        print("Bloqueo de Tarjeta")
        break