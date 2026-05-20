#Crea es_par(numero) que retorne True si el número es par, y False si es impar

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(5))