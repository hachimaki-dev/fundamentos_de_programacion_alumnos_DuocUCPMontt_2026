#Desarrolle un programa en Python que calcule el valor final de la cuenta mensual de energía eléctrica y el valor final del cargo por servicio de medición.

#Valores base:

#Cuenta mensual: $45.000
#Cargo de medición: $6.000
#Reglas de descuento para la cuenta:

#Si el consumo es mayor o igual a 500 kWh:
#Tarifa A o B → 20% descuento
#Tarifa C o D → 14% descuento
#Si el consumo está entre 200 y 499 kWh:
#Tarifa A o B → 12% descuento
#Tarifa C o D → 8% descuento
#Si el consumo es menor a 200 kWh → sin descuento.
#Reglas para el cargo de medición:

#Tarifa A o B → 10% descuento.
#Si además el consumo es mayor o igual a 400 kWh → 5% adicional.
#Debe mostrar ambos valores finales.

cuenta_mensual = 45000
cargo_medicion = 6000

tarifa_a_b_mayor_igual_500 = 0.20
tarifa_c_d_mayor_igual_500 = 0.14
tarifa_a_b_entre_200_499 = 0.12
tarifa_c_d_entre_200_499 = 0.8
tarifa_a_b_menor_200 = 0.10
tarifa_a_b_menor_200 = 0.10
consumo_mayor_400 = 0.5


kWh_ocupados = int(input("Indique cuantos kilo watts ha ocupado este mes: "))

print("Tarifa a")
print("Tarifa b")
print("Tarifa c")
print("Tarifa d")


tarifa_escogida = input("Seleccione su tarifa: ")


if kWh_ocupados >= 500:
    if tarifa_escogida == "a":
        cuenta_mensual = cuenta_mensual - tarifa_a_b_mayor_igual_500
        print(f"hola chaval {cuenta_mensual}") 
    elif tarifa_escogida == "c" or "d":
        cuenta_mensual = cuenta_mensual - tarifa_c_d_mayor_igual_500
        print(f"hola chaval {cuenta_mensual}")


#Trabajo en Progreso!!
