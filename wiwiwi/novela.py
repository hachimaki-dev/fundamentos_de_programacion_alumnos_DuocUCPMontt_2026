import os
import subprocess
import time

RESET = '\033[0m'

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

B_BLACK = '\033[40m'
B_RED = '\033[41m'
B_GREEN = '\033[42m'
B_YELLOW = '\033[43m'
B_BLUE = '\033[44m'
B_MAGENTA = '\033[45m'
B_CYAN = '\033[46m'
B_WHITE = '\033[47m'

BOLD = '\033[1m'
UNDERLINE = '\033[4m'

current_dialog = ""

def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        subprocess.run('cls', shell=True, check=True)
    else:
        # Command for Linux/macOS (posix)
        subprocess.run('clear', shell=True, check=True)

def mostrar_mensaje(mensaje):
    lista_de_caracteres = list(mensaje)

    for caracter in lista_de_caracteres:
        print(caracter, end = "", flush = True)

        match caracter:
            case " ":
                time.sleep(0.01)
            case ".":
                time.sleep(0.4)
            case ",":
                time.sleep(0.2)
            case ";":
                time.sleep(0.2)
            case _:
                time.sleep(0.04)
    
    print(RESET + "\n", end = "", flush = True)

def esperando_input_para_seguir():
    time.sleep(0.2)
    input("\n---> ENTER")
    clear_screen()  

def input_int(min, max):
    respuesta_correcta = False
    respuesta = -1
    es_int = False

    while not respuesta_correcta:
        try:
            respuesta = int(input())
            es_int = True
        except ValueError:
            print("", end = "")

        if es_int:
            if respuesta >= min and respuesta <= max:
                respuesta_correcta = True

    return respuesta

def responder_alternativa(min, max):
    preguntar_alternativa = True
    respuesta = -1

    while preguntar_alternativa:
        respuesta = input_int(min, max)

        if respuesta >= 1:
            preguntar_alternativa = False

    clear_screen()

    return respuesta

clear_screen()

mostrar_mensaje("Vas caminando tranquilamente por la playa. Es de noche y el cielo está despejado; la luna brilla con un fulgor fascinante.")
mostrar_mensaje("No hay ninguna otra persona cerca.")
mostrar_mensaje("Hace más de un mes que empezaste esta rutina para despejar tus problemas que no te dejan dormir con tranquilidad.")
mostrar_mensaje("Cada vez te encariñas más con el sonido de las olas y el olor de la brisa se te hace más familiar.")
mostrar_mensaje("Definitivamente te sientes más relajado que hace un tiempo atrás.")

esperando_input_para_seguir()

mostrar_mensaje(f"{YELLOW}Sin embargo...")

esperando_input_para_seguir()

mostrar_mensaje(f"{YELLOW}Un inesperado vendaval te empieza a sacudir fuertemente desde el mar.")
mostrar_mensaje(f"{YELLOW}El suave olor de la brisa con la que te has estado familiarizando en estas últimas semanas se transforma súbitamente en un horrible olor a putrefacción, como si estuviese acarreando los cadáveres nauseabundos de los peces más extraños y grotescos de la profundidad del océano.")
mostrar_mensaje(f"{YELLOW}No entiendes qué está pasando, pero claramente no deberías estar acá.")
mostrar_mensaje(f"{YELLOW}¿Qué deberías hacer?\n")
time.sleep(1)

print("1) Cubrirme la cara con los brazos para protegerme del viento y evitar el mal olor.")
print("2) Correr y alejarme del mar.")

respuesta = responder_alternativa(1, 2)

match respuesta:
    case 1:
        mostrar_mensaje(f"En un intento desesperado de enfrentar el extraño fenómeno intentas protegerte cubriéndote la cara, pero {MAGENTA}es inútil.")
        mostrar_mensaje(f"El {YELLOW}hedor{RESET} sigue siendo igual de {YELLOW}insoportable{RESET} y los {YELLOW}fuertes vientos sacuden violentamente{RESET} el resto de tu cuerpo.")
    case 2:
        mostrar_mensaje(f"Intentas huir alejándote del mar, pero notas que mientras más intentes alejarte, {YELLOW}más fuerte es el hedor y con más fuerza te golpean los vientos.")
        mostrar_mensaje(f"Sientes una {MAGENTA}impotente aversión{RESET} con tu {MAGENTA}intento de huída,{RESET} por lo que decides volver a acercarte al mar con la {GREEN}ilusión{RESET} de que, de alguna extraña manera, {GREEN}toda esta situación deje de empeorar.")
        mostrar_mensaje(f"{RED}Estabas equivocado.")

time.sleep(1)