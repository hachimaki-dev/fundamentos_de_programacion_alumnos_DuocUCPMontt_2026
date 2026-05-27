#todas las funciones llevan una ()

#def definir funcion

#def nombreDeLaFuncion(Parametros):
    #return Cualquier_Tipo_De_Datos

# una tupla es algo que no cambia a compracion de una lista tambien ocupa () en vez de []


#funcion global
nombre = "Carlitos"

#funcion local
def saludar():
    print(nombre)
    apellido = "Lechuga"

#llamo a la funcion por lo que imprime la variable en esta caso nombre = "Carlitos" y apellido = "Lechuga"
saludar()


#scope puede estar en dos tipos de ambitos global o local
#ejemplo nombre es global y apellido es local

#se recomienda no modificar una funcion global con una definicion local

#ejercicios para la prube con for listas y diccionarios