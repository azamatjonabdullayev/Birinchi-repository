son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))

if son1+son2>son3:
    print(f"{son1} + {son2} > {son3}")
elif son1+son3>son2:
    print(f"{son1} + {son3} > {son2}")
elif son2 + son3 > son1:
    print(f"{son2} + {son3} > {son1}")
else:
    print("Xato!")