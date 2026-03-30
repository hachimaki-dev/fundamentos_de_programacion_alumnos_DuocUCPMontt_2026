#Calculadora de numeros primos

print("Bienvenido a esta calculadora de numeros primos. Selecciona el numero MAXIMO que quieres llegar")

while true:
    maximo_de_range = input("Ingrese numero")
    respuesta = input("Estas seguro que ese sea tu maximo (Responder con SI o NO)")
    if respuesta == NO:
        print("Perfecto, volveremos a empezar")
if respuesta == SI:
