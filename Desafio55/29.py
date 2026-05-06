#Calcula cuánto rato te tomará quemar tus calorías del día trotando.
#Datos Iniciales: Tu meta es quemar 300 kcal. Empiezas desde el minuto 0.
#Reglas de Negocio: Los primeros 10 minutos tienes mucha energía y quemas 20 kcal por minuto. Del minuto 11 en adelante te cansas, así que empiezas a quemar solo 10 kcal por minuto. Tienes que sumar minutos y calorías hasta llegar a 300.
#Restricciones: Usa un `while`. Adentro, pon un `if/else` que revise cuántos minutos llevas para saber cuántas calorías sumar en esa vuelta. Imprime solo el total de minutos que tardaste.
meta = 300
minuto = 0
quemado = 0
while quemado != meta:
    minuto +=1
    if minuto <= 10:
        quemado += 20
    else:
        quemado += 10
print(minuto)