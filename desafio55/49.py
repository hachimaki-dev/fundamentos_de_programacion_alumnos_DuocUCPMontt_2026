admin = {"rol":"dev", "permisos": {"S3": True, "EC2": False}}
if admin["permisos"]["EC2"] == True:        #Primero tomamos la clave, luego la clave dentro de la clave.
    print("Creando Instancia")
else:
    print("Acceso Denegado.")