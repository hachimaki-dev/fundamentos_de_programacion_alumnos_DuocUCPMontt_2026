#Crea el clásico reloj de cuenta regresiva para el despegue de un cohete.
#Datos Iniciales: Tienes un cronómetro que parte en 10.
#Reglas de Negocio: El reloj debe imprimir los números hacia atrás. Mientras el reloj sea mayor a cero, imprime el número actual y luego réstale 1. Cuando termine el tiempo, imprime 'Despegue 🚀'.
#Restricciones: No hagas trampa escribiendo diez `prints`. Tienes que usar un ciclo `while` para hacerlo de forma automática.

tiempo = 11
while True:
    tiempo = tiempo - 1
    print(f"{tiempo}")
    if tiempo <= 0:
        print("Despegue 🚀")
        break