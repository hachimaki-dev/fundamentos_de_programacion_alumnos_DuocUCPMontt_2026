""" Ejercicio 19 — Registro de vehículos en una empresa de transporte
de carga

Una empresa de transporte registra su flota. El sistema debe:

Preguntar cuántos vehículos se registrarán (entero positivo, validado)
Para cada vehículo:
Patente: exactamente 6 caracteres, sin espacios
Capacidad de carga en toneladas: entero positivo, validado
Clasificar:
Capacidad > 15 ton → Camión pesado
Capacidad ≤ 15 ton → Camión liviano

Al finalizar:
"La flota cuenta con 3 camiones pesados y 5 camiones livianos. 
Registro completado." """

while True:
    try:
        vehiculos_registro = int(input("ingresa la cantidad de vehiculos a registrar : "))
        if vehiculos_registro > 0: 
            break
        else:
            print("ingresa un numero mayor que 0")
    except ValueError:
        print("ingresa un numero valido")



patentes = []

for patente_por_vehiculo in range(vehiculos_registro):
    while True:
        try:
            patente = input(f"ingresa la patente del vehiculo {patente_por_vehiculo +1} : ")
            if len(patente) == 6 and " " not in patente:
                break
            else:
                print(" los parametros de las patentes son:\n exactamente 6 caracters\n la patente no puede tener espacios.")
        except:
            print("ingresa los datos de manera correcta")
    patentes.append(patente)


camion_pesado = 0
camion_liviano = 0

for capacidad_de_carga_por_vehiculo in range(len(patentes)):
    while True:
        try:
            capacidad_vehiculo = int(input(f"ingresa la capacidad de carga del vehiculo {capacidad_de_carga_por_vehiculo + 1} , en toneladas: "))
            if capacidad_vehiculo > 0:
                if capacidad_vehiculo > 15:
                    camion_pesado+=1
                    break
                elif capacidad_vehiculo <=15:
                    camion_liviano +=1
                    break
            else:
                print("ingresa un valor de carga mayor a 0")

        except:
            print("ingresa un numero valido")

print(f" La flota cuenta con :\n {camion_pesado} camion\s pesado\s y {camion_liviano} camion\s liviano\s\n Registro completado.")

"""Capacidad de carga en toneladas: entero positivo, validado
Clasificar:
Capacidad > 15 ton → Camión pesado
Capacidad ≤ 15 ton → Camión liviano"""