weapon = 0

while weapon < 5:
    weapon += 1
    print(f"Displaying weapon number:{weapon}")
    
    if weapon == 4:
        print("weapon number 4 unavailable")
        continue
    choice = input("do you wish to buy this weapon? (y/n)")
    if choice == "y":
        print("weapon bought enjoy murder c:")
        break