#Ejercicio 22: Ahorro Meta Mensual (PS5)
#Simula tu chanchito de ahorros para saber cuántos meses te faltan para comprar una consola.

#Datos Iniciales: Tu alcancía parte en 0. Ahorras religiosamente 80000 todos los meses. La consola cuesta 450000.

#Reglas de Negocio: Cada mes que pasa, tú echas plata a la alcancía. 
#Tienes que ir sumando hasta que tu ahorro iguale o supere el precio de la consola.

#Restricciones: Usa un ciclo `while`. Aumenta tu ahorro y suma 1 a tu contador de meses en cada vuelta.
#Imprime solo cuántos meses te tomó llegar a la meta.

alcancia=0
ahorros=80000
consola=450000
diferencia=0
mes=0

print("")
print("Quieres una consola de videojuegos, por ende ahorraras 80.000 todos los meses hasta llegar a la meta")
print(f"Empezaras de {alcancia} asi que iremos sumando lo dicho cada mes")
print("")
while alcancia<consola:
    alcancia=alcancia+ahorros
    mes=mes+1
    if mes==1:
        print(f"Pasa {mes} mes, llevas ahorrados {alcancia} pesos")
    else:
        print(f"Pasan {mes} meses, llevas ahorrados {alcancia} pesos")
else:
    diferencia=alcancia-consola
    print("")
    print("!Alcanzaste tu meta para tu consola!")
    print(f"Solo te tomo {mes} meses")
    print(f"Tambien te sobraron {diferencia} pesos, comprate un juego!!!")