valor_frascos = 100
monedas = 500
valor_hierba = 50
Monedas = 500
import time 

while Monedas > 0:

    compras_de_frascos = int(input("¿Cuántos frascos vas a llevar? : "))
    print()
    print (f" 'Bien, creo que me llevare {compras_de_frascos} frascos.'\n")
    print (f" 'Bueno, ahora veamos cuantas hierbas me llevo.'\n")
    total_de_frascos = valor_frascos * compras_de_frascos
                

    compras_de_hierbas = int(input("¿Cuántas hierbas te vas a llevar? : "))
    total_de_hierbas = valor_hierba * compras_de_hierbas
    print()
    total_de_compras = total_de_frascos + total_de_hierbas
    print (f"'Me llevare unas {compras_de_hierbas} hierbas.'")

    if total_de_compras > monedas:
        print ("Dinero insuficiente, vuelva a comprar.")
        continue


    print ("CAMINO AL CAJERO...")
    time.sleep(3)

    Monedas -= total_de_compras  # 🔥 aquí se descuenta el dinero

    print("\n🛒 Resumen de compra:")
    print(f"Frascos: {compras_de_frascos} -> ${compras_de_frascos}")
    print(f"Hierbas: {compras_de_hierbas} -> ${compras_de_hierbas}")
    print(f"Total: ${total_de_compras}")
    print(f"💵 Dinero restante: ${Monedas}")

    print("\nCAMINO AL CAJERO...")
    time.sleep(2)

    if Monedas == 0:
        print("\n💀 Te quedaste sin dinero")
        break



    

