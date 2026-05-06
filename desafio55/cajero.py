# Tienes 50000 de saldo. Tu límite máximo diario para sacar plata es 200000. Quieres retirar 60000.
#  Regla 1: Si lo que pides es más que tu límite diario, rechaza con 'Excede límite diario'. Regla 2: Si pides más de lo que tienes en el saldo, rechaza con 'Saldo insuficiente'. Regla 3: Si lo que pides no es múltiplo de 5000 (el cajero no da monedas), rechaza con 'Monto inválido'. Si pasas todas las reglas, 'Retiro exitoso'.

monto_maximo = 200000
saldo_usuario = 50000


print(f"bienvenido al banco , solo se permite sacar un monto maximo al dia de {monto_maximo} mil pesos y su saldo actual es de {saldo_usuario} (solo puedes retirar dinero con un numero multiplo de 5000)")
saldo_a_sacar = int(input("cuanto dinero quieres sacar ?: "))

if saldo_a_sacar > 200000:
    print("excede limite diario")
elif saldo_a_sacar > 50000:
    print("saldo insuficiente")
elif saldo_a_sacar % 5000 == 0:
    saldo_usuario -= saldo_a_sacar
    print(saldo_usuario)
else:
    print("monto invalido")












