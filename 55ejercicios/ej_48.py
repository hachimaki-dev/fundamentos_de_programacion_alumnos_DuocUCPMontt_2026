# Ejercicio 48: Merge de Perfiles de Usuario

print("=============================")
print("Sistema de mezcla de perfiles")
print("=============================")

perfil_local = {'id': 1}
datos_google = {'email': 'a@a.cl', 'foto': 'url'}

perfil_local.update(datos_google)

print(perfil_local)