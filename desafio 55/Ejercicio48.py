datos_locales = {'id': 1}
datos_gmail = {'email': 'a@a.cl', 'foto': 'url'}

print(datos_locales)
print(datos_gmail)

datos_locales.update(datos_gmail)

print(datos_locales)