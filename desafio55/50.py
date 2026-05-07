cuenta = {
    "Papas" : 5000,
    "Pizza" : 10000

}

suma = 0

for claves, valores in cuenta.items():
    suma = suma + valores
    

propina = suma*0.1
suma = suma + propina
print("Total final: ", suma)