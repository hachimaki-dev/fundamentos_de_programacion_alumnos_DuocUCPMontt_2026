duracion_total = 0
minutos = 0
contador = 0

print("Bienvenido al reproductor de Python")
print("Este reproductor consta de una capacidad máxima de 60 minutos")

while duracion_total < 60:
    contador = contador + 1
    minutos = int(input(f"Por favor, indique los minutos de la canción {contador} "))

    if duracion_total + minutos <= 60:
        duracion_total += minutos
        print(f"Su cancion {contador} ha sido agregada. Le queda un total de {60 - duracion_total} minutos ")
    else:
        print("LA CANCION NO CABEEEEE. Por favor seleccione una del tiempo adecuado")

print("CAPACIDAD AL 100%. Espero disfrutes de tu musica")