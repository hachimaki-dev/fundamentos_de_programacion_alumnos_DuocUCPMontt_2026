# Guía Progresiva de Ejercicios Python
### Del input básico al sistema completo con menú

---

> **Cómo usar esta guía:** Los ejercicios están ordenados por nivel. No saltes niveles. Cada uno construye sobre el anterior. El objetivo final es que puedas enfrentar cualquier ejercicio de evaluación con confianza porque ya dominas cada pieza por separado.

---

## NIVEL 1 — Validación de entrada numérica
**Habilidad que desarrollas:** Pedir un número al usuario y no seguir hasta que sea válido.

> **⚠️ Importante:** Antes de combinar `try/except` con validación de rango, practica capturar `ValueError` de forma aislada. El **Ejercicio 1A** (abajo) existe para eso. Una vez que entiendas el mecanismo de excepciones, el resto de ejercicios agrega condiciones adicionales.

---

### Ejercicio 1A — Solo capturar ValueError (calentamiento)

Escribe un programa que pida al usuario un número entero. Si el usuario ingresa algo que no sea un número (por ejemplo `"abc"` o `"3.7"`), el programa debe capturar la excepción `ValueError` y mostrar:

```
"Error: eso no es un número entero."
```

Repite la solicitud hasta que el usuario ingrese un entero válido (puede ser cualquier entero, positivo, negativo o cero). Cuando lo logre, muestra:
```
"Número recibido: {valor}"
```

**Objetivo:** Entender `try/except ValueError` de forma aislada, sin combinar aún con validaciones de rango.

**Casos de prueba:** `"abc"`, `"3.7"`, `""`, `0`, `-5`, `42`

---

### Ejercicio 1B — Registro de pasajeros en un vuelo

Una aerolínea necesita saber cuántos pasajeros abordaron un vuelo. El número debe ser mayor que cero (no puede haber un vuelo con cero o menos pasajeros).

Escribe un programa que pida el número de pasajeros y que **no avance** hasta recibir un entero positivo. Si el dato es inválido, muestra:

```
"Error: ingresa un número entero positivo de pasajeros."
```

Cuando el dato sea válido, muestra el valor que el usuario ingresó:
```
"Vuelo registrado con {pasajeros} pasajeros."
```
*(Ejemplo: si el usuario ingresa `142`, se muestra `"Vuelo registrado con 142 pasajeros."`)*

**Casos de prueba que debes intentar:** `0`, `-5`, `"abc"`, `3.7`, `200`

---

### Ejercicio 2 — Stock de una farmacia

Una farmacia necesita ingresar la cantidad de unidades disponibles de un medicamento. No puede ser cero ni negativo (una farmacia con stock negativo no tiene sentido).

Escribe un programa que pida la cantidad de unidades. Si es inválida, muestra:
```
"Dato inválido. Ingresa un entero positivo para el stock."
```

Cuando sea válido, muestra el valor que el usuario ingresó:
```
"Stock registrado: {cantidad} unidades disponibles."
```
*(Ejemplo: si el usuario ingresa `350`, se muestra `"Stock registrado: 350 unidades disponibles."`)*

**Piensa:** ¿Qué diferencia hay entre capturar `ValueError` y validar con `> 0`? ¿Necesitas ambas cosas?

---

### Ejercicio 3 — Edad de un conductor para arriendo de autos

Una empresa de arriendo de vehículos solicita la edad del conductor. Debe ser un entero positivo (nadie tiene -3 años ni 0 años).

El programa debe pedir la edad repetidamente hasta recibir un valor válido. Luego muestra:
```
"Edad registrada: 29 años."
```

**Desafío extra:** ¿Qué pasa si el usuario ingresa `"veintinueve"`? ¿Tu código lo maneja?

---

## NIVEL 2 — Validación de texto (strings)
**Habilidad que desarrollas:** Validar que un string cumpla reglas de formato antes de aceptarlo.

---

### Ejercicio 4 — Nombre de usuario para una app bancaria

Un banco digital pide al usuario crear un nombre de usuario. Las reglas son:
- Mínimo 6 caracteres
- Sin espacios

Si no cumple, muestra:
```
"Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios."
```

Ejemplos válidos: `juanp23`, `mariatorres`, `cliente99`
Ejemplos inválidos: `juan`, `maria torres`, `ok`

Cuando sea válido:
```
"Usuario creado: juanp23"
```

---

### Ejercicio 5 — Código de producto en una bodega

Una bodega industrial registra productos por código. El código debe:
- Tener al menos 6 caracteres
- No tener espacios

Pide el código hasta que sea válido. Luego muestra:
```
"Producto registrado con código: PROD7X"
```

**Ejercicio de análisis:** ¿Qué función de Python usarías para detectar si hay espacios? Hay al menos dos formas distintas. Encuentra ambas.

---

### Ejercicio 6 — Patente de vehículo en un estacionamiento

Un sistema de estacionamiento pide la patente del auto. Debe:
- Tener exactamente 6 caracteres
- No contener espacios

> **Dato cultural:** En Chile existen dos formatos de patente, ambos de 6 caracteres:
> - **Formato antiguo** (hasta 2007): 4 letras + 2 números (ej: `BBCR45`)
> - **Formato nuevo** (desde 2007): 2 letras + 4 números (ej: `AB1234`)
>
> Para este ejercicio solo validaremos largo y ausencia de espacios, no el patrón exacto de letras/números.

Si no es válida:
```
"Patente inválida. Ingresa exactamente 6 caracteres sin espacios."
```

Válidas: `BBCR45`, `AB1234`
Inválidas: `BB CR45`, `AB12`, `ABCDEFG`

---

## NIVEL 3 — Clasificación y contadores
**Habilidad que desarrollas:** Tomar un valor y clasificarlo en una categoría, llevando conteo de cada categoría.

---

### Ejercicio 7 — Clasificación de temperaturas en una planta industrial

Una planta industrial mide la temperatura de 5 sensores. Cada temperatura es un número decimal (usa `float()` para leerlo, **no** `int()`). El operador las ingresa una a una.

> **Nota sobre el Patrón 1 de referencia:** El patrón usa `int()` como ejemplo genérico. En este ejercicio reemplázalo por `float()` porque las temperaturas pueden tener decimales (ej: `75.5`).

Clasifica cada temperatura con estos rangos exactos:
- **Mayor a 80°C** (> 80, no incluye 80) → `"ALERTA: temperatura crítica"`
- **De 50°C a 80°C** (>= 50 y <= 80) → `"Normal operativo"`
- **Menor a 50°C** (< 50) → `"Temperatura baja"`

> **Condiciones de borde:** Una temperatura de exactamente 80°C es "Normal operativo". Una de exactamente 50°C también es "Normal operativo".

Al final, muestra cuántas lecturas cayeron en cada categoría.

**Ejemplo de salida:**
```
Temperaturas críticas: 2
Temperaturas normales: 2
Temperaturas bajas: 1
```

---

### Ejercicio 8 — Clasificación de ventas de un local

Un local de ventas registra los montos de 6 ventas del día. Cada venta es un entero positivo (en pesos).

Clasifica cada venta con estos rangos exactos:
- **Mayor a $50.000** (> 50000) → Venta mayor
- **De $10.000 a $50.000** (>= 10000 y <= 50000) → Venta media
- **Menor a $10.000** (< 10000) → Venta menor

> **Condiciones de borde:** Una venta de exactamente $50.000 es "Venta media". Una de exactamente $10.000 también es "Venta media".

Al final, muestra el conteo de cada tipo y el total recaudado.

---

### Ejercicio 9 — Evaluación de solicitudes de crédito

Un banco recibe solicitudes de crédito. El analista ingresa el score crediticio de cada solicitante (entero de 0 a 1000).

Clasifica el score con estos rangos exactos:
- **Mayor a 750** (> 750) → `"Aprobado automáticamente"`
- **De 500 a 750** (>= 500 y <= 750) → `"Revisión manual"`
- **Menor a 500** (< 500) → `"Rechazado"`

> **Condiciones de borde:** Un score de exactamente 750 es "Revisión manual". Un score de exactamente 500 también es "Revisión manual".

Registra 8 solicitudes y muestra al final cuántas quedaron en cada categoría.

**Desafío:** valida que el score esté entre 0 y 1000. Si no, pide ingresar de nuevo.

---

## NIVEL 4 — Bucle for con N iteraciones (el corazón del Ejercicio 1 de evaluación)
**Habilidad que desarrollas:** Primero validar cuántas veces iterar, luego iterar exactamente esa cantidad de veces, validando cada dato dentro del loop.

---

### Ejercicio 10 — Registro de notas de un curso universitario

El docente ingresa cuántos estudiantes tiene en su curso (entero positivo). Luego, para cada estudiante, ingresa su nota (entero de 1 a 7, validado).

Al final muestra:
- Cuántos aprobaron (nota ≥ 4)
- Cuántos reprobaron (nota < 4)
- El promedio del curso

**Estructura que debes aplicar:**
```
1. Validar N (cantidad de estudiantes)
2. for i in range(N):
       validar nota
       clasificar y contar
3. Mostrar resumen
```

---

### Ejercicio 11 — Registro de despachos en una empresa de transporte

Un coordinador de despachos necesita registrar los pesos de los paquetes del día. Primero ingresa cuántos paquetes despacha (entero positivo). Luego, para cada paquete:
- Ingresa el peso en kg (entero positivo, validado)
- Ingresa el código del paquete (mínimo 6 caracteres, sin espacios, validado)

Clasifica cada paquete:
- Peso > 20 kg → Carga pesada
- Peso ≤ 20 kg → Carga normal

Al final muestra cuántos de cada tipo y el peso total despachado.

---

### Ejercicio 12 — Control de asistencia en una empresa

Un jefe de RRHH quiere registrar la asistencia de empleados. Ingresa cuántos empleados tiene (entero positivo). Para cada empleado:
- Ingresa su ID (mínimo 6 caracteres, sin espacios)
- Ingresa los días trabajados en el mes (entero de 0 a 23, validado)

> **¿Por qué 0 a 23?** Un empleado con licencia médica completa puede tener 0 días trabajados. Algunos meses tienen hasta 23 días hábiles. El rango 0–23 cubre todos los casos reales.

Clasifica:
- 20 o más días → Asistencia completa
- Menos de 20 días → Asistencia parcial

Muestra el resumen final.

---

### Ejercicio 13 — Inventario de computadores en una empresa TI

Un técnico registra computadores en el sistema de inventario. Ingresa cuántos equipos ingresarán. Para cada computador:
- Código de activo: mínimo 6 caracteres, sin espacios
- Año de fabricación: entero entre **1990 y 2026** (validado)

> **¿Por qué un rango?** Validar solo "entero positivo" aceptaría valores absurdos como `3` o `9999`. Un rango razonable (1990 a año actual) es más realista y te obliga a practicar **validación de rango**, una habilidad muy útil para la evaluación.

Clasifica:
- Fabricado antes del año 2018 → Equipo obsoleto
- Fabricado en 2018 o después → Equipo vigente

Muestra el resumen al finalizar.

---

## NIVEL 5 — Menú con while + operaciones sobre stock
**Habilidad que desarrollas:** Menú interactivo que no cierra hasta que el usuario decida salir, con operaciones que modifican variables de estado.**

---

### Ejercicio 14 — Sistema de caja de una cafetería

Una cafetería comienza con $0 en caja. El cajero trabaja con el siguiente menú:

```
=== SISTEMA DE CAJA CAFETERÍA CAMPUS ===
1. Ver saldo en caja
2. Registrar venta (ingresa monto)
3. Registrar gasto (ingresa monto)
4. Salir
```

Reglas:
- Las ventas suman al saldo
- Los gastos restan, pero no se puede gastar más de lo que hay en caja
- Monto siempre es entero positivo (validar)
- El menú se repite hasta que se elija salir

Al salir: `"Cierre de caja: $45.300 en caja. Hasta mañana."`

---

### Ejercicio 15 — Sistema de control de inventario de una tienda

Una tienda de electrónica comienza con 80 unidades de un producto en stock. Capacidad máxima de la bodega: 200 unidades. El encargado usa el siguiente menú:

```
=== INVENTARIO TIENDA DIGITAL ===
1. Ver stock actual
2. Registrar entrada de mercancía
3. Registrar venta
4. Salir
```

Validaciones:
- La entrada debe ser un entero positivo
- **El stock resultante no puede superar la capacidad máxima** (es decir: `stock + entrada <= 200`). No basta con validar que la entrada sea menor que 200.
- La venta no puede superar el stock actual
- Ambos valores deben ser enteros positivos

> **Ejemplo:** Si el stock actual es 180 y el usuario intenta ingresar 30 unidades, debe rechazarse porque `180 + 30 = 210 > 200`, aunque `30 < 200`.

Al salir: `"Stock final: {stock} unidades. Sesión cerrada."`

---

### Ejercicio 16 — Gestión de turnos en un servicio de urgencias

Un hospital gestiona los turnos de atención en urgencias. Comienza con 0 pacientes en sala. Capacidad máxima: 25 pacientes.

```
=== URGENCIAS HOSPITAL REGIONAL ===
1. Ver pacientes en sala
2. Registrar ingreso de paciente(s)
3. Registrar alta de paciente(s)
4. Total de ingresos del turno
5. Salir
```

Reglas:
- No puede haber más pacientes que la capacidad máxima
- No se puede dar de alta más pacientes de los que hay
- El historial de ingresos aumenta con cada ingreso y disminuye con cada alta (igual que en la evaluación)

---

### Ejercicio 17 — Control de aforo en un evento masivo

Un evento de música comienza con aforo de 500 cupos disponibles. El control de acceso usa:

```
=== CONTROL DE ACCESO - FESTIVAL AUSTRAL ===
1. Ver cupos disponibles
2. Registrar entrada de grupo
3. Registrar salida de grupo
4. Total de personas que han ingresado
5. Salir
```

Aplica todas las validaciones correspondientes. Esta estructura es **casi idéntica** a los ejercicios de evaluación. Si lo resuelves bien, estás listo.

---

## NIVEL 6 — Combinación completa (Ejercicio 1 de evaluación: registro + clasificación + resumen)
**Habilidad que desarrollas:** Integrar validación de N, bucle for, validación de cada campo, clasificación y resumen final.**

---

### Ejercicio 18 — Sistema de registro de técnicos en una empresa minera

Una empresa minera necesita registrar a sus técnicos de mantención. El sistema debe:

1. Preguntar cuántos técnicos se registrarán (entero positivo, validado con mensaje de error)
2. Para cada técnico pedir:
   - **Código de técnico:** mínimo 6 caracteres, sin espacios (validado)
   - **Años de experiencia:** entero positivo (validado con mensaje de error)
3. Clasificar según experiencia:
   - Más de 10 años → Técnico Maestro
   - 10 años o menos → Técnico Operario
4. Llevar conteo de cada categoría
5. Al finalizar mostrar:
   ```
   "La planta cuenta con 4 Técnicos Maestros y 6 Técnicos Operarios. Sistema listo."
   ```

---

### Ejercicio 19 — Registro de vehículos en una empresa de transporte de carga

Una empresa de transporte registra su flota. El sistema debe:

1. Preguntar cuántos vehículos se registrarán (entero positivo, validado)
2. Para cada vehículo:
   - **Patente:** exactamente 6 caracteres, sin espacios
   - **Capacidad de carga en toneladas:** entero positivo, validado
3. Clasificar:
   - Capacidad > 15 ton → Camión pesado
   - Capacidad ≤ 15 ton → Camión liviano
4. Al finalizar:
   ```
   "La flota cuenta con 3 camiones pesados y 5 camiones livianos. Registro completado."
   ```

---

## NIVEL 7 — Sistema completo con menú (Ejercicio 2 de evaluación)
**Habilidad que desarrollas:** Integrar menú, stock, historial y todas las validaciones en un solo programa cohesionado.**

---

### Ejercicio 20 — Sistema de préstamos de equipos en una universidad

La biblioteca de equipos tecnológicos de una universidad tiene 60 dispositivos disponibles (tablets, notebooks, etc.).

```
=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===
1. Ver equipos disponibles
2. Prestar equipo(s)
3. Recibir devolución
4. Ver historial de préstamos activos
5. Salir
```

Implementa:
- Stock inicial: 60 (equipos disponibles)
- Capacidad máxima: 60
- Préstamo reduce stock e incrementa historial (préstamos activos)
- Devolución aumenta stock y reduce historial
- Validar que préstamo no supere stock disponible
- **Validar que devolución no supere los préstamos activos** (es decir: `devolución <= historial`). No se puede devolver más equipos de los que están prestados.
- Todos los valores deben ser enteros positivos
- Menú se repite hasta seleccionar salir
- Al salir: `"Gracias por utilizar el sistema. Hasta pronto."`

> **Aclaración:** `historial` en este contexto representa la cantidad de equipos actualmente prestados (no un conteo de operaciones). Si se prestan 10 y luego se devuelven 3, `historial = 7`.

---

### Ejercicio 21 — Sistema de gestión de mesas en un restaurante

Un restaurante tiene 20 mesas disponibles.

```
=== SISTEMA DE MESAS - RESTAURANTE EL FARO ===
1. Ver mesas disponibles
2. Asignar mesa(s)
3. Liberar mesa(s)
4. Mesas ocupadas actualmente
5. Salir
```

Reglas:
- No puedes asignar más mesas de las disponibles
- No puedes liberar más mesas de las que están ocupadas (pista: `mesas_ocupadas = capacidad - disponibles`)
- Historial refleja ocupación actual (sube con asignación, baja con liberación)
- Al salir: `"Servicio finalizado. Buenas noches."`

**Este ejercicio es el más cercano a lo que verás en la evaluación. Resuélvelo sin mirar los anteriores.**

---

## NIVEL 8 — Ejercicio integrador final
**El desafío completo.**

---

### Ejercicio 22 — Sistema completo de gestión de una clínica veterinaria

**Parte A (similar al Ejercicio 1 de evaluación):**

Una clínica veterinaria registra a los animales que ingresan. El sistema debe:

1. Preguntar cuántos animales se registrarán (entero positivo, validado)
2. Para cada animal:
   - **ID del animal:** mínimo 6 caracteres, sin espacios (ej: `GATO01`, `PERR7X`, `CONEJO2`)
   - **Peso en kg:** entero positivo, validado
3. Clasificar:
   - Peso > 25 kg → Paciente Grande
   - Peso ≤ 25 kg → Paciente Pequeño
4. Al finalizar:
   ```
   "La clínica ha registrado 3 pacientes grandes y 8 pacientes pequeños. ¡Bienvenidos!"
   ```

**Parte B (similar al Ejercicio 2 de evaluación):**

La misma clínica gestiona sus horas de atención (stock inicial: 30 horas disponibles al día).

```
=== AGENDA CLÍNICA VETERINARIA PATITAS ===
1. Ver horas disponibles
2. Reservar hora(s)
3. Cancelar hora(s)
4. Ver historial de reservas
5. Salir
```

Implementa todas las reglas de validación correspondientes.

---

## Referencia Rápida de Patrones

### Patrón 1: Validar un entero positivo
```python
while True:
    try:
        valor = int(input("Ingresa un valor: "))
        if valor > 0:
            break
        else:
            print("Error: debe ser mayor que cero.")
    except ValueError:
        print("Error: debe ser un número entero.")
```

### Patrón 2: Validar un string (largo mínimo, sin espacios)
```python
while True:
    nombre = input("Ingresa el nombre: ")
    if len(nombre) >= 6 and " " not in nombre:
        break
    else:
        print("Inválido: mínimo 6 caracteres, sin espacios.")
```

### Patrón 3: Bucle for con N validado
```python
# Primero validar N
while True:
    try:
        n = int(input("¿Cuántos registros? "))
        if n > 0:
            break
        print("Debe ser mayor que cero.")
    except ValueError:
        print("Solo enteros positivos.")

# Luego iterar
for i in range(n):
    # validar cada campo adentro del for
    pass
```

### Patrón 4: Menú con while
```python
while True:
    print("1. Opción A")
    print("2. Opción B")
    print("3. Salir")
    opcion = input("Elige: ")
    
    if opcion == "1":
        pass  # lógica opción 1
    elif opcion == "2":
        pass  # lógica opción 2
    elif opcion == "3":
        print("Hasta pronto.")
        break
    else:
        print("Opción inválida.")
```

### Patrón 5: Gestión de stock con historial
```python
stock = 100        # unidades disponibles
capacidad = 100    # máximo posible
historial = 0      # unidades actualmente en uso/prestadas (NO es conteo de operaciones)

# ¿Qué significa historial?
# historial acumula UNIDADES, no operaciones.
# Ejemplo: si se prestan 10 y luego 5, historial = 15 (no 2).
# Si luego se devuelven 3, historial = 12.

# Operación de "entrada/reserva" (disminuye stock):
# - validar que cantidad > 0
# - validar que cantidad <= stock
# stock -= cantidad
# historial += cantidad

# Operación de "salida/devolución" (aumenta stock):
# - validar que cantidad > 0
# - validar que cantidad <= historial  ← no puedes devolver más de lo prestado
# stock += cantidad
# historial -= cantidad
```
