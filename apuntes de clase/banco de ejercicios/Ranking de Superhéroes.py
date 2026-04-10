import sys
import time
import os

rojo = '\033[31m'
amarillo = '\033[33m'
negrita = '\033[1m'
gris = '\033[90m'
verde = '\033[32m'
cian = '\033[36m'
reset = '\033[0m'

def escribir(texto, velocidad=0.05, nueva_linea=True):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    if nueva_linea:
        print()

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpiar_dinero(texto):
    if isinstance(texto, (int, float)): 
        return texto
    t = str(texto).lower().replace(".", "").strip()
    es_millon = "m" in t or "millon" in t
    numero_limpio = "".join(filter(str.isdigit, t))
    if not numero_limpio:
        return 0
    valor = int(numero_limpio)
    if es_millon:
        return valor * 1000000
    return valor


limpiar()
escribir(f"{verde}{negrita}BIENVENIDO AL RANKING DE SUPERHEROES{reset} \n{negrita}PARA CALCULAR TU RANKING PRIMERO INICIA SESIÓN")
usuario = str(input(f"{negrita}USUARIO{reset}:{gris} "))
escribir(f"{reset}{negrita}CONTRASEÑA{reset}: ", 0.05, nueva_linea=False) 
escribir(f"{gris}*********{reset}", 0.2)
time.sleep(1)
escribir("INICIANDO SESION")
escribir("..........", 0.3)
time.sleep(1)
limpiar()


escribir(f"{verde}{negrita}{usuario}, HAZ INICIADO SESION CORRECTAMENTE.{reset} \n{negrita}PARA CALCULAR TU RANKING INGRESA LOS SIGUIENTES DATOS:")
while True:
    try:
        misiones = int(input(f"\nNUMERO DE MISIONES EXITOSAS: "))
        entrada_costos = input("COSTOS DE DAÑOS CIVILES (ej: 8M o 12000000): ")
        costos_civiles = limpiar_dinero(entrada_costos)
        escribir(f"{cian}CALCULANDO TU RANKING...{reset}")
        time.sleep(3)

        if misiones >= 10 and costos_civiles == 0:
            limpiar()
            escribir(f"{cian}FELICIDADES {usuario}, GRACIAS A TU GRAN TRABAJO TE POSICIONASTE EN LA{reset} '{verde}CATEGORIA S{reset}'")
        elif 5 <= misiones <= 9:
            limpiar()
            escribir(f"{cian}FELICIDADES {usuario}, HICISTE UN BUEN TRABAJO. TE POSICIONASTE EN LA{reset} '{verde}CATEGORIA A{reset}'")
        elif misiones < 5 and costos_civiles > 10000000:
            limpiar()
            escribir(f"{rojo}¡{usuario} CAUSASTE UN DESASTRE! ¡ESTÁS DESPEDIDO!{reset}")
        else:
            limpiar()
            escribir(f"{amarillo}Héroe en observación\n{gris}Tu ranking está en proceso de evaluación...{reset}")
        break
    except ValueError:
        print(f"{rojo}Error: Por favor ingresa un número válido en misiones.{reset}")