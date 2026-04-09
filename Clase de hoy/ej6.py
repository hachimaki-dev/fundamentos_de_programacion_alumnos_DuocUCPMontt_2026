"""
Requerimientos:
1. Usa un ciclo para las 3 habitaciones (for i in range(1, 4)).
2. En cada habitación, hay una puerta cerrada. El jugador debe elegir: 'Forzar', 'Ganzúa' o 'Buscar Llave'.
3. Lógica de la habitación:
- Si elige 'Buscar Llave', hay un 50% de probabilidad (puedes simularlo pidiendo un número y viendo si es par) de encontrarla. Si la tiene, puede abrir.
- Si elige 'Ganzúa', debe tener la habilidad (pregunta al inicio del juego si es Ladrón o Guerrero). Solo el Ladrón abre con ganzúa.
- Si elige 'Forzar', debe ser Guerrero.
4. Si el jugador no logra abrir la puerta tras 3 intentos fallidos por habitación (ciclo while interno), pierde el juego completo.
"""
intento = 3
print("Antes de empezar el juego")
Eleccion = input("Eres Ladron o Guerrero? ")
print("Respuesta guardada. Esto afectara en el futuro")
for i in range(1, 4):
    while intento != 0:
        print(f"Estas en la habitacion {i}")
        print("Te encuentras en frente una puerta. Intenta abrirla")
        print("""    1) Buscar llave
    2) Ganzua
    3) Forzar""")
        Abrir = int(input())
        if Abrir == 1:
            numero = int(input("Dame un numero "))
            if numero % 2 == 0:
                intento = 3
                print("Lograste abrir la puerta")
                break
            else:
                print("No lograste abrir la puerta")
                intento = intento - 1
        elif Abrir == 2:
            if Eleccion == "Ladron":
                intento = 3
                print("Lograste abrir la puerta")
                break
            else:
                print("No pudiste abrir la puerta")
                intento = intento - 1
        elif Abrir == 3:
            if Eleccion == "Guerrero":
                intento = 3
                print("Lograste abrir la puerta")
                break
            else:
                print("No pudiste abrir la puerta")
                intento = intento - 1
        else:
            print("Respuesta no valida")
            intento = intento - 1
if intento == 0:
    print("Fracasaste")
else:
    print("Ganaste")