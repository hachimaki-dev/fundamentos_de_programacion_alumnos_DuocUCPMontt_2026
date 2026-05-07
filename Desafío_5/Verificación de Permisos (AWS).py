admin = {"ROL" : "DEV", "PERMISOS" : {"S3" : True,
        "EC2" : False}}

if admin["PERMISOS"]["EC2"]:
    print ("Creando Instancia")

else:
    print ("Permiso denegado")