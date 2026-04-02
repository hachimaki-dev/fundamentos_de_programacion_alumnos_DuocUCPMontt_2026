# Objetivo: Crear un pequeño simulador de un combate de rol (RPG).

import random
import subprocess
import sys
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

if sys.platform == "win32":
    def clear_console():
        subprocess.run("CLS", shell=True)
if sys.platform == "linux":
    def clear_console():
        subprocess.run("clear", shell=True)

puntos_de_vida_del_jefe = 1000
contador = -1
resultado = ""

print(Fore.RED + "El jefe se acerca! Preparate para la batalla!" + Style.RESET_ALL)
while puntos_de_vida_del_jefe > 0:
    contador += 1
    if contador >= 3:
        print("Ataque Cargado Listo! \n")
    print(f"BARRA DE VIDA ==[{puntos_de_vida_del_jefe}]==")
    print(resultado, "\n")
    resultado = ""
    print("Elija uno de los siguentes ataques (1-3)")
    print(Fore.GREEN + "1. Ataque Basico [Alta Precision | Daño Bajo]")
    print(Fore.GREEN + "2. Ataque Especial [Baja Precision | Daño Alto]")
    print(Fore.GREEN + "3. Ataque Cargado [Alta Precision | Daño Critico]" + Style.RESET_ALL)
    ataque = int(input("[]: "))
    try:
        if ataque == 1:
            chance = random.randint(1, 10)
            if chance >= 3:
                puntos_de_vida_del_jefe -= 100
                resultado = Fore.YELLOW + "Ataque Exitoso!" + Style.RESET_ALL
                clear_console()
            elif chance < 3:
                resultado = Fore.BLUE + "Ataque Fallado!" + Style.RESET_ALL
                clear_console()
        if ataque == 2:
            chance = random.randint(1, 10)
            if chance >= 6:
                puntos_de_vida_del_jefe -= 200
                resultado = Fore.YELLOW + "Ataque Exitoso!" + Style.RESET_ALL
                clear_console()
            elif chance < 6:
                resultado = Fore.BLUE + "Ataque Fallado!" + Style.RESET_ALL
                clear_console()
        if ataque == 3 and contador >= 3:
            puntos_de_vida_del_jefe -= 300
            resultado = Fore.YELLOW + "Ataque Critico!" + Style.RESET_ALL
            contador = 0
            clear_console()
        elif ataque == 3 and contador <= 3:
            resultado = "Cargas insuficientes"
            clear_console()
    except:
        print("Ataque no valido!")

print("Jefe Derrotado! Felicitaciones Heroe!")