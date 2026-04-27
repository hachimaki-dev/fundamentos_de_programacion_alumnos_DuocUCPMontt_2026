# TERMINADO PERO REVISA Y ESTUDIA

print("==== DELIVERY APP NCL ====")

cantidad_platos = int(input("cuantos platos desea pedir:"))

platos_registrados = 0
total_a_pagar = 0

while platos_registrados < cantidad_platos:
    
    print(f"plato {platos_registrados + 1}")
    precio_de_comida = int(input("¿cuanto cuesta su plato?:"))

    total_a_pagar += precio_de_comida
    platos_registrados += 1
    
    continue


if platos_registrados == cantidad_platos and total_a_pagar <= 15000:  

    print(f"su precio a pagar es {total_a_pagar} \n Envio: $2000 \n total a pagar {total_a_pagar + 2000}") 

elif total_a_pagar > 15000 and platos_registrados == cantidad_platos:

    
    descuento = total_a_pagar * 0.10
    print(f"subtotal {total_a_pagar} descuento del 10% activado \n se le descuentan {descuento} su precio final es de {total_a_pagar - descuento}")