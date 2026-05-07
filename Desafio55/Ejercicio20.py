"""Ejercicio 20: Simulador de Cajero: Retiro Complejo
El Mini-Boss: Haz que el cajero automático valide 3 reglas antes de dar dinero.

Datos Iniciales: Tienes 50000 de saldo. Tu límite máximo diario para sacar plata es 200000. Quieres retirar 60000.

Reglas de Negocio: Regla 1: Si lo que pides es más que tu límite diario, rechaza con 'Excede límite diario'. 

Regla 2: Si pides más de lo que tienes en el saldo, rechaza con 'Saldo insuficiente'. Regla 3: Si lo que pides no es múltiplo de 5000 (el cajero no da monedas), 
rechaza con 'Monto inválido'. Si pasas todas las reglas, 'Retiro exitoso'.

Restricciones: Usa un bloque `if / elif / elif / else` para revisar regla por regla. Apenas falle una, debe imprimir el error y detenerse. Imprime el error de este caso."""

Saldo = 50000

Limite_Diario = 200000

Retirar = 60000

print(f"Vas a intentar Retirar {Retirar}$")

if Retirar > Limite_Diario:
    print("Excede limite diario")
    
elif Retirar > Saldo:
    print("Saldo insuficiente")
    
elif Retirar % 5000 != 0:
    print("Monto invalido")
    
else:
    print("Retiro exitoso")