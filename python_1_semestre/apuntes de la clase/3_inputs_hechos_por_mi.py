# 1 - ENTRADA DE DATOS BASICOS
# leer datos del usuario con input()
# input () pausa el programa y espera que el usuario ingrese algo 
# siempre devuelve un txt (str) incluso si el usuario escribe un numero.

print("INPUT BASICO: ")
print("")

nombre = input("como te llamas: ")
print ("enhorabuena, saludos", nombre + " " "eres bienvenido")
#aca se junta el print con el valor de "nombre" `+ el str
apellido = input("cual es tu apellido?: ")
print ("wow asi que tu nombre es, ", nombre + " " + apellido+ " " + "que maravilloso c:")
# aca junte las variables asignadas por input entre ellos +`otro str 
pasatiempo = input("cual es tu pasatiemnpo?: ")
print(f"entonces", nombre,apellido, "tu pasatiempo es " " ", pasatiempo, "suena como buen pasatiempo" )
# la consola no avanza hasta que se ingrese las entradas del usuario. 