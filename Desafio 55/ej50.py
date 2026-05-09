#Ejercicio 50: Ejercicio 50: Imprimir Boleta Detallada

#El Mini-Boss: Sácale la información a un diccionario para armar una boleta real de restaurante.

#Datos Iniciales: La cuenta es: {'Papas': 5000, 'Pizza': 10000}.

#Reglas de Negocio: Tienes que sumar el total de los platos. Una vez sumado, tienes que calcular el 10% extra por la propina y sumárselo al total final.

#Restricciones: Usa la herramienta .items() en un ciclo for para extraer la pareja completa (el nombre del plato y el precio) al mismo tiempo. Haz la matemática e imprime 'Total final: ' junto al número final con propina.

cuenta = {
    'Papas':5000,
    'Pizza':10000
}
total = 0 

for plato, precio in cuenta.items():
    total += precio
    
total += (total * 0.1)

print(f"Total final: ${int(total)}")