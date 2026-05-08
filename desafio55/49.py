admin = {
    "rol" : "dev",
    "permisos" : {
        "S3" : True, 
        "EC2" : False
    }
}
if admin["permisos"]["EC2"]:
    print("creamos instancia")
else:
    print("Acceso denegado")
