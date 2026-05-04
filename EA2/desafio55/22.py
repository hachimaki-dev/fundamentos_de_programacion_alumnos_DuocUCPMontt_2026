'''Ejercicio 22: Ahorro Meta Mensual (PS5)
Simula tu chanchito de ahorros para saber cuántos meses te faltan para comprar una consola.

Datos Iniciales: Tu alcancía parte en 0. Ahorras religiosamente 80000 todos los meses. La consola cuesta 450000.

Reglas de Negocio: Cada mes que pasa, tú echas plata a la alcancía. Tienes que ir sumando hasta que tu ahorro iguale o supere el precio de la consola.

Restricciones: Usa un ciclo `while`. Aumenta tu ahorro y suma 1 a tu contador de meses en cada vuelta. Imprime solo cuántos meses te tomó llegar a la meta.'''

alcancia = 0
ahorro_mes = 80000
precio_consola = 450000
meses = 0

while alcancia < precio_consola:
    alcancia += ahorro_mes
    meses += 1
print(meses)