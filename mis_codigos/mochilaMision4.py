clave_correcta = 1234
contador = 3

print("ingresar contraseña")

while True :
    clabe = int(input())
    if contador < 1 :
        print("tarjeta bloqueada por seguridad")
        break
    elif clave_correcta != clabe :
        if contador > 1:
            print("contraseña incorrecta")
            print("ingresar de nuevo la contraseña")
        contador = contador - 1
    elif clave_correcta == clabe :
        print("puedes ingresar")
        break
saldo = 50000

print(f"tu saldo actual ${saldo}")
print("dinero a retirar: ")
monto = int(input())
if saldo < monto :
    print("fondos insuficientes")
elif monto <= 0 :
    print("monto inválido")
print("retiro exitoso")
saldo -= monto
print("tu saldo actual: $")
print(f"${saldo}")