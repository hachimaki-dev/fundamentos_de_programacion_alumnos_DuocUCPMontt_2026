
#Inicio del jueguito de rol
eleccion = ""
vidajefe = 1000

while vidajefe>0:
    eleccion = int(input("Ingrese daño de ataque: "))
    if eleccion<0:
        print("El ataque ha fallado")
    if eleccion>=0:
        vidajefe -= eleccion
        print(f"El jefe le queda {vidajefe} de vida")
    if vidajefe <=0:
        print("El jefe ha sido cruelmente derrotado, ¡Felicidades!")
        break
#Fin del jueguito de rol