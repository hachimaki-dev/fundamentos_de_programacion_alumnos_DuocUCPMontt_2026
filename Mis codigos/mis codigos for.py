for i in range(5):
    print(i)

# Imprime: 0, 1, 2, 3, 4


suma = 0  # ← inicializar ANTES

for i in range(1, 6):
    suma += i  # ← actualizar DENTRO

print(suma)  # ← usar DESPUÉS → 15