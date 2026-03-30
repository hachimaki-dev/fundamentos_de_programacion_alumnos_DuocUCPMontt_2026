# A diferencia del while, el for sí o sí debe saber cuántas vueltas hay que dar

# RANGE

for cada_elemento in range(5): # Primer tipo de rango, parte por el 0 y el límite es el valor en paréntesis (para en el número anterior)
    print(f"Hola, vamos en el número {cada_elemento}")

print("\n\n")

for cada_elemento in range(10, 20): # Segundo tipo de rango, parte por el primer valor y el límite es el segundo valor
    print(f"Hola, vamos en el número {cada_elemento}")

print("\n\n")

for cada_elemento in range(0, 101, 10): # Tercer tipo de rango, parte por el primer valor, el límite es el segundo valor y da pasos del tercer valor
    print(f"Hola, vamos en el número {cada_elemento}")

print("\n\n")

# CONTINUE

for i in range (6):
    if i % 2 == 0: # Módulo. Saca el resto de una división, en este caso una división por 2
        continue   # Vuelve a empezar el bucle, ignorando el código siguiente
    print(i)

print("\n\n")

# BREAK

for i in range (10):
    if i > 5:
        break
    print(i)
