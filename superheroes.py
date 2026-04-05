misiones = int(input(" Cuantas misiones exitosas a tenido su superheroe?  "))
daños = float(input(" Cuantos daños civiles han sido provocados por su superheroe? "))

if misiones >= 10 and daños == 0:
    print(" Tu heroe es categoria S. Bono Maximo!")

elif 5 <= misiones <= 9:
    print(" Tu heroe es categoria A. Cumple promedio!")

elif misiones < 5 and daños > 10000000:
    print(" Tu heroe ha sido despedido. Demasiado caotico!!")

else:
    print(" Heroe en observacion!")
    