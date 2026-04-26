salario=0
opcion=0
barrer=10000
limpiar_baño=40000
lavar_auto=50000

print("")
print("================================================================================")        
print("Necesitas ganar 100.000 pesos antes de que termine el dia")
print("Tu puedes hacer los siguientes trabajos")
trabajos=[f"1. Barrer {barrer} $", f"2. Limpiar el baño {limpiar_baño} $", f"3. Lavar el auto {lavar_auto} $"]
print(trabajos)
print("================================================================================")
print("")

while salario < 100000:
    for trabajos in trabajos:
        print(trabajos)
    opcion=int(input("¿Que trabajo quieres hacer? "))
    
    if opcion==1:
        salario=salario+barrer
    elif opcion==2:
        salario=salario+limpiar_baño
    elif opcion==3:
        salario=salario+lavar_auto
    else:
        print("Opcion no valida")
    print(f"Bien ahora tines {salario} pesos")
    print("")
print(f"¡Felicidades alcanzaste tu meta. Ya tienes {salario} pesos!")
print("")