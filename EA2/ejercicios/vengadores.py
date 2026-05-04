'''Thanos se acerca. Nick Fury de Marvel necesita un programa que le permita alistar a los Avengers en la base. Si envía a alguien al frente, debe ser eliminado de la base usando menús.

Instrucciones:

Inicializa tu base vengadores = [].
Inicia un ciclo infinito while True: con un menú de opciones numéricas: 1-Agregar Avenger, 2-Mostrar Base y Modificar, 3-Salir.
Si es 1: Solicita al usuario el nombre del héroe y lo agregas al final de la lista. (Pista: .append())
Si es 2: Recorre la lista por Índices: for i in range(len(vengadores)): e imprime cada héroe junto a su código de posición (Ej: `0 - Iron Man`, `1 - Thor`). Luego permite a Fury poner en mayúsculas a todos los héroes procesando: vengadores[i] = vengadores[i].upper().
Opcional de Destrucción: Integra la opción de permitir hacer vengadores.pop() si el usuario escribe la palabra secreta "Sacrificar".'''

vengadores = []

while True:
    print("-   1. Agregar Avenger\n-   2. Mostrar Base y Modificar\n-   3. Salir")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        vengadores.append(input("Ingresa el nombre del héroe"))
    elif opcion == 2:
        for i in range(len(vengadores)):
            