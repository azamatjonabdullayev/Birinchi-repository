son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

if son1 == son2:
    son1 = 0
    son2 = 0
else:
    yigindi = son1+son2
    son1 = yigindi
    son2 = yigindi

print(f"Son1: {son1}\nSon2: {son2}")