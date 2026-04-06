import time
import sys

dia = 1
total_km= 0



print ("/=======================/")
print ("/=======Smartwach=======/")
print ("/=======================/\n")

print ("Para continuar con el protocolo.")
print (" ingrese su Nombre en la sección de abajo.\n")
Nombre_de_usuario = str(input("Ingrese su nombre : "))
print ()

print (f"Bienvenido {Nombre_de_usuario} a tu Smartwatch Activity Tracker.\n")
print ("Con el Smartwach podras ver y analizar tu actividad física durante 7 dias.")
print ("Pero antes de empezar con unas pequeñas intrucciones.\n")
print ("Espere unos segundos...")
time.sleep(2)


print ("INTRUCCIONES DEL TRACKER.\n")

print ("1. Durante los dias debe de ingresar solo los kilometros que haya recorrido.")
print ("2. En caso de que se haya lesionado, debe de ingresar un número negativo. Ejemplo (-1).")
print ("3. Si llega a ingresar algún caracter invalido, solo sera un error.\n")

print (f"dicho esto, emepecemos a ejercitarnos ({Nombre_de_usuario})")
print ()

while dia <= 7:
    km = float(input(f"¿Cuántos km corriste el día {dia}?: "))
    
    if km < 0:
        print("Día saltado\n")
    else:
        total_km += km
    
    dia += 1

print ()
print("======= RESUMEN SEMANAL =======")
time.sleep(5)

if total_km >= 30:
    print(f"Total recorrido: {total_km} km")
    print("¡Meta semanal cumplida! Eres un atleta")
else:
    print(f"Sigue intentando, llevas {total_km} km, ¡tú puedes!")






    
    

    
