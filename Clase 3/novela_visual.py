#se importa las librerias de sys y time para la ejecucion de dormir el programa por unos segundos y el de sys que permite interacturar como interprete entre el lenguaje de programacion y el del sistema operativo
import sys
import time
print("-----------ESTUDIANTE DEL DUOC------------")
print("Bienvenido , puede ingresar su nombre?")
nombre = input()
time.sleep(2)
print("Cargando...")
time.sleep(10)
print(f"TU AVENTURA COMIENZA {nombre}, ESTAS DESPERTANDO PARA IR AL INSTITUTO")
print("Que deseas realizar a continuacion?")
print("1.Levantarte de la cama")
print("2.Quedarse dormido")
time.sleep(10)
#Primeras opciones para el protagonista 
opcion=input("Ingrese su opcion como numero")
print("Pulse Enter para continuar")
if opcion == "1" : 
    print("FELICIDADES POR OTRO DIA MAS HACIA EL INSTITUTO!")
    input()
    print("Ahora debes de tomar una decision dificil ya que el tiempo apremia , deberias de tomar desayuno  o tomar una ducha?")
    time.sleep(10)
    print("1.Tomar ducha")
    print("2.Tomar desayuno")
elif opcion == "2" :
    print ("Sera en otra ocasion!")
    sys.exit
opcion2 = input("Ingrese su opcion como numero")

if opcion2 : "1"
print("Tomaste la ducha , pero te estas tardando mucho tiempo , asi que con las prisas no pudiste tambien tomar desayuno!")
time.sleep(5)
print("Lo unico que te resta por hacer es alistarte y esperar la micro")
