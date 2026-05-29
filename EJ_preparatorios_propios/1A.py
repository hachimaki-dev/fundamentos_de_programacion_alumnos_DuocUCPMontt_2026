#EJERCICIO 1A

while True:
    try:
        pedir_numero_entero = int(input("Ingrese un numero entero :  "))
        print(f"Numero Recibido : {pedir_numero_entero}")
        break
    except ValueError:
        print("Error : eso no es un numero entero .")
