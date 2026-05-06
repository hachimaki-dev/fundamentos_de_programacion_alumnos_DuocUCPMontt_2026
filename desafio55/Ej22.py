#Ejercicio : Ejercicio 22: Ahorro Meta Mensual (PS5)
#MEDIUM
#Simula tu chanchito de ahorros para saber cuántos meses te faltan para comprar una consola.[cite: 2]

#Datos Iniciales: Tu alcancía parte en 0. Ahorras religiosamente 80000 todos los meses. La consola cuesta 450000.[cite: 2]

#Reglas de Negocio: Cada mes que pasa, tú echas plata a la alcancía. Tienes que ir sumando hasta que tu ahorro iguale o supere el precio de la consola.[cite: 2]

#Restricciones: Usa un ciclo while. Aumenta tu ahorro y suma 1 a tu contador de meses en cada vuelta. Imprime solo cuántos meses te tomó llegar a la meta.[cite: 2]

dinero_alcancia = 0
ahorro_mensual = 80000
valor_consola = 450000
meses_ahorrando = 0

while dinero_alcancia < valor_consola :
    dinero_alcancia = dinero_alcancia + ahorro_mensual
    meses_ahorrando = meses_ahorrando + 1
    print(f"Llevas ahorrando {meses_ahorrando} mes/es.")
print(f"Felicidades has logrado llegar a la meta de dinero, para comprar tu consola, y solo te tomo {meses_ahorrando} meses :D")