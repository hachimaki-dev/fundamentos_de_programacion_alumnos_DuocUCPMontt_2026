#Ejercicio 1 =================================
def saludar(nombre):
    return f"Hola, {nombre}, bienvenido al sistema"

respuesta = saludar("Pepito")
print({respuesta})


#Ejercicio 2 =================================
def sumar(a, b):
    return a + b

respuesta2 = sumar(300, 420)
print(respuesta2)


#Ejercicio 3 =================================

def es_par(numero_recibido):
    if numero_recibido % 2 == 0:
        return True
    else:
        return False

print(es_par(546841584))


#Ejercicio 4 =================================
def Saludar():
    nombre1 = input("Ingrese nombre 1 ")
    nombre2 = input("Ingrese nombre 2 ")
    nombre3 = input("Ingrese nombre 3 ")
    return nombre1, nombre2, nombre3

Respuesta = Saludar()
print(Respuesta[1])