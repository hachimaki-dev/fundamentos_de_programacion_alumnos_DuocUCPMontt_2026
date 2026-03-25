#Hacer un algoritmo en diagrama de flujos y luego que lo valide mi compañero, crear el codigo.

#Adivinar un numero determinado entre 1 y 10. Si el usuario se equivoca, volver a preguntar. Si el usuario acierta, entonces felicitarlo 

numero_secreto = 4 

numero_ingresado = 0 

while numero_secreto != numero_ingresado: 
    numero_ingresado = int(input("Ingrese numero a adivinar"))
    print("Has fallado, porfavor volver a intentar")

if numero_secreto == numero_ingresado:
    print("Has acertado felicidades")
