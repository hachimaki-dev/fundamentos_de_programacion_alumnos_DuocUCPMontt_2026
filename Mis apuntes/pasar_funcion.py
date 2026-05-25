medicamento_mensual = 60000
despacho_domicilio = 8000

edad = int(input('Ingresa tu edad: '))
tramo = input('Ingresa el tramo (A, B, C, D): ').upper()

# Descuento medicamento
if edad <= 30:
    if tramo == 'A' or tramo == 'B':
        descuento_medicamento = 18
    elif tramo == 'C' or tramo == 'D':
        descuento_medicamento = 12
    else:
        descuento_medicamento = 0

elif 31 <= edad <= 60:
    if tramo == 'A' or tramo == 'B':
        descuento_medicamento = 12
    elif tramo == 'C' or tramo == 'D':
        descuento_medicamento = 8
    else:
        descuento_medicamento = 0

else:
    descuento_medicamento = 0

# Calcular valor final medicamento
monto_medicamento_mensual = medicamento_mensual * descuento_medicamento / 100
valor_final_medicamento_mensual = medicamento_mensual - monto_medicamento_mensual

# Calcular despacho
valor_final_despacho_domicilio = despacho_domicilio

if tramo == 'A' or tramo == 'B':
    valor_final_despacho_domicilio = despacho_domicilio * 0.90

if edad >= 55:
    valor_final_despacho_domicilio = valor_final_despacho_domicilio * 0.95

# Mostrar resultados
print('Valor del medicamento es: $', int(valor_final_medicamento_mensual))
print('El valor del despacho es: $', int(valor_final_despacho_domicilio))