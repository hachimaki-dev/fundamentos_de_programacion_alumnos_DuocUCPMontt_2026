# Preguntar cantidad de platos
cantidad_platos = int(input("¿Cuántos platos desea pedir señor/a? "))

#acumulador para el total
subtotal = 0 

#ciclo while con contador 
i = 0 
while i < cantidad_platos:
    precio = int(input(f"Ingrese el precio del plato {i+1}: "))
    subtotal += precio 
    i += 1  
 #evaluar el subtototal
print("\nResumen del pedido:") 

if subtotal > 16000:
    descuento = subtotal * 0.15
    total = subtotal - descuento
    print(f"subtotal: ${int(subtotal)}") 
    print(f"descuento aplicado: ${int(descuento)}")
    print(f"total a pagar: ${int(total)}")

else: 
    envio = 5000
    total = subtotal + envio
    print(f"subtotal: ${int(subtotal)}")
    print(f"costo de envío: ${int(envio)}")
    print(f"total a pagar: ${int(total)}")
 