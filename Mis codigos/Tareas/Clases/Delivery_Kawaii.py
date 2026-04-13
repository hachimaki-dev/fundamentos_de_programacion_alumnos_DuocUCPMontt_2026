Fideos_boloñesa = 4000
Pure_pollo = 6500
Salchipapa350 = 3500
Salchipapa500 = 5000
completo = 3500

Pedido = []
total = 0
print("Buenas tardes. Bienvenido a KawaiiDelivery\nA continuaciòn te dejarè el menù para que ordenes tu pedido\nPor cierto, a partir de los 20.000 pesos hay descuento ;)\n")

while True:
    print("___Menu KawaiiDelivery___\n\nPlatos fuertes:\n\n1-. Fideos a la boloñesa (4000)\n2-. Pure con pollo asado (6500)\n3-. Salchipapas 350g (3500)\n4-. Salchipapas 500g (5000)\n5-. Completo italiano (3500)")

    comida = input("¿Què desea ordenar?")
    if comida == "1":
        Pedido = Pedido + ["Fideos a la boloñesa"]
        total = total + Fideos_boloñesa
    elif comida == "2":
        Pedido = Pedido + ["Purè con pollo asado"]
        total = total + Pure_pollo
    elif comida == "3":
        Pedido = Pedido + ["Salchipapas 350g"]
        total = total + Salchipapa350
    elif comida == "4":
        Pedido = Pedido + ["Salchipapas 500g"]
        total = total + Salchipapa500
    elif comida == "5":
        Pedido = Pedido + ["Completo italiano"]
        total = total + completo
    else:
        print("Opcion invàlida")
    
    mas = input("¿Desea algo màs? (si/no): ").lower()
    if mas == "no":
        break

if total >= 20000 and total <= 29999:
    descuento = total * 0.1
    total_con_descuento = total - descuento
elif total >= 30000 and total <= 39999:
    descuento = total * 0.15
    total_con_descuento = total - descuento
elif total >= 40000:
    descuento = total * 0.30
    total_con_descuento = total - descuento
else:
    descuento = 0
    total_con_descuento = total

print("\n\nGracias por pedir en KawaiiDelivery\n")
print(f"Pedido: {Pedido}")
print(f"Total: {total}\n")
print(f"Descuento: {int(descuento)}")
print(f"Total a pagar: {int(total_con_descuento)}")













