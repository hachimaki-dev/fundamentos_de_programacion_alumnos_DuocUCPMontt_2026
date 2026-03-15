print ("================================")
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
producto10 = "Agua caliente"

print ("Productos disponibles:")
print ("1. " + producto1)
print ("2. " + producto2)
print ("3. " + producto3)   
print ("4. " + producto4)
print ("5. " + producto5)
print ("6. " + producto6)
print ("7. " + producto7)
print ("8. " + producto8)
print ("9. " + producto9)
print ("10. " + producto10)

print ("Ingrese el número del producto que desea comprar:")
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

