# usamos def para las funciones (tenemos que usar palabras no reservadas) TODAS LAS FUNCIONES LLEVAN PARENTESIS
# con variables?? Como:
# def saludar(parametro1, parametro2, parametro3) # espacio de memoria para cuandola mandemos a llamar
# el parametro es lo que le llega a la maquina 
# como llamamos una fioncion? si no llamamos la funcion el codigo no se ejecuta 
def saludar(nombre):
    print(f"hola {nombre} como estas?")
    return "chaos"
# en este momemto no pasa nada pq no hemos llamdo la funcion
#la llamamos:
saludar("carlitos")
# argumento: saludar("carlitos")
# parametro: saludar(nombre)
saludar("camila")
saludar("amparo")
saludar("juan")
# mandamos a llamar la funcion en distntos casos osea con distintos nombres
# saludar(carlitos), ahi seria una vareiable y no un texto
saludar(101) # tambien funciona, podemos pasarle hasta listas o diccionarios
# como argumento le podemos psar cualquier tipo de dato
# la salida de una funcion es la entrada de la otra a esta funcion nos falta una salida "return"
respuesta = saludar("pepe")
print(f"la respuesta es {respuesta}") #respuesta obtiene el valor de "chaos", tmabien podems hacer retun de cualquier dato
#no simpre necesitamos que las funciones devualvan algo
# los parametro y el retrurn es opcional 
# si tiene return devuelve algo