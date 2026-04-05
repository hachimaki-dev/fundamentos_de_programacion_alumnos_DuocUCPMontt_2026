cantidad = int(input("¿cuantos perros paseaste hoy?:"))

contador = 0
total = 0 

#ciclo para cada perro 
while contador < cantidad: 
    peso = float(input(f"ingrese el peso del perro {contador + 1} en kg: " ))

    if peso < 10: 
        precio = 2000
    elif peso < 25: 
       precio = 6000

    total += precio 
    contador += 1 

    print (f"Resumen del día: has paseado {cantidad} perros, ganando en total ${total}") 