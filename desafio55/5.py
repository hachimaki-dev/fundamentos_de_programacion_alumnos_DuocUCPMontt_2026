saldo = 10000

pasaje_micro = 730

pasaje_metro = 850

recarga = 3000

#en el dia toma 1 micro y 2 metros, y luego de eso recargas la tarjeta 

print("\n\nTienes $10.000 en tu Tarjeta BIP")
print(f"\nUsaste un minibus hoy: - ${pasaje_micro} \nY tambien usaste 2 veces el transporte en metro: - ${pasaje_metro * 2}")

resta_saldo = pasaje_metro + pasaje_micro + pasaje_metro

total = saldo - resta_saldo

print(f"Tienes ${total} en tu cuenta BIP.")
respuesta = int(input("Deseas recargar los 3000?:\n1.- si\n2.- no"))
if respuesta == 1:
    total = total + 3000
    print(f"Tienes ${total} en total")
else: 
    print(f"tienes ${total}")

