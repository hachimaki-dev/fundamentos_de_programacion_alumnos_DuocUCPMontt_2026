#Partiendo desde despues de ingresada la tarjeta
import getpass

saldo= 50000
monto_retirado= 0
intentos= 0
numero_maximo_intentos= 3
clave= 1234

while intentos < numero_maximo_intentos:
    clave_ingresada= int(getpass.getpass("Ingresa tu clave: "))
    if clave_ingresada == clave:
        print(f"Haz Ingresado")
        print(f"tu saldo es de {saldo}")
        while True:
            monto_retirado= int(input("Ingrese monto a retirar: "))
            if monto_retirado > saldo:
                print("Monto retirado excede saldo")
            elif monto_retirado == 0:
                print("Monto invalido")
            else:
                print(f"Monto retirado es de {monto_retirado}")
                saldo= saldo - monto_retirado
                print(f"tu saldo final es de {saldo}")
                break
        break
    else:
        print("Clave incorrecta, intente de nuevo")
        intentos= intentos + 1

print("FIN DEL PROGRAMA")