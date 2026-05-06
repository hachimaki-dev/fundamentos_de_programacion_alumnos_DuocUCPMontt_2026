"""Ejercicio 22: Ahorro Meta Mensual (PS5)
Simula tu chanchito de ahorros para saber cuántos meses te faltan para comprar una consola.

Datos Iniciales: Tu alcancía parte en 0. Ahorras religiosamente 80000 todos los meses. La consola cuesta 450000.

Reglas de Negocio: Cada mes que pasa, tú echas plata a la alcancía. Tienes que ir sumando hasta que tu ahorro iguale o supere el precio de la consola.

Restricciones: Usa un ciclo `while`. Aumenta tu ahorro y suma 1 a tu contador de meses en cada vuelta. Imprime solo cuántos meses te tomó llegar a la meta."""
import time
Alcancia = 0

Ahorro_Mensual = 80000

Precio_Consola = 450000

Mes = 0

print(f"Quieres comprar una consola de {Precio_Consola}$")

input()

print(f"Asi que vas ahorrar {Ahorro_Mensual}$ mensualmente")

input()

while Precio_Consola > Alcancia:
    
    Mes += 1
    
    Alcancia += Ahorro_Mensual
    
    time.sleep(1)
    print(f"Mes: {Mes}")
    time.sleep(0.5)
    print(f"Tienes ahorrado {Alcancia}$")
    
time.sleep(0.3)
print(f"Te tomo {Mes} meses")
    
    