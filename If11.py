son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

if son1 == son2:
    son1 = 0
    son2 = 0
else:
    if son1 > son2:
        son2 = son1
    elif son2 > son1:
        son1 = son2

print(f"Son1: {son1}\nSon2: {son2}")