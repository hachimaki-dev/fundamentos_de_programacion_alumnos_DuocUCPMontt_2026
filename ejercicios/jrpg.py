Vida_jefe = 1000 
print("pelea contra el jefe que tiene 1000 de vida")
while Vida_jefe > 0 :
    print("el jefe esta vivo")
    Daño = int(input("ingrese daño que quieras hacer"))
    Vida_jefe = Vida_jefe - (Daño)
    if Daño < 0 :
        Vida_jefe = Vida_jefe + (Daño)
        print("el ataque fallo")
    if Vida_jefe < 0 :
        Vida_jefe = 0
    print(f"vida jefe {Vida_jefe}")
    

        
print("el jefe a sido derrotado")