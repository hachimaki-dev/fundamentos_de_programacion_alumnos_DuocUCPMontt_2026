#Valores base
mensualidad = 85000
kit_materiales = 18000

print("------ Bienvenido al Jardín infantil: Puntitos ------")
edad_niño = int(input("\nIngresa la edad de tu bebé (meses): "))
print("\n¿A qué nivel ingresa?")
print("Nivel 1")
print("Nivel 2")
print("Nivel 3")
print("Nivel 4")
nivel = int(input("Ingresa el número del nivel: "))

#Descuentos para la mensualidad
if edad_niño <= 18:
    if nivel == 1 or nivel == 2:
        mensualidad -= (mensualidad * 0.2)
    elif nivel == 3 or nivel == 4:
        mensualidad -= (mensualidad * 0.13)
elif 19 <= edad_niño <= 36:
    if nivel == 1 or nivel == 2:
        mensualidad -= (mensualidad * 0.12)
    elif nivel == 3 or nivel == 4:
        mensualidad -= (mensualidad * 0.07)
elif edad_niño > 36:
    mensualidad

#Descuentos kit
if nivel == 1 or nivel == 2:
    kit_materiales -= (kit_materiales * 0.1)

if edad_niño <= 12:
    kit_materiales -= (kit_materiales * 0.05)

print(f"\nMensualidad: ${int(mensualidad)}")
print(f"Kit de materiales: ${int(kit_materiales)}")