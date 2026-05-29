medicamentos_mensual = 60000
despacho_a_domicilio = 8000

def descuento_18(descuento18):
     return  medicamentos_mensual - (medicamentos_mensual * 0.18)

def descuento_12(descuento12):
     return medicamentos_mensual - (medicamentos_mensual * 0.12)

def descuento_8(descuento8):
     return medicamentos_mensual - (medicamentos_mensual * 0.08)


def descuento10_despacho(despacho_des10):
    return despacho_a_domicilio - (despacho_a_domicilio * 0.1)

def descuento5_despacho(despacho_des5):
    return despacho_a_domicilio - (despacho_a_domicilio * 0.05)


while True:
    try:
        edad = int(input("Ingrese su Edad :  "))
    except ValueError:
        print("Ingrese Una Opcion Valida")
        continue
    

    try:
        tramo = input("Ingrese Al tramo al que Pertenece (A/B/C/D) :  ").upper()
    except ValueError:
        print("Ingrese Una Opcion Valida")
        continue

    
    if edad > 60 :
        print("No se Aplica Descuento Por tener mas de 60 Años ")
        print(f"Su total a Pagar es :  {medicamentos_mensual}")
    elif edad <= 30 and tramo == "A" or tramo == "B":
        print("Se le aplica un descuento de el 18%")
        total_medicamentos = descuento_18(medicamentos_mensual)
        print(f"Total a Pagar por los medicamentos :  {total_medicamentos}")
    elif edad <= 30 and tramo == "C" or tramo == "D":
        print("Se le aplico un descuento de el 12%")
        total_medicamentos = descuento_12(medicamentos_mensual)
        print(f"Total a Pagar por los medicamentos :  {total_medicamentos}")
    elif 31 <= edad <= 60 and tramo == "A" or tramo == "B":
        print("Se le aplico un descuento de el 12%")
        total_medicamentos = descuento_12(medicamentos_mensual)
        print(f"Total a Pagar por los medicamentos :  {total_medicamentos}")
    elif 31 <= edad <= 60 and tramo == "C" or tramo == "D":
        print("Se le aplico un descuento de el 8%")
        total_medicamentos = descuento_8(medicamentos_mensual)
        print(f"Total a Pagar por los medicamentos :  {total_medicamentos}")
    else:
        print()
        print("No se a Aplicado ningun Descuento")
        


    if tramo == "A" or tramo == "B" :
        print("Se Aplico un descuento (10%) en el Despacho")
        total_despacho = descuento10_despacho(despacho_a_domicilio)
        print(f"Lo cual su despacho queda en {total_despacho}")
        
        if edad >= 55:
            print("Se Aplico un descuento (5%) extra mas al Despacho")
            total_despacho = descuento5_despacho(despacho_a_domicilio)
            print(f"Lo cual su despacho queda en {total_despacho}")
    else:
        print()
        print("No se aplica un Descuento al Despacho a Domicilio ")
        print()
        print(f"El Total a Pagar es :  {despacho_a_domicilio}")
    
    break