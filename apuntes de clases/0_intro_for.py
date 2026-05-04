vida_del_jefe = 1000

while True:
    print("bienvenido a esta epica batalla!")
    respuesta = input("¿se encuentra apto para comenzar esta batalla?: (si/no) ")
    if respuesta == "si":
        break
    elif respuesta == "no":
        print("huiste de la batalla como un cobarde")
        exit()
    else:
        print("La opción ingresada no es valida, vuelva a intentarlo")

print("LA BATALLA VA A COMENZAR!")
print(f"La vida del jefe es de {vida_del_jefe}")

while vida_del_jefe > 0:
    try:
        daño = int(input("ingrese el daño del ataque: "))
        if daño <= 0:
            print("el ataque fallo")
        else:
            vida_del_jefe -= daño
            if vida_del_jefe < 0: vida_del_jefe = 0
            print(f"la vida restante es de: {vida_del_jefe}")
    except ValueError:
        print("ingrese un valor valido")
    
print("HAZ DERROTADO A LA GRAN AMENEZA. Ahora ve y toca pasto")
