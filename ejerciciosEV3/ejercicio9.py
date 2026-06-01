""" Ejercicio 9 — Evaluación de solicitudes de crédito
Un banco recibe solicitudes de crédito. El analista ingresa el score crediticio de cada solicitante (entero de 0 a 1000).

Clasifica el score con estos rangos exactos:

Mayor a 750 (> 750) → "Aprobado automáticamente"
De 500 a 750 (>= 500 y <= 750) → "Revisión manual"
Menor a 500 (< 500) → "Rechazado"
Condiciones de borde: Un score de exactamente 750 es "Revisión manual". Un score de exactamente 500 también es "Revisión manual".

Registra 8 solicitudes y muestra al final cuántas quedaron en cada categoría.

Desafío: valida que el score esté entre 0 y 1000. Si no, pide ingresar de nuevo. """


solicitudes = 1
aprovado_automaticamente = 0
revision_manual = 0
rechazado = 0

while solicitudes < 9:
    try:
        score_crediticio = int(input(f"ingresa el score del solicitante numero {solicitudes}: "))
        
        if score_crediticio >= 750 and score_crediticio <=1000 :
            aprovado_automaticamente += 1
            solicitudes +=1
    
        elif score_crediticio >= 500 and score_crediticio <= 750:
            revision_manual +=1
            solicitudes +=1
    
        elif score_crediticio < 500:
            rechazado+=1
            solicitudes +=1
        
        
        else:
            print("ingrese de nuevo el score de nuevo")
    
    except ValueError:
        print("ingrese numero real entero")

print(f"numero de aprovados fueron : {aprovado_automaticamente}\n numero de revisiones manuales por hace fueron : {revision_manual}\n numero de rechazados fueron : {rechazado} ")

                           
