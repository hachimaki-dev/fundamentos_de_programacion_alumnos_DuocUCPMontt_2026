#Vas a automatizar la creación de perfiles falsos para hacer pruebas.

#Datos Iniciales: La palabra base de todos los nombres será 'user_'.

#Reglas de Negocio: Necesitas generar exactamente 5 usuarios, numerados del 1 al 5. (ejemplo: user_1, user_2, etc).

#Restricciones: Usa un ciclo `for` con la herramienta `range()`. Recuerda que en Python, el `range` se detiene un número ANTES del final, así que ajusta el límite para que llegue a 5. Imprime los nombres generados en cada vuelta.
user = "user_"
for i in range(1,6):
    print(f"{user}{i} ")