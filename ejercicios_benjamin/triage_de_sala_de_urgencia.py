#pedir datos 
edad = int(input("Ingrese la edad: "))
respira = input("¿la persona tiene la dificultad para respirar? (si/no): ")
dolor = input("nivel de dolor de la persona del 1 al 10: ")

#lógica de triage 
if respira == "si":
    print("URGENCIA NIVEL 1 pase inmediatamente") 
elif respira == "no":
    if edad > 60 and dolor >= 7:
        print("URGENCIA NIVEL 2 pase lo antes posible") 
    
    elif dolor >= 4 and dolor < 7:
        print("URGENCIA NIVEL 5 puede irse a su casa o al consultorio")
    else: print("URGENCIA NIVEL 3-4: Tome asiento por favor")

else: print("Respuesta no válida.") 