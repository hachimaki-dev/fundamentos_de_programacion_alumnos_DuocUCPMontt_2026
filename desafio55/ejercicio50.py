cuenta = {"papas": 5000, "pizza": 10000}

total = 0
propina = 0
for comida, precio in cuenta.items():
    total += precio
    print(total)
    propina = total * 0.10
    total_final = total + propina

print(f"El total a pagar es {total_final}")