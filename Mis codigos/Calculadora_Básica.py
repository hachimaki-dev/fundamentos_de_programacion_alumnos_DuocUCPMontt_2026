ROJO = "\033[91m"
RESET = "\033[0m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MORADO = "\033[95m"

import time
import sys

print ("\n/============================/")
print ("/===/ CALCULADORA BÁSICA /===/")
print ("/============================/\n")


for i in range (101):
    barra = "█" * (i // 5)
    print ("\033[94m" f"\rCargando : \033[0m \033[92m[{barra:<20}] {i}%" , end= " ")
    time.sleep(0.006)

print ()
print ()

print ("\033[93mBienvenido a la \033[91m'Calculadora Básica'\033[0m \033[93maquí pondremos a prueba la siguietes funciones.\033[0m \n")

print ("\033[92m1. \033[0m \033[93m ValueError  \033[0m")
print ("\033[92m2. \033[0m \033[93m ZeroDivisionError  \033[0m")
print ("\033[92m3. \033[0m \033[93m FileNotFoundError  \n \033[0m")


input ("Presione cualquier botón para continuar: ")



print ("\n Un resumen basico de estas funciones son las siguientes:\n")
print (" \033[91m- ValueError\033[0m \033[93mestá función  en caso de ver \033[91mtexto donde se encuenta un entero\033[0m \033[93meste lanzara un error.")
print (" \033[91m- ZeroDivisionError\033[0m \033[93mestá función  en caso de \033[91mdividir entre 0\033[0m \033[93meste lanzara un error.")
print (" \033[91m- FileNotFoundError\033[0m \033[93mestá función  en caso de \033[91mno encontrar un archivo\033[0m \033[93meste lanzara un error.\033[0m\n")

input ("Presione cualquier botón para continuar: ")

print ("\nEspere un momento.")
print ("Estamos cargando algunos datos.")
print ("Esto puede demorar unos minutos.\n")

for i in range (101):
    barra = "█" * (i // 5)
    print ("\033[94m" f"\rCargando : \033[0m \033[92m[{barra:<20}] {i}%" , end= " ")
    time.sleep(0.2)

print ()

print ("\n\033[92mCarga completada...\033[0m\n")

print ("Calculadora ya disponible.\n")

while True :

    print ("\033[93m\n¿Que desea hacer el día de hoy?\n\033[0m")

    print ("\033[92m 1 ➕ Sumar o Restar ➖ \033[0m")
    print ("\033[92m 2 ✖️  Multiplicar o Dividir ➗\033[0m ")
    print ("\033[92m 3 📄 Ver historial\033[0m📄")
    print ("\033[91m 4 ❌  Salir ❌\033[0m\n")

    try :
                Opcion_de_Usuario = int(input("\033[93mIngrese su elección : \033[0m"))

                match Opcion_de_Usuario:
                    case 1:
                        print ("\n¿Desea ➕ Sumar o ➖ restar?\n")
                        Eleccion_de_Usuario = str(input("\033[93mEscriba su Opción : \033[0m")).lower()

                        match Eleccion_de_Usuario:
                            case "sumar":
                                print ("\033[93mIngrese los números que desea ➕ sumar\033[0m\n")

                                while True :
                                    try:
                                        Numero_1 = int(input("Número 1 : "))
                                        Numero_2 = int(input("Número 2 : "))

                                        Resultado = Numero_1 + Numero_2

                                        print (f"\n\033[92mEl resultado de su suma es {Resultado}\033[0m\n") 
                                        print ("¿Desea continuar?\n")

                                        Eleccion_de_Usuario_2 = str(input("\033[93mIngrese (SI/NO) : \033[0m")).lower()

                                        if Eleccion_de_Usuario_2 == "si":
                                            continue  

                                        elif Eleccion_de_Usuario_2 == "no": 
                                            break

                                    except ValueError :
                                        print ("\033[91mIngrese solo números\033[0m")


                            case "restar":
                                print ("\033[93mIngrese los números que desea ➖ restar\033[0m\n")
                                while True :
                                    try:
                                        Numero_1 = int(input("Número 1 : "))
                                        Numero_2 = int(input("Número 2 : "))

                                        Resultado = Numero_1 - Numero_2

                                        print (f"\n\033[92mEl resultado de su resta es {Resultado}\033[0m\n") 
                                        print ("¿Desea continuar?\n")

                                        Eleccion_de_Usuario_2 = str(input("\033[93mIngrese (SI/NO) : \033[0m")).lower()

                                        if Eleccion_de_Usuario_2 == "si":
                                            continue  

                                        elif Eleccion_de_Usuario_2 == "no": 
                                            break

                                    except ValueError :
                                        print ("\033[91mIngrese solo números\033[0m")

                    case 2:
                        print ("\n¿Desea ✖️  Multiplicar o Dividir ➗?\n")
                        Eleccion_de_Usuario = str(input("\033[93mEscriba su Opción : \033[0m")).lower()

                        match Eleccion_de_Usuario: 
                            case "multiplicar" : 
                                print ("\033[93mIngrese los números que desea ✖️ Multiplicar\033[0m\n")
                                while True :
                                    try:
                                        Numero_1 = int(input("Número 1 : "))
                                        Numero_2 = int(input("Número 2 : "))

                                        Resultado = Numero_1 * Numero_2

                                        print (f"\n\033[92mEl resultado de su multiplicación es {Resultado}\033[0m\n") 
                                        print ("¿Desea continuar?\n")

                                        Eleccion_de_Usuario_2 = str(input("\033[93mIngrese (SI/NO) : \033[0m")).lower()

                                        if Eleccion_de_Usuario_2 == "si":
                                            continue  

                                        elif Eleccion_de_Usuario_2 == "no": 
                                            break

                                    except ValueError :
                                        print ("\033[91mIngrese solo números\033[0m")


                            case "dividir": 
                                print ("\033[93mIngrese los números que desea ➗ dividir\033[0m\n")
                                while True :
                                    try:
                                        Numero_1 = int(input("Número 1 : "))
                                        Numero_2 = int(input("Número 2 : "))

                                        Resultado = Numero_1 / Numero_2

                                        print (f"\n\033[92mEl resultado de su división es {Resultado}\033[0m\n") 
                                        print ("¿Desea continuar?\n")

                                        Eleccion_de_Usuario_2 = str(input("\033[93mIngrese (SI/NO) : \033[0m")).lower()

                                        if Eleccion_de_Usuario_2 == "si":
                                            continue  

                                        elif Eleccion_de_Usuario_2 == "no": 
                                            break
  

                                    except ValueError :
                                        print ("\033[91mIngrese solo números\033[0m")
                                    except ZeroDivisionError :
                                        print ("\033[91mERROR : No se puede dividir entre 0\033[0m")


                    case 3: 
                        while True :
                            
                            print ("\n/===================/")
                            print ("/====/Historial/====/")
                            print ("/===================/\n")

                            print ("1. ➕ \033[92mVer historial de Sumas ➕\033[0m")
                            print ("2. ➖ \033[92mVer historial de Restas ➖\033[0m")
                            print ("3. ✖️ \033[92m Ver historial de Multiplicaciones ✖️\033[0m")
                            print ("4. ➗ \033[92mVer historial de Divisiones ➗\033[0m")
                            print ("5. ❌ \033[91mVolver al menú principal ❌\033[0m\n")

                            try:
                                Opcion_Historial = int(input("\033[93mIngrese su elección : \033[0m"))

                                match Opcion_Historial :

                                    case 1:
                                        try:
                                            with open("suma.txt", "r", encoding="utf-8") as archivo:
                                                print("\n--- Historial de Sumas ---\n")
                                                print(archivo.read())
                                        except FileNotFoundError:
                                            print("\033[91mNo hay historial de sumas.\033[0m")
                                        finally:
                                            print("\033[94m[Fin del historial]\033[0m\n")
                                    

                                    case 2:
                                        try:
                                            with open("resta.txt", "r", encoding="utf-8") as archivo:
                                                print("\n--- Historial de Restas ---\n")
                                                print(archivo.read())
                                        except FileNotFoundError:
                                            print("\033[91mNo hay historial de restas.\033[0m")
                                        finally:
                                            print("\033[94m[Fin del historial]\033[0m\n")

                                    case 3:
                                        try:
                                            with open("multiplicacion.txt", "r", encoding="utf-8") as archivo:
                                                print("\n--- Historial de Multiplicación ---\n")
                                                print(archivo.read())
                                        except FileNotFoundError:
                                            print("\033[91mNo hay historial de multiplicación.\033[0m")
                                        finally:
                                            print("\033[94m[Fin del historial]\033[0m\n")

                                    case 4:
                                        try:
                                            with open("division.txt", "r", encoding="utf-8") as archivo:
                                                print("\n--- Historial de Divisiones ---\n")
                                                print(archivo.read())
                                        except FileNotFoundError:
                                            print("\033[91mNo hay historial de divisiones.\033[0m")
                                        finally:
                                            print("\033[94m[Fin del historial]\033[0m\n")

                                    case 5:
                                        print("\033[92mVolviendo al menú principal...\033[0m\n")
                                        break

                                    case _:
                                        print("\033[91mOpción inválida\033[0m")

                                input("Presione cualquier botón para continuar: ")

                            except ValueError:
                                print("\033[91mIngrese un número válido\033[0m")


                    case 4:
                        print ("\n\033[91mSaliendo de la Calculadora.\033[0m")
                        print ("\033[92mGracias por probar.\033[0m\n")
                        break

    except ValueError:
                print ("\n\033[91mPor favor ingrese solo 1 , 2 o 3.\033[0m") 