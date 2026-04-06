usuario_n = 0
usuario_e = 0
dinero_total = 0

while True:
    tipo_pasajero = input("¿Que tipo de pasajero es? N=Normal o E=Estudiante. Para finalizar, use CORTE\n")
    if tipo_pasajero == 'N':
        usuario_n = usuario_n + 1
        dinero_total = dinero_total + 800
    elif tipo_pasajero == 'E':
        usuario_e = usuario_e + 1
        dinero_total = dinero_total + 250
    elif tipo_pasajero == 'CORTE':
        break
print(f"Pasajeros normales: {usuario_n} \nEstudiantes: {usuario_e} \nTotal dinero caja: {dinero_total}")