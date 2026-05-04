# Calculadora Avanzada #
# Mi nombre es Héctor Gallegos y hoy 'creare' una calculadora más# 
# usando los siguientes comandos 'ValueError' , 'ZeroDivisionError' , 'FileNotFoundError' #
# Esta calculadora contiene las siguientes caracteristicas :
    # 1. Operadores básicos como por ejemplo :
            # - Suma , Resta , Multiplicación y División.
           
    # 2. Operadores más avanzados :
            # - Potencía, Raíz Cuadrada y Porcentaje.

    # 3. Función de Guardado :
            # Historial de de cálculos , lectura de Archivos y Guardar resultados.

# Fin.

# Librerías #

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"

from colorama import Fore, Style , init 
import time
import sys
import pyfiglet
init ()

# 1. Título (No entendi mucho al inicio pero logre pillarle el truco.) #

def Mostrar_Titulo():
    titulo = pyfiglet.figlet_format("CALCULADORA")
    print(Fore.YELLOW + titulo + Style.RESET_ALL)

Mostrar_Titulo ()

# 2. Una pantalla de carga #

def pantalla_de_carga ():
    
        for i in range (101):
                barra = Fore.GREEN + "█" * (i // 5)
                print (Fore.CYAN + f"\rCargando : {Fore.RESET} [{barra:<20}] {i}%", end= "")
                time.sleep(0.02)
        
        print ()

        print ("\n Sistema listo \n")

pantalla_de_carga ()

def inicio (texto, velocidad = 0.06):
       for letra in texto:
              print (letra, end= "", flush=True)
              time.sleep(velocidad)
print() 
       
inicio("\n Bienvenido a la \033[91mcalculadora avanzanda\033[0m \n" \
"\n\033[92mEsta cuenta con un siste más legile y con una multifuncionalidad\n" \
"Ademas contiene las siguientes funciones : \033[0m\n" \
        "\n\033[93m 1. Suma y resta más legibles\033[0m\n" \
        "\n\033[93m 2. Multiplicación y Divisiones\033[0m\n" \
        "\n\033[93m 3. Potencía, Raices Cuadradas y Porcentajes\033[0m\n" \
        "\n\033[93m 4. Historial de los Calculos, Lecturas de Archivos\n\033[0m" \
        "\n\033[92m Ahora espere unos minutos en lo que carga el \033[91mMenú.\033[0m\n")
print ()


for i in range(101):
       barra = Fore.GREEN + "█" * (i // 5)
       print (Fore.CYAN +f"\rCargando : {Fore.RESET} [{barra:<20}] {i}%", end= "")
       time.sleep(0.02)
print ()

print ("\n\033[92m Carga Completada con exito...")

print ("\n\033[93m MENÚ LISTO... \n\033[0m")



       
def segundo_menu ():
        menu = pyfiglet.figlet_format("Menu")
        print (Fore.RED + menu + Style.RESET_ALL)
              
segundo_menu ()

while True :

        def opciones (texto, velocidad = 0.06):
                for letra in (texto):
                        print (letra, end= "" , flush=True)
                        time.sleep(velocidad)
                print ()

        opciones("\n\033[92m A continuación se mostraran las\033[0m \033[91mopciones disponibles.\n\033[0m" \
        "\n\033[93m 1. SUMAR O RESTAR \033[0m" \
        "\n\033[93m 2. MÚLTIPLICAR O DIVIDIR\033[0m" \
        "\n\033[93m 3. POTENCÍA, RAÍZ CUADRADA O PORCENTAJES\033[0m" \
        "\n\033[93m 4. VER HISTORIAL\033[0m" \
        "\n\033[91m 5. SALIR \n\033[0m")

        print (end=" ")
        print ()

        try :
                opcion_de_usuario = int(input("¿Qué desea hacer el día de hoy? : "))

                if opcion_de_usuario > 5 :
                        print ("\n\033[91mERROR : NÚMERO NO IDENTIFICADO.\033[0m\n")

        except ValueError : 
                ("\n\033[91mERROR : INGRESE NÚMERO DEL 1 AL 5.\033[0m\n")