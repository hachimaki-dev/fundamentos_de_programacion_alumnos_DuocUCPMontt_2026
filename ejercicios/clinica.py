print("bienvenido")
edad = int(input("ingrese su edad"))
respirar = input("tiene dificultad para respirar si/no")
dolor = int(input("nivel de dolor del 1 al 10"))
if respirar == "si" :
    print("URGENCIA NIVEL 1, pasa inmediatamente")
elif respirar == "no" and edad > 60 and dolor > 7 :
    print("urgencia nivel 2, pasa pronto")
elif dolor < 4 :
    print("urgencia nivel 5, puede ir a su casa o a consultorio")
else :
    print("urgencia nivel 3-4, tome asiento")

