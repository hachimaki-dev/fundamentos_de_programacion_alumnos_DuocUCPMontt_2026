cuenta_restaurante = {
    "Papas": 5000,
    "Pizza": 10000
}

subtotal = 0

print("--- BOLETA DE CONSUMO ---")


for plato, precio in cuenta_restaurante.items():
    print(f"{plato}: ${precio}")
    subtotal += precio  
porcentaje_propina = 0.10
propina = subtotal * porcentaje_propina
total_final = subtotal + propina

print("-------------------------")
print(f"Subtotal: ${subtotal}")
print(f"Propina (10%): ${propina}")
print(f"Total Final: ${total_final}")
