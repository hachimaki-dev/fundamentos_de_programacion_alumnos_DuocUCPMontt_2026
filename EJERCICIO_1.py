import time
import random
vida_jefe = 10000
vida_protagonista = 5000

print("Acabas de llegar a la Ciudad Anillada, donde te espera Gael, el caballero Esclavo.")
time.sleep(2)
print("Gael: ¿Llegaste hasta aqui? ¿Hasta los rincones del mundo? No importa, lo unico que importa es que arrancare el alma oscura de tu cuerpo inerte.")
time.sleep(2)
print("Tu, en silencio solo aceptas lo que vendrá a continuación, una batalla entre dos caballeros en el fin del mundo.")

while vida_jefe > 0:
    try:
        ataque_protagonista = int(input("¿Cuanto daño le harás a Gael?: "))
        if ataque_protagonista < 0:
            print("Acabas de fallar tu ataque contra Gael.")
            
        else:
            vida_jefe -= ataque_protagonista
            
            vida_restante = max(0, vida_jefe)
            print(f" Gael esta siendo destruido mientras el sigue de pie, inmutable. Vida faltante: {vida_jefe}")
            
    except ValueError:
        print("No puedes escribir letras caballero de la ceniza, solo numeros.")
        
print("Estas presenciando el fin de todo...")
time.sleep(1.5)
print("...")
time.sleep(2)
print("Gael: ... Sabia este resultado, sin duda... eres")
time.sleep(2)
print("Gael: El caballero de la Oscuridad.")  
time.sleep(3)
print("Dark Souls 3 by Juan Pablo Sanchez.")
          