# 1. DEFINICIÓN: La "máquina" que procesa los datos
def clasificar_estrella(temperatura):
    if temperatura >= 30000:
        return "O", "Azul"
    elif temperatura >= 10000:
        return "B", "Blanco azulado"
    elif temperatura >= 7500:
        return "A", "Blanco"
    elif temperatura >= 6000:
        return "F", "Blanco amarillento"
    elif temperatura >= 5200:
        return "G", "Amarillo"
    elif temperatura >= 3700:
        return "K", "Naranja"
    elif temperatura >= 2400:
        return "M", "Rojo"
    else:
        return "Desconocido", "Marrón/Infrarrojo"

# 2. PROCESAMIENTO: Aquí usamos la función en un flujo real
def ejecutar_programa():
    print("--- BIENVENIDO AL SISTEMA DE CLASIFICACIÓN DE HARVARD ---")
    
    # Lista de datos simulando una lectura de base de datos o archivo
    temperaturas_detectadas = [35000, 5800, 2500, 12000, 9500]
    
    print(f"\nProcesando {len(temperaturas_detectadas)} registros...\n")
    print(f"{'Temp (K)':<12} | {'Tipo':<6} | {'Color'}")
    print("-" * 35)

    for temp in temperaturas_detectadas:
        # Llamamos a la función y guardamos lo que el 'return' nos entrega
        tipo, color = clasificar_estrella(temp)
        print(f"{temp:<12} | {tipo:<6} | {color}")

# 3. EJECUCIÓN: El punto de entrada al programa
if __name__ == "__main__":
    ejecutar_programa()