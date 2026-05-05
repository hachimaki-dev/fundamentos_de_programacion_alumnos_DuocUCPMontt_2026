# Datos Iniciales: El cliente tiene un sueldo de 550000 y tiene 1 deuda activa.
# Reglas de Negocio: El banco exige DOS cosas a la vez: que el sueldo sea mayor a 500000 Y que la cantidad de deudas sea exactamente 0.
sueldo_minimo = 500000
deudas = 0

print(" hola bienvenido el banco para sacar un credito es necesario DOS cosas teenre un sueldo mayor de 500.000 y tener 0 deudas activas")
sueldo_usuario = int(input(" tu sueldo de cuanto es?: "))
deudas_usuario = int(input(" cuentas deudas tienes?: "))
if sueldo_usuario >= 500000 and deudas_usuario == 0:
    print("aprobado")
else:
    print("rechazado")
    




