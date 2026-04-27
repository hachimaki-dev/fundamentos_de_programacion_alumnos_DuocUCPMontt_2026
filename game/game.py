#Novela visual "El último mensaje"

 #Textos
print(input("-El último mensaje-"))

print(input("Estás solo en tu casa, son las 2:13 am."))
print(input("Tu teléfono vibra,"))
print(input("Es un número desconocido: No abras la puerta, Ya estoy dentro."))

#Decision 1
print(input("¿Que Haces?"))
print(input("1. Revisar la casa."))
print(input("2. Ignorar el mensaje."))

desicion1 = input("elige una decisión: > ")

if desicion1 == "1":
    print(input("Tomas aire y caminas por el pasillo,"))
    print(input("Todo está en silencio... hasta que escuchas un leve sonido en el baño,"))
    print(input("La puerta esta entreabierta."))
elif desicion1 == "2":
    print(input("Decides ignorarlo, piensas que problamente sea una tonta broma,"))
    print(input("Y sigues jugando al minecraft."))
    print(input("Despues de un par de minutos, el teléfono vibra de nuevo."))
    print(input("Esta vez.... es un audio, lo reproduces.."))
    print(input("Y escuchas tu propia voz: "))
    print(input("¨Estoy en el baño, no entres¨."))

else:
    print("No has elegido ninguna decisión")


#Desicion 2
    print(input("¿Que Haces?"))
    print(input("3. Abrir la puerta del baño."))
    print(input("4. Retroceder y salir de la casa."))

    desicion2 = input("elige una desición: > ")

    if desicion2 == "3":
        print(input("Empujas la puerta lentamente.."))
        print(input("el baño está vacío."))
        print(input("Pero el espejo... no refleja ningún movimiento,"))
        print(input("tu reflejo sonríe."))
        print(input("¨Pantalla en negro¨"))
        print(input("¨Simulación inestable detectada¨"))
    elif desicion2 == "4": 
        print(input("Corres hacia la salida,"))
        print(input("Abres la puerta y sales.... pero ... apareces nuevamente dentro de tu casa"))
        print(input("Exactamente en el mismo lugar."))
        print(input("Tu teléfono vibra otra vez,"))
        print(input("¨No puedes salir¨"))
        print(input("¨Reíniciando Entorno¨")) 
    else:
        print("No has elegido ninguna decisión")    

#Desición 3
print(input("¿Que Haces?"))
print(input("5. Ir al baño."))
print(input("6. Apagar el teléfono."))

desicion3 = input("elige una desición: > ")

if desicion3 == "5":
    print(input("Te acercas lentamente,"))
    print(input("la puerta está cerrada."))
    print(input("Desde dentro... alguien susurra: "))
    print(input("¨si estás escuchando esto, ya es tarde."))
    print(input("...Intentas abrir."))
    print(input("Aparece una pantalla en negro."))
    print(input("¨Error de duplicación de sujeto."))
elif desicion3 == "6":
    print(input("Silencio Total......."))
    print(input("levantas la vista..."))
    print(input("Y frente a ti hay alguien identico a ti, sosteniendo el mismo teléfono."))
    print(input("Ambos reciben el mismo mensaje al mismo tiempo,"))
    print(input("¨No abras la puerta, ya estoy dentro¨."))
    print(input("Pantalla en negro: ¨Simulación completada¨."))
    
else:
    print("No has elegido ninguna decisión")

#El elif es una "abreviatura del else, if lo use para ahorrarme hardcodear el "if".
#Use print(input(" ")) para que al momento de que el usuario presione enter(input) se despliegue el str o string de texto dentro del print.


    

