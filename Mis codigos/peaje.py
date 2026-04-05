import time
import sys

#Valor de cada automovil
valor_de_auto = 1500
valor_de_camion = 3500
valor_de_moto_ = 500

#Cantidad de automoviles
cantidad_de_autos = 0
cantidad_de_motos = 0
cantidad_de_camiones = 0

#Dinero acumulado 
dinero_acumulado = 0

print ("==========================/")
print ("/======Zona de Peaje======/")
print ("/=========================/\n")

print ("Bienvenidos a la zona de peajes.")
print ("Aquí deberas pagar una ciertas cantidad de dinero dependiendo del vehiculo con el que manejes.")
print ("A continuación aparecera en pantalla cada valor de automoviles.")
print ("Espere pacientemente.\n")

print ("PROCESANDO VALOR...\n")
time.sleep(3)

print (f"1. (A) Auto, El valor del peaje es de ${valor_de_auto}.")
print (f"2. (C) Camión, El valor del peaje es de ${valor_de_camion}.")
print (f"3. (M) Moto, El valor del peaje es de ${valor_de_moto_}.")
print ("4. (S) SALIR.\n")

print ("Bien, dicho esto, en la sección de abajo ingrese el tipo de automovil que maneja.")
print ("Recuerde solo ingresar (A) , (C) o (M) para confirmar su automovíl o si lo desea ingrese (S) para salir de la sesión.")
print ("En caso de no de que ingrese alguna de las letras mencionadas e ingrese un caracter invalido, ocurrira un error.\n")

while True:
    vehiculo_del_usuario = str(input("Confirme el vehiculo que esta manejenado : ")).lower()

    if vehiculo_del_usuario == "a" :
        print()
        print (f"Usted va manejando un Auto normal por lo que su peaje es de {valor_de_auto}")
        cantidad_de_autos += 1 
        dinero_acumulado = dinero_acumulado + valor_de_auto
        print (f"La cantidad de autos es de {cantidad_de_autos}")
        print (f"La cantidad de dinero acumulado es de ${dinero_acumulado}\n")

    elif vehiculo_del_usuario == "c":
        print()
        print (f"Usted va manejando un Camión por lo que su peaje es de {valor_de_camion}")
        cantidad_de_camiones += 1
        dinero_acumulado = dinero_acumulado + valor_de_camion
        print (f"La cantidad de camiones es de {cantidad_de_camiones}")
        print (f"La cantidad de dinero acumulado es de ${dinero_acumulado}\n")

    elif vehiculo_del_usuario == "m":
        print ()
        print (f"Usted va manejando una Moto por lo que su peaje es de {valor_de_moto_}")
        cantidad_de_motos += 1
        dinero_acumulado = dinero_acumulado + valor_de_moto_
        print (f"La Cantidad de moto es de {cantidad_de_motos}")
        print (f"La cantidad de dinero acumulado es de ${dinero_acumulado}\n")

    elif vehiculo_del_usuario == "s":
        break

    else :
        print ("ERROR")
        print ("Por favor ingrese (A) , (C) , (M) o  (S).")
        print ("Vuelva a ingresar el tipo de vehiculo.")

print ()
print ("Se ha cerrado la sesión.")
print ("Vamor a reunir los datos.\n")

print ("REUNIENDO LOS DATOS...\n")
time.sleep(5)
print ("CALCULADO DATOS...\n")
time.sleep(5)

#Total de vehiculos
total_vehiculos = cantidad_de_autos + cantidad_de_camiones + cantidad_de_motos

print("========== CIERRE DE CAJA ==========\n")

print(f"Ganancia total del día: ${dinero_acumulado}\n")

if total_vehiculos > 0:
    porcentaje_autos = (cantidad_de_autos / total_vehiculos) * 100
    porcentaje_camiones = (cantidad_de_camiones / total_vehiculos) * 100
    porcentaje_motos = (cantidad_de_motos / total_vehiculos) * 100

    print(f"Autos: {cantidad_de_autos} ({porcentaje_autos:.2f}%)")
    print(f"Camiones: {cantidad_de_camiones} ({porcentaje_camiones:.2f}%)")
    print(f"Motos: {cantidad_de_motos} ({porcentaje_motos:.2f}%)\n")

#Determinar el ganador
    if cantidad_de_autos > cantidad_de_camiones and cantidad_de_autos > cantidad_de_motos:
        print("El vehículo ganador del día fue: AUTOS 🚗")
    elif cantidad_de_camiones > cantidad_de_autos and cantidad_de_camiones > cantidad_de_motos:
        print("El vehículo ganador del día fue: CAMIONES 🚚")
    elif cantidad_de_motos > cantidad_de_autos and cantidad_de_motos > cantidad_de_camiones:
        print("El vehículo ganador del día fue: MOTOS 🏍️")
    else:
        print("Hubo un empate entre tipos de vehículos.")
else:
    print("No se registraron vehículos.")












