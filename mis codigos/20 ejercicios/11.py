#ejercicio11
enemigo = {'nombre': 'slime', 'hp': 45}
salud_actual = enemigo['hp']
print(f"la salud actual del enemigo es: {salud_actual}")


#ejercicio12
total_ventas = 0
ventas = {"frutas": 2000, "verduras": 3000, "dulces": 2500}
for productos in ventas.values():
    total_ventas += productos
    
print(f"El total de ventas es de {total_ventas}")


#ejercicio13
mayores_edad = 0
edades = [12, 76, 34, 18, 15, 66]

for edad in edades:
    if edad > 18:
        mayores_edad += 1

print(f"En la lista hay {mayores_edad} personas mayores de edad")


#ejercicio14
aprobados = 0
alumnos = [{"nombre": "Isabella", "nota": 4.0}, {"nombre": "Emma", "nota": 5.5}, {"nombre": "Mateo", "nota": 3.4}, {"nombre": "Juan", "nota": 6.1}]

for estudiante in alumnos:
    if estudiante["nota"] >= 4.0:
        aprobados += 1

print(f"Hay {aprobados} estudiantes aprobados")

#ejercicio15 (examinar despues para entenderlo bien)
capital_total = 0
tienda = {
    "cuaderno": {"precio": 1800, "stock": 2}, 
    "lapices": {"precio": 500, "stock": 5}, 
    "cartulina": {"precio": 400, "stock": 3}
}

for producto in tienda:
    # 1. Obtenemos el diccionario interno del producto actual
    datos = tienda[producto]
    
    # 2. Multiplicamos su precio por su stock
    capital_producto = datos["precio"] * datos["stock"]
    
    # 3. Lo sumamos al total
    capital_total += capital_producto

print(f"La capital total es de ${capital_total}")


#ejercicio16
votos = ["A", "A", "B", "A", "B"]
resultados = {"A": 0, "B": 0}
for letra in votos:
    if letra == "A":
        resultados["A"] += 1
    else:
        resultados["B"] += 1

print(resultados)


#ejercicios17
max_puntos = -1
mejor_jugador = ""
jugadores = [{"nombre": "Ash", "pts": 150},
          {"nombre": "Gary", "pts": 200},
          {"nombre": "Neo", "pts": 180}]

for jugador in jugadores:
    if max_puntos  < jugador["pts"]:
        max_puntos = jugador["pts"]
        mejor_jugador = jugador["nombre"]
    else:
        continue

print(f"El ganador es {mejor_jugador}")


#ejercicio18
numero = [2, 3, 5, 6, 1, 8, 9]
clasificacion = {"pares": [] , "impares" : []}

for n in numero:
    if n % 2 == 0:
        clasificacion["pares"].append(n)
    else:
        clasificacion["impares"].append(n)
    
print(clasificacion)


#ejercicio19
total_final = 0
precio_actual = 0
compras = ["jabon", "suavizante", "detergente", "cloro"]
precios = {"jabon": 3000,
         "suavizante": 3000, 
         "detergente": 2500, 
         "cloro": 2800}

for producto in precios:
    precio_actual += precios[producto]

if precio_actual > 200:
    precio_actual * 0.9

precio_total = precio_actual
print(precio_total)



#ejercicio20
catalogo = {"armas": ["espada", "arco", "hacha"],
         "pociones": ["luz", "mana", "vida"]}

todo_stock = [""]

