print("averigua si el numero es par!")
def es_par(numero):
    if numero %  2 == 0:
        return True
    else:
        return False
resulatdo = es_par(int(input("ingresa un numero: ")))
print(resulatdo)