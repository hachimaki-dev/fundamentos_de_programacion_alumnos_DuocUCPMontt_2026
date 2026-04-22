opcion = 0
saldo = 50000
PIN = 1234
n_maximo = 3
contador_intentos_fallido = 0
print("*****bienvenido al banco etao******")
match opcion :
    case 1 :
        saldo = 50000
        print("Su saldo es : {saldo}")
    case 2 :
        print("Giro de dinero")
        
        
while True:        
    p_ingresado = int(input("ingrese su clave"))
if p_ingresado == PIN :
    print("Acceso concedido")
    print("Ha ingresado a su cuenta corriente")
    print(f"su saldo actual es de {saldo}")
    print("Desea sacar dinero?")
    respuestausuario = input("Si o no").lower
    if respuestausuario == "si":
        print("Ha ingresado a sacar dinero")
        
elif p_ingresado != PIN :
    print("No haz accedido")
    contador_intentos_fallido =+ 1
else :
    print("Ingrese una contraseña valida")