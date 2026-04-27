for i in range(1, 20, 1):       #Se asigna primero desde (donde comienza, antes de terminar, en cuantos pasos).
    print(i)                    #Por ejemplo comienzo desde 1, cuento en 1 hasta llegar antes del 20.

for e in range (5):             #Cuenta por defecto desde el 0 y cuenta hasta antes de llegar al 5, osea;
    print(e)                    #0, 1, 2, 3 y 4.

for y in range (10, 0, -1):     #Se comienza desde el 10 y retrocede hasta llegar antes de 0 como cuenta regresiva
    print(y)                    #Se asigna el - para poner el numero en negativo e ir restando.

print("###############")

suma = 0
for s in range(1, 6):           #Se comienza desde el 1 y va sumando hasta antes de terminar en el 6.
    suma += s                   #Osea: 1 + 2 + 3 + 4 + 5 = 15
print(suma)
print("##############")

for m in range(1, 11):              #Podemos añadir if para filtrar, clasificar y decidir
    if m % 2 == 0:                  #El modulo entre m y 2 (el restante de la division) si es igual a 0 entonces será par
        print(f"{m} es par.")       #Es decir: 1%2 = 0.5 no es par, 2%2 = 0, es par...
    else:
        print(f"{m} no es par.")

print("#############")

for q in range(10):
    if q == 5:
        break
    print(q)

print("##############")

for w in range(11):
    if w % 2 == 0:
        continue
    print(w)

print("###############")        #¿que le enseñaria a mi compañero de lo que acabo de leer/aprender?
                                #Que puede crear una cuenta regresiva

#Las posiciones del Rango se leen siempre desde el 0, por ejemplo: CARLOS que letra está en la posición 2? r= la letra R
#Se puede colocar [] para cambiar el rango de numeros a alfabetico

#EJERCICIO PROPIO

for r in range(1, 6):
    if r == 1:
        print("Usted debe 1000 pesos.")
    elif r == 2:
        print("Usted debe 10 pesos")
    elif r == 3:
        print("Usted no debe nada")
    elif r == 4:
        print("Usted debe 100.000.000 de pesos")
    else:
        print("Usted debe 1 peso")

print("################")