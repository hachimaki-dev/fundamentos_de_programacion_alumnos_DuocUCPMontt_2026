# Calcular multa
# Crea calcular_multa(dias_atraso, valor_por_dia=100) que retorne el total de la multa. Pruébala con un solo argumento y luego con dos.

# 🤔 Pregúntate: ¿qué pasa si intentas def calcular_multa(valor_por_dia=100, dias_atraso)? ¿Por qué da error?

def calcularMulta(dias_atraso, valor_por_dia = 100):
    return dias_atraso * valor_por_dia

# def calcularMulta(valor_por_dia = 100, dias_atraso):
#     return valor_por_dia * dias_atraso

print(calcularMulta(20))

#No se puede poner una parametro con un default antes que un parametro sin default. 