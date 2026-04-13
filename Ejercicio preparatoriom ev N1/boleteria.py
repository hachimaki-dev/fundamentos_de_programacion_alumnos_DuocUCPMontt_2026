total_venta= 0
precio_frutillar = 5000
precio_puertovaras= 3000
precio_osorno= 7000

print("bienvenido a boleteria")
print(" por favor indique su destino")


print("1. frutillar $5000")
print("2. puerto varas $3000")
print("3. osorno $7000")

destino_elegido= int(input("a donde desea ir?"))

if destino_elegido == 1: 
    print(f"1. ida 5000")
    print(f"2. ida y vuela 10000")

    
    total_venta = total_venta+ 5000

