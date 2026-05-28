#Escribe un programa que pida al usuario un número entero. 
#Si el usuario ingresa algo que no sea un número (por ejemplo "abc" o "3.7"), el programa debe capturar la excepción ValueError y mostrar:
#"Error: eso no es un número entero."

while True:
    try:
        numero=int(input("Ingrese un número "))
        break
    except ValueError:
        print("Error: eso no es un número entero")
