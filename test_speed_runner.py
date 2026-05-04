"""
Test script that simulates the speed-runner evaluation engine.
Tests multiple student code variants per exercise.
"""
import re

def preprocess(code, setup_vars):
    if not setup_vars:
        return code
    lines = code.split('\n')
    processed = []
    for line in lines:
        trimmed = line.strip()
        remove = False
        for var in setup_vars:
            patterns = [
                rf'^{var}\s*=\s*input\s*\(',
                rf'^{var}\s*=\s*int\s*\(\s*input\s*\(',
                rf'^{var}\s*=\s*float\s*\(\s*input\s*\(',
                rf'^{var}\s*=\s*str\s*\(\s*input\s*\(',
                rf'^{var}\s*=\s*[0-9"\'\[\{{]',
            ]
            if any(re.match(p, trimmed) for p in patterns):
                remove = True
                break
        if not remove:
            processed.append(line)
    return '\n'.join(processed)

def run_test(setup_code, init_code, user_code, assert_code):
    """Mirrors the Pyodide exec() namespace isolation exactly."""
    _ns = {}
    # Step 1: setup injects test variables
    if setup_code.strip():
        exec(setup_code, _ns)
    _ns['_ns'] = _ns  # Self-reference so assert code can access _ns
    # Step 2: initialCode resets accumulators (filter out prompt lines)
    init_lines = []
    for il in init_code.split('\n'):
        s = il.strip()
        if s == '' or s.startswith('#'):
            continue
        if s.endswith('= ') or s.endswith('='):
            continue
        init_lines.append(il)
    clean_init = '\n'.join(init_lines)
    if clean_init.strip():
        exec(clean_init, _ns)
    # Step 3: user code runs in same namespace
    exec(user_code, _ns)
    # Step 4: asserts run in same namespace (can access _ns via self-reference)
    exec(assert_code, _ns)

exercises = [
    {
        "id": 1, "title": "Calentamiento", "initialCode": "saludo = \n", "setupVars": [],
        "tests": [{"setup": "", "assert": "assert 'saludo' in _ns\nassert _ns['saludo'] == 'Hola Mundo'"}],
        "variants": [
            ("directa", "saludo = 'Hola Mundo'"),
            ("comillas dobles", 'saludo = "Hola Mundo"'),
        ]
    },
    {
        "id": 2, "title": "Matemáticas Rápidas", "initialCode": "total = \n", "setupVars": [],
        "tests": [{"setup": "", "assert": "assert _ns['total'] == 80"}],
        "variants": [
            ("con paréntesis", "total = (15 + 25) * 2"),
            ("sin paréntesis directo", "total = 80"),
            ("paso a paso", "total = 15 + 25\ntotal = total * 2"),
        ]
    },
    {
        "id": 3, "title": "El Guardián (If/Else)", "initialCode": "# Escribe tu condicional aquí:\n", "setupVars": ["nota"],
        "tests": [
            {"setup": "nota = 5.5", "assert": "assert 'estado' in _ns\nassert _ns['estado'] == 'Aprobado'"},
            {"setup": "nota = 3.9", "assert": "assert 'estado' in _ns\nassert _ns['estado'] == 'Reprobado'"},
        ],
        "variants": [
            ("simple", "if nota >= 4.0:\n    estado = 'Aprobado'\nelse:\n    estado = 'Reprobado'"),
            ("con input", "nota = float(input('Ingrese nota: '))\nif nota >= 4.0:\n    estado = 'Aprobado'\nelse:\n    estado = 'Reprobado'"),
            ("con hardcode", "nota = 5.5\nif nota >= 4.0:\n    estado = 'Aprobado'\nelse:\n    estado = 'Reprobado'"),
            ("comillas dobles", 'if nota >= 4.0:\n    estado = "Aprobado"\nelse:\n    estado = "Reprobado"'),
            ("con elif", "if nota >= 4.0:\n    estado = 'Aprobado'\nelif nota < 4.0:\n    estado = 'Reprobado'"),
        ]
    },
    {
        "id": 4, "title": "Ciclo While", "initialCode": "suma = 0\ncontador = 1\n", "setupVars": [],
        "tests": [{"setup": "", "assert": "assert _ns['suma'] == 15"}],
        "variants": [
            ("while <=5", "suma = 0\ncontador = 1\nwhile contador <= 5:\n    suma += contador\n    contador += 1"),
            ("while <6", "suma = 0\ncontador = 1\nwhile contador < 6:\n    suma = suma + contador\n    contador = contador + 1"),
        ]
    },
    {
        "id": 5, "title": "Ciclo For y Rango", "initialCode": "resultado = 0\n", "setupVars": [],
        "tests": [{"setup": "", "assert": "assert _ns['resultado'] == 55"}],
        "variants": [
            ("range(11)", "resultado = 0\nfor i in range(11):\n    resultado += i"),
            ("range(0,11)", "resultado = 0\nfor i in range(0, 11):\n    resultado = resultado + i"),
        ]
    },
    {
        "id": 6, "title": "Extracción de Vocales", "initialCode": "contador_a = 0\n", "setupVars": ["palabra"],
        "tests": [
            {"setup": "palabra = 'manzana'", "assert": "assert _ns['contador_a'] == 3"},
            {"setup": "palabra = 'elefante'", "assert": "assert _ns['contador_a'] == 1"},
        ],
        "variants": [
            ("for letra", "contador_a = 0\nfor letra in palabra:\n    if letra == 'a':\n        contador_a += 1"),
            ("for c", "contador_a = 0\nfor c in palabra:\n    if c == 'a':\n        contador_a = contador_a + 1"),
        ]
    },
    {
        "id": 7, "title": "Mi Primera Lista", "initialCode": "inventario = \n", "setupVars": [],
        "tests": [{"setup": "", "assert": "assert _ns['inventario'] == ['Espada', 'Escudo', 'Poción']"}],
        "variants": [("directa", "inventario = ['Espada', 'Escudo', 'Poción']")]
    },
    {
        "id": 8, "title": "Agregando Elementos", "initialCode": "", "setupVars": ["mochila"],
        "tests": [
            {"setup": "mochila = ['Brújula']", "assert": "assert len(_ns['mochila']) == 2\nassert _ns['mochila'][-1] == 'Mapa'"},
            {"setup": "mochila = []", "assert": "assert _ns['mochila'] == ['Mapa']"},
        ],
        "variants": [
            ("append", "mochila.append('Mapa')"),
            ("append doble comilla", 'mochila.append("Mapa")'),
        ]
    },
    {
        "id": 9, "title": "Sumando una Lista", "initialCode": "total_pagar = 0\n", "setupVars": ["precios"],
        "tests": [
            {"setup": "precios = [1000, 2500, 500]", "assert": "assert _ns['total_pagar'] == 4000"},
            {"setup": "precios = [10, 20]", "assert": "assert _ns['total_pagar'] == 30"},
        ],
        "variants": [
            ("for p", "total_pagar = 0\nfor p in precios:\n    total_pagar += p"),
            ("for precio", "total_pagar = 0\nfor precio in precios:\n    total_pagar = total_pagar + precio"),
        ]
    },
    {
        "id": 10, "title": "Creando un Diccionario", "initialCode": "perfil = \n", "setupVars": [],
        "tests": [{"setup": "", "assert": "assert _ns['perfil'].get('nombre') == 'Ash'\nassert _ns['perfil'].get('edad') == 10"}],
        "variants": [
            ("directa", "perfil = {'nombre': 'Ash', 'edad': 10}"),
            ("comillas dobles", 'perfil = {"nombre": "Ash", "edad": 10}'),
        ]
    },
    {
        "id": 11, "title": "Acceso a Diccionarios", "initialCode": "salud_actual = \n", "setupVars": ["enemigo"],
        "tests": [
            {"setup": "enemigo = {'nombre': 'Slime', 'hp': 45, 'ataque': 5}", "assert": "assert _ns['salud_actual'] == 45"},
            {"setup": "enemigo = {'hp': 100}", "assert": "assert _ns['salud_actual'] == 100"},
        ],
        "variants": [
            ("corchetes", "salud_actual = enemigo['hp']"),
            ("get", "salud_actual = enemigo.get('hp')"),
        ]
    },
    {
        "id": 12, "title": "Recorriendo un Diccionario", "initialCode": "total_ventas = 0\n", "setupVars": ["ventas"],
        "tests": [
            {"setup": "ventas = {'pan': 1000, 'leche': 800, 'huevos': 1500}", "assert": "assert _ns['total_ventas'] == 3300"},
            {"setup": "ventas = {'agua': 500}", "assert": "assert _ns['total_ventas'] == 500"},
        ],
        "variants": [
            ("values", "total_ventas = 0\nfor v in ventas.values():\n    total_ventas += v"),
            ("items", "total_ventas = 0\nfor k, v in ventas.items():\n    total_ventas += v"),
        ]
    },
    {
        "id": 13, "title": "La Búsqueda", "initialCode": "mayores_edad = 0\n", "setupVars": ["edades"],
        "tests": [
            {"setup": "edades = [15, 18, 22, 12, 40]", "assert": "assert _ns['mayores_edad'] == 3"},
            {"setup": "edades = [10, 11, 12]", "assert": "assert _ns['mayores_edad'] == 0"},
        ],
        "variants": [
            ("for edad", "mayores_edad = 0\nfor edad in edades:\n    if edad >= 18:\n        mayores_edad += 1"),
        ]
    },
    {
        "id": 14, "title": "Lista de Diccionarios", "initialCode": "aprobados = 0\n", "setupVars": ["alumnos"],
        "tests": [
            {"setup": "alumnos = [{'nombre': 'Ana', 'nota': 5.5}, {'nombre': 'Luis', 'nota': 3.5}, {'nombre': 'Marta', 'nota': 6.0}]", "assert": "assert _ns['aprobados'] == 2"},
            {"setup": "alumnos = [{'nombre': 'Pedro', 'nota': 1.0}]", "assert": "assert _ns['aprobados'] == 0"},
        ],
        "variants": [
            ("for alumno", "aprobados = 0\nfor alumno in alumnos:\n    if alumno['nota'] >= 4.0:\n        aprobados += 1"),
        ]
    },
    {
        "id": 15, "title": "Boss Final", "initialCode": "capital_total = 0\n", "setupVars": ["tienda"],
        "tests": [
            {"setup": "tienda = {'pocion': {'precio': 50, 'stock': 3}, 'espada': {'precio': 200, 'stock': 1}}", "assert": "assert _ns['capital_total'] == 350"},
            {"setup": "tienda = {'escudo': {'precio': 100, 'stock': 0}, 'manzana': {'precio': 10, 'stock': 5}}", "assert": "assert _ns['capital_total'] == 50"},
        ],
        "variants": [
            ("values", "capital_total = 0\nfor item in tienda.values():\n    capital_total += item['precio'] * item['stock']"),
        ]
    },
    {
        "id": 16, "title": "Frecuencias", "initialCode": "resultados = {}\n", "setupVars": ["votos"],
        "tests": [
            {"setup": "votos = ['A', 'B', 'A', 'C', 'A', 'B']", "assert": "assert _ns['resultados'] == {'A': 3, 'B': 2, 'C': 1}"},
            {"setup": "votos = ['X', 'X']", "assert": "assert _ns['resultados'] == {'X': 2}"},
        ],
        "variants": [
            ("if/else", "resultados = {}\nfor v in votos:\n    if v in resultados:\n        resultados[v] += 1\n    else:\n        resultados[v] = 1"),
            ("get", "resultados = {}\nfor v in votos:\n    resultados[v] = resultados.get(v, 0) + 1"),
        ]
    },
    {
        "id": 17, "title": "El Campeón", "initialCode": "mejor_jugador = ''\nmax_pts = -1\n", "setupVars": ["jugadores"],
        "tests": [
            {"setup": "jugadores = [{'nombre': 'Ash', 'pts': 150}, {'nombre': 'Gary', 'pts': 200}]", "assert": "assert _ns['mejor_jugador'] == 'Gary'"},
            {"setup": "jugadores = [{'nombre': 'Brock', 'pts': 500}, {'nombre': 'Misty', 'pts': 300}]", "assert": "assert _ns['mejor_jugador'] == 'Brock'"},
        ],
        "variants": [
            ("for j", "mejor_jugador = ''\nmax_pts = -1\nfor j in jugadores:\n    if j['pts'] > max_pts:\n        max_pts = j['pts']\n        mejor_jugador = j['nombre']"),
        ]
    },
    {
        "id": 18, "title": "Agrupación", "initialCode": "clasificacion = {'pares': [], 'impares': []}\n", "setupVars": ["numeros"],
        "tests": [
            {"setup": "numeros = [1, 2, 3, 4, 5]", "assert": "assert _ns['clasificacion']['pares'] == [2, 4] and _ns['clasificacion']['impares'] == [1, 3, 5]"},
            {"setup": "numeros = [10, 11]", "assert": "assert _ns['clasificacion']['pares'] == [10] and _ns['clasificacion']['impares'] == [11]"},
        ],
        "variants": [
            ("% 2", "clasificacion = {'pares': [], 'impares': []}\nfor n in numeros:\n    if n % 2 == 0:\n        clasificacion['pares'].append(n)\n    else:\n        clasificacion['impares'].append(n)"),
        ]
    },
    {
        "id": 19, "title": "Inventario Cruzado", "initialCode": "total_final = 0\n", "setupVars": ["compras", "precios"],
        "tests": [
            {"setup": "compras = ['espada', 'pocion', 'espada']\nprecios = {'espada': 100, 'pocion': 50}", "assert": "assert _ns['total_final'] == 225.0"},
            {"setup": "compras = ['pocion', 'pocion']\nprecios = {'espada': 100, 'pocion': 50}", "assert": "assert _ns['total_final'] == 100"},
        ],
        "variants": [
            ("con subtotal", "total_final = 0\nfor c in compras:\n    total_final += precios[c]\nif total_final > 200:\n    total_final = total_final * 0.9"),
            ("con var sub", "total_final = 0\nsubtotal = 0\nfor item in compras:\n    subtotal += precios[item]\nif subtotal > 200:\n    total_final = subtotal * 0.9\nelse:\n    total_final = subtotal"),
        ]
    },
    {
        "id": 20, "title": "Jefe Supremo", "initialCode": "todo_stock = []\n", "setupVars": ["catalogo"],
        "tests": [
            {"setup": "catalogo = {'armas': ['espada', 'arco', 'hacha'], 'pociones': ['luz', 'mana', 'vida']}", "assert": "assert sorted(_ns['todo_stock']) == sorted(['espada', 'hacha'])"},
            {"setup": "catalogo = {'comida': ['pan', 'manzana']}", "assert": "assert _ns['todo_stock'] == ['manzana']"},
        ],
        "variants": [
            ("values", "todo_stock = []\nfor lista in catalogo.values():\n    for producto in lista:\n        if len(producto) > 4:\n            todo_stock.append(producto)"),
            ("items", "todo_stock = []\nfor cat, prods in catalogo.items():\n    for p in prods:\n        if len(p) > 4:\n            todo_stock.append(p)"),
        ]
    },
]

# ─── Run ───
total_pass = 0
total_fail = 0
failures = []

for ex in exercises:
    for var_name, var_code in ex["variants"]:
        clean = preprocess(var_code, ex["setupVars"])
        for ti, test in enumerate(ex["tests"]):
            try:
                run_test(test["setup"], ex["initialCode"], clean, test["assert"])
                total_pass += 1
            except Exception as e:
                total_fail += 1
                failures.append(f"#{ex['id']} {ex['title']} | {var_name} | test {ti+1}: {e}")

print(f"\n{'='*60}")
print(f"  RESULTS: {total_pass} PASSED / {total_fail} FAILED")
print(f"{'='*60}")
if failures:
    for f in failures:
        print(f"  ❌ {f}")
else:
    print("\n  ✅ ALL TESTS PASSED!")
