amigos= 5
dos_pichangas= 30000
schops= 17500
consumo= dos_pichangas + schops
propina= 10
consumo_total= consumo + (consumo*propina /100)
consumo_total= consumo_total / 5

print(f"Cada uno debe pagar {consumo_total}")