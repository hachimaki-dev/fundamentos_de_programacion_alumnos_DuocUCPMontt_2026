"""
Ejercicio 29: Simulación de Trote (Apple Watch)
Calcula cuánto rato te tomará quemar tus calorías del día trotando.

Datos Iniciales: Tu meta es quemar 300 kcal. Empiezas desde el minuto 0.

Reglas de Negocio: Los primeros 10 minutos tienes mucha energía y quemas 20 kcal por minuto. 

Del minuto 11 en adelante te cansas, así que empiezas a quemar solo 10 kcal por minuto. Tienes que sumar minutos y calorías hasta llegar a 300.

Restricciones: Usa un `while`. Adentro, pon un `if/else` que revise cuántos minutos llevas para saber cuántas calorías sumar en esa vuelta. 

Imprime solo el total de minutos que tardaste."""

Objetivo = 300 #Kcal

Minuto = 0

Calorias_quemadas_10_primeros_minutos = 20

Calorias_quemadas_11_primeros_minutos = 10

while Objetivo > 0:
    while Minuto < 10:
        Objetivo -= Calorias_quemadas_10_primeros_minutos
        Minuto += 1
    Objetivo -= Calorias_quemadas_11_primeros_minutos
    Minuto += 1

print(f"Te tomo {Minuto} Minutos")