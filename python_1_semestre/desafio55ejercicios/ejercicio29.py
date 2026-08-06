""" Ejercicio 29: Simulación de Trote (Apple Watch)
Calcula cuánto rato te tomará quemar tus calorías del día trotando.

Datos Iniciales: Tu meta es quemar 300 kcal. Empiezas desde el minuto 0.

Reglas de Negocio: Los primeros 10 minutos tienes mucha energía y quemas 20 kcal por minuto. Del minuto 11 en adelante te cansas, 
así que empiezas a quemar solo 10 kcal por minuto. Tienes que sumar minutos y calorías hasta llegar a 300.

Restricciones: Usa un `while`. Adentro, pon un `if/else` que revise cuántos minutos llevas para saber cuántas calorías sumar en esa vuelta. 
Imprime solo el total de minutos que tardaste. """


meta_calorias = 300

tiempo_de_inicio = 0
calorias_quemadas = 0

while calorias_quemadas < meta_calorias:
    tiempo_de_inicio += 1
    if tiempo_de_inicio <=10:
        calorias_quemadas +=20
    else :
        calorias_quemadas +=10

print(f"{tiempo_de_inicio}")

    
        
