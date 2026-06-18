# Ejercicio 3 — Edad de un conductor para arriendo de autos

print("===================================")
print("Renta de autos para mayores de edad")
print("===================================")

while True:
    try:
        edad = int(input("Ingrese su edad por favor, su edad no puede ser ni 0 ni número negativo: "))

        if edad >= 18:
            print(f"La edad del usuario es {edad} por lo que puede rentar un veiculo")
            break
        elif edad <= 17:
            print(f"La edad del usuario es {edad} por lo que no puede rentar un veiculo")

    except ValueError:
        print("Error, lo sentimos pero no podemos rentarle un veiculo")