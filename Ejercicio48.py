'''Ejercicio 48: Merge de Perfiles de Usuario
Junta los datos de tu aplicación con los datos que descargaste desde Google.

Datos Iniciales: Tus datos locales: `{'id': 1}`. Los datos que mandó Google: `{'email': 'a@a.cl', 'foto': 'url'}`.

Reglas de Negocio: El perfil del usuario necesita tener todo mezclado en un solo lugar para funcionar bien en la pantalla.

Restricciones: Usa la herramienta `.update()` para inyectarle de un solo golpe todo el diccionario de Google a tu diccionario local. 

Imprime cómo quedó el diccionario mezclado.'''

Datos_Locales = {'ID': 1}

Datos_GOOGLE = {'Email': 'a@a.cl', 'Foto': 'Url'}

Datos_Locales.update(Datos_GOOGLE)

print(Datos_Locales)