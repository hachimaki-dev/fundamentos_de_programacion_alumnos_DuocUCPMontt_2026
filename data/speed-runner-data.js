const speedRunnerExercises = [
  {
    id: 1,
    title: "Nivel 1: Calentamiento",
    description: "Crea una variable llamada <code>saludo</code> que contenga el texto exacto <code>'Hola Mundo'</code>.",
    initialCode: "saludo = ",
    tests: [
      {
        setup: "",
        assert: "assert 'saludo' in globals(), 'No definiste la variable saludo'\nassert saludo == 'Hola Mundo', 'El valor debe ser exactamente Hola Mundo'"
      }
    ]
  },
  {
    id: 2,
    title: "Nivel 2: Matemáticas Rápidas",
    description: "Crea una variable <code>total</code> que sea el resultado de sumar 15 y 25, y luego multiplicar todo por 2.",
    initialCode: "total = ",
    tests: [
      {
        setup: "",
        assert: "assert 'total' in globals(), 'No definiste la variable total'\nassert total == 80, 'El cálculo no es correcto. (15 + 25) * 2 = 80'"
      }
    ]
  },
  {
    id: 3,
    title: "Nivel 3: El Guardián (If/Else)",
    description: "Completa el código para que la variable <code>estado</code> sea <code>'Aprobado'</code> si <code>nota</code> es mayor o igual a 4.0. De lo contrario, debe ser <code>'Reprobado'</code>.",
    initialCode: "# Escribe tu condicional aquí:\n",
    tests: [
      {
        setup: "nota = 5.5",
        assert: "assert 'estado' in globals(), 'Debes definir la variable estado'\nassert estado == 'Aprobado', 'Con nota 5.5 el estado debe ser Aprobado'"
      },
      {
        setup: "nota = 3.9",
        assert: "assert estado == 'Reprobado', 'Con nota 3.9 el estado debe ser Reprobado'"
      }
    ]
  },
  {
    id: 4,
    title: "Nivel 4: Ciclo While Básico",
    description: "Usa un ciclo <code>while</code> para sumar los números del 1 al 5. Guarda el resultado final en la variable <code>suma</code>.",
    initialCode: "suma = 0\ncontador = 1\n# Tu ciclo while aquí:\n",
    tests: [
      {
        setup: "",
        assert: "assert 'suma' in globals(), 'Debes definir suma'\nassert suma == 15, 'La suma de 1 al 5 debe ser 15 (1+2+3+4+5)'"
      }
    ]
  },
  {
    id: 5,
    title: "Nivel 5: Ciclo For y Rango",
    description: "Usa un ciclo <code>for</code> con <code>range()</code> para sumar todos los números del 0 al 10 (incluyendo el 10). Guarda el resultado en la variable <code>resultado</code>.",
    initialCode: "resultado = 0\n# Tu ciclo for aquí:\n",
    tests: [
      {
        setup: "",
        assert: "assert 'resultado' in globals(), 'Debes definir resultado'\nassert resultado == 55, 'La suma del 0 al 10 inclusive debe ser 55'"
      }
    ]
  },
  {
    id: 6,
    title: "Nivel 6: Extracción de Vocales",
    description: "Itera sobre la cadena <code>palabra</code> usando un ciclo <code>for</code>. Cada vez que encuentres la letra 'a' (minúscula), aumenta la variable <code>contador_a</code> en 1.",
    initialCode: "contador_a = 0\n# Tu ciclo for aquí:\n",
    tests: [
      {
        setup: "palabra = 'manzana'",
        assert: "assert contador_a == 3, 'manzana tiene 3 letras a'"
      },
      {
        setup: "palabra = 'elefante'",
        assert: "assert contador_a == 1, 'elefante tiene 1 letra a'"
      }
    ]
  },
  {
    id: 7,
    title: "Nivel 7: Mi Primera Lista",
    description: "Crea una lista llamada <code>inventario</code> que contenga tres strings: <code>'Espada'</code>, <code>'Escudo'</code> y <code>'Poción'</code> (en ese exacto orden).",
    initialCode: "inventario = ",
    tests: [
      {
        setup: "",
        assert: "assert 'inventario' in globals(), 'No definiste inventario'\nassert type(inventario) == list, 'inventario debe ser una lista'\nassert inventario == ['Espada', 'Escudo', 'Poción'], 'Los elementos o el orden no son los correctos'"
      }
    ]
  },
  {
    id: 8,
    title: "Nivel 8: Agregando Elementos",
    description: "Se te entrega una lista llamada <code>mochila</code>. Usa el método correcto para añadir el string <code>'Mapa'</code> al final de la lista.",
    initialCode: "# Agrega 'Mapa' a la mochila\n",
    tests: [
      {
        setup: "mochila = ['Brújula']",
        assert: "assert len(mochila) == 2, 'La mochila debe tener 2 elementos'\nassert mochila[-1] == 'Mapa', 'El último elemento debe ser Mapa'"
      },
      {
        setup: "mochila = []",
        assert: "assert mochila == ['Mapa'], 'El método append sirve incluso si la lista está vacía'"
      }
    ]
  },
  {
    id: 9,
    title: "Nivel 9: Sumando una Lista",
    description: "Dada la lista <code>precios</code>, usa un ciclo <code>for</code> para sumar todos sus valores y guarda el resultado en <code>total_pagar</code>.",
    initialCode: "total_pagar = 0\n# Tu ciclo for aquí:\n",
    tests: [
      {
        setup: "precios = [1000, 2500, 500]",
        assert: "assert 'total_pagar' in globals(), 'Debes definir total_pagar'\nassert total_pagar == 4000, 'La suma debe ser 4000'"
      },
      {
        setup: "precios = [10, 20]",
        assert: "assert total_pagar == 30, 'Para [10, 20] la suma debe ser 30'"
      }
    ]
  },
  {
    id: 10,
    title: "Nivel 10: Creando un Diccionario",
    description: "Crea un diccionario llamado <code>perfil</code> con las siguientes claves y valores: clave <code>'nombre'</code> con valor <code>'Ash'</code>, y clave <code>'edad'</code> con valor <code>10</code>.",
    initialCode: "perfil = ",
    tests: [
      {
        setup: "",
        assert: "assert 'perfil' in globals(), 'No definiste perfil'\nassert type(perfil) == dict, 'perfil debe ser un diccionario'\nassert perfil.get('nombre') == 'Ash', 'La clave nombre debe ser Ash'\nassert perfil.get('edad') == 10, 'La clave edad debe ser 10'"
      }
    ]
  },
  {
    id: 11,
    title: "Nivel 11: Acceso a Diccionarios",
    description: "Dado el diccionario <code>enemigo</code>, extrae el valor asociado a la clave <code>'hp'</code> y guárdalo en una variable llamada <code>salud_actual</code>.",
    initialCode: "salud_actual = ",
    tests: [
      {
        setup: "enemigo = {'nombre': 'Slime', 'hp': 45, 'ataque': 5}",
        assert: "assert 'salud_actual' in globals(), 'Debes definir salud_actual'\nassert salud_actual == 45, 'La salud_actual debe extraerse del diccionario'"
      },
      {
        setup: "enemigo = {'hp': 100}",
        assert: "assert salud_actual == 100, 'Debes extraer la clave hp dinámicamente, no hardcodear el número'"
      }
    ]
  },
  {
    id: 12,
    title: "Nivel 12: Recorriendo un Diccionario",
    description: "Se te da un diccionario <code>ventas</code> donde la clave es el producto y el valor el monto. Usa un ciclo <code>for</code> con <code>.values()</code> o <code>.items()</code> para calcular el monto total de ventas y guárdalo en <code>total_ventas</code>.",
    initialCode: "total_ventas = 0\n# Tu ciclo for aquí:\n",
    tests: [
      {
        setup: "ventas = {'pan': 1000, 'leche': 800, 'huevos': 1500}",
        assert: "assert 'total_ventas' in globals(), 'Falta definir total_ventas'\nassert total_ventas == 3300, 'La suma debe ser 3300'"
      },
      {
        setup: "ventas = {'agua': 500}",
        assert: "assert total_ventas == 500, 'La suma debe funcionar para cualquier diccionario'"
      }
    ]
  },
  {
    id: 13,
    title: "Nivel 13: La Búsqueda (Lista + Condicional)",
    description: "Dada la lista de números <code>edades</code>, usa un ciclo <code>for</code> para contar cuántas personas son mayores o iguales a 18. Guarda la cantidad en <code>mayores_edad</code>.",
    initialCode: "mayores_edad = 0\n# Tu código aquí:\n",
    tests: [
      {
        setup: "edades = [15, 18, 22, 12, 40]",
        assert: "assert 'mayores_edad' in globals(), 'Falta definir mayores_edad'\nassert mayores_edad == 3, 'Hay 3 personas >= 18 en la primera prueba'"
      },
      {
        setup: "edades = [10, 11, 12]",
        assert: "assert mayores_edad == 0, 'Hay 0 personas >= 18 en la segunda prueba'"
      }
    ]
  },
  {
    id: 14,
    title: "Nivel 14: Lista de Diccionarios",
    description: "Dada una lista llamada <code>alumnos</code> (donde cada elemento es un diccionario con claves 'nombre' y 'nota'), encuentra cuántos alumnos tienen una nota >= 4.0. Guarda el resultado en <code>aprobados</code>.",
    initialCode: "aprobados = 0\n# Tu código aquí:\n",
    tests: [
      {
        setup: "alumnos = [{'nombre': 'Ana', 'nota': 5.5}, {'nombre': 'Luis', 'nota': 3.5}, {'nombre': 'Marta', 'nota': 6.0}]",
        assert: "assert 'aprobados' in globals(), 'Falta definir aprobados'\nassert aprobados == 2, 'Deben haber 2 aprobados en este caso'"
      },
      {
        setup: "alumnos = [{'nombre': 'Pedro', 'nota': 1.0}]",
        assert: "assert aprobados == 0, 'Deben haber 0 aprobados en este caso'"
      }
    ]
  },
  {
    id: 15,
    title: "Nivel 15: Boss Final 🐉",
    description: "Se te entrega un inventario en forma de diccionario de diccionarios, ej: <code>tienda = {'pocion': {'precio': 50, 'stock': 3}, 'espada': {'precio': 200, 'stock': 1}}</code>. Calcula el <strong>valor total de todo el stock de la tienda</strong> (precio * stock para cada item) y guárdalo en <code>capital_total</code>.",
    initialCode: "capital_total = 0\n# Tu código aquí:\n",
    tests: [
      {
        setup: "tienda = {'pocion': {'precio': 50, 'stock': 3}, 'espada': {'precio': 200, 'stock': 1}}",
        assert: "assert 'capital_total' in globals(), 'Falta definir capital_total'\nassert capital_total == 350, 'El cálculo correcto es (50*3) + (200*1) = 350'"
      },
      {
        setup: "tienda = {'escudo': {'precio': 100, 'stock': 0}, 'manzana': {'precio': 10, 'stock': 5}}",
        assert: "assert capital_total == 50, 'El cálculo correcto es (100*0) + (10*5) = 50'"
      }
    ]
  },
  {
    id: 16,
    title: "Nivel 16: Frecuencias Clásicas",
    description: "Dada la lista <code>votos</code>, crea un diccionario llamado <code>resultados</code> que cuente cuántos votos tiene cada opción.<br>Ejemplo: si votos es ['A', 'A', 'B'], resultados debe ser <code>{'A': 2, 'B': 1}</code>.",
    initialCode: "resultados = {}\n# Tu código aquí:\n",
    tests: [
      {
        setup: "votos = ['A', 'B', 'A', 'C', 'A', 'B']",
        assert: "assert 'resultados' in globals(), 'Debes definir resultados'\nassert resultados == {'A': 3, 'B': 2, 'C': 1}, 'Las frecuencias de la prueba 1 no son correctas'"
      },
      {
        setup: "votos = ['X', 'X']",
        assert: "assert resultados == {'X': 2}, 'Las frecuencias de la prueba 2 oculta no son correctas'"
      }
    ]
  },
  {
    id: 17,
    title: "Nivel 17: El Campeón (Búsqueda de Máximo)",
    description: "Dada la lista de diccionarios <code>jugadores</code> (cada uno con 'nombre' y 'pts'), encuentra el nombre del jugador con más puntos y guárdalo en la variable <code>mejor_jugador</code>.",
    initialCode: "mejor_jugador = ''\nmax_pts = -1\n# Tu código aquí:\n",
    tests: [
      {
        setup: "jugadores = [{'nombre': 'Ash', 'pts': 150}, {'nombre': 'Gary', 'pts': 200}]",
        assert: "assert 'mejor_jugador' in globals(), 'Debes definir mejor_jugador'\nassert mejor_jugador == 'Gary', 'El jugador con más pts en la prueba 1 es Gary'"
      },
      {
        setup: "jugadores = [{'nombre': 'Brock', 'pts': 500}, {'nombre': 'Misty', 'pts': 300}]",
        assert: "assert mejor_jugador == 'Brock', 'Cuidado, tu código no funcionó para la prueba 2 oculta'"
      }
    ]
  },
  {
    id: 18,
    title: "Nivel 18: Agrupación Clasificatoria",
    description: "Dada una lista <code>numeros</code>, clasifícalos: guarda los números pares en la lista asociada a la clave <code>'pares'</code> y los impares en <code>'impares'</code> dentro del diccionario <code>clasificacion</code>.",
    initialCode: "clasificacion = {'pares': [], 'impares': []}\n# Tu código aquí:\n",
    tests: [
      {
        setup: "numeros = [1, 2, 3, 4, 5]",
        assert: "assert clasificacion['pares'] == [2, 4] and clasificacion['impares'] == [1, 3, 5], 'La clasificación de la prueba 1 falló'"
      },
      {
        setup: "numeros = [10, 11]",
        assert: "assert clasificacion['pares'] == [10] and clasificacion['impares'] == [11], 'Tu código hardcodeó valores, falló en la prueba oculta'"
      }
    ]
  },
  {
    id: 19,
    title: "Nivel 19: Inventario Cruzado",
    description: "Tienes una lista <code>compras</code> (nombres de items) y un diccionario <code>precios</code> (item: costo). Calcula el costo sumando los precios de cada compra. Si el subtotal supera los 200, aplica un 10% de descuento. Guarda el resultado final en <code>total_final</code>.",
    initialCode: "total_final = 0\n# Tu código aquí:\n",
    tests: [
      {
        setup: "compras = ['espada', 'pocion', 'espada']\nprecios = {'espada': 100, 'pocion': 50}",
        assert: "assert 'total_final' in globals(), 'Debes definir total_final'\nassert total_final == 225.0, 'El subtotal (250) supera 200, por lo que el descuento aplicado debe dar 225.0'"
      },
      {
        setup: "compras = ['pocion', 'pocion']\nprecios = {'espada': 100, 'pocion': 50}",
        assert: "assert total_final == 100, 'El subtotal es 100 (<= 200), no debe haber descuento'"
      }
    ]
  },
  {
    id: 20,
    title: "Nivel 20: Jefe Supremo ☠️",
    description: "Se te entrega un diccionario <code>catalogo</code> cuyas claves son categorías y sus valores son listas de productos. Debes recorrer todo y agregar a la lista <code>todo_stock</code> ÚNICAMENTE los nombres de productos que tengan estrictamente <strong>más de 4 letras</strong>.",
    initialCode: "todo_stock = []\n# Tu código aquí:\n",
    tests: [
      {
        setup: "catalogo = {'armas': ['espada', 'arco', 'hacha'], 'pociones': ['luz', 'mana', 'vida']}",
        assert: "assert sorted(todo_stock) == sorted(['espada', 'hacha']), 'De los 6 items, solo espada y hacha tienen > 4 letras'"
      },
      {
        setup: "catalogo = {'comida': ['pan', 'manzana']}",
        assert: "assert todo_stock == ['manzana'], 'La prueba oculta falló. Asegúrate de recorrer todas las listas'"
      }
    ]
  }
];
