# Esta es la salida más simple.
print 

import modulo
modulo.dividir (218, 37)

Respuesta = input('Ingresa tu edad: ')
Edad = int(Respuesta)

if Edad > 14:
     print('Desactiva cam')
elif Edad < 14:
     print('Ve comprando la cam')
elif Edad == 14:
     print('Tienes 14, activa cam')
else:
     print('No tienes 14')

#Los prints pueden concatenar.
#Interpolación es imprimir una variable dentro de una cadena de texto.
usuario1 = "Brayan"
usuario2 = "Franco"
usuario3 = "Matias"

print(f"El primer usuario es: {usuario1}, y el segundo usuario es: {usuario2} y el tercer usuario es: {usuario3}")


#Vas a crear un programa en python que de la bienvenida al recorrido puerto montt alerce