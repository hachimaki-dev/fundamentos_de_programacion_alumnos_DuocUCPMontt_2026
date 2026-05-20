def saludar():
    nombre1 = input("Ingrese nombre 1: ")
    nombre2 = input("Ingrese nombre 2: ")
    nombre3 = input("Ingrese nombre 3: ")

    return nombre1, nombre2, nombre3

#De esta forma podemos pedirle a Python que pongan los nombres uno separado del otro, en caso contrario se forma una tupla
#Una tupla es una lista INMUTABLE
respuesta1, respuesta2, respuesta3 = saludar()

print(respuesta1)
print(respuesta2)
print(respuesta3)