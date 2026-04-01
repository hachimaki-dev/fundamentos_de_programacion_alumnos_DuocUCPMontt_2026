import sys
paciente = int(input("Ingrese su edad : "))
dificultad = input("Siente que le falta aire? (ingrese su respuesta como Si o No) : ")
dolor = int(input("del 1 al 10 , cuanto dolor siente? :"))

if dificultad == "Si" or "si" or "sI" :
    print ("quiero que mantenga la calma en estos momentos")
    print("sera llamado enseguida")
    sys.exit
elif paciente <= 60  and dolor <= 6:
    print ("Usted acaba de ingresar a la lista grado 2 en urgencia , sera llamado a la brevedad")
    sys.exit
elif paciente  <= 50 and dolor <= 4 :
    print("Usted acaba de ingresar a la lista grado 3 , sera llamado en las proximas horas")
else : 
    print("Se recomienda asistir a un centro de asistencia municipal , favor no usar la urgencia si no es una urgencia")    

