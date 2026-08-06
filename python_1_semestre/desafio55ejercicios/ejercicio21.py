""" Ejercicio 21: Cuenta Regresiva Básica (SpaceX)
Crea el clásico reloj de cuenta regresiva para el despegue de un cohete.

Datos Iniciales: Tienes un cronómetro que parte en 10.

Reglas de Negocio: El reloj debe imprimir los números hacia atrás.
 Mientras el reloj sea mayor a cero, imprime el número actual y luego réstale 
 1. Cuando termine el tiempo, imprime 'Despegue 🚀'.

Restricciones: No hagas trampa escribiendo diez `prints`. 
Tienes que usar un ciclo `while` para hacerlo de forma automática."""

cronometro : 1
reloj = 11

while reloj > 0:
    reloj = reloj - 1
    print(f"{reloj}")
    if reloj == 0:
        print("despegue")