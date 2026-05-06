#jercicio 11: Clave Única Básico
#imula el ingreso a tu cuenta con una clave secreta.

#atos Iniciales: Crea un contador `intentos_fallidos` en 0. 
# Asume que escribiste la clave 'Admin123'.

#eglas de Negocio: La clave correcta es 'secreto'. 
# Si la clave que escribiste es igual a la correcta, entraste. Si es diferente,
#  suma 1 a tus intentos fallidos.

#estricciones: Usa un bloque `if/else`. Como en este caso la clave está mal, 
# imprime exactamente: `'Intentos fallidos: '` seguido del número de intentos.

#esultado esperado en consola:
#ntentos fallidos: 1


clave_secreta = "secreto"
intentos_fallidos = 0

ingresa_tu_clave = input("ingrersa tu clave:")

if ingresa_tu_clave  == clave_secreta:
    print("entraste")

else:
    intentos_fallidos += 1
    print(f"intentos fallidos, numero de intentos{intentos_fallidos}")
  







