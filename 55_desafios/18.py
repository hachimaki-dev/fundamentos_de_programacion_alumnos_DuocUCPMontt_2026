#Configura la alarma de tu casa para que suene solo cuando debe.

#Datos Iniciales: Hubo movimiento (`movimiento = True`). Son las 3 de la mañana (`hora = 3`). El dueño está en casa (`dueño_en_casa = True`).

#Reglas de Negocio: La alarma suena si se cumple ALGUNA de estas dos situaciones: Situación A: Hay movimiento y el dueño NO está en casa. Situación B: Hay movimiento y es de madrugada (antes de las 6 AM), no importa si el dueño está o no.

#Restricciones: Usa paréntesis para separar ambas situaciones con un `or` al medio. Imprime `'Alarma Sonando'` o `'Modo Silencioso'`.

movimiento = True
hora = 3
dueño_en_casa = True
alarma = False
alarma = True == (movimiento == True and dueño_en_casa == False) or (movimiento == True and hora == 3)

if alarma == True:
    print("Alarma Sonando")
else:
    print("Modo Silencio")