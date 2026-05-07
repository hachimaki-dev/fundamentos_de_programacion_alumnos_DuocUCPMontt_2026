# Ejercicio 48: Merge de Perfiles de Usuario
# Junta los datos de tu aplicación con los datos que descargaste desde Google.

# Datos Iniciales: Tus datos locales: `{'id': 1}`. Los datos que mandó Google: `{'email': 'a@a.cl', 'foto': 'url'}`.

# Reglas de Negocio: El perfil del usuario necesita tener todo mezclado en un solo lugar para funcionar bien en la pantalla.

# Restricciones: Usa la herramienta `.update()` para inyectarle de un solo golpe todo el diccionario de Google a tu diccionario local. 
# Imprime cómo quedó el diccionario mezclado.

datos_locales = {'id': 1}
datos_google = {'email': 'a@a.cl', 'foto': 'url'}

datos_locales.update(datos_google)
print(datos_locales)