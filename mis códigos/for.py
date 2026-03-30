panchitos = ["Benja", "Matias", "Franco", "Beto", "Brayan", "Micaela"]

for panchos in panchitos:
    print(panchitos)

suma = 0
for i in range(1, 6):
    suma += i

print(suma)

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} es par.")
    else:
        print(f"{i} es impar")

for i in range(1, 1288):
    if i < 777:
        print(f"{i} No es simetrico")
    if i == 777:
        print(f"{i} ¡Pero madre mía willy que haces aqui compañero!")

# a diferencia del while, en el for si es necesario determinar
# la cantidad de vueltas de alguna forma.

print(f"Los panchitos informaticos son: {panchitos}")