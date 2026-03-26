#Adivinar el numero
numero_secreto = 7
numero_adivinado = 0

#Pedir numero por primera vez
numero_adivinado = int(input("ingrese un numero entre el 1 y 10"))
while numero_adivinado != numero_secreto :
    print("Fallaste, intentalo de nuevamente")
    numero_adivinado = int(input("ingrese un numero entre el 1 y 10"))

print("!Acertaste¡ :")