mediacamentos = 60000
despacho_a_domicilio = 8000

edad_usuario = int(input("ingrese su edad: "))
tramo = input("ingrese el tramo que desea : A,B,C o D : ").upper()

if (edad_usuario <= 30) and (tramo == "A" or tramo =="B"):
    descuento_medicamentos_18porciento = mediacamentos  * 0.18
    mediacamentos = mediacamentos - descuento_medicamentos_18porciento
    descuento_despacho_10porciento = despacho_a_domicilio * 0.10
    despacho_a_domicilio = despacho_a_domicilio - descuento_despacho_10porciento

elif edad_usuario <= 30 and (tramo == "C" or tramo == "D"):
    descuento_medicamento_12_porciento = mediacamentos * 0.12
    mediacamentos = mediacamentos - descuento_medicamento_12_porciento
    

elif edad_usuario >= 31 and edad_usuario <=60:
    if tramo == "A" or tramo == "B":
        descuento_medicamento_12_porciento = mediacamentos * 0.12
        mediacamentos = mediacamentos - descuento_medicamento_12_porciento
        descuento_despacho_10porciento = despacho_a_domicilio * 0.10
        despacho_a_domicilio = despacho_a_domicilio - descuento_despacho_10porciento
        if edad_usuario >= 55:
             descuento_adicional_despacho5porciento = despacho_a_domicilio * 0.05
             despacho_a_domicilio = despacho_a_domicilio - descuento_adicional_despacho5porciento
    elif tramo == "C" or tramo == "D":
                descuento_medicamento_8_porciento = mediacamentos * 0.08
                mediacamentos = mediacamentos - descuento_medicamento_8_porciento


        
print(f"el valor de los medicamentos es: {mediacamentos}")
print(f"el valor del despacho es : {despacho_a_domicilio}")






    
    
