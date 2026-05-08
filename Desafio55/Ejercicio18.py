"""Ejercicio 18: Sistema Anti-Robo Inteligente (Smart Home)
Configura la alarma de tu casa para que suene solo cuando debe.

Datos Iniciales: Hubo movimiento (`movimiento = True`). Son las 3 de la mañana (`hora = 3`). El dueño está en casa (`dueño_en_casa = True`).

Reglas de Negocio: La alarma suena si se cumple ALGUNA de estas dos situaciones: 
Situación A: Hay movimiento y el dueño NO está en casa. Situación B: Hay movimiento y es de madrugada (antes de las 6 AM), no importa si el dueño está o no.

Restricciones: Usa paréntesis para separar ambas situaciones con un `or` al medio. Imprime `'Alarma Sonando'` o `'Modo Silencioso'`."""


Movimiento = True

Hora = 3

Dueño_en_la_Casa = True

if Movimiento == True and Dueño_en_la_Casa == False or Movimiento == True and 0 < Hora < 6:
    print("ALARMA SONANDO! ! !")
else:
    print()