
#clave unica 

intentos_fallidos = 0
clave_ingresada = 'Admin123'
clave_correcta = 'Secreto'

if clave_ingresada  == clave_correcta: 
    print(f"clave correcta: acceso concedido")
else: 
     intentos_fallidos =+1
print(f"intentos fallidos {intentos_fallidos}")



