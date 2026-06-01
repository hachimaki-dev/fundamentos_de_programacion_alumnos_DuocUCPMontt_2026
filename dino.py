# =====================================================
# DINO RUNNER - SOLO PYTHON ESTÁNDAR
# =====================================================

import os
import time
import random


# =====================================================
# CONFIG
# =====================================================

ANCHO = 60
SUELO = 10
GRAVEDAD = 1
FUERZA_SALTO = -4


# =====================================================
# FUNCIONES FUNCIONALES
# =====================================================

def crear_estado():
    return {
        "dino_y": SUELO,
        "velocidad_y": 0,
        "obstaculos": [],
        "score": 0,
        "game_over": False
    }


def aplicar_gravedad(estado):
    nueva_vel = estado["velocidad_y"] + GRAVEDAD
    nueva_y = estado["dino_y"] + nueva_vel

    if nueva_y >= SUELO:
        nueva_y = SUELO
        nueva_vel = 0

    return {
        **estado,
        "dino_y": nueva_y,
        "velocidad_y": nueva_vel
    }


def saltar(estado):
    if estado["dino_y"] == SUELO:
        return {
            **estado,
            "velocidad_y": FUERZA_SALTO
        }

    return estado


def mover_obstaculos(estado):
    nuevos = []

    for obs in estado["obstaculos"]:
        nuevo_x = obs - 1

        if nuevo_x >= 0:
            nuevos.append(nuevo_x)

    return {
        **estado,
        "obstaculos": nuevos
    }


def generar_obstaculo(estado):
    if random.random() < 0.15:
        return {
            **estado,
            "obstaculos": estado["obstaculos"] + [ANCHO - 1]
        }

    return estado


def detectar_colision(estado):
    for obs in estado["obstaculos"]:

        # Dino está en x = 5
        if obs == 5 and estado["dino_y"] >= SUELO:
            return {
                **estado,
                "game_over": True
            }

    return estado


def sumar_puntos(estado):
    return {
        **estado,
        "score": estado["score"] + 1
    }


# =====================================================
# RENDER
# =====================================================

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def crear_pantalla():
    return [[" "] * ANCHO for _ in range(SUELO + 2)]


def dibujar_suelo(pantalla):
    for x in range(ANCHO):
        pantalla[SUELO + 1][x] = "_"

    return pantalla


def dibujar_dino(pantalla, estado):
    x = 5
    y = int(estado["dino_y"])

    pantalla[y][x] = "D"

    return pantalla


def dibujar_obstaculos(pantalla, estado):
    for obs in estado["obstaculos"]:
        pantalla[SUELO][obs] = "#"

    return pantalla


def renderizar(estado):

    pantalla = crear_pantalla()

    pantalla = dibujar_suelo(pantalla)
    pantalla = dibujar_dino(pantalla, estado)
    pantalla = dibujar_obstaculos(pantalla, estado)

    limpiar()

    for fila in pantalla:
        print("".join(fila))

    print(f"\nPuntaje: {estado['score']}")
    print("ENTER = avanzar")
    print("'s' + ENTER = saltar")
    print("'q' + ENTER = salir")


# =====================================================
# LOOP
# =====================================================

def actualizar(estado):

    estado = aplicar_gravedad(estado)
    estado = mover_obstaculos(estado)
    estado = generar_obstaculo(estado)
    estado = detectar_colision(estado)
    estado = sumar_puntos(estado)

    return estado


def juego():

    estado = crear_estado()

    while not estado["game_over"]:

        renderizar(estado)

        comando = input("> ")

        if comando == "s":
            estado = saltar(estado)

        elif comando == "q":
            break

        estado = actualizar(estado)

    print("\nGAME OVER")
    print("Puntaje final:", estado["score"])


# =====================================================
# MAIN
# =====================================================

juego()