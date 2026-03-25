numerosecreto = 9
numeroselecto = int(input("Por favor, seleccione un número entre el 1 y el 10. "))
while numeroselecto != numerosecreto:
    print("Se ha equivocado.")
    numeroselecto = int(input("Por favor vuelva a ingresar otro digito. "))
print("Felicidades, has adivinado el número.")