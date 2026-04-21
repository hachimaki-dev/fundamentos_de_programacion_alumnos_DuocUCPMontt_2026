# 🔴 Reto Avanzado: Ensamblando a los Vengadores
# Thanos se acerca. Nick Fury de Marvel necesita un programa que le permita alistar a los Avengers en la base. 
# Si envía a alguien al frente, debe ser eliminado de la base usando menús.

# Instrucciones:

# Inicializa tu base vengadores = [].
# Inicia un ciclo infinito while True: con un menú de opciones numéricas: 1-Agregar Avenger, 2-Mostrar Base y Modificar, 3-Salir.
# Si es 1: Solicita al usuario el nombre del héroe y lo agregas al final de la lista. (Pista: .append())
# Si es 2: Recorre la lista por Índices: for i in range(len(vengadores)): e imprime cada héroe junto a su código de posición 
#     (Ej: `0 - Iron Man`, `1 - Thor`). Luego permite a Fury poner en mayúsculas a todos los héroes procesando: vengadores[i] = vengadores[i].upper().
# Opcional de Destrucción: Integra la opción de permitir hacer vengadores.pop() si el usuario escribe la palabra secreta "Sacrificar".

vengadores = []
palabra_secreta = "SACRIFICAR"

while True:
    print("\nMenú: \n1. Agregar Avenger\n2. Mostrar Base\n3. Destrucción\n4. Salir")
    eleccion = int(input("Ingrese su elección: "))
    if eleccion == 1:
        nombre_heroe = input("\nIngrese el nombre del héroe: ")
        vengadores.append(nombre_heroe)
    elif eleccion == 2:
        print("\n-------- BASE --------")
        for i in range(len(vengadores)):
            print(f"{i}-{vengadores[i]}")
            vengadores[i] = vengadores[i].upper()
        print("----------------------")
    elif eleccion == 3:
        print("\nHa ingresado al modo de DESTRUCCIÓN...")
        palabra_ingresada = input("Ingrese la palabra secreta para eliminar a un héroe: ").upper()
        if len(vengadores) > 0 and palabra_ingresada == palabra_secreta:
            vengadores.pop()
            print("----- Héroe eliminado -----")
        elif palabra_ingresada != palabra_secreta:
            print("\nNo has adivinado la palabra...")
        else:
            print("\n----- No hay héroes en la base -----")
    elif eleccion == 4:
        print("\nSaliendo del programa...")
        break
    else:
        print("\nIngrese una opción correcta")

