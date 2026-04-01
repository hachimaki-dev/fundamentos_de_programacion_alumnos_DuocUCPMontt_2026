# Monitorear tu actividad física de los últimos 7 días.

contador = 1
km_totales = 0

print("======Bienvenido a su medidor de actividad física personal======")

while contador < 8 :
    
    km_totales = km_totales + int(input(f"Día número {contador} ¿Cuántos kilómetros corriste este día?"))
    contador = contador + 1
print("Sus kilómetros recorridos esta semana fueron " + km_totales "km's")
