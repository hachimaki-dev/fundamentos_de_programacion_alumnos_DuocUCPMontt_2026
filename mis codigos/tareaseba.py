#Primero se muestra una breve descripción del juego, el cual indica el numero de jugadores y si se juega de forma simultanea o por turnos
print("¡Bienvenido a ChuxiaWorld! un juego entre \n2 jugadores que participan en forma simultánea.")
print("==================================================================================================================")
#se le pide los datos en minutos del tiempo de juego al usuario, y lo transformo a int para utlizarlo para calcular.

print("Tiempo de juego")
tiempo_jugador_1 = int(input("JUGADOR 1 (minutos):"))
tiempo_jugador_2 = int(input("JUGADOR 2 (minutos):"))
#como el juego es simultaneo el minuto tiene que ser el mayor por eso el if ademas se definen variables dentro como minutos y horas segun cual sea el mayor.

if tiempo_jugador_1 >= tiempo_jugador_2:
    tiempo = tiempo_jugador_1
    minutos = (tiempo_jugador_1) %60
    horas = int((tiempo_jugador_1) /60)
    print("Tiempo total del juego:",horas ,"horas, y",minutos,"minutos")
else:
    tiempo = tiempo_jugador_2
    minutos = (tiempo_jugador_2) %60
    horas = int((tiempo_jugador_2) / 60)
    print("Tiempo total del juego:", horas, "horas, y", minutos,"minutos")
#ademas agregue la variable tiempo para un ejercicio mas adelante que lo necesita.
print("==================================================================================================================")

print("Energía")

#se piden los datos correspondientes en int, float y se ponen las formulas con los datos.

peso_jugador_1 = float(input("Peso jugador 1 (kg):"))
percepcion_jugador_1 = int(input("Percepción de esfuerzo jugador 1 (1-10):"))

#aqui es la transformación de minutos a hora.
duracion_jugador_1 = (tiempo_jugador_1) /60
#aqui se pone la formula de el esfuerzo.
esfuerzo_jugador_1= 1.5 + 0.4 * percepcion_jugador_1**1.3
#y aqui junto los datos y pongo la respuesta.
energia_jugador_1 = peso_jugador_1 * duracion_jugador_1 * esfuerzo_jugador_1


print("Energía Jugador 1:", round(energia_jugador_1,2), "kcal")

#aqui es lo mismo.

peso_jugador_2 = float(input("Peso jugador 2 (kg):"))
percepcion_jugador_2 = int(input("Percepción de esfuerzo jugador 2 (1-10):"))

duracion_jugador_2 = (tiempo_jugador_2) /60

esfuerzo_jugador_2= 1.5 + 0.4 * percepcion_jugador_2**1.3

energia_jugador_2 = peso_jugador_2 * duracion_jugador_2 * esfuerzo_jugador_2

print("Energía Jugador 2:", round(energia_jugador_2,2), "kcal")

#aqui solo saco el promedio de ambas energías.

promedio_energía = (energia_jugador_1 + energia_jugador_2) /2

print("Promedio de energía:", round(promedio_energía,2))
#y termino imprimiendo el promedio redondeado.

print("==================================================================================================================")

print("Puntaje")
#aqui solo pido los datos con el int ya que no me sirve en str pq aplicare formulas.
acciones = int(input("Cantidad de acciones realizadas:"))
rotaciones = int(input("Cantidad de rotaciones de rol (0-5):"))
seguridad = int(input("Seguridad del juego (1-5):"))

#aqui aplique la formula para saber el puntaje base.
puntaje_base = 2000 + 300 * acciones + 1200 * rotaciones + 1000 * seguridad

#aqui aplique los bonos utlizando el if y el elif ya que son 3 casos por eso el else no me servia.
if puntaje_base < 10000:
    sinergia = (8/100)* puntaje_base
elif  10000 <= puntaje_base <= 20000:
    sinergia = (10/100)* puntaje_base
elif puntaje_base > 20000:
    sinergia = (12/100)* puntaje_base
#aqui nomas puse la formula del puntaje total.
puntaje_total = puntaje_base + sinergia + esfuerzo_jugador_1 + esfuerzo_jugador_2
#aqui como el puntaje total con bonos puede ser igual al total, puse la definicion afuera tambien.
puntaje_total_b = puntaje_total

#aqui utilize muchos if ya que pedian triple condiciones para añadirle el bono, ademas aqui utilize el tiempo que hablaba mas arriba.
if seguridad >= 2:
    if tiempo >= 45:
        if acciones >= 25:
            puntaje_total_b = puntaje_total_b + 500

    if rotaciones > 4:
                puntaje_total_b = puntaje_total_b + 300
    else:
     if seguridad > 3:
        puntaje_total_b = puntaje_total_b + 300
#como se pide que en si cualquiera de estos dos casos se cumple se suman 300 lo q hice fue poner un else para que si se cumple lo primero pase al segundo y asi no se termine sumando 600 si se cumplen ambas.


#aqui solo imprimo todo y listo.
print("Puntaje base:", round(puntaje_base,2))

print("Puntaje total sin bonos:", round(puntaje_total,2) )

print("Puntaje total con bonos:", round(puntaje_total_b,2) )

print("==================================================================================================================")

print("Tiempo de armado")

elementos = int(input("Elementos a instalar:"))

minutos_elementos = int(input("Elementos por minuto que puede armar:"))

armado = elementos / minutos_elementos
