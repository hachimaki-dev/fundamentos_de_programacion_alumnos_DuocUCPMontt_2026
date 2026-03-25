# Hacer un algoritmo en diagrama de flujos y luego que lo valide mi compañero, crear el codigo
# Adivinar un numero determinado entre 1 y 10. Si el usuario se equivoca, volver a preguntar.
# Si el usuario acierta, entonces felicitarlo

numero_secreto = 3
numero_usuario = 0

while numero_secreto != numero_usuario : 
    numero_usuario = int(input("Adivine un numero entre 1 y 10: "))
    if numero_usuario != numero_secreto:
        print("Lo lamento, fallaste")
print("Felicidades")