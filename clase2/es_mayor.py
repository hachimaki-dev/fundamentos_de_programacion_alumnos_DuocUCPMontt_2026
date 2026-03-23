# Determinar la edad #

print("Esta entrando en una pagina donde se requiere que sea mayor de edad")
print("Por favor, diganos su edad en la sección de abajo ")

print("¿Cúal es su edad ?")

edad_de_usuario = int(input ("Ingrese su edad : "))

if edad_de_usuario <= 17 :
    print ("Usted es menor de edad, Se cancalera su ingreso")

elif edad_de_usuario >= 18 or edad_de_usuario <= 50 :
    print ("Bienvedio a nuestra pagina de apuestas, disfrute y que tenga suerte :) ")

else : 
    print ("Usted es mayor de 50 por lo cual tiene prohibido entrar a esta pagina")




print ("Bienvedio a nuestro juego de  ")

nombre_usuario1 = str(input ("Ingrese su nombre : "))

print ("Un saludo" + nombre_usuario1 )

