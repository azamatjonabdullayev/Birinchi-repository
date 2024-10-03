son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

if son1>=son2:
    a = son1
    son1 = son2
    son2 = a

print(f"Katta son: {son2}\nKichik son: {son1}")