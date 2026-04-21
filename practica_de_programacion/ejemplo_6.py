# Simula una aventura donde debes atravesar 3 habitaciones consecutivas para ganar.

"""
1. Usa un ciclo para las 3 habitaciones (for i in range(1, 4)).
2. En cada habitación, hay una puerta cerrada. El jugador debe elegir: 'Forzar', 'Ganzúa' o 'Buscar Llave'.
3. Lógica de la habitación:
- Si elige 'Buscar Llave', hay un 50% de probabilidad (puedes simularlo pidiendo un número y viendo si es par) de encontrarla. Si la tiene, puede abrir.
- Si elige 'Ganzúa', debe tener la habilidad (pregunta al inicio del juego si es Ladrón o Guerrero). Solo el Ladrón abre con ganzúa.
- Si elige 'Forzar', debe ser Guerrero.
4. Si el jugador no logra abrir la puerta tras 3 intentos fallidos por habitación (ciclo while interno), pierde el juego completo.
"""

Clase = ""
intentos = 0
ciclo_de_habitacion = True

print("Te encuentras en una habitacion extraña, tendras que escapar")
eleccion_de_clase = input("Que clase eres? (Guerrero | Ladron): ")
eleccion_de_clase = eleccion_de_clase.lower()

for i in range(1, 4):
    intentos = 0
    while ciclo_de_habitacion == True:
        print(f"Habitacion {i} de 3 | Intentos: {intentos}")
        print("Opcion (1) Buscar Llave [50% de chance]")
        print("Opcion (2) Ganzua")
        print("Opcion (3) Forzar")
        seleccion = int(input("[Solo ingrese el numero]: "))
        if seleccion == 1:
            calcular_probabilidad = int(input("Ingrese un numero para calcular el dado: "))
            if calcular_probabilidad & 2 == 0:
                print("Llave encontrada!")
                break
            elif calcular_probabilidad & 2 != 0:
                print("Llave no encontrada")
                intentos += 1
        if seleccion == 2:
            if eleccion_de_clase == "ladron":
                print("La puerta se abre excitosamente!")
                break
            elif eleccion_de_clase != "ladron":
                print("No has podido abrir la puerta")
                intentos += 1
        if seleccion == 3:
            if eleccion_de_clase == "guerrero":
                print("La puerta se abre excitosamente!")
                break
            elif eleccion_de_clase != "guerrero":
                print("No has podido abrir la puerta")
                intentos += 1
        if intentos >= 3:
            print("No has podido escapar")
            exit()

print("Felicidades en tu escape!")
