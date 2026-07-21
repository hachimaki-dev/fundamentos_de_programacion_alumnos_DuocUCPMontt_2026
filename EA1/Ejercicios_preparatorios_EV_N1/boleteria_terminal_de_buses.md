# 🚌 Ejercicio: Sistema de Ventas - Terminal de Buses

## 🎯 Objetivo
Desarrollar un programa en Python que gestione la venta de pasajes, aplicando lógica de control de flujo y cálculos matemáticos básicos.

### Conceptos a practicar:
* **Entrada/Salida:** `input()` y `print()`
* **Condicionales:** `if`, `elif`, `else`
* **Bucles:** `while` (para el flujo principal) y `for` (para la impresión de boletos)
* **Aritmética:** Acumuladores y cálculo de porcentajes.

---

## 📋 Instrucciones del Proyecto

### 1. Configuración Inicial
* Inicializar una variable `total_dia` en **0** fuera del bucle principal.
* Mostrar un mensaje de bienvenida: `--- Bienvenido a la Boletería ---`.

### 2. Estructura de Selección (Destinos)
El sistema debe permitir elegir entre los siguientes destinos:

| ID | Destino | Precio Unitario |
| :--- | :--- | :--- |
| **1** | Puerto Varas | $3.000 |
| **2** | Osorno | $7.000 |
| **3** | Frutillar | $5.000 |

> ⚠️ **Validación:** Si el usuario ingresa una opción distinta a 1, 2 o 3, debe mostrar `"Opción inválida"` y saltar al siguiente cliente.

### 3. Lógica de Pasaje y Cantidad
* **Tipo de Viaje:**
    1. **Solo ida:** Precio base.
    2. **Ida y vuelta:** Precio base multiplicado por 2.
* **Cantidad:** Solicitar cuántos pasajes desea comprar.
* **Cálculo Base:** `subtotal = precio_destino * tipo_viaje * cantidad`.

### 4. Aplicación de Descuentos
Si el subtotal de la compra es **superior a $10.000**, se debe aplicar un **10% de descuento** sobre ese valor.
* Si aplica: Mostrar `"Descuento del 10% aplicado"`.
* Si no: Mostrar `"Sin descuento aplicado"`.

### 5. Ciclo de Repetición (`while`)
Al finalizar cada venta, el programa debe preguntar:
`¿Desea atender a otro cliente? (si/no)`

* Si la respuesta es `"si"`, el ciclo se reinicia.
* Si la respuesta es `"no"`, el ciclo termina y se muestra el cierre de caja.

---

## 🔄 Extra: Simulación de Impresión
Para darle más realismo, utiliza un bucle `for` con `range()` para simular la impresión física de cada boleto vendido al cliente actual:

```python
# Ejemplo de lógica esperada
for i in range(cantidad):
    print(f"🎫 Imprimiendo boleto {i+1} de {cantidad}...")