print("bienvenidos a sala de urgencias")
print("introdusca su edad")
edad = int(input(""))
print("introdusca su nivel de dolor entre 1 - 10")
nivel_de_dolor = int(input(""))
print("tienes problemas para respirar??")
respuesta = input(f" SI o NO ")
if respuesta == "SI":
    print("URGENCIAS NIVEL 1 pase inmediatamente")
elif respuesta == "NO" and edad >= 60 and nivel_de_dolor >= 7:
    print("URGENCIAS NIVEL 2, pase pronto.")
elif nivel_de_dolor < 4:
  print("URGENCIAS NIVEL 5, puede irse a su casa o a consultorio.")
else:
   print("URGENCIAS NIVEL 3-4, tome asiento por favor.")
