**Resolver**

Desarrolla un programa en Python que implemente un sistema de registro de bichos para una aplicación de "Cazabichos", donde todo el comportamiento se organice mediante funciones bien definidas. El programa debe incluir un menú interactivo, validaciones de entrada, operaciones lógicas (decisiones y comparaciones) y uso de funciones separadas.

## 1. Datos que debe manejar el sistema

El sistema trabaja con una colección de bichos capturados. Esta colección debe existir desde que el programa inicia y estar disponible durante toda la ejecución. Cada vez que se registra un bicho, se incorpora a esa colección como un nuevo elemento.

Cada bicho se representa como un conjunto de campos asociados: especie, tamaño, nivel de peligrosidad y un indicador de si es peligroso o no. La siguiente tabla resume los campos de cada registro:

| Campo | Qué representa | Restricciones de validación |
|---|---|---|
| `"especie"` | Nombre de la especie del bicho | No vacío ni solo espacios en blanco |
| `"tamaño"` | Tamaño del bicho, en centímetros | Número entero mayor que cero |
| `"peligrosidad"` | Nivel de peligrosidad del bicho (1.0–10.0) | Número decimal entre 1.0 y 10.0 (incluidos) |
| `"peligroso"` | ¿Es considerado un bicho peligroso? | `False` al registrar. No se valida ni se solicita al usuario: el sistema lo asigna automáticamente. Su valor puede cambiar a `True` cuando se ejecute la opción 4 (Actualizar estados), según la peligrosidad del bicho. |

Cada diccionario se guarda dentro de una lista. La lista es la colección general; los diccionarios son los bichos individuales dentro de ella. El programa comienza con la lista vacía y la va llenando a medida que se registran nuevos bichos.

## 2. Lo que debe hacer el sistema

El sistema se controla desde un menú que aparece en pantalla cada vez que el usuario termina una acción. El usuario elige una opción numérica, el programa ejecuta la tarea correspondiente y vuelve a mostrar el menú. Esto se repite hasta que el usuario elige salir.

El menú tiene seis opciones:

```
========== MENÚ PRINCIPAL ==========
1. Agregar bicho
2. Buscar bicho
3. Eliminar bicho
4. Actualizar estados
5. Mostrar bichos
6. Salir
=====================================
```

Para implementar este comportamiento debes definir dos funciones separadas: una que muestre las opciones en pantalla (sin recibir nada ni retornar nada) y otra que lea y retorne la opción elegida por el usuario (sin recibir nada, retornando el número validado). Ambas funciones deben invocarse en cada vuelta del ciclo.

A continuación, se describe qué debe ocurrir al elegir cada opción:

### Opción 1 - Agregar bicho

El sistema solicita al usuario la especie, el tamaño y el nivel de peligrosidad del bicho. Antes de guardar el registro, verifica que cada dato cumpla su condición:

- La especie no puede estar vacía ni ser solo espacios en blanco.
- El tamaño debe ser un número entero mayor que cero.
- La peligrosidad debe ser un número decimal entre 1.0 y 10.0.

Si algún dato no cumple la condición, el sistema informa al usuario y no registra al bicho. Solo cuando todos los datos son válidos se crea el diccionario y se agrega a la lista.

Para implementar esta opción debes definir una función que reciba la lista como parámetro. Dentro de ella se solicitan los datos al usuario y se llama a una función de validación distinta para cada campo. Los mensajes de error se muestran en esta función, no dentro de las validaciones.

### Opción 2 - Buscar bicho

El sistema solicita una especie al usuario y recorre la lista buscando un registro cuyo campo especie coincida exactamente con el ingresado. Si lo encuentra, muestra la posición en la que está y sus datos. Si no existe ningún registro con esa especie, informa al usuario.

Para implementar esta opción debes definir una función que reciba la lista y la especie a buscar como parámetros. La función recorre la lista y retorna la posición del registro encontrado, o -1 si no existe. Es el programa principal quien recibe ese valor y decide qué hacer con él: si la posición es válida, muestra los datos del bicho en esa posición; si es -1, muestra el mensaje de no encontrado.

### Opción 3 - Eliminar bicho

El sistema solicita la especie del bicho que se desea eliminar. Para localizarlo, llama a la función de búsqueda definida en la opción anterior, pasándole la lista y la especie ingresada. Si la función retorna una posición válida, el sistema elimina el registro en esa posición. Si retorna -1, informa al usuario con el siguiente mensaje:

```
El bicho 'especie' no se encuentra registrado.
```

### Opción 4 - Actualizar estados

El sistema recorre la lista completa de bichos y actualiza el campo `"peligroso"` de cada registro según su peligrosidad: si la peligrosidad es mayor o igual a 7.0, el campo pasa a `True`; si es menor, queda en `False`. Esta operación afecta a todos los registros de la lista sin excepción.

Para implementar esta opción debes definir una función que reciba la lista como parámetro y aplique esa regla a cada elemento.

### Opción 5 - Mostrar bichos

El sistema primero actualiza los estados de todos los bichos haciendo el llamado a la función anterior, luego recorre la lista mostrando los datos de cada bicho. El formato de salida es el siguiente:

```
=== LISTA DE BICHOS ===

Especie: Escarabajo Rinoceronte
Tamaño: 15
Peligrosidad: 8.5
Estado: PELIGROSO
********************************************
Especie: Mariquita
Tamaño: 1
Peligrosidad: 2.0
Estado: NO PELIGROSO
*********************************************
```

### Opción 6 - Salir

El sistema termina la ejecución de forma limpia, sin errores. El ciclo del menú se detiene y el programa finaliza con un mensaje de despedida:

```
"Gracias por usar el Cazabichos. ¡Hasta la próxima expedición!"
```