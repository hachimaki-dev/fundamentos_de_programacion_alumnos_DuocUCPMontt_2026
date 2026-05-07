alcansia = 0
por_mes = 80000
consola = 450000

meses = 0

while True:
     meses += 1
     alcansia += por_mes
     print (f"ya paso {meses} y ahorrarste {alcansia}")

     if alcansia >= consola:
          break