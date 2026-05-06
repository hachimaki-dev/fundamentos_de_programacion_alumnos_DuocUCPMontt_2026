chanchito = 0
ingreso_mensual = 80000
precio_consola = 450000
meses = 0
import time
while True:
    print(f"En el mes {meses} tengo {chanchito} pesos ahorrados, tu consola cuesta {precio_consola}")
    time.sleep(1)
    meses = meses + 1
    chanchito = chanchito + ingreso_mensual
    if chanchito >= precio_consola:
        print(f"En el mes {meses} lograste ahorrar {chanchito} pesos para tu consola, te sobro {chanchito - precio_consola} pesos")
        break