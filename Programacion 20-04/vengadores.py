""" Reto Avanzado: Ensamblando a los Vengadores
Thanos se acerca. Nick Fury de Marvel necesita un programa que le permita alistar a los Avengers en la base. 
Si envía a alguien al frente, debe ser eliminado de la base usando menús.

Instrucciones:

Inicializa tu base vengadores = [].
Inicia un ciclo infinito while True: con un menú de opciones numéricas: 1-Agregar Avenger, 2-Mostrar Base y Modificar, 3-Salir.
Si es 1: Solicita al usuario el nombre del héroe y lo agregas al final de la lista. (Pista: .append())
Si es 2: Recorre la lista por Índices: for i in range(len(vengadores)): 
e imprime cada héroe junto a su código de posición (Ej: `0 - Iron Man`, `1 - Thor`). 
Luego permite a Fury poner en mayúsculas a todos los héroes procesando: vengadores[i] = vengadores[i].upper().
Opcional de Destrucción: Integra la opción de permitir hacer vengadores.pop() si el usuario escribe la palabra secreta "Sacrificar"."""

vengadores = []

while True:
    print("""1-Agregar Avenger
2-Mostrar Base y Modificar
3-Salir.""")
    Respuesta = int(input())
    if Respuesta == 1:
        Nombre_Superheroe = input("Cual es el nombre del avenger?")
        vengadores.append(Nombre_Superheroe)
    elif Respuesta == 2:
        for numero_avenger in range(len(vengadores)):
            print(f"{numero_avenger + 1} - {vengadores[numero_avenger]}")
    elif Respuesta == 3:
        break
    else:
        print()