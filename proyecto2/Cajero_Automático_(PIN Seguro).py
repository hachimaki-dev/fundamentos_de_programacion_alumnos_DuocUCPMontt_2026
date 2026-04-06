#Inicio
saldocliente = 30000
pincliente = "2423"
maximointentos = 3
montoretirar = 0

print("**Bienvenido Cliente**")
print("Ingrese su Tarjeta")

pincliente = input("Ingrese su PIN de 4 Números: ")
while pincliente != "2423" :
    print("PIN incorrecto, vuelva a intentar")
    print(f"Le quedan {maximointentos} intentos, vuelva a intentarlo")
    pincliente = input("Ingrese su PIN de 4 Números: ")
    maximointentos -= 1
    if maximointentos <= 0 :
        print("Lo sentimos su tarjeta ha sido bloqueada por seguridad, Pongase en contacto con atención al cliente")
        break
while pincliente == "2423" :
    print(f"Su saldo disponible es de ${saldocliente}")
    montoretirar = int(input("¿Cuanto dinero desea retirar?: "))
    if montoretirar == 0 :
        print("El monto ingresado es inválido")
    if montoretirar > saldocliente :
        print("Fondo Insuficiente")
    if montoretirar <= saldocliente :
        print(f"Retirando ${montoretirar} de su saldo")
        saldocliente -= montoretirar
        print(f"¡Retiro exitoso! su nuevo saldo es ${saldocliente}")
        break
    
#Fin del cajero automático
            

    





        




    







