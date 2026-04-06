numero_secreto = 42
respuesta_usuario = 0
while respuesta_usuario != numero_secreto :
    respuesta_usuario = int(input("Ingrese un numero :"))
    if respuesta_usuario <= 50 : 
     print("Ingresaste un numero muy alto")
      