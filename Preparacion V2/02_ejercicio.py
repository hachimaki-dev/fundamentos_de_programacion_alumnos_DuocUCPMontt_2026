# Ejercicio 2: Membresía de Gimnasio
# Desarrolle un programa que calcule el valor final de
#  una membresía mensual de gimnasio y el valor final del arriendo de casillero.

# valor base

menbresiea= 35000
casillero = 4500
meses = int(input('Ingrese la cantidad de meses: '))
plan = input('Ingrese le plan (1, 2, 3, 4): ')

# -------------------------
# DESCUENTO de menbresia 
# -------------------------

if meses >= 12:

    if plan == '1' or plan == '2':

        descuento_plan = 22

    elif plan == '3' or plan == '4':    

        descuento_plan = 15

elif 6 <= meses < 12:

    if plan == '1' or plan == '2':

        descuento_plan = 12

    elif plan == '3' or plan == '4':

        descuento_plan = 7

else:

    descuento_plan = 0

monto_descuento_menbresia = menbresiea * descuento_plan / 100
valor_final_menbresia = menbresiea - monto_descuento_menbresia

# calculadora el casillero    

valor_final_casillero = casillero

if plan == '1' or plan == '2':

    # Primer descuento 15%
    valor_final_casillero = valor_final_casillero * 0.85

    # Segundo descuento 5%
    if meses >= 9 :
        
        valor_final_casillero = valor_final_casillero * 0.95


print('valor final de la menbresia: $', int(valor_final_menbresia))
print('valor fianl del casillero: $', int(valor_final_casillero))