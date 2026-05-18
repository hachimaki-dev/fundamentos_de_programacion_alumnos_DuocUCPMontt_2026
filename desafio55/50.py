cuenta = {"Papas": 5000, "Pizza": 10000}
total_final = 0
for plato, valor in cuenta.items():
    total_final = cuenta["Papas"] + cuenta["Pizza"]
    propina = total_final * 0.10
    total_final += propina

print("Total final " + str(total_final))   
