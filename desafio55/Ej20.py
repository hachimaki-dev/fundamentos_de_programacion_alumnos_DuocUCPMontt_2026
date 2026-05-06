#Ejercicio : Ejercicio 20: Simulador de Cajero: Retiro Complejo
#HARD
#El Mini-Boss: Haz que el cajero automático valide 3 reglas antes de dar dinero.[cite: 2]

#Datos Iniciales: Tienes 50000 de saldo. Tu límite máximo diario para sacar plata es 200000. Quieres retirar 60000.[cite: 2]

#Reglas de Negocio: Regla 1: Si lo que pides es más que tu límite diario, rechaza con 'Excede límite diario'. Regla 2: Si pides más de lo que tienes en el saldo, rechaza con 'Saldo insuficiente'. Regla 3: Si lo que pides no es múltiplo de 5000 (el cajero no da monedas), rechaza con 'Monto inválido'. Si pasas todas las reglas, 'Retiro exitoso'.[cite: 2]

#Restricciones: Usa un bloque if / elif / elif / else para revisar regla por regla. Apenas falle una, debe imprimir el error y detenerse. Imprime el error de este caso.[cite: 2]

saldo_inicial = 50000
max_giro = 200000
giro_solicitado = 60000

if saldo_inicial >= giro_solicitado and giro_solicitado < max_giro and giro_solicitado / 5000 == 0 :
    saldo_inicial = saldo_inicial - giro_solicitado
    print("Retiro Exitoso")
elif saldo_inicial >= giro_solicitado and giro_solicitado > max_giro :
    print("Excede límite diario")
elif saldo_inicial < giro_solicitado :
    print("Rechazado. Saldo Insuficiente")
elif saldo_inicial >= giro_solicitado and giro_solicitado < max_giro and giro_solicitado / 5000 != 0 :
    print("Monto Inválido")
