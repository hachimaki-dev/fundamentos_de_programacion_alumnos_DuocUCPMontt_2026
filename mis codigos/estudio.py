

precio_noche_camping_por_persona = 15000
seguro_de_asistencia_medica_por_persona = 5000


dias_de_estadia = int(input("¿cuantos dias te vas a quedar?: "))
tramo = (input("¿que tramo eres (A,B,C o D)?: ")).upper()

if (dias_de_estadia <= 5) and (tramo == "A" or tramo == "B"):
    descuento_noche_camping_por_persona = precio_noche_camping_por_persona * 0.10
    precio_noche_camping_por_persona = precio_noche_camping_por_persona - descuento_noche_camping_por_persona
    valor_camping = precio_noche_camping_por_persona * dias_de_estadia
    descuento_seguro = seguro_de_asistencia_medica_por_persona * 0.15
    seguro_de_asistencia_medica_por_persona = seguro_de_asistencia_medica_por_persona - descuento_seguro
    
elif (dias_de_estadia <= 5) and (tramo == "C" or tramo == "D"):
    descuento_noche_camping_por_persona = precio_noche_camping_por_persona * 0.05
    precio_noche_camping_por_persona = precio_noche_camping_por_persona - descuento_noche_camping_por_persona
    valor_camping = precio_noche_camping_por_persona * dias_de_estadia
    

elif (6 >=dias_de_estadia <= 12 ) and (tramo == "A" or tramo == "B"):
    descuento_noche_camping_por_persona = precio_noche_camping_por_persona * 0.20
    precio_noche_camping_por_persona = precio_noche_camping_por_persona - descuento_noche_camping_por_persona
    valor_camping = precio_noche_camping_por_persona * dias_de_estadia
    descuento_seguro = seguro_de_asistencia_medica_por_persona * 0.15
    seguro_de_asistencia_medica_por_persona = seguro_de_asistencia_medica_por_persona - descuento_seguro
    if dias_de_estadia <= 10:
        descuento_mas_o_igual_diez_dias = seguro_de_asistencia_medica_por_persona * 0.05
        seguro_de_asistencia_medica_por_persona -= descuento_mas_o_igual_diez_dias
        
        
    


elif (6 >=dias_de_estadia <= 12 ) and (tramo == "C" or tramo == "D"):
    descuento_noche_camping_por_persona = precio_noche_camping_por_persona * 0.15
    precio_noche_camping_por_persona = precio_noche_camping_por_persona - descuento_noche_camping_por_persona
    valor_camping = precio_noche_camping_por_persona * dias_de_estadia
    if dias_de_estadia <= 10:
        descuento_mas_o_igual_diez_dias = seguro_de_asistencia_medica_por_persona * 0.05
        seguro_de_asistencia_medica_por_persona -= descuento_mas_o_igual_diez_dias
   

elif (dias_de_estadia >= 12):
    print(f"no tienes descuento queda en {precio_noche_camping_por_persona}")




print(f"el precio es de {valor_camping}")
print(f"el precio es de {seguro_de_asistencia_medica_por_persona}")
