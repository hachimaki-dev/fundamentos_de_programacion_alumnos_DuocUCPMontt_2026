print("#####Adivina el Numero####")

numero_secreto = 7 
numero_adivinado = 0
while numero_adivinado != numero_secreto :
    numero_adivinado = int(input("Seleccione un numero entre 1 y 10"))
    if numero_adivinado != numero_secreto :
        print("Fallaste")

print("acertaste")
        


