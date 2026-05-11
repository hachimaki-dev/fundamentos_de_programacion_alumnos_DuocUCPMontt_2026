# Programa para calcular:
# 1. Valor final de la mensualidad
# 2. Valor final del kit de materiales
# -----------------------------------
# VALORES BASE
# -----------------------------------
# Mensualidad = $85.000
# Kit de materiales = $18.000
# -----------------------------------
# DESCUENTOS PARA LA MENSUALIDAD
# ----------------------------------
# Si la edad es menor o igual a 18 meses:
#     - Nivel 1 o 2 -> 20% de descuento
#     - Nivel 3 o 4 -> 13% de descuento
# Si la edad está entre 19 y 36 meses:
#     - Nivel 1 o 2 -> 12% de descuento
#     - Nivel 3 o 4 -> 7% de descuento
# Si la edad es mayor a 36 meses:
#     - No hay descuento
# ----------------------------------
# DESCUENTOS PARA EL KIT
# -----------------------------------
# Si el nivel es 1 o 2:
#     - 10% de descuento
# Además, si la edad es menor o igual a 12 meses:
#     - 5% de descuento adicional
# -----------------------------------
# EL PROGRAMA DEBE MOSTRAR:
# ----------------------------------
# - Valor final de la mensualidad
# - Valor final del kit de materiales

mensualidad = 85000
kit_materiales = 18000

meses = int(input("¿cuantos edad tiene su hijo? :"))
nivel = int(input("¿En que nivel esta? :"))

if meses <= 18:
    if nivel in [1,2] :
        descuento_mensualidad = 0.20
    else:
        descuento_mensualidad = 0.13    
        
elif meses <= 36:
    if nivel in [1,2] :
        descuento_mensualidad = 0.12
    else:
        descuento_mensualidad = 0.07
        
else:
    descuento_mensualidad = 0   
    
mensualidad = mensualidad * (1 - descuento_mensualidad)


if nivel in [1,2] :
    descuento_kit = 0.10
    if meses <= 12 :
        descuento_kit = 0.15
        
else:
    descuento_kit = 0
    

kit_materiales = kit_materiales * (1 - descuento_kit)
print(mensualidad)
print(kit_materiales)
    
        
