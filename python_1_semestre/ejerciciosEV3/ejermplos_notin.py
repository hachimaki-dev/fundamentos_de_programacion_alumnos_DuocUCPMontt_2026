
contador = 0
while contador == 0:
    nombre = input("ingresa un nombre:")
    tamano= len(nombre)
    if  "@" not in nombre :
        print("errros")
    else:
        print("bien hecho")
        contador +=1