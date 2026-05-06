# Datos Iniciales del Cliente
ingresos = 800000
antiguedad = 6
deudas = 0

# Evaluación de Reglas de Negocio
if ingresos > 1000000 or (antiguedad >= 5 and deudas == 0):
    print('Cliente VIP')
else:
    print('Cliente Normal')
