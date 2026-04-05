duracion_total = 0

while duracion_total <= 60: 
    if duracion_total == 60:
        print("¡Tu playlist está completa!")
        break
    minutos = int(input("Minutos de la siguente cancion: "))

#verificar si la cancion cabe 
if duracion_total + minutos <= 60: 
    print(f"cancion agregado. Total actual: {duracion_total} minutos") 

else:
    print(f"la cancion de {minutos} minutos no cabe") 
  
print("Duración final guardada:", duracion_total, "minutos") 