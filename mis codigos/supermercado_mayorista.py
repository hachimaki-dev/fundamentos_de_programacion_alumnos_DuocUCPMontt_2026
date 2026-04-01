item = input("Ingrese un producto: ")
price = float(input("Ingrese el precio por unidad: "))
quantity = int(input("Ingrese la cantidad: "))

discount = 0

if quantity in range(5, 11):
    print("Tiene 10% de descuento")
    discount = 0.1
elif quantity > 10:
    print("Tiene 20% de descuento")
    discount = 0.2
else:
    print("No tiene descuento")

total_quantity_price = price * quantity
price_with_discount = total_quantity_price * discount
total_final_price = total_quantity_price - price_with_discount
print(f"El precio total es: {total_final_price}")