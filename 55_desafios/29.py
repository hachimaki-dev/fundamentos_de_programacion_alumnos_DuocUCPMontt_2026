#Calcula cuánto rato te tomará quemar tus calorías del día trotando.

kcal = 0
minuto = 0

#Reglas de Negocio: Los primeros 10 minutos tienes mucha energía y quemas 20 kcal por minuto. Del minuto 11 en adelante te cansas, así que empiezas a quemar solo 10 kcal por minuto. Tienes que sumar minutos y calorías hasta llegar a 300.

#Restricciones: Usa un `while`. Adentro, pon un `if/else` que revise cuántos minutos llevas para saber cuántas calorías sumar en esa vuelta. Imprime solo el total de minutos que tardaste.

while kcal <= 300:
    if minuto <= 10:
        kcal += 20
    else:
        kcal += 10
    
    minuto += 1

print(minuto)