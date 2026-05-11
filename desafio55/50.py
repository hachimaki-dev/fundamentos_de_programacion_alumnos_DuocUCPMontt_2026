cuenta = {
    "papas": 5000, 
    'Pizza' : 10000
}
subtotal = 0
for alimentacion, precio in cuenta.items():
    subtotal += precio
propina = subtotal *0.10
total_final = subtotal + propina
print(f"Total final ${total_final}")
    
