# Ejercicio 44: Baja de Suscripción
# Borra la suscripción que el usuario acaba de cancelar para que no le cobren más.

# Datos Iniciales: Tus cobros mensuales son: `{'spotify': 4000, 'netflix': 7000}`.

# Reglas de Negocio: Ya no quieres pagar Spotify. Hay que borrarlo del registro.

# Restricciones: Usa la palabra reservada `del` seguida de la llave que quieres matar (ej. `del diccionario['llave']`), o usa la herramienta `.pop()`. Imprime cómo quedaron tus cuentas.

cobros_mensuales_son = {"spotify": 4000, "netflix": 7000}

cobros_mensuales_son.pop("spotify")

print(cobros_mensuales_son)