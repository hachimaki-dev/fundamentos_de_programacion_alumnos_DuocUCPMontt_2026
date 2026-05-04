servidor= 16384 #Mb
os= 2560 #Mb
programas= 4915.2 #Mb
almacenamiento_utilizado= os + programas
almacenamiento_restante= servidor - almacenamiento_utilizado

print(f"Tienes {almacenamiento_restante} de espacio disponible")