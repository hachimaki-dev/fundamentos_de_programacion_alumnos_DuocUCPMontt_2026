medicamentos_mensual = 60000
despacho_a_domicilio = 8000

while True:
    
    try:
        edad = int(input("Ingrese su edad : "))
    except ValueError:
        print("Ingrese una opcion valida")
        print()
        continue
    try:
        tramo = input("A que Tramo Pertenece (A/B/C/D): ").upper()
    except ValueError:
        print()
        print("Ingrese una Opcion Valida")
        continue

    if edad >= 65 :
        print("No se Aplica descuento por ser Mayor de Edad")
    elif edad <= 30 and tramo == "A" or tramo == "B":
        descuento_medicamentos = medicamentos_mensual * 0.18
        medicamentos_mensual = medicamentos_mensual - descuento_medicamentos
        print("Se le aplico un descuento a sus medicamentos ( 18% )")
    elif edad <= 30 and tramo == "C" or tramo == "D":
        descuento_medicamentos = medicamentos_mensual * 0.12
        medicamentos_mensual = medicamentos_mensual - descuento_medicamentos
        print("Se le aplico un descuento a sus medicamentos (12%) ")
    elif 31 <= edad <= 60 and tramo == "A" or tramo == "B":
        descuento_medicamentos = medicamentos_mensual * 0.12
        medicamentos_mensual = medicamentos_mensual - descuento_medicamentos
        print("Se le aplico un descuento a suCs medicamentos (12%) ")
    elif 31 <= edad <= 60 and tramo == "C" or tramo == "D":
        descuento_medicamentos = medicamentos_mensual * 0.08
        medicamentos_mensual = medicamentos_mensual - descuento_medicamentos
        print("Se le aplico un descuento a sus medicamentos (8%) ")
    else:
        print()
        print("No se Aplica ningun descuento a los Medicamentos")


    if tramo == "A" or tramo == "B" :
        descuento_despacho = despacho_a_domicilio * 0.10
        despacho_a_domicilio = despacho_a_domicilio - descuento_despacho
        if edad >= 55:
            descuento_despacho = despacho_a_domicilio * 0.05
            despacho_a_domicilio = despacho_a_domicilio - descuento_despacho
        
        break
    else:
        print()
        print("No se le aplica un descuento al Despacho a Domocilio")
        print()
    break


print(f"el Total a paga por los Medicamentos es {medicamentos_mensual}")
print(f"El total a pagar por el Despacho a Domicilio es {despacho_a_domicilio}")