print ("/=================================/")
print ("/========Reproductor MP3==========/")
print ("/=================================/")

import time
import sys

print ("Bienvenido a un reproductor mp3.")
print ("Aquí podras guardar tus canciones favoritas o las que mas prefieras.")
print ("Aunque tendras que tener en cuenta que solo se permiten canciones con minutos exactos o que no superen los 60 minutos.\n")

print ("Si no quedo claro, aquí una explicación más clara.\n")

print ("1. Podras guardar canciones pero estas se acumularan dependiendo del tiempo.")
print ("2. Entre más se acumulen canciones menos espacio te quedara.")
print ("3. El mp3 cuenta con un espacio de 60 Minutos como maximo.")
print ("4. En caso de gastar la mitad se le notificara.\n")

print ("Dicho todo, empieza a guardar tus canciones favoritas.")
print ("Para que nunca te falten en viajes.\n")

contador_de_minutos = 0

while contador_de_minutos < 60 : 
    print ("Bien, dime que canción deseas guardar, indicando nombre y duranción de esta misma.")
    Nombre_de_la_cancion = str(input ("Ingrese el nombre de su canción : ")).lower()
    print (f"La canción {Nombre_de_la_cancion} me parece muy interesante. \n")
    durancion_de_la_cancion = float(input("Ingrese la duración de la canción :"))
    print ("Bien, ahora se guardara su canción.\n")
    time.sleep(5)


    contador_de_minutos = contador_de_minutos + durancion_de_la_cancion
    print (f"Hemos guardado {Nombre_de_la_cancion} con una duranción de {durancion_de_la_cancion}")
    print (f"Ha usado un total de {contador_de_minutos}.\n")

else:
    print ("Usted se quedo sin espacio, ha usado el ' 100% ' del espacio.")








