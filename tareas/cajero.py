saldo = 50000
PIN = 1234
n_maximo = 3
contador_intentos_fallido = 0
print("*****bienvenido al banco etao******")
while True:        
    p_ingresado = int(input("ingrese su clave"))
if p_ingresado == PIN :
    print("Acceso concedido")
elif p_ingresado != PIN :
    print("No haz accedido")
    contador_intentos_fallido =+ 1
else :
    print("Ingrese una contraseña valida")
if contador_intentos_fallido >= 3 :