#Este es un output basico 
print("Hello World")

#Estos son variables y puedo guardar lo que me de en gana 
usuario_1 = "Juan"
usuario_2 = "Seba"
usuario_3 = "Yosmer"

es_mayor_de_edad = True
estatura_usuario_1 = 170.5
edad_usuario_1 = 27 

#A continuacion aprenderemos a concatenar 
#con mis propias palabras explicar lo que entiendo por concatenar = es unir variables dentro de una cadena de textos
print("El nombre del primer usuario es " + usuario_1 + " y el nombre del segundo usuario es " + usuario_2 + " y el nombre del tercer usuario es " + usuario_3)

#Hay una forma mas elegante, esta es la interpolacion de variables (la F es la que pone la interpolacion)
print(F"El nombre del primer usuario es {usuario_1} y el nombre del segundo usuario es {usuario_2} y el nombre del tercer usuario es {usuario_3}")