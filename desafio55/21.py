#Ejercicio 21: Cuenta Regresiva Básica (SpaceX)
#Crea el clásico reloj de cuenta regresiva para el despegue de un cohete.

#Datos Iniciales: Tienes un cronómetro que parte en 10.

#Reglas de Negocio: El reloj debe imprimir los números hacia atrás. Mientras el reloj sea mayor a cero, imprime el número actual y luego réstale 1. Cuando termine el tiempo, imprime 'Despegue 🚀'.

#Restricciones: No hagas trampa escribiendo diez `prints`. Tienes que usar un ciclo `while` para hacerlo de forma automática.

#Resultado esperado en consola:
#10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nDespegue 🚀

cronometro = 11
tiempo = 0
while tiempo < cronometro:
    
    cronometro = cronometro - 1
    print(cronometro)
    if cronometro < 1:
        print("Despegue🚀")