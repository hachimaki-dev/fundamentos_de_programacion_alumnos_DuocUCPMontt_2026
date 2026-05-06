#Ejercicio 20: Simulador de Cajero: Retiro Complejo
#El Mini-Boss: Haz que el cajero automático valide 3 reglas antes de dar dinero.

#Datos Iniciales: Tienes 50000 de saldo. Tu límite máximo diario para sacar plata es 200000. Quieres retirar 60000.

#Reglas de Negocio: Regla 1: Si lo que pides es más que tu límite diario, rechaza con 'Excede límite diario'.    LISTO
#Regla 2: Si pides más de lo que tienes en el saldo, rechaza con 'Saldo insuficiente'.                           FALTA
#Regla 3: Si lo que pides no es múltiplo de 5000 (el cajero no da monedas), rechaza con 'Monto inválido'.        FALTA
#Si pasas todas las reglas, 'Retiro exitoso'.

#Restricciones: Usa un bloque `if / elif / elif / else` para revisar regla por regla. Apenas falle una, debe imprimir el error y detenerse.
#Imprime el error de este caso.

saldo=50000
limite_diario=200000
retiro=60000
if retiro>limite_diario:
    print('Excede límite diario')
elif retiro>saldo:
    print("Saldo insuficiente")
elif retiro%5000!=0:
    print("Monto invalido")
else:
    saldo=saldo-retiro
    print(saldo)
    print("Retiro exitoso")