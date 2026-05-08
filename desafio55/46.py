ventas = {
    "LocalA" : 150,
    "LocalB" : 300,
    "LocalC" : 100
}
total_plata = 0
for monto in ventas.values():
    total_plata += monto

print(total_plata)