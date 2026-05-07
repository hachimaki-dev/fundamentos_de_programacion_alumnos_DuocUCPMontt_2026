#Ejercicio 24: Generador de Nombres (Instagram)
#Vas a automatizar la creación de perfiles falsos para hacer pruebas.

#Datos Iniciales: La palabra base de todos los nombres será 'user_'.

#Reglas de Negocio: Necesitas generar exactamente 5 usuarios, numerados del 1 al 5. (ejemplo: user_1, user_2, etc).

#Restricciones: Usa un ciclo `for` con la herramienta `range()`. Recuerda que en Python, el `range` se detiene un número ANTES del final,
# así que ajusta el límite para que llegue a 5. Imprime los nombres generados en cada vuelta.

#oOPCION BASE
print("")
for i in range(1, 6):
    print(f"user_{i}")
print("")

#OPCION AVANZADA
users_ig=[]

for i in range(1, 6):
    name=input("Ingrese su nombre de usuario ")
    users_name=(f"user_{name}")
    users_ig.append(users_name)

print("\nUsuarios creados:")

for users_name in users_ig:
    print(users_name)
print("")