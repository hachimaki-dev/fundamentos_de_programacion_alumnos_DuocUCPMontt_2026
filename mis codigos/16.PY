TIPO_CLIENTE = "Postpago"

limite_GB = 15

Gb_consumidos = 18

diferencia_GB = Gb_consumidos - limite_GB

costo_diferencia_GB = diferencia_GB * 1000

print("===== CONTROL DE DATOS MÓVILES =====")

ingreso_tipo_cliente = input("Ingrese el tipo de cliente  /1. Postpago / 2. Prepago /: ")

if ingreso_tipo_cliente.lower() == "postpago" or ingreso_tipo_cliente == "1":

    if Gb_consumidos > limite_GB:
        print("¡Has superado tu límite de datos!")
        print(f"Has consumido {diferencia_GB} GB adicionales.")
        print("Se aplicarán cargos adicionales por el exceso de datos.")

        print(f"El costo adicional es de ${costo_diferencia_GB}")

    else:
        print("¡Datos dentro del límite!")

elif ingreso_tipo_cliente.lower() == "prepago" or ingreso_tipo_cliente == "2":
    print("¡Cliente prepago accion automatica!")