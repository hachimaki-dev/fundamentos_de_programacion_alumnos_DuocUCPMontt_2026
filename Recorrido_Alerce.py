name = input("Cual es su nombre?: ")
print(f"Bienvenido {name} al recorrido Puerto montt-Alerce.")
dirección = input("Hacía donde desea ir?: ")
print(f"Entonces se dirige hacia: {dirección}")
Respuesta = input('Ingresa tu edad: ')
Edad = int(Respuesta)

if Edad > 18:
     print('Pagas tarifa normal.')
elif Edad < 18:
     print('Pagas tarifa de estudiante.')
elif Edad > 65:
     print('Pagas tarifa de adulto mayor.')
else:
     print('Pagas tarifa normal.')
print("Disfrute del viaje.")

