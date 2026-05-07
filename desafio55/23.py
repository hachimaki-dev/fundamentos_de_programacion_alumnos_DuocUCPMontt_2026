intentos_fallidos = 0
clave_ingresada = "123"

while True :
 
     clave_ingresada = input(" ingrese clave")
     if clave_ingresada == "123":
      print("acceso permitido")
      break
     else: 
        intentos_fallidos += 1
        print(f"clave incorrecta. intento {intentos_fallidos} son 3.") 

        if intentos_fallidos == 3:
          print("tarjeta bloqueada")
