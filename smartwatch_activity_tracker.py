# Monitorear tu actividad física de los últimos 7 días.

import os

contador = 0
distancia_corrida = 0

os.system('clear')
print("Iniciando rastreo de ejercicio, meta semanal (30 KM) \n")
while contador < 7:
    print(f"Quedan {7 - contador} dias esta semana")
    print(f"Distancia recorrida esta semana: < {distancia_corrida} KM > \n")
    print("Cuanto corriste el dia de hoy? (Ingrese un valor, si el valor es -1 te saltaste el dia!)")
    eleccion = int(input("[]: "))
    try:
        if eleccion > 0:
            distancia_corrida += eleccion
            contador += 1
            os.system('clear')
        elif eleccion == -1:
            contador += 1
            os.system('clear')
    except:
        print("Valor invalido!")

if distancia_corrida >= 30:
    print("Meta alcanzada! Sigue asi!")
elif distancia_corrida < 30:
    print(f"Meta fallada! Llevas {distancia_corrida} KM, sigue dandole que tu puedes!")