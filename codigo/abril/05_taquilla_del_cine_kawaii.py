contador = 1
acumulador_precio = 0

valor_entrada_regular = 6000
valor_entrada_ninos = 3000
valor_entrada_tercera_edad = 4000

edad_maxima_ninos = 11
edad_minima_tercera_edad = 65

total_de_entradas = int(input("¿Cuántas entradas se van a comprar?: "))

while contador <= total_de_entradas:
    edad_cliente = int(input(f"¿Edad del cliente {contador}?: "))

    if edad_cliente <= edad_maxima_ninos: # Entrada niños
        acumulador_precio += valor_entrada_ninos
        print(f"Valor entrada niño: ${valor_entrada_ninos}, Precio actual: ${acumulador_precio}\n")
        contador = contador + 1

    elif edad_cliente > edad_maxima_ninos and edad_cliente < edad_minima_tercera_edad: # Entrada regular
        acumulador_precio += valor_entrada_regular
        print(f"Valor entrada regular: ${valor_entrada_regular}, Precio actual: ${acumulador_precio}\n")
        contador = contador + 1
    
    elif edad_cliente >= edad_minima_tercera_edad: # Entrada tercera edad
        acumulador_precio += valor_entrada_tercera_edad
        print(f"Valor entrada tercera edad: ${valor_entrada_tercera_edad}, Precio actual: ${acumulador_precio}\n")
        contador = contador + 1
        
print(f"Total a pagar: ${acumulador_precio}")       
