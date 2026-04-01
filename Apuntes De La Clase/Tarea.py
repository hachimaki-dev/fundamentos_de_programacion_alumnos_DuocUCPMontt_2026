#Calculadora de numeros primos
maximo_de_range = 0
respuesta = ""
print("Bienvenido a esta calculadora de numeros primos. Selecciona el numero MAXIMO que quieres llegar")
bandera = True
while bandera:
    maximo_de_range = int(input("Ingrese numero"))
    respuesta = input("Estas seguro que ese sea tu maximo (Responder con SI o NO)")
    if respuesta == "NO":
        print("Perfecto, volveremos a empezar")
    else:
        print("Perfecto, entonces continuamos")
    bandera = False
num = maximo_de_range
for i in range (num):
    if i % 1 or i == 0:
        continue
    print(i)