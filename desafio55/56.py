palabra_base = "user_"

# Usamos range(1, 6) para empezar en 1 y terminar exactamente en 5
for i in range(1, 6):
    nombre_usuario = f"{palabra_base}{i}"
    print(nombre_usuario)