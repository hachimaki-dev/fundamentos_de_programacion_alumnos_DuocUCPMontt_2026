# Desarrolle un programa en Python que permita resolver la siguiente situación:

# Una persona desea verificar si cumple con los requisitos para inscribirse en un taller gratuito. Para ello, el sistema debe realizar una validación básica.

# El programa debe solicitar los siguientes datos:

# Edad de la persona (número entero).
# Indicar si la persona está inscrita previamente (responder SI o NO).

# Condiciones:

# Si la edad es mayor o igual a 18:
# Si la respuesta es SI, mostrar el mensaje:
# “Inscripción aceptada”
# En cualquier otro caso, mostrar:
# “Inscripción rechazada”
# Si la edad es menor a 18:
# Mostrar el mensaje:
# “Debe ser mayor de edad para poder inscribirse”

# Al finalizar el proceso, siempre se debe:

# Mostrar el mensaje: “Fin del proceso”
# Finalizar la ejecución del programa.

"""def edad_persona():
    edad_usuario = int(input("ingresa su edad: "))
    if edad_usuario >= 18:
        inscripcion()
    else:
        print("Debe ser mayor de edad para poder inscribirse")

    print("Fin del proceso")

def inscripcion():
    inscripcion_usuario = input("está inscrita previamente (responder SI o NO) : ").upper()
    if inscripcion_usuario == "SI":
        print("inscripcion aceptada")
    else:
        print("inscripcion rechazada")

edad_persona()"""

def sumar(a , b):
    return a + b

resultado1 = sumar(100 , 200)
print(resultado1)

iva = 19
neto = 100
resultado2 = sumar(iva, neto)
print(resultado2)

resultado_nombres = sumar("pedro", "juan")
print(resultado_nombres)

nombre = "jose"
apellido = "gonzales"

def ordenar_nombres(nombre, apellido):
    return(nombre + " " + apellido + " " + "hola").upper()

nombre_completo = ordenar_nombres(nombre , apellido)
print(nombre_completo)

otro_nombre = ordenar_nombres("juanin","pedrin",)
print(otro_nombre)

