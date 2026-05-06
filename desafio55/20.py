"""
🟠 Rango: Peligro
Ejercicio 20: Simulador de Cajero: Retiro Complejo
El Mini-Boss: Haz que el cajero automático valide 3 reglas antes de dar dinero.

Datos Iniciales: Tienes 50000 de saldo. Tu límite máximo diario para sacar plata es 200000. Quieres retirar 60000.

Reglas de Negocio: Regla 1: Si lo que pides es más que tu límite diario, rechaza con 'Excede límite diario'. 
Regla 2: Si pides más de lo que tienes en el saldo, rechaza con 'Saldo insuficiente'. Regla 3: Si lo que pides no es múltiplo de 5000 (el cajero no da monedas), 
rechaza con 'Monto inválido'. Si pasas todas las reglas, 'Retiro exitoso'.

Restricciones: Usa un bloque `if / elif / elif / else` para revisar regla por regla. Apenas falle una, debe imprimir el error y detenerse. Imprime el error de este caso.

Resultado esperado en consola:
Saldo insuficiente
"""

saldo_cliente = 50000
limite_giro_maximo_cliente = 200000
retiro_dinero_cliente = 60000

regla_1 = False
regla_2 = False
regla_3 = False


if retiro_dinero_cliente > limite_giro_maximo_cliente:
    print(f"Estimado cliente, su retiro excede limite maximo porque el limite maximo es {limite_giro_maximo_cliente} y tu quieres sacar {retiro_dinero_cliente}")
else:
    regla_1 = True

if retiro_dinero_cliente > saldo_cliente:
    print(f"No puedes retirar un monto mayor a tu saldo. Tu saldo actual es: {saldo_cliente} y tu quieres retirar {retiro_dinero_cliente}")
else:
    regla_2 = True

if retiro_dinero_cliente % 5000 == 0:
    print("Si puedes sacar dinero, dado que el monto que quiere sacar son multiplos de 5000")
    regla_3 = True

else:
    print("Cajero solo puede entregar billetes de 10000")

if regla_1 == True and regla_2 == True and regla_3 == True:
    print(f"El usuario a retirado: {retiro_dinero_cliente} su saldo era: {saldo_cliente} y tu quieres retirar: {retiro_dinero_cliente}")