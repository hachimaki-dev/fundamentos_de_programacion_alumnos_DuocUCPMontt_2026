Ejercicios (1-5)

if,elif and else.
if dentro de rangos, ejemplo: 0 < variable < 100:
if anidados:(descuentos sobre descuentos)

Ejercicios (6-10)

import random !! para poder utilizar la funcion random de python(no activada por defecto)

ejemplo de numero random=
numerorandom=random.randint(rango1,rango2)
randint genera un numero entero aleatorio!

para verificar el numero generado=
numerorandom%2 = 0 -> el numero aleatorio es par
numerorandom%2 = 1 -> el numero aleatorio es impar

convertir el numero de par a impar o de impar a par= numerorandom +=1 o -=1(si lo anterior resulta en un numero fuera del rango)

para verificar que el numero quede en el rango = numerorandom + in range(rango1,rango2):

contador de intentos
se puede hacer con while o con for. ejemplo con while

intentos = 0
while intentos <3: <----- condicion TRUE hasta que se llegue a los 3 intentos.

si la variable con el input del usuario es == al numero aleatorio, se hace un break.

si la vriable no es igual, se agrega +=1 al contador de intentos
en cada uno de los intentos se puede dar una pista con ifs

compararar mayor o menor con < o >
la diferencia = abs(numerorandom-el numero adivinado por el usuario) nos permite saber a cuantas unidades estamos lejos del numero secreto

al llegar al intento 3 el programa se cierra e imprime el numero que no pudimos adivinar.