cuenta = {"Papas" : 5000,
          "Pizza" : 10000}

total = 0

for key, value in cuenta.items() :
    total += value

total *= 1.1

print(f"Total final: {total}")