Boss = {"HP" : 100, "ESTADO" : "vivo"}


(Boss["HP"]) -=150

if Boss["HP"] < 0 :

    Boss["ESTADO"] = "Muerto"
    Boss["HP"] = 0

    print (Boss)
