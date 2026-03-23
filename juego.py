import time
import os
import sys
import random

normalC = "\033[0m"
redC = "\033[91m"
greenC = "\033[92m"
yellowC = "\033[93m"
blueC = "\033[94m"
cyanC = "\033[96m"
grayC = "\033[90m"

name_player = ""
inventary = []
tool = False
opcion_ventilacion = ""

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir(texto, velocidad=0.05, color=normalC):
    sys.stdout.write(color)
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print(normalC)

def suspenso(segundos):
    for _ in range(segundos):
        sys.stdout.write(grayC + ". ")
        sys.stdout.flush()
        time.sleep(2)
    print(normalC)

def sobreviviste():
    limpiar()
    escribir(f"{greenC}FELICIDADES {blueC}{name_player}{normalC}, HAS SOBREVIVIDO A LA CRIATURA Y LOGRASTE ESCAPAR DE {yellowC}ASGARD{normalC}.", 0.05)
    time.sleep(3)
    limpiar()

def game_over():
    limpiar()
    escribir(f"{redC}GAME OVER", 0.5)
    time.sleep(3)
    limpiar()

def inicio():
    limpiar()
    escribir(f"Es tu segunda semana trabajando en {yellowC}ASGARD{normalC}, una empresa de prestigio dentro del área farmacéutica. Eres el encargado de la seguridad del ala oeste de las instalaciones, un lugar donde se experimenta con virus y enfermedades para desarrollar nuevos medicamentos, o eso crees. Tu trabajo es sencillo: no permitir que nadie entre a esa zona sin autorización y monitorear las cámaras de seguridad. Llegas a tu oficina y enciendes la computadora para iniciar tu turno.", 0.05)
    time.sleep(4)
    menu_principal()

def menu_principal():
    limpiar()
    print(greenC + "==================================================================")
    print("      CENTRAL DE SEGURIDAD ASGARD - SISTEMA ODÍN - Ala Oeste")
    print("==================================================================" + normalC)
    escribir(f"\n{greenC}[SISTEMA]:{grayC} Presione ENTER para iniciar sesión", 0.02)
    input()
    login()

def login():
    global name_player
    limpiar()
    escribir(f"{greenC}[SISTEMA]:{grayC} SISTEMA DE SEGURIDAD ODÍN - INICIO DE SESIÓN", 0.03)
    print(f"{greenC}{'=' * 70}{normalC}")
    escribir(f"{greenC}[SISTEMA]:{grayC} Ingrese su nombre de usuario:", 0.05, grayC)
    name_player = input("> ")
    confirmacion_usuario()

def confirmacion_usuario():
    limpiar()
    escribir(f"{greenC}[SISTEMA]:{grayC} Confirmando identidad de {yellowC}{name_player}{grayC}...", 0.05)
    suspenso(3)
    if random.random() < 0.9:
        escribir(f"{greenC}[SISTEMA]:{grayC} Usuario {yellowC}{name_player}{grayC} autenticado correctamente.", 0.05, grayC)
        time.sleep(3)
        fallo_seguridad()
    else:
        escribir(f"{redC}[SISTEMA]:{grayC} Error de conexión. Intente nuevamente.", 0.05, grayC)
        time.sleep(2)
        login()

def fallo_seguridad():
    limpiar()
    escribir("Escuchas un fuerte sonido de alarma proveniente de la sala de contenedores del ala oeste. Parece que algo ha ocurrido; decides revisar las cámaras de seguridad para ver qué está pasando.", 0.05)
    time.sleep(2)
    escribir(f"{redC}ALERTA DE SEGURIDAD: {grayC}Fallo de seguridad en el contenedor {redC}X-456T {grayC}del ala oeste. Se ha detectado una brecha en el sistema de contención. Se recomienda evacuar la zona inmediatamente.{normalC}", 0.05)
    time.sleep(2)
    escribir(f"Al mirar las cámaras de seguridad, ves que el contenedor {redC}X-456T {normalC}está abierto y alguien tiene el virus que se encontraba ahí. Notas que es un científico de ASGARD que estuvo trabajando allí por unos días. Toma el inyector con el virus y {redC}se lo inyecta en el cuello{normalC}.", 0.05)
    time.sleep(5)
    limpiar()
    suspenso(3)
    escribir(f"El científico comienza a convulsionar y a gritar. Parece que el virus está haciendo efecto; de repente se detiene y queda completamente inmóvil. Luego de unos segundos, comienza a {redC}mutar violentamente en una criatura monstruosa. Su tamaño aumenta, pareciéndose más a un gorila; se le desfigura la cara, le salen garras afiladas y sus ojos se vuelven rojos brillantes. De los codos salen huesos afilados que parecen cuchillas. La criatura se lanza hacia la cámara de seguridad y la destroza{normalC}.", 0.05)
    time.sleep(2)
    escribir(f"¿Qué haces?\n{cyanC}1. Ir a la sala de contenedores. \n2. Ir a la salida de emergencia. \n3. Revisar el cajón de tu escritorio.", 0.05)
    opcion = input(f">{grayC} elige una opción: {normalC}")

    if opcion == "1":
        sala_contenedores()
    elif opcion == "2":
        salida_emergencia()
    elif opcion == "3":
        cajon_escritorio()

def sala_contenedores():
    limpiar()
    escribir(f"Decides ir a la sala de contenedores. Al entrar, la criatura ya no está allí. Miras a los alrededores y ves que en el techo hay una {yellowC}rejilla de ventilación rota{normalC}; parece que la criatura se ha escapado por allí. Sigues mirando a los alrededores y notas que falta un virus en el contenedor {redC}Z-012{normalC}. Al leer la etiqueta, te das cuenta que es un virus que puede ser usado para controlar a las personas. Deduces que alguien infectó al científico para que se inyectara el virus {redC}X-456T{normalC} y así controlar a la criatura. Escuchas un ruido proveniente de la rejilla de ventilación y otro proveniente de la puerta de salida. \n¿Qué haces?\n{cyanC}1. Ir a la rejilla de ventilación. \n2. Ir a la puerta de salida.", 0.05)
    opcion = input(f">{grayC} elige una opción: {normalC}")
    if opcion == "1":
        rejilla_ventilacion()
    elif opcion == "2":
        puerta_de_salida()

def rejilla_ventilacion():
    global opcion_ventilacion
    limpiar()
    escribir(f"Decides ir a la rejilla de ventilación. Mueves unas mesas para poder subirte y entrar. Al entrar, está completamente oscuro. Te arrastras durante unos minutos hasta que llegas a una esquina donde se divide en dos caminos y escuchas {redC}ruidos provenientes de ambos lados{normalC}. Parece que {yellowC}la criatura está en uno de ellos.{normalC} \n¿Qué camino eliges?\n{cyanC}1. Camino de la izquierda. \n2. Camino de la derecha.", 0.05)
    opcion_ventilacion = input(f">{grayC} elige una opción: {normalC}")
    if opcion_ventilacion == "1" or opcion_ventilacion == "2":
        muerte_ventilacion()

def muerte_ventilacion():
    limpiar()
    direccion_ventilacion = "izquierda" if opcion_ventilacion == "1" else "derecha"
    escribir(f"Decides ir por el camino de la {blueC}{direccion_ventilacion} {normalC}y avanzas por la rejilla. De repente, escuchas un ruido fuerte y {redC}sientes que algo te agarra por la espalda.{normalC} Es la criatura; te arrastra hacia ella. De tronco se abre una boca con dientes afilados y te da un mordisco. Sientes un dolor intenso. La ventilación colapsa y caes. Al mirarte, ves que te falta desde la cintura para abajo. {redC}Has muerto.{normalC}", 0.05)
    time.sleep(5)
    game_over()

def puerta_de_salida():
    limpiar()
    escribir(f"Decides ir a la puerta de salida. Al abrirla, ves un pasillo largo e iluminado con una luz parpadeante. Al avanzar, escuchas {redC}ruidos{normalC} provenientes del techo. Estás por abrir la puerta para salir al hall de entrada cuando de repente {redC}la criatura cae del techo y te ataca.{normalC} Te da un golpe con las garras y te lanza contra la pared. Intentas pararte pero no tienes fuerzas. Ves donde te golpeó y tienes {redC}los intestinos expuestos. {normalC}La criatura te agarra y te levanta; de su tronco se abre una boca con dientes afilados y {redC}te devora. \nHAS MUERTO.", 0.06)
    time.sleep(6)
    game_over()

def salida_emergencia():
    global tool
    limpiar()
    escribir(f"Decides ir a la salida de emergencia. Al intentar abrir la puerta, notas que está atascada. Miras alrededor y ves que tiene {yellowC}pernos de seguridad{normalC}; parece que necesitas una {yellowC}llave{normalC} para poder abrirla.", 0.05)
    if tool:
        escribir(f"Usas la {blueC}llave {normalC}que encontraste en el cajón de tu escritorio para abrir la puerta. Luego de quitar los pernos, logras abrirla y sales a unas escaleras de emergencia. Bajas las escaleras y ves que unos helicópteros de ASGARD llegan para evacuar a los empleados. Logras subirte a uno de ellos y escapas. \n{greenC}HAS SOBREVIVIDO", 0.05)
        time.sleep(4)
        sobreviviste()
    else:
        escribir(f"No tienes la {redC}llave {normalC}para abrir la puerta.\n ¿Qué haces?\n{cyanC}1. Ir a la sala de contenedores. \n2. Revisar el cajón de tu escritorio.", 0.05)
        opcion = input(f">{grayC} elige una opción: {normalC}")
        if opcion == "1":
            sala_contenedores()
        elif opcion == "2":
            cajon_escritorio()

def cajon_escritorio():
    global tool
    limpiar()
    escribir(f"Decides revisar el cajón de tu escritorio. Al abrirlo, ves que hay una {yellowC}llave española{normalC}. Tomas la llave y {blueC}la guardas en tu riñonera.{normalC}", 0.05)
    tool = True
    escribir(f"¿Qué haces ahora?\n{cyanC}1. Ir a la salida de emergencia. \n2. Ir a la sala de contenedores.", 0.05)
    opcion = input(f">{grayC} elige una opción: {normalC}")
    if opcion == "1":
        salida_emergencia()
    elif opcion == "2":
        sala_contenedores()

inicio()