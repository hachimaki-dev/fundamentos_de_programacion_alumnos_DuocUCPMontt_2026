""" >) y menor que (< {} """

edad = int(input("ingrese su edad:"))
if edad >= 18:
    vip = input("eres vip:")
    if vip == "si " or " SI ":
        print("bienvenido vip")
    elif vip == "no " or " NO":
        print("bienvenido")   
elif edad < 18:
    print("acceso denegado")
else:
    print("acceso denegado")
