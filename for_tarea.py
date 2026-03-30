import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

for letra in "python":
    python = "python"
    letra_mayuscula = letra.capitalize()
    python = python.replace(letra, letra_mayuscula)
    divided_python = list(python)
    time.sleep(0.5)
    for i, n in enumerate(divided_python):
            if n == letra_mayuscula:
                divided_python[i] = f"{Fore.BLACK + letra_mayuscula}"
    print(divided_python)
    print(Fore.RESET + "- - - - - - - - - - -")

# Esto es un WIP