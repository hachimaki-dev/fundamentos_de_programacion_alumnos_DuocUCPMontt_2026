print(" C A L C U L A D O R A ")

operacion = input(" Q U E  D E S E A  H A C E R  (+, -, *, /): ")

numero1 = int(input("P O R  F A V O R  I N G R E S E  E L  P R I M E R  N U M E R O: "))
numero2 = int(input("P O R  F A V O R  I N G R E S E  E L  S E G U N D O  N U M E R O: "))

if operacion == "+":
    resultado = numero1 + numero2

elif operacion == "-":
    resultado = numero1 - numero2

elif operacion == "*":
    resultado = numero1 * numero2

elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("E r r o r: n o   s e   p u e d e   d i v i d i r   p o r   c e r o")
        resultado = None

else:
    print("O p e r a c i o n  n o   V a l i d a")
    resultado = None

if resultado is not None:
    print("E l  R e s u l t a d o  e s :", resultado)
