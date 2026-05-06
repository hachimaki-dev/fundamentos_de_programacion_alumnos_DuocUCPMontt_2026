print("Bienvenido a banco estado, vamos a comprobar si cumples los requisitos para solicitar un prestamo.")
print("Los requisitos son tener un sueldo sobre 500000 y ninguna deuda activa")
sueldo_cliente = 550000
deudas_cliente = 1

if sueldo_cliente > 500000 and deudas_cliente == 0:
    print("Eres apto para recibir el prestamo")
else:
    print("No cumples con las condiciones prestablecidas por el estado, tu petición será rechazada.")