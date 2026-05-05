#Ejercicio 20: Simulador de Cajero: Retiro Complejo

saldo = 50000
limite_retiro = 200000
retiro = 60000

if retiro > limite_retiro :
    print("Excede el limite")
elif retiro > saldo:
    print("Saldo insuficiente")
elif retiro % 5000:
    print("Monto invalido")
else:
    print("Retiro exitoso")

    