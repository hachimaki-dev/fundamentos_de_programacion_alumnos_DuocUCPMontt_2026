#Argumento se transforma en un programación funcional (parametros)

#algo garcodeado es algo implantado en el codigo como el número pi que nunca cambia su valor

#def = (definicion de función) despues sigue la funcion que no tenga el nombre reservado en el lenguaje ej: input, int, in, ect
#todas las funciones tienen un argumento () donde se coloca el parametro donde se tiene que recibir


#esto es una variable
el_triple_de_un_numero = 5

#esto es una parametro no es lo mismo
#el nombre numero_ingresado es distinto no funciona el input
def el_triple_de_un_numero(numero_ingresado):
    resultado = numero_ingresado * 3
    return resultado


#return puedes devolver cual quier cosa lista, dicionarios, numeros, letras , ect 

#llamando al parametro y al argumento () 
el_triple_de_un_numero(10)

#ahora el paramentro funciona esta cargado en memoria:
#def el_triple_de_un_numero(numero_ingresado):
#    resultado = numero_ingresado * 3
#    print(resultado)

#en python interpreta y el llamado del parametro debe estar abajo del parametro
# ¿Cúal es la diferencia entre un lenguaje interpretado y compilado?