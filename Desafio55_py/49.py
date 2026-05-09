admin = {"rol" : "dev" , "permisos" : {"S3" : True , "EC2" : False}}


if admin["permisos"]["EC2"] == True :
    print("CREANDO INSTANCIA")
else:
    print("ACCESO DENEGADO")
    