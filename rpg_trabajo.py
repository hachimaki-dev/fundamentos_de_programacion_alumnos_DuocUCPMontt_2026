import random

nombres_jugadores = []
vidas_jugadores = []

clases_disponibles = ["Guerrero", "Sanador", "Tanque", "Mago", "Asesino"]

habilidades_enemigo = ["Ataque en área", "Ataque directo", "Stun", "Ataque fuerte"]

vida_clase = [150, 70, 350, 50, 90]
mana_clase = [15, 30, 10, 60, 15]
velocidad_clase = [20, 30, 5, 30, 50]

index_guerrero = 0
index_sanador = 1
index_tanque = 2
index_mago = 3
index_asesino = 4


clase_primer_jugador = 0

nombre_clase_primer_jugador = ""
vida_primer_jugador = 0
mana_primer_jugador = 0
velocidad_primer_jugador = 0

print(velocidad_primer_jugador)

while True :
    print("Escoja su clase: ")

    print("1) Guerrero")
    print("2) Sanador")
    print("3) Tanque")
    print("4) Mago")
    print("5) Asesino")

    clase_primer_jugador = int (input())

    clase_primer_jugador -= 1

    nombre_clase_primer_jugador = clases_disponibles[clase_primer_jugador]
    vida_primer_jugador = vida_clase[clase_primer_jugador]
    mana_primer_jugador = mana_clase[clase_primer_jugador]
    velocidad_primer_jugador = velocidad_clase[clase_primer_jugador]

    print("Mostrando atributos: ")
    print(f"Clase: {nombre_clase_primer_jugador}")
    print(f"Vida: {vida_primer_jugador}")
    print(f"Maná: {mana_primer_jugador}")
    print(f"Velocidad: {velocidad_primer_jugador}")

#numero_aleatorio = random.randint(int (velocidad_asesino * 0.8), int (velocidad_asesino * 1.2))

#print(numero_aleatorio)