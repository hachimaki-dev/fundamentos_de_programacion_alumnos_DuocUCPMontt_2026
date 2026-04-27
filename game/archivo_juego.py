import sys
import time
import os
import random

rojo = '\033[31m'
negrita = '\033[1m'
gris = '\033[90m'
verde = '\033[32m'
cian = '\033[36m'
reset = '\033[0m'

def escribir(texto, velocidad=0.05):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
    


vida_jefe = 700
ataque1 = random.randint(100, 199)
ataque2 = 0
ataque3 = random.randint(200, 300)
ataque_cargado = random.randint(600, 1000)
numero_ataques = 0
ataque_elegido = 0

limpiar()
escribir(f"{cian}EL LABERINTO DE CRETA{reset}")
time.sleep(2)
limpiar()

escribir("El hilo de Ariadna se termina. Tras la ultima esquina, el pasillo se abre en una fosa circular bañada en sangre seca. En el centro, el minotauro devora los restos del ultimo tributo. oye tus pasos y levata la cabeza, sus ojos amarillos se clavan en ti. \n -Minotauro: Atenas se ha quedado sin niños que ahora envía a sus hombres? \n -Teseo: No soy tu banquete monstruo, soy el fin de tu linaje maldito. El mar dejará de traer sangre a estas costas hoy mismo. \n -minotauro: Ven entonces! deja que tus huesos se unan al resto!")
time.sleep(2)
input(f"{gris}Presiona enter para continuar...{reset}")
limpiar()


while vida_jefe > 0:
    limpiar()
    escribir(f"El Minotauro tiene: {negrita}{rojo}{vida_jefe}{reset} puntos de vida.")
    escribir("Ataca!")
    escribir(f"{verde}(1){reset}{negrita} Estocada de Bronce {gris}DAÑO: 100 - 199{reset} \n{verde}(2){reset}{negrita} Golpe con el puño{gris} TU ELIGES EL DAÑO: 0 - 150{reset} \n{verde}(3){reset}{negrita} Tajo de Atenas {gris}DAÑO: 200 - 300{reset} \n{verde}(4){reset}{negrita} IRA DE POSEIDÓN {gris}DAÑO ATAQUE CARGADO: 600 - 1000{reset}", 0.01)
    ataque_elegido = int(input("Elige tu ataque: "))
    if ataque_elegido == 1:
        limpiar()
        escribir("Le das una estocada con tu espada!")
        escribir(f"le quitaste {rojo}{ataque1}{reset} puntos de vida")
        vida_jefe -= ataque1
        numero_ataques += 1
        time.sleep(2)
    elif ataque_elegido == 2:
        limpiar()
        escribir("Con cuanta fuerza golpearas?")
        ataque2 = int(input("ingresa un numero: "))
        if ataque2 > 0 and ataque2 <= 150 :
            escribir(f"Le diste un puñetazo y le quitaste: {rojo}{ataque2}{reset} puntos de vida")
            vida_jefe -= ataque2
            numero_ataques += 1
            time.sleep(2)
        elif ataque2 > 150:
            escribir("Intentas golpearlo con mucha fuerza, eso te hace perder el equilibrio y el minotauro te golpea.")
            time.sleep(2)
        else:
            escribir("Golpeas sin fuerza y no le haces ni cosquillas. \nEl minotauro te da una patada.") 
        time.sleep(2)
    elif ataque_elegido == 3:
        limpiar()
        escribir("Le das un golpe rapido con el filo de la espada en el abdomen")
        escribir(f"le quitaste {rojo}{ataque3}{reset} puntos de vida")
        vida_jefe -= ataque3
        numero_ataques += 1
        time.sleep(2)
    elif ataque_elegido == 4 and numero_ataques >= 2:
        limpiar()
        escribir("le das un golpe rapido en el talon haciendo que se arrodille y le golpeas el cuello con el filo de la espada")
        escribir(f"le quitaste {rojo}{ataque_cargado}{reset} puntos de vida")
        vida_jefe -= ataque_cargado
        numero_ataques -= 2
        time.sleep(2)
    elif ataque_elegido == 4 and numero_ataques < 2:
        limpiar()
        escribir("Aun no puedes usar este ataque... El minotauro te golpea")
        escribir(f"{gris}EL ATAQUE SE CARGA CUANDO REALIZAS DOS GOLPES EXITOSOS{reset}")
        time.sleep(2)
    else:
        limpiar()
        escribir("No atacaste, el minotauro te arroja contra una pared!")
        time.sleep(2)

escribir(f"Los puntos de vida del Minotauro llegan a {rojo}0{reset}.")
time.sleep(2)
limpiar()
escribir(f"{verde}{negrita}FELICIDADES DERROTASTE AL MINOTAURO DE CRETA{reset}")
time.sleep(2)
limpiar