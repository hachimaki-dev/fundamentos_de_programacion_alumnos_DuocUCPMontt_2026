# ============================================
# 37 - CICLO FOR (BREAK Y CONTINUE)
# Tema: Control de flujo en for
# Nivel: ⭐⭐⭐ Intermedio
# ============================================
# break y continue funcionan igual que en while.
# for también tiene el bloque else.

# --- BREAK: salir del bucle al encontrar algo ---
print("=== BREAK: BUSCAR NÚMERO ===")
n_buscar = input("¿Qué número buscas (1-20)? ")
numero_a_buscar = int(n_buscar) if n_buscar.isdigit() else 0

obj_encontrado = False
for n in range(1, 21):
    if n == numero_a_buscar:
        print(f"Encontrado! {numero_a_buscar} está en el rango")
        obj_encontrado = True
        break

if not obj_encontrado:
    print(f"{numero_a_buscar} no se encontró en el rango 1-20")

print()

# --- CONTINUE: saltar iteraciones ---
print("=== CONTINUE: SALTAR MÚLTIPLOS DE 3 ===")
print("Números del 1 al 20, saltando múltiplos de 3:")
for num_cont in range(1, 21):
    if num_cont % 3 == 0:
        continue    # salta el print
    print(num_cont, end=" ")
print("\n")

# --- Combinando break y continue ---
print("=== COMBINADO: FILTRAR Y BUSCAR ===")
print("Buscando el primer impar divisible por 7 entre 1 y 50")

for k in range(1, 51):
    if k % 2 == 0:
        continue    # saltar pares
    if k % 7 == 0:
        print(f"Resultado: {k} (impar y divisible por 7)")
        break       # salir al encontrar el primero
    print(f"  Probando {k}...")

print()

# --- FOR...ELSE ---
print("=== FOR...ELSE ===")
print("El bloque 'else' se ejecuta si el for termina sin break")

val_primo = input("Ingresa un número para ver si es primo: ")
num_primo = int(val_primo) if val_primo.isdigit() else 0

if num_primo < 2:
    print(f"{num_primo} no es primo")
else:
    es_primo_flag = True
    for d in range(2, num_primo):
        if num_primo % d == 0:
            print(f"{num_primo} NO es primo (divisible por {d})")
            es_primo_flag = False
            break
    
    if es_primo_flag:
        print(f"{num_primo} SI es primo")

print()

# --- Ejemplo práctico: procesar notas ---
print("=== PROCESAR NOTAS ===")
print("Ingresa 5 notas (1.0 a 7.0). Las inválidas se ignorarán.")

n_validas = 0
suma_total = 0.0

for i_nota in range(5):
    txt_nota = input(f"  Nota {i_nota + 1}: ")

    try:
        val_nota = float(txt_nota)
        
        if 1.0 <= val_nota <= 7.0:
            suma_total = suma_total + val_nota
            n_validas = n_validas + 1
        else:
            print("    Fuera de rango (1.0 - 7.0), se ignora")
            continue
            
    except ValueError:
        print("    No es un número, se ignora")
        continue

if n_validas > 0:
    print(f"\nNotas válidas: {n_validas}")
    prom = suma_total / n_validas
    print(f"Promedio: {prom:.2f}")
else:
    print("\nNo se ingresaron notas válidas")

