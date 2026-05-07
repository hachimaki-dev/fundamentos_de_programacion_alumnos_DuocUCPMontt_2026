#Ejercicio : Ejercicio 24: Generador de Nombres (Instagram)
#MEDIUM
#Vas a automatizar la creación de perfiles falsos para hacer pruebas.[cite: 2]

#Datos Iniciales: La palabra base de todos los nombres será 'user_'.[cite: 2]

#Reglas de Negocio: Necesitas generar exactamente 5 usuarios, numerados del 1 al 5. (ejemplo: user_1, user_2, etc).[cite: 2]

#Restricciones: Usa un ciclo for con la herramienta range(). Recuerda que en Python, el range se detiene un número ANTES del final, así que ajusta el límite para que llegue a 5. Imprime los nombres generados en cada vuelta.[cite: 2]

base_usuario = "user_"
for i in range(1, 6):
    user_completo = base_usuario + str(i)
    print(user_completo)


