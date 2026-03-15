print ("=================================")
print ("===Maquina Expendedora de Café===")
print ("=================================")

print ("Bienvenido a la Maquina Expendedora de Café")
print ("Por favor, seleccione el producto que desea comprar:")



producto1 = "Café Americano"
producto2 = "Té"
producto3 = "Chocolate caliente"
producto4 = "Café con leche"
producto5 = "Café Latte"
producto6 = "Cappuccino"
producto7 = "Mocha"
producto8 = "Frappuccino"
producto9 = "Té helado"
producto10 = "Café descafeinado"

precio_producto1 = 1.50
precio_producto2 = 1.00
precio_producto3 = 2.00
precio_producto4 = 1.75
precio_producto5 = 2.25
precio_producto6 = 2.50
precio_producto7 = 2.75
precio_producto8 = 3.00
precio_producto9 = 1.25
precio_producto10 = 1.50

print ("Productos disponibles:")
print ("1. " + producto1 + " - $" + str(precio_producto1))
print ("2. " + producto2 + " - $" + str(precio_producto2))
print ("3. " + producto3 + " - $" + str(precio_producto3))
print ("4. " + producto4 + " - $" + str(precio_producto4))
print ("5. " + producto5 + " - $" + str(precio_producto5))
print ("6. " + producto6 + " - $" + str(precio_producto6))
print ("7. " + producto7 + " - $" + str(precio_producto7))
print ("8. " + producto8 + " - $" + str(precio_producto8))
print ("9. " + producto9 + " - $" + str(precio_producto9))
print ("10. " + producto10 + " - $" + str(precio_producto10))

print ("Ingrese el número del producto que desea comprar (1-10)")
opcion = int(input("su pedido es : "))
if opcion == 1:
    print ("Ha seleccionado: " + producto1)
elif opcion == 2:
    print ("Ha seleccionado: " + producto2) 
elif opcion == 3:
    print ("Ha seleccionado: " + producto3)
elif opcion == 4:
    print ("Ha seleccionado: " + producto4)
elif opcion == 5:
    print ("Ha seleccionado: " + producto5)
elif opcion == 6:
    print ("Ha seleccionado: " + producto6)
elif opcion == 7:
    print ("Ha seleccionado: " + producto7)
elif opcion == 8:
    print ("Ha seleccionado: " + producto8)
elif opcion == 9:
    print ("Ha seleccionado: " + producto9)
elif opcion == 10:
    print ("Ha seleccionado: " + producto10)
else:
    print ("Opción no válida. Por favor, seleccione un número del 1 al 10.")

cantidad_de_Azucar = int(input("¿Cuanta azucár desea agregar? , Igrese una numero del 0 al 5 :  "))

if cantidad_de_Azucar >= 0 and cantidad_de_Azucar <= 5:
    print ("Ha seleccionado agregar " +  str (cantidad_de_Azucar) + " cucharadas de azúcar.")
else:  print ("Cantidad no valida. porfavor ingrese un nunmero del 0 al 5")

print ("Seleccione un metodo de pago")
print ("1. tarjeta de credito")
print ("2. efectivo")

ingrese_un_metodo_de_pago = int (input ("Ingrese el numero del metodo de pago que desea usar,  1 o 2 : "))

metodo_de_pago1 = "tarjeta de credito"
metodo_de_pago2 = "efectivo"

if ingrese_un_metodo_de_pago == 1:

    print ("Ha seleccionado: " + metodo_de_pago1)
    print ("Esta seguro seguro de realizar la compra? , ingrese 1 para confirmar o 2 para cancelar : ")
    confirmacion_de_compra = int (input ("Ingrese su respuesta : "))
    if confirmacion_de_compra == 1:
        print ("Compra confirmada. Gracias por su compra!")
    elif confirmacion_de_compra == 2:
        print ("Compra cancelada. Gracias por visitar nuestra maquina expendedora de café.")
    else: print ("Opción no válida. Por favor, seleccione un número del 1 al 2.")

elif ingrese_un_metodo_de_pago == 2:
        vuelto = float(input("Ingrese el monto que ha pagado: "))
if opcion == 1:
    precio = precio_producto1
elif opcion == 2:
    precio = precio_producto2
elif opcion == 3:
    precio = precio_producto3
elif opcion == 4:
    precio = precio_producto4
elif opcion == 5:
    precio = precio_producto5
elif opcion == 6:
    precio = precio_producto6
elif opcion == 7:
    precio = precio_producto7
elif opcion == 8:
    precio = precio_producto8
elif opcion == 9:
    precio = precio_producto9
elif opcion == 10:
    precio = precio_producto10
else:
    print ("Opción no válida. Por favor, seleccione un número del 1 al 10.")
    precio = 0 
if vuelto >= precio:
    cambio = vuelto - precio
    print ("Su cambio es: $" + str(cambio))
else:
    print ("Monto insuficiente. Por favor, ingrese un monto mayor o igual al precio del producto.")
    print ("Ha seleccionado: " + metodo_de_pago2)
    print ("Esta seguro seguro de realizar la compra? , ingrese 1 para confirmar o 2 para cancelar : ")
    confirmacion_de_compra = int (input ("Ingrese su respuesta : "))
    if confirmacion_de_compra == 1:
        print ("Compra confirmada. Gracias por su compra!")
    elif confirmacion_de_compra == 2:
        print ("Compra cancelada. Gracias por visitar nuestra maquina expendedora de café.")
    else: print ("Opción no válida. Por favor, seleccione un número del 1 al 2.")


print ("Gracias por usar la Maquina Expendedora de Café. ¡Que tenga un buen día!")