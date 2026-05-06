#Ejercicio : Ejercicio 21: Cuenta Regresiva Básica (SpaceX)
#MEDIUM
#Crea el clásico reloj de cuenta regresiva para el despegue de un cohete.[cite: 2]

#Datos Iniciales: Tienes un cronómetro que parte en 10.[cite: 2]

#Reglas de Negocio: El reloj debe imprimir los números hacia atrás. Mientras el reloj sea mayor a cero, imprime el número actual y luego réstale 1. Cuando termine el tiempo, imprime 'Despegue 🚀'.[cite: 2]

#Restricciones: No hagas trampa escribiendo diez prints. Tienes que usar un ciclo while para hacerlo de forma automática.[cite: 2]

cuenta_regresiva = 10

while cuenta_regresiva != 0 :
    print(f"Faltan {cuenta_regresiva} segundos para el despegue")
    cuenta_regresiva = cuenta_regresiva - 1
print("El Cohete ha despegado, esto es un pequeño paso, pero una grande para la humanidad o como se diga...")