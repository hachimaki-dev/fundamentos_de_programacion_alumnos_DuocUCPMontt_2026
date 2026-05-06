#Ejercicio 21: Cuenta Regresiva Básica (SpaceX)
#Crea el clásico reloj de cuenta regresiva para el despegue de un cohete.

#Datos Iniciales: Tienes un cronómetro que parte en 10.

#Reglas de Negocio: El reloj debe imprimir los números hacia atrás. Mientras el reloj  , imprime el número actual y luego réstale 1. Cuando termine el tiempo, imprime 'Despegue 🚀'.

#Restricciones: No hagas trampa escribiendo diez `prints`. Tienes que usar un ciclo `while` para hacerlo de forma automática.

#Resultado esperado en consola:
#10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nDespegue 🚀


cronometro = 11
reloj = 1

while cronometro > 0:
    reloj =  cronometro + 1
    cronometro -=  1
    reloj =  cronometro
    print(reloj)
    

   
  
   