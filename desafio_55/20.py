#El Mini-Boss: Haz que el cajero automático valide 3 reglas antes de dar dinero.

#Datos Iniciales: Tienes 50000 de saldo. Tu límite máximo diario para sacar plata es 200000. Quieres retirar 60000.

#Reglas de Negocio: Regla 1: Si lo que pides es más que tu límite diario, rechaza con 'Excede límite diario'. Regla 2: Si pides más de lo que tienes en el saldo, rechaza con 'Saldo insuficiente'. Regla 3: Si lo que pides no es múltiplo de 5000 (el cajero no da monedas), rechaza con 'Monto inválido'. Si pasas todas las reglas, 'Retiro exitoso'.

#Restricciones: Usa un bloque `if / elif / elif / else` para revisar regla por regla. Apenas falle una, debe imprimir el error y detenerse. Imprime el error de este caso.
saldo = 50000
limete_diario = 200000
retirar = 60000
if retirar > limete_diario:
    print("Excede limete diario")
elif retirar > saldo:
    print("saldo insuficiente")
elif retirar % 5000:
    print("monto invalido")
else:
    print("retiro exitoso ")
    