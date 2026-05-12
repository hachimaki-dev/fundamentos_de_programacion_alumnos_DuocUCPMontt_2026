plan_mensual = 28000
instalacion = 15000
velocidad = int(input(" de cuanto es tu velocidad: "))

# 1. CORRECCIÓN: Pedir la categoría UNA SOLA VEZ aquí arriba
categoria = int(input(" que categoria eres (1 a 4): "))

# 2. CORRECCIÓN: Darle un valor inicial a las boletas por si no hay descuentos
boleta_plan_mensual = plan_mensual
boleta_instalacion = instalacion

if velocidad >= 600:
    # ELIMINADO: Ya no necesitamos pedir la categoría otra vez aquí
    if categoria in [1,2]:
        descuento = plan_mensual * 0.18
        boleta_plan_mensual = plan_mensual - descuento
    elif categoria in [3, 4]:
        descuento = plan_mensual * 0.11
        boleta_plan_mensual = plan_mensual - descuento

elif 300 <= velocidad < 600 :
    if categoria in [1,2]:
        descuento = plan_mensual * 0.10
        boleta_plan_mensual = plan_mensual - descuento
    elif categoria in [3, 4]:
        descuento = plan_mensual * 0.06
        boleta_plan_mensual = plan_mensual - descuento

else:
    print("no tienes descuento ")

# 3. Lógica de instalación corregida para usar la boleta_instalacion base
if categoria in [1,2]:
    descuento_instalacion = instalacion * 0.20
    boleta_instalacion = instalacion - descuento_instalacion
    
    if velocidad >= 500:
        # CORRECCIÓN: Se resta el 10% adicional al valor que ya calculamos
        aumento_velocidad = instalacion * 0.10
        boleta_instalacion = boleta_instalacion - aumento_velocidad
    else:
     print("no tienes descuento")

print(f"tu boleta de velocidad es de {boleta_plan_mensual} y de instalacion {boleta_instalacion}")






