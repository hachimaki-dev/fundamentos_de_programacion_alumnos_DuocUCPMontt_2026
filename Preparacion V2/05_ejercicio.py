# Ejercicio 5: Seguro de Mascota
# Desarrolle un programa que calcule el valor final de la prima mensual de un seguro de mascota y
#  el valor final del chip de identificación.

# valor base

prima_mensual = 22000
chip = 9000
peso = int(input('Ingresa el peso: ')) 
cobertura = input('Ingresa la cobertura (A, B,C ,D): ').upper()

# Reglas de descuento de la prima:

if peso >= 20:

    if cobertura == 'A' or cobertura == 'B':

        descuento_prima = 16

    elif cobertura == 'C' or cobertura == 'D':

        descuento_prima = 10

elif peso >= 8 and peso <= 20:

    if cobertura == 'A' or cobertura == 'B':

        descuento_prima = 10

    elif cobertura == 'C' or cobertura == 'D':

        descuento_prima = 6

else:
    descuento_prima = 0

monto_prima_mensual = prima_mensual * descuento_prima / 100
valor_final_prima_mensual = prima_mensual - monto_prima_mensual

# calculadora de chip 

valor_fianl_chip = chip

if cobertura == 'A' or cobertura == 'B':
     
     # Primer descuento 12%
     valor_fianl_chip = valor_fianl_chip * 0.88

     if peso >= 15:
         
         # segundo descuento 6% 
         valor_fianl_chip = valor_fianl_chip * 0.94

print('valor final de prima mensual: $', int(valor_final_prima_mensual))   
print('valor final de chip: $', int(valor_fianl_chip))      