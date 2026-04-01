import sys
import random
import time
import os

def escribir(texto, velocidad=0.05):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush() # Obliga a la terminal a imprimir la letra sin esperar al final de la línea
        time.sleep(velocidad)
    print()

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
    


vida_jefe = 1000
ataque1 = 100
ataque2 = 50
ataque3 = 200
ataque_cargado = 500


escribir("Algo se escucha del otro lado de la puerta de la mazmorra", 0.07)
time.sleep(1)
limpiar()
escribir("¡Cuidado! \n Un minotauro atraviesa la puerta y se para delante de ti!")
time.sleep(1)
limpiar()
escribir("-Minotauro: LLegaste muy lejos pero, aquí se termina tu aventura. \n él minotauro levanta un hacha para atacarte pero lo esquivas.", 0.07)

escribir("¡Ataca!")
ataque_elegido = int(input("Elige tu ataque: \n 1) Estocada \n 2) Patada baja \n 3)Fendente \n 4) Ataque cargado"))
while vida_jefe != 0:
    if ataque_elegido == 1:
