vengadores = []
heroe = str
while True:
    print("1. Agregar avenger")
    print("2. Mostrar base y modificar")
    print("3. Salir")
    eleccion = input("Elije una opcion (1, 2, 3): ")
    if eleccion == 1:
        heroe = input("ingresa el nombre del heroe: ")
        vengadores.append(heroe)
    if eleccion == 2:
        for nombres in range(len(vengadores)):
            vengadores[nombres] = vengadores[nombres].upper()
    if eleccion == 3:
        break
    if eleccion == 0:
        palabra_secreta = input("Escriba la palabra secreta para ejecutar la accion: ")
        if palabra_secreta == "Sacrificar".lower():
            vengadores.pop()
# esta mal, hay que modificarlo 