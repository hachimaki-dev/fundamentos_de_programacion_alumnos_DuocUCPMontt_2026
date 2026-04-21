# Desarrolla un sistema de validación de acceso que solicite mediante texto a qué grupo de K-Pop pertenece el usuario. El programa actuará como un guardia de seguridad y solo permitirá el paso a miembros de grupos autorizados. 

"""
Crea un bucle de validación donde el usuario deba ingresar el nombre de su grupo favorito usando un input().

Utiliza la estructura while combinando lógicas múltiples (con and y el comparador !=) para evaluar si el ingreso resulta no ser autorizado. Es decir, que el ciclo siga solicitando datos mientras no sea "BTS", tampoco sea "BLACKPINK", ni sea "Stray Kids".

Si el usuario ingresa cualquier otro valor erróneo, deberá quedar atrapado pidiéndoselo nuevamente en la misma consola de ingreso general dentro de la limitante cíclica temporal sin excepción permitiendo salida lógica a las restantes ejecuciones programadas fuera de las llaves del bucle.

Una vez que se ingrese exitosamente una de las tres opciones válidas y finalice el ciclo general, procede a imprimir un "¡Acceso Concedido! Bienvenido al Fandom." de manera exitosa para informar que validó el programa.
"""

fandom_del_usuario = ""
proceso_de_ingreso = True

print("Bienvenido al concierto!")
print("- - - - - - - - - - - - - - - - - - - - \n")
print("BTS | BLACKPINK | Stray Kids \n")
while fandom_del_usuario != "BTS" and fandom_del_usuario != "BLACKPINK" and fandom_del_usuario != "Stray Kids":
    print(fandom_del_usuario)
    pregunta_de_seguridad = input("Cual es su grupo preferido? \n []: ").lower()
    try:
        if pregunta_de_seguridad == "bts":
            print("Bienvenido al fandom de BTS!")
            fandom_del_usuario = "BTS"
            continue
        if pregunta_de_seguridad == "blackpink":
            print("Bienvenido al fandom de BLACKPINK")
            fandom_del_usuario = "BLACKPINK"
            continue
        if pregunta_de_seguridad == "stray kids":
            print("Bienvenido al fandom de Stray Kids!")
            fandom_del_usuario = "Stray Kids"
            continue
        else:
            print("Banda no esta presente!")
    except:
        print("Banda no valida")
