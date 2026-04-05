print("bienvenido")
duracion_total = 0
while duracion_total <= 59 :
    min = int(input("ingrese minutos de la cancion"))
    duracion_total = duracion_total + min
  
    if duracion_total > 60 :
        print(f"la cancion de {min} minutos no cabe, por ende no se agrega")
        duracion_total = duracion_total - min
    print(f"llevas acupado {duracion_total}")
   
    

print("espacio lleno al 100%")
print("fin")    

###if min > 60 :
    ##    duracion_total = duracion_total - min
      ##  print("demasiado pesada, no se agrega")