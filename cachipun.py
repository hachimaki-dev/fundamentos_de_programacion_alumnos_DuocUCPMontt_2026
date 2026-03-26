import os
import subprocess

RESET = '\033[0m'

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

puntaje_primer_jugador = 0
puntaje_segundo_jugador = 0

nombre_primer_jugador = "Miguel"
nombre_segundo_jugador = "Mauricio"

mano_de_primer_jugador = ""
mano_de_segundo_jugador = ""

piedra = "Piedra"
papel = "Papel"
tijera = "Tijera"

def limpiar_pantalla():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        subprocess.run('cls', shell=True, check=True)
    else:
        # Command for Linux/macOS (posix)
        subprocess.run('clear', shell=True, check=True)

def esperando_input_para_seguir():
    input("\n---> ENTER")
    limpiar_pantalla() 

def ha_terminado_la_partida():
    return puntaje_primer_jugador == 3 or puntaje_segundo_jugador == 3

def mostrar_opciones_al_jugador(nombre_jugador_actual):
    mostrar_tabla_puntajes()

    if mano_de_primer_jugador != "":
        print(f"{nombre_primer_jugador} ---> {mano_de_primer_jugador}\n")
    
    print(f"Jugador {nombre_jugador_actual}, juegue:")
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijera.")

def escogiendo_opcion_correcta(nombre_jugador):
    while True:
        mostrar_opciones_al_jugador(nombre_jugador)
        opcion_del_jugador_actual = int (input(""))

        if opcion_del_jugador_actual >= 1 and opcion_del_jugador_actual <= 3:
            return opcion_del_jugador_actual
        else:
            mostrar_anuncio("X Error X. Escoja un número entre 1 y 3.")

def mostrar_anuncio(anuncio):
    limpiar_pantalla()
    print(anuncio)
    esperando_input_para_seguir()

def mostrar_tabla_puntajes():
    print(f"***********************************")
    if puntaje_primer_jugador == puntaje_segundo_jugador:
        if puntaje_primer_jugador > 0 and puntaje_segundo_jugador > 0:
            print(f"*** {YELLOW}{nombre_primer_jugador} : {puntaje_primer_jugador}{RESET} /// {YELLOW}{nombre_segundo_jugador} : {puntaje_segundo_jugador}{RESET} ***")
        else:
            print(f"*** {nombre_primer_jugador} : {puntaje_primer_jugador} /// {nombre_segundo_jugador} : {puntaje_segundo_jugador} ***")
    if puntaje_primer_jugador > puntaje_segundo_jugador: 
        print(f"*** {GREEN}{nombre_primer_jugador} : {puntaje_primer_jugador}{RESET} /// {RED}{nombre_segundo_jugador} : {puntaje_segundo_jugador}{RESET} ***")
    if puntaje_segundo_jugador > puntaje_primer_jugador:
        print(f"*** {RED}{nombre_primer_jugador} : {puntaje_primer_jugador}{RESET} /// {GREEN}{nombre_segundo_jugador} : {puntaje_segundo_jugador}{RESET} ***")
    print(f"***********************************\n")

def obtener_nombre_de_mano_por_numero(numero):
    if numero == 1:
        return piedra
    if numero == 2:
        return papel
    if numero == 3:
        return tijera

def comparar_manos(mano_de_primer_jugador, mano_de_segundo_jugador, nombre_primer_jugador, nombre_segundo_jugador):
    if mano_de_primer_jugador == mano_de_segundo_jugador:
        mostrar_anuncio("¡Ha habido un EMPATE!")
    else:
        global puntaje_primer_jugador
        global puntaje_segundo_jugador

        if mano_de_primer_jugador == piedra and mano_de_segundo_jugador == tijera:
            mostrar_anuncio(f"El jugador {nombre_primer_jugador} ha ganado +1 punto.")
            puntaje_primer_jugador += 1
        if mano_de_primer_jugador == piedra and mano_de_segundo_jugador == papel:
            mostrar_anuncio(f"El jugador {nombre_segundo_jugador} ha ganado +1 punto.")
            puntaje_segundo_jugador += 1
        if mano_de_primer_jugador == tijera and mano_de_segundo_jugador == papel:
            mostrar_anuncio(f"El jugador {nombre_primer_jugador} ha ganado +1 punto.")
            puntaje_primer_jugador += 1
        if mano_de_primer_jugador == tijera and mano_de_segundo_jugador == piedra:
            mostrar_anuncio(f"El jugador {nombre_segundo_jugador} ha ganado +1 punto.")
            puntaje_segundo_jugador += 1
        if mano_de_primer_jugador == papel and mano_de_segundo_jugador == piedra:
            mostrar_anuncio(f"El jugador {nombre_primer_jugador} ha ganado +1 punto.")
            puntaje_primer_jugador += 1
        if mano_de_primer_jugador == papel and mano_de_segundo_jugador == tijera:
            mostrar_anuncio(f"El jugador {nombre_segundo_jugador} ha ganado +1 punto.")
            puntaje_segundo_jugador += 1

limpiar_pantalla()

while not ha_terminado_la_partida():
    opcion_primer_jugador = escogiendo_opcion_correcta(nombre_primer_jugador)
    mano_de_primer_jugador = obtener_nombre_de_mano_por_numero(opcion_primer_jugador)

    limpiar_pantalla()

    opcion_segundo_jugador = escogiendo_opcion_correcta(nombre_segundo_jugador)
    mano_de_segundo_jugador = obtener_nombre_de_mano_por_numero(opcion_segundo_jugador)

    comparar_manos(mano_de_primer_jugador, mano_de_segundo_jugador, nombre_primer_jugador, nombre_segundo_jugador)

    mano_de_primer_jugador = ""
    mano_de_segundo_jugador = ""

nombre_ganador = ""
puntaje_ganador = 0
puntaje_perdedor = 0

if puntaje_primer_jugador > puntaje_segundo_jugador:
    nombre_ganador = nombre_primer_jugador
    puntaje_ganador = puntaje_primer_jugador
    puntaje_perdedor = puntaje_segundo_jugador
if puntaje_segundo_jugador > puntaje_primer_jugador:
    nombre_ganador = nombre_segundo_jugador
    puntaje_ganador = puntaje_segundo_jugador
    puntaje_perdedor = puntaje_primer_jugador

print(f"¡Ha ganado el jugador {nombre_ganador} con un puntaje de {puntaje_ganador} - {puntaje_perdedor}!")