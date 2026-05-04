velocidad=120
paso="Camion"
vel_camion=95

if velocidad > 80 and paso=="Camion":
    print("multa grave camion")
elif velocidad > 120 and paso=="Auto":
    print("multa gravisima")
else:
    print("no hay multa")