camion = 95
tipo = "camion"

if camion > 120:
    print("MULTA GRAVISIMA")
elif camion > 80 and tipo == "camion":
    print("MULTA GRAVE CAMION")
elif camion > 80 :
    print("MULTA GRAVE")
elif camion < 80:
    print("NO HAY MULTA")
    