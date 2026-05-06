sueldo = 800000
antiguedad_años = 6
deudas = 0

if sueldo > 1000000 or (antiguedad_años >= 5 and deudas == 0):
    print('Cliente VIP')
else:
    print('Cliente Normal')