#Simula tu chanchito de ahorros para saber cuántos meses te faltan para comprar una consola.
#Datos Iniciales: Tu alcancía parte en 0. Ahorras religiosamente 80000 todos los meses. La consola cuesta 450000.
#Reglas de Negocio: Cada mes que pasa, tú echas plata a la alcancía. Tienes que ir sumando hasta que tu ahorro iguale o supere el precio de la consola.
#restricciones: Usa un ciclo `while`. Aumenta tu ahorro y suma 1 a tu contador de meses en cada vuelta. Imprime solo cuántos meses te tomó llegar a la meta
# 6.
contador_meses = 0
ahorro_mensual = 80000
alcancia = 0
costo_consola = 450000
while alcancia < costo_consola:
    alcancia = alcancia + ahorro_mensual 
    contador_meses += 1
print(contador_meses)


