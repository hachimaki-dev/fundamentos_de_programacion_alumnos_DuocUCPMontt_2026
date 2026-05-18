intentos=0
clave_real=4321

while True:

   intentos == input("ingrese su clave:  ")

   if intentos == clave_real:
      print("acesso exitoso. bienvenido")
      break
   else:
      intentos= intentos + 1
      print(f"clave incorrecta- intento {intentos} de 3.")
    
    if intentos == 3:
        print('Bloqueo de Tarjeta')
    
if break



    

