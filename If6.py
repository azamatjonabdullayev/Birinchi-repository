son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

if son1>son2:
    print(f"{son1} > {son2}")
elif son2>son1:
    print(f"{son2} > {son1}")
else: print(f"{son1} = {son2}")