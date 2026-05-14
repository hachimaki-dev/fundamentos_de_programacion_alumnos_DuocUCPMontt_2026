plan_mensual = 28000
instalacion = 15000
velocidad = int(input(" de cuanto es tu velocidad: "))


categoria = int(input(" que categoria eres (1 a 4): "))


boleta_plan_mensual = plan_mensual
boleta_instalacion = instalacion

if velocidad >= 600:
  
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


if categoria in [1,2]:
    descuento_instalacion = instalacion * 0.20
    boleta_instalacion = instalacion - descuento_instalacion
    
    if velocidad >= 500:
       
        aumento_velocidad = instalacion * 0.10
        boleta_instalacion = boleta_instalacion - aumento_velocidad
    else:
     print("no tienes descuento")

print(f"tu boleta de velocidad es de {boleta_plan_mensual} y de instalacion {boleta_instalacion}")






