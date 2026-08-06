""" Objetivo: Contador analítico de transporte para un peaje de carretera.

1. Usar bucle infinito hasta que el cobrador ingrese tipo vehiculo "SALIR".
2. Los tipos que se pueden ingresar son: "AUTO", "CAMION", "MOTO".

3. Precios: AUTO=$1500, MOTO=$500, CAMION=$3500. 
Si introducen otra cosa muestra error.

4. Acumular en todo momento LA CANTIDAD de cada vehiculo que pasó.
5. Acumular el DINERO GLOBAL generado.

6. Al poner "SALIR", muestra un cierre de caja: (Ganancia Total, 
y por porcentaje aproximado qué tipo de vehiculo es el ganador del dia, 
ej: pasaron mas motos que autos)."""

print("bienvenido a la carretera")

menu = 0
auto = 1500
moto = 500
camion = 3500

unidad_auto = 0
unidad_moto = 0
unidad_camion = 0

while True:
    menu = input("ingrese su tipo de vehiculo:  o salir")
    
    if menu == "auto":
        unidad_auto = unidad_auto + 1
        dinero_global = dinero_global + auto

    elif menu == "moto":
        unidad_moto = unidad_moto + 1
        dinero_global = dinero_global + moto

    elif menu == " camion":
        unidad_camion = unidad_camion + 1
        dinero_global = dinero_global 

    elif menu == "salir":
        break
    

print(f"ganancia total = {dinero_global} el tipo de vehiculo que mas paso fue: {cantidad_de_vehiculos}")
 