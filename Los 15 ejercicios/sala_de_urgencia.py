print("#####"*15)
print("     S   a   l  a    d  e     U  r  g  e  n  c  i  a s  ")
print("#####"*15)

edad = int(input("Ingrese su edad:   "))
dificultad_respirar = input("¿Tiene Dificultades para Respirar (si / no ):   ").lower()
nivel_de_dolor = int(input("Ingrese que Nivel de Dolor tiene ( del 1 al 10 ):  "))

if dificultad_respirar == "si":
    print("URGENCIA NIVEL 1 , Pase inmediatamente")
elif dificultad_respirar == "no" and edad > 60 and nivel_de_dolor > 7:
    print("URGENCIA NIVEL 2, Pase Pronto ")
elif nivel_de_dolor < 4 :
    print("URGENCIAS NIVEL 5, puede irse a su Casa o a Consultorio.")
else:
    print(" URGENCIAS NIVEL 3-4 , tome asiento por favor ")