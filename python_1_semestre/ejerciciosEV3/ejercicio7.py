""" Ejercicio 7 — Clasificación de temperaturas en una planta industrial
Una planta industrial mide la temperatura de 5 sensores. Cada temperatura es un número decimal (usa float() para leerlo, no int()). El operador las ingresa una a una.

Nota sobre el Patrón 1 de referencia: El patrón usa int() como ejemplo genérico. En este ejercicio reemplázalo por float() porque las temperaturas pueden tener decimales 
(ej: 75.5).

Clasifica cada temperatura con estos rangos exactos:

Mayor a 80°C (> 80, no incluye 80) → "ALERTA: temperatura crítica"
De 50°C a 80°C (>= 50 y <= 80) → "Normal operativo"
Menor a 50°C (< 50) → "Temperatura baja"
Condiciones de borde: Una temperatura de exactamente 80°C es "Normal operativo". Una de exactamente 50°C también es "Normal operativo".

Al final, muestra cuántas lecturas cayeron en cada categoría.

Ejemplo de salida:

Temperaturas críticas: 2
Temperaturas normales: 2
Temperaturas bajas: 1 """

sensores = 1
contador = 0
Temperaturas_críticas = 0
Temperaturas_normales = 0
Temperaturas_bajas = 0

while sensores < 6:
    temperatura_sensores = float(input(f"ingresa la temperatura del sensor {sensores} : "))
    
    if temperatura_sensores > 80 :
        Temperaturas_críticas +=1
        sensores +=1

    elif temperatura_sensores >= 50 and temperatura_sensores <= 80:
        Temperaturas_normales +=1
        sensores +=1
    
    elif temperatura_sensores < 50:
        Temperaturas_bajas +=1
        sensores +=1

print(f" temperaturas criticas: {Temperaturas_críticas}\n temperaturas normales: {Temperaturas_normales}\n temperatuas bajas : {Temperaturas_bajas}")
