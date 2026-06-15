def verificadorMayorQ0(texto):

    while True:
        try:
            numero = int(input(texto))
            if numero > 0:
                return numero
            else:
                print("el numero tiene que ser mayor que cero")
        except ValueError:
            print("el valor tiene que ser un numero entero")
def verificadorTextoLen6(texto):
    while True:
        if len(texto) >= 6 and texto.isal():
            return texto
        else:
            print("el texto tiene que contener mas de 6 caracteres y no debe contener espacios o caracteres especiales")
            continue         
def sortExperiencia(objeto):
    objeto_verificado = verificadorMayorQ0(objeto)
    if objeto_verificado > 45:
        senior.append({"codigo":codigo_ingeniero,"nivel":nivel_tecnico})
        print(f"Ingeniero {codigo_ingeniero} registrado como Senior (nivel {nivel_tecnico})")
    else:
        junior.append({"codigo":codigo_ingeniero,"nivel":nivel_tecnico})
        print(f"Ingeniero {codigo_ingeniero} registrado como Senior (nivel {nivel_tecnico})")
senior = []
junior = []
cantidad_ing = verificadorMayorQ0("ingrese la cantidad de ingenieros")
for i in range(cantidad_ing):
    codigo_ingeniero = verificadorTextoLen6(input("ingrese su codigo de ingeniero"))
    nivel_tecnico = verificadorMayorQ0("ingrese su nivel tecnico")
    sortExperiencia(nivel_tecnico)