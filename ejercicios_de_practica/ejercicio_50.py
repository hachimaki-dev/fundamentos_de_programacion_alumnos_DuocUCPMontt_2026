cuenta = {"Papas": 5000, "Pizza": 10000}
total = 0

for i, k in cuenta.items():
    total += k

total *= 1.10
print(f"Total final: {total}")