vida_jefe = 10000
ataque_usuario = 0

while vida_jefe > 0 :
    ataque_usuario = int (input ("Ingrese el daaño que le desea hacer al jefe : "))
    vida_jefe -= ataque_usuario
    print (f"Le has infligido {ataque_usuario} de daño al jefe, le queda {vida_jefe}")

 
print ("Lo insta mataste")