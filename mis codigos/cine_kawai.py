# REVISA Y ESTUDIA PARA ENTENDER


print("====== Taquilla Cine Kawai =====")

# 1. Preguntamos la cantidad total de entradas
cantidad_entradas = int(input("¿Cuántas entradas desea comprar?: "))

# Inicializamos el acumulador en 0
total_recaudado = 0
# Usamos un contador para controlar el ciclo while
entradas_procesadas = 0

# 2. Usamos el ciclo para procesar CADA entrada
while entradas_procesadas < cantidad_entradas:
    # Mostramos qué número de entrada estamos registrando
    print(f"\nProcesando entrada #{entradas_procesadas + 1}")
    
    # 3. Preguntamos la edad
    edad = int(input("¿Cuál es la edad del espectador?: "))
    
    precio_actual = 0
    
    if edad < 12:
        precio_actual = 3000
    elif 12 <= edad < 65:
        precio_actual = 6000
    else: # 65 o más
        precio_actual = 4000
        
    print(f"Entrada registrada correctamente. Precio: ${precio_actual}")
    
    # 4. Usamos el acumulador para sumar el precio
    total_recaudado += precio_actual
    
    # Incrementamos el contador para que el ciclo avance
    entradas_procesadas += 1

# 5. Imprimimos el gran total al final
print("-" * 30)
print(f"Gran total recaudado: ${total_recaudado}")
print("=================================")









